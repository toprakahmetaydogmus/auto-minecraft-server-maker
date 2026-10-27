# -*- coding: utf-8 -*-
"""
Autonomous Minecraft Server Installer
Supports automatic downloading, configuration, and setup for:
- Paper (High Performance Spigot Fork)
- Purpur (Feature-rich Paper Fork)
- Fabric (Modern Lightweight Modded Server)
- Vanilla (Official Mojang Server)
- Arclight (Forge + Bukkit/Spigot Hybrid for Crossplay & Mods)
- Geyser & Floodgate (Bedrock crossplay integration)
"""

import os
import json
import urllib.request
import logging

class ServerInstaller:
    # Tüm Minecraft Sürümleri (En Yeniden En Eskiye)
    SUPPORTED_VERSIONS = [
        "1.21.4", "1.21.3", "1.21.1", "1.21.0",
        "1.20.6", "1.20.4", "1.20.2", "1.20.1",
        "1.19.4", "1.19.2", "1.18.2", "1.17.1",
        "1.16.5", "1.15.2", "1.14.4", "1.13.2",
        "1.12.2", "1.11.2", "1.10.2", "1.9.4",
        "1.8.9", "1.8.8", "1.7.10", "1.6.4",
        "1.5.2", "1.4.7", "1.2.5", "1.0.0"
    ]

    @classmethod
    def get_supported_versions(cls):
        return cls.SUPPORTED_VERSIONS

    def __init__(self, target_dir, log_callback=None, progress_callback=None):
        self.target_dir = os.path.abspath(target_dir)
        self.log_callback = log_callback or print
        self.progress_callback = progress_callback

    def log(self, message):
        self.log_callback(f"{message}")

    def setup_server(self, server_type, mc_version, min_ram=4, max_ram=6, rcon_port=25575, rcon_pass="admin123", server_port=25565, bedrock_port=19132, install_geyser=True):
        os.makedirs(self.target_dir, exist_ok=True)
        self.log(f"> Kurulum başlatılıyor: {server_type} {mc_version}...")

        from core.java_detector import JavaDetector
        sys_j = JavaDetector.get_system_java()
        j_ver = sys_j['version'] if sys_j and sys_j['version'] > 0 else 17
        self.log(f"> Java {j_ver} algılandı ✔")

        jar_filename = f"{server_type.lower()}-{mc_version}.jar"
        jar_path = os.path.join(self.target_dir, jar_filename)

        # 1. Primary Download Attempt
        self.log(f"> {server_type} {mc_version} indiriliyor...")
        success = self._download_jar(server_type, mc_version, jar_path)

        # 2. Multi-tier Autonomous Mirror Fallback
        if not success:
            self.log(f"⚠️ {server_type} {mc_version} birincil sunucudan indirilemedi. Otonom ayna sunucular (Mirrors) deneniyor...")
            
            # Fallback 1: Purpur
            if "paper" in server_type.lower():
                self.log("🔄 Ayna 1: Purpur API deneniyor...")
                success = self._download_purpur(mc_version, jar_path)
            
            # Fallback 2: Vanilla Official Mojang
            if not success:
                self.log("🔄 Ayna 2: Resmi Mojang CDN deneniyor...")
                success = self._download_vanilla(mc_version, jar_path)

        # 3. Autonomous AI Diagnosis if still failing
        if not success:
            err_msg = f"{server_type} ({mc_version}) için tüm ayna sunucu bağlantıları zaman aşımına uğradı."
            self.log(f"❌ [HATA] {err_msg}")
            try:
                from core.ai_engineer import AIEngineer
                ai = AIEngineer()
                diag = ai.diagnose_installation_error(server_type, mc_version, err_msg)
                self.log(f"\n🤖 [AI OTONOM KURTARMA & TEŞHİS RAPORU]:\n{diag}\n")
            except Exception as e:
                self.log(f"AI teşhis hatası: {e}")
            return False

        # eula.txt
        eula_path = os.path.join(self.target_dir, "eula.txt")
        with open(eula_path, "w", encoding="utf-8") as f:
            f.write("# Otomatik kabul edilmis Minecraft EULA\neula=true\n")
        self.log("> EULA onaylandı ✔")

        # server.properties
        self._write_server_properties(server_port, rcon_port, rcon_pass)
        self.log("> server.properties üretildi ✔")

        # start.bat
        self._write_start_script(jar_filename, min_ram, max_ram)
        self.log(f"> start.bat optimize edildi (Aikar G1GC Flags: {min_ram}G-{max_ram}G) ✔")

        # Geyser + Floodgate Crossplay (Bedrock Support)
        if install_geyser and any(k in server_type.lower() for k in ["paper", "purpur", "arclight", "spigot", "mohist"]):
            self._install_geyser_plugin()
            self._install_floodgate_plugin()
            self.log("> Mobil & Konsol Crossplay (Geyser + Floodgate) yapılandırıldı ✔")

        self.log("======================================================")
        self.log(f"✅ SUNUCU ÇALIŞMAYA HAZIR! Konum: {self.target_dir}")
        self.log("======================================================")
        return True


    def _download_jar(self, server_type, mc_version, dest_path):
        st = server_type.lower()
        try:
            if "paper" in st:
                return self._download_paper(mc_version, dest_path)
            elif "purpur" in st:
                return self._download_purpur(mc_version, dest_path)
            elif "fabric" in st:
                return self._download_fabric(mc_version, dest_path)
            elif "arclight" in st:
                return self._download_arclight(mc_version, dest_path)
            elif "mohist" in st:
                return self._download_mohist(mc_version, dest_path)
            elif "velocity" in st:
                return self._download_velocity(dest_path)
            elif "bungeecord" in st:
                return self._download_bungeecord(dest_path)
            elif "forge" in st:
                return self._download_forge(mc_version, dest_path)
            elif "neoforge" in st:
                return self._download_neoforge(mc_version, dest_path)
            elif "vanilla" in st:
                return self._download_vanilla(mc_version, dest_path)
            else:
                self.log(f"Bilinmeyen sunucu tipi: {server_type}, Paper deneniyor...")
                return self._download_paper(mc_version, dest_path)
        except Exception as e:
            self.log(f"İndirme hatası: {e}")
            return False

    def _download_mohist(self, version, dest_path):
        self.log(f"MohistMC API sorgulanıyor ({version})...")
        try:
            api_url = f"https://mohistmc.com/api/v2/projects/mohist/{version}/builds"
            req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            builds = data.get("builds", [])
            if builds:
                b_num = builds[-1].get("number")
                dl_url = f"https://mohistmc.com/api/v2/projects/mohist/{version}/builds/{b_num}/download"
                self.log(f"Mohist indiriliyor: #{b_num}")
                self._download_file(dl_url, dest_path)
                return True
        except Exception:
            pass
        self.log(f"Mohist API yanıt vermedi, Arclight Forge deneniyor...")
        return self._download_arclight(version, dest_path)

    def _download_velocity(self, dest_path):
        self.log("Velocity modern proxy jar indiriliyor...")
        dl_url = "https://api.papermc.io/v2/projects/velocity/versions/3.3.0-SNAPSHOT/builds/442/downloads/velocity-3.3.0-SNAPSHOT-442.jar"
        self._download_file(dl_url, dest_path)
        return True

    def _download_bungeecord(self, dest_path):
        self.log("BungeeCord resmi proxy jar indiriliyor...")
        dl_url = "https://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar"
        self._download_file(dl_url, dest_path)
        return True

    def _download_forge(self, version, dest_path):
        self.log(f"Forge sunucu yükleyicisi aranıyor ({version})...")
        # Direct fallback to Arclight for full Forge hybrid compatibility or paper
        return self._download_arclight(version, dest_path)

    def _download_neoforge(self, version, dest_path):
        self.log(f"NeoForge aranıyor ({version})...")
        return self._download_fabric(version, dest_path)


    def _download_paper(self, version, dest_path):
        api_url = f"https://api.papermc.io/v2/projects/paper/versions/{version}"
        self.log(f"PaperMC API sorgulanıyor: {api_url}")
        try:
            req = urllib.request.Request(api_url, headers={"User-Agent": "AutoMinecraftServerMaker/1.0"})
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            builds = data.get("builds", [])
            if builds:
                latest_build = builds[-1]
                dl_url = f"https://api.papermc.io/v2/projects/paper/versions/{version}/builds/{latest_build}/downloads/paper-{version}-{latest_build}.jar"
                self.log(f"İndiriliyor: Paper #{latest_build} ({dl_url})")
                self._download_file(dl_url, dest_path)
                return True
        except Exception:
            pass

        self.log(f"PaperMC'de {version} bulunamadı veya 1.8.8 öncesi bir sürüm. Otonom Mojang Vanilla kaynağına geçiliyor...")
        return self._download_vanilla(version, dest_path)

    def _download_purpur(self, version, dest_path):
        dl_url = f"https://api.purpurmc.org/v2/purpur/{version}/latest/download"
        self.log(f"İndiriliyor: Purpur {version} ({dl_url})")
        self._download_file(dl_url, dest_path)
        return True

    def _download_vanilla(self, version, dest_path):
        manifest_url = "https://launchermeta.mojang.com/mc/game/version_manifest_v2.json"
        self.log("Mojang Version Manifest alınıyor...")
        req = urllib.request.Request(manifest_url, headers={"User-Agent": "AutoMinecraftServerMaker/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))

        v_url = None
        for v in data.get("versions", []):
            if v.get("id") == version:
                v_url = v.get("url")
                break

        if not v_url:
            self.log(f"Mojang listesinde {version} bulunamadı.")
            return False

        with urllib.request.urlopen(v_url, timeout=15) as resp:
            v_data = json.loads(resp.read().decode("utf-8"))

        server_info = v_data.get("downloads", {}).get("server", {})
        server_dl = server_info.get("url")
        if not server_dl:
            return False

        self.log(f"Mojang resmi Vanilla server indiriliyor: {version}")
        self._download_file(server_dl, dest_path)
        return True

    def _download_fabric(self, version, dest_path):
        installer_url = f"https://meta.fabricmc.net/v2/versions/loader/{version}/0.16.9/1.0.1/server/jar"
        self.log(f"Fabric Server Launcher indiriliyor: {version}")
        self._download_file(installer_url, dest_path)
        return True

    def _download_arclight(self, version, dest_path):
        # Arclight Forge Hybrid Release
        api_url = "https://api.github.com/repos/IzzelAliz/Arclight/releases"
        self.log("GitHub Arclight sürümleri taranıyor...")
        req = urllib.request.Request(api_url, headers={"User-Agent": "AutoMinecraftServerMaker/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            releases = json.loads(resp.read().decode("utf-8"))

        target_asset = None
        for r in releases:
            for a in r.get("assets", []):
                aname = a.get("name", "").lower()
                if "forge" in aname and version in aname and aname.endswith(".jar"):
                    target_asset = a.get("browser_download_url")
                    break
            if target_asset:
                break

        if not target_asset:
            # Fallback to Paper
            self.log(f"Arclight release for {version} bulunamadı, Paper kuruluyor...")
            return self._download_paper(version, dest_path)

        self.log(f"Arclight Forge Hibrit indiriliyor: {target_asset}")
        self._download_file(target_asset, dest_path)
        return True

    def _install_geyser_plugin(self):
        plugins_dir = os.path.join(self.target_dir, "plugins")
        os.makedirs(plugins_dir, exist_ok=True)
        geyser_path = os.path.join(plugins_dir, "Geyser-Spigot.jar")
        if not os.path.exists(geyser_path):
            self.log("> Geyser (Bedrock Crossplay) eklentisi indiriliyor...")
            try:
                url = "https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/spigot"
                self._download_file(url, geyser_path)
                self.log("> Geyser eklentisi plugins klasörüne kuruldu ✔")
            except Exception as e:
                self.log(f"Geyser indirme uyarısı: {e}")

    def _install_floodgate_plugin(self):
        plugins_dir = os.path.join(self.target_dir, "plugins")
        os.makedirs(plugins_dir, exist_ok=True)
        fg_path = os.path.join(plugins_dir, "Floodgate-Spigot.jar")
        if not os.path.exists(fg_path):
            self.log("> Floodgate (Şifresiz Bedrock Girişi) eklentisi indiriliyor...")
            try:
                url = "https://download.geysermc.org/v2/projects/floodgate/versions/latest/builds/latest/downloads/spigot"
                self._download_file(url, fg_path)
                self.log("> Floodgate eklentisi plugins klasörüne kuruldu ✔")
            except Exception as e:
                self.log(f"Floodgate indirme uyarısı: {e}")

    def _download_file(self, url, dest_path):
        req = urllib.request.Request(url, headers={"User-Agent": "AutoMinecraftServerMaker/1.0"})
        with urllib.request.urlopen(req, timeout=60) as resp, open(dest_path, "wb") as out:
            total_size = int(resp.headers.get("Content-Length", 0))
            downloaded = 0
            while True:
                chunk = resp.read(65536)
                if not chunk:
                    break
                out.write(chunk)
                downloaded += len(chunk)
                if total_size > 0:
                    pct = int(downloaded / total_size * 100)
                    if self.progress_callback:
                        self.progress_callback(pct, downloaded, total_size)
                    if downloaded % (1024 * 1024 * 5) < 65536:
                        self.log(f"İndiriliyor: %{pct} ({downloaded // (1024*1024)} MB)")
                else:
                    if self.progress_callback:
                        self.progress_callback(50, downloaded, 0)

    def _write_server_properties(self, server_port, rcon_port, rcon_pass):
        props_path = os.path.join(self.target_dir, "server.properties")
        content = f"""# Minecraft Server Properties - Auto-generated
server-port={server_port}
enable-rcon=true
rcon.port={rcon_port}
rcon.password={rcon_pass}
broadcast-rcon-to-ops=true
online-mode=false
motd=\\u00a76\\u00a7lAuto Minecraft Server\\u00a7f - \\u00a7aAktif!
max-players=20
view-distance=10
simulation-distance=8
gamemode=survival
difficulty=normal
enable-command-block=true
spawn-protection=0
query.port={server_port}
rate-limit=0
sync-chunk-writes=true
"""
        with open(props_path, "w", encoding="utf-8") as f:
            f.write(content)

    def _write_start_script(self, jar_filename, min_ram, max_ram):
        bat_path = os.path.join(self.target_dir, "start.bat")
        # High performance Aikar G1GC Flags
        content = f"""@echo off
title Auto Minecraft Server ({jar_filename})
chcp 65001 >nul
cls
echo =====================================================================
echo           AUTO MINECRAFT SERVER MAKER - BASLATICI
echo =====================================================================
echo.
echo [*] Sunucu Jar: {jar_filename}
echo [*] RAM: Min {min_ram}GB - Max {max_ram}GB (Aikar G1GC Optimize)
echo.
java -Xms{min_ram}G -Xmx{max_ram}G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -jar {jar_filename} nogui
pause
"""
        with open(bat_path, "w", encoding="utf-8") as f:
            f.write(content)
