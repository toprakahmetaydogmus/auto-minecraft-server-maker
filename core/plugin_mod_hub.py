# -*- coding: utf-8 -*-
"""
1-Click Plugin & Mod Hub (v3.9.0 Ultimate)
Autonomous downloader & installer for essential high-performance Minecraft plugins.
Direct download from official verified CDNs and repositories.
"""

import os
import urllib.request
import threading
import logging

POPULAR_PLUGINS = [
    {
        "id": "geyser",
        "name": "Geyser-Spigot",
        "category": "Crossplay",
        "desc": "Bedrock (Mobil & Konsol) oyuncularının Java sunucusuna bağlanmasını sağlar.",
        "url": "https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/spigot",
        "filename": "Geyser-Spigot.jar"
    },
    {
        "id": "floodgate",
        "name": "Floodgate",
        "category": "Crossplay",
        "desc": "Bedrock oyuncularının Java hesabı olmadan kolayca giriş yapmasını sağlar.",
        "url": "https://download.geysermc.org/v2/projects/floodgate/versions/latest/builds/latest/downloads/spigot",
        "filename": "floodgate-spigot.jar"
    },
    {
        "id": "viaversion",
        "name": "ViaVersion",
        "category": "Uyumluluk",
        "desc": "Daha yeni Minecraft sürümlerinin eski sunuculara girmesini sağlar.",
        "url": "https://api.spiget.org/v2/resources/19254/download",
        "filename": "ViaVersion.jar"
    },
    {
        "id": "viabackwards",
        "name": "ViaBackwards",
        "category": "Uyumluluk",
        "desc": "Daha eski Minecraft istemcilerinin yeni sunuculara girmesini sağlar.",
        "url": "https://api.spiget.org/v2/resources/27448/download",
        "filename": "ViaBackwards.jar"
    },
    {
        "id": "essentialsx",
        "name": "EssentialsX",
        "category": "Yönetim",
        "desc": "Temel sunucu komutları: /sethome, /spawn, /warp, /tpa, /fly vb.",
        "url": "https://api.spiget.org/v2/resources/9089/download",
        "filename": "EssentialsX.jar"
    },
    {
        "id": "luckperms",
        "name": "LuckPerms",
        "category": "Yetki & Rütbe",
        "desc": "Minecraft'ın en gelişmiş, modern web editörlü yetki ve rütbe yönetim eklentisi.",
        "url": "https://download.luckperms.net/1559/bukkit/loader/LuckPerms-Bukkit-5.4.145.jar",
        "filename": "LuckPerms.jar"
    },
    {
        "id": "vault",
        "name": "Vault",
        "category": "Ekonomi & API",
        "desc": "Tüm ekonomi ve yetki eklentilerinin birbiriyle konuşmasını sağlayan temel köprü.",
        "url": "https://api.spiget.org/v2/resources/34315/download",
        "filename": "Vault.jar"
    },
    {
        "id": "worldedit",
        "name": "WorldEdit",
        "category": "İnşa & Yapı",
        "desc": "Büyük yapıları saniyeler içinde inşa etme ve harita düzenleme aracı.",
        "url": "https://mediafilez.forgecdn.net/files/5460/346/worldedit-bukkit-7.3.6.jar",
        "filename": "WorldEdit.jar"
    },
    {
        "id": "chunky",
        "name": "Chunky",
        "category": "Lag Önleme",
        "desc": "Dünya chunk'larını önceden oluşturarak oyuncular gezerken oluşan lagı %95 yok eder.",
        "url": "https://api.spiget.org/v2/resources/81534/download",
        "filename": "Chunky.jar"
    },
    {
        "id": "clearlag",
        "name": "ClearLag",
        "category": "Lag Önleme",
        "desc": "Yerdeki gereksiz eşyaları ve fazla entity'leri otomatik temizler, RAM kazandırır.",
        "url": "https://api.spiget.org/v2/resources/28271/download",
        "filename": "ClearLag.jar"
    },
    {
        "id": "skinsrestorer",
        "name": "SkinsRestorer",
        "category": "Görsel",
        "desc": "Tüm oyuncuların gerçek Minecraft skinlerini eksiksiz gösterir (/skin komutu).",
        "url": "https://api.spiget.org/v2/resources/2124/download",
        "filename": "SkinsRestorer.jar"
    },
    {
        "id": "authme",
        "name": "AuthMe Reloaded",
        "category": "Güvenlik & Giriş",
        "desc": "Korsan/ücretsiz sunucularda oyuncuların hesaplarını şifreyle korur (/register, /login).",
        "url": "https://api.spiget.org/v2/resources/6269/download",
        "filename": "AuthMe-Reloaded.jar"
    },
    {
        "id": "spark",
        "name": "Spark Profiler",
        "category": "Analiz & TPS",
        "desc": "Sunucudaki lagın hangi mod, plugin veya chunk'tan kaynaklandığını tespit eder.",
        "url": "https://sparkapi.lucko.me/download/bukkit",
        "filename": "spark.jar"
    },
    {
        "id": "griefprevention",
        "name": "GriefPrevention",
        "category": "Koruma & Claim",
        "desc": "Oyuncuların altın kürekle arazi sahiplenmesini sağlayarak sandık ve ev hırsızlığını engeller.",
        "url": "https://api.spiget.org/v2/resources/1884/download",
        "filename": "GriefPrevention.jar"
    },
    {
        "id": "multiverse",
        "name": "Multiverse-Core",
        "category": "Çoklu Dünya",
        "desc": "Birden çok dünya yönetimi (Ayrı Survival dünyası, Maden dünyası, Skyblock dünyası).",
        "url": "https://api.spiget.org/v2/resources/390/download",
        "filename": "Multiverse-Core.jar"
    },
    {
        "id": "grimac",
        "name": "GrimAC (Next-Gen AntiCheat)",
        "category": "Güvenlik & Hile Önleme",
        "desc": "Modern Minecraft için paket tabanlı, 0 false-positive profesyonel hile engelleme motoru.",
        "url": "https://github.com/GrimAnticheat/Grim/releases/latest/download/GrimAC.jar",
        "filename": "GrimAC.jar"
    },
    {
        "id": "tab",
        "name": "TAB (Scoreboard & Prefix)",
        "category": "Görsel & Tablist",
        "desc": "Gelişmiş animasyonlu Tablist, sağ Scoreboard, oyuncu rütbe ve can göstergeleri.",
        "url": "https://github.com/NEZNAMY/TAB/releases/latest/download/TAB.v4.1.9.jar",
        "filename": "TAB.jar"
    },
    {
        "id": "placeholderapi",
        "name": "PlaceholderAPI (PAPI)",
        "category": "Ekonomi & API",
        "desc": "Tüm ekonomi, rütbe, dünya ve can değişkenlerini TAB ve sohbette gösteren temel köprü.",
        "url": "https://api.spiget.org/v2/resources/6245/download",
        "filename": "PlaceholderAPI.jar"
    },
    {
        "id": "antixray_forge",
        "name": "AntiXray Forge 1.20.1",
        "category": "Hile Engelleme (Mod)",
        "desc": "Forge 1.20.1 sunucularda yeraltı madenlerini gizleyerek X-Ray hilelerini tamamen etkisiz kılar.",
        "url": "https://github.com/astei/antixray-forge/releases/download/v1.4.6+1.20.1/antixray-forge-1.4.6+1.20.1.jar",
        "filename": "antixray-forge-1.4.6+1.20.1.jar",
        "is_mod": True
    }
]

SERVER_PRESETS = {
    "ultimate_rpg_crossplay": {
        "title": "👑 Ultimate Pro RPG, Survival & Crossplay (Full Hazır Paket)",
        "desc": "Mobil & PC Crossplay, GrimAC Anti-Cheat, Canlı Akçe/Ekonomi, TAB Scoreboard, 24 Rol, Türkçe Komutlar ve Anti-Xray koruması.",
        "plugins": ["geyser", "floodgate", "viaversion", "viabackwards", "essentialsx", "luckperms", "vault", "placeholderapi", "tab", "grimac", "chunky", "clearlag"],
        "mods": ["antixray_forge"],
        "deploy_commands": True,
        "deploy_guide": True,
        "deploy_antixray": True,
        "deploy_tab_sync": True
    },
    "safe_crossplay_vanilla": {
        "title": "🛡️ Güvenli Sade Crossplay (Bedrock + Java)",
        "desc": "Arkadaşlarla lag yapmayan, telefon/konsol destekli, GrimAC korumalı ve ViaVersion ile tüm sürümlerden girişe açık sade sunucu.",
        "plugins": ["geyser", "floodgate", "viaversion", "grimac", "chunky", "clearlag", "skinsrestorer"],
        "mods": [],
        "deploy_commands": True,
        "deploy_guide": False,
        "deploy_antixray": False,
        "deploy_tab_sync": False
    },
    "hardcore_towny_economy": {
        "title": "💰 Büyük Ekonomi, Krallık & Arsa Paketi",
        "desc": "Vault, EssentialsX, GriefPrevention arazi koruması, LuckPerms rütbeleri ve pazar ekonomisi.",
        "plugins": ["essentialsx", "vault", "placeholderapi", "luckperms", "griefprevention", "tab", "clearlag", "spark"],
        "mods": [],
        "deploy_commands": True,
        "deploy_guide": True,
        "deploy_antixray": False,
        "deploy_tab_sync": True
    }
}

class PluginModHub:
    def __init__(self, target_dir, log_callback=None):
        self.target_dir = os.path.abspath(target_dir)
        self.plugins_dir = os.path.join(self.target_dir, "plugins")
        self.mods_dir = os.path.join(self.target_dir, "mods")
        self.config_dir = os.path.join(self.target_dir, "config")
        self.log_callback = log_callback or print

    def log(self, msg):
        try:
            self.log_callback(f"[Plugin Hub] {msg}")
        except Exception:
            try:
                clean = msg.encode("ascii", "replace").decode("ascii")
                self.log_callback(f"[Plugin Hub] {clean}")
            except Exception:
                pass

    def get_installed_plugins(self):
        """Lists all installed jar files in plugins directory."""
        if not os.path.exists(self.plugins_dir):
            return []
        return [f for f in os.listdir(self.plugins_dir) if f.lower().endswith(".jar")]

    def is_plugin_installed(self, filename):
        return os.path.exists(os.path.join(self.plugins_dir, filename))

    def install_plugin(self, plugin_info, progress_callback=None):
        """Downloads and installs a plugin or mod into target directory."""
        is_mod = plugin_info.get("is_mod", False)
        dest_dir = self.mods_dir if is_mod else self.plugins_dir
        os.makedirs(dest_dir, exist_ok=True)
        dest_path = os.path.join(dest_dir, plugin_info["filename"])
        url = plugin_info["url"]

        self.log(f"'{plugin_info['name']}' indiriliyor...")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AutoMinecraftServerMaker/4.1.0"})
            with urllib.request.urlopen(req, timeout=45) as resp, open(dest_path, "wb") as out:
                total = int(resp.headers.get("Content-Length", 0))
                downloaded = 0
                while True:
                    chunk = resp.read(65536)
                    if not chunk:
                        break
                    out.write(chunk)
                    downloaded += len(chunk)
                    if total > 0 and progress_callback:
                        pct = int((downloaded / total) * 100)
                        progress_callback(pct, f"%{pct} indirildi")

            target_name = "mods" if is_mod else "plugins"
            self.log(f"✅ '{plugin_info['name']}' başarıyla {target_name} klasörüne kuruldu!")
            return True
        except Exception as e:
            self.log(f"❌ '{plugin_info['name']}' indirme hatası: {e}")
            return False

    def deploy_turkish_commands(self):
        """Generates server commands.yml with rich Turkish aliases."""
        commands_yml_path = os.path.join(self.target_dir, "commands.yml")
        content = """# Auto Minecraft Server Maker - Türkçe Komut Kısayolları ve Alias Haritası
command-block-overrides: []
ignore-vanilla-permissions: false
aliases:
  hewlp:
  - info $1-
  hlp:
  - info $1-
  yardim:
  - info $1-
  komutlar:
  - info $1-
  arsa:
  - plot $1-
  arsalar:
  - plot $1-
  doyur:
  - feed $1-
  para:
  - eco $1-
  bakiye:
  - balance $1-
  takas:
  - trade $1-
  secim:
  - vote $1-
  oy:
  - vote $1-
  spawnagit:
  - spawn $1-
  evim:
  - home $1-
  evkaydet:
  - sethome $1-
"""
        try:
            with open(commands_yml_path, "w", encoding="utf-8") as f:
                f.write(content)
            self.log("✅ Türkçe komut haritası (commands.yml) başarıyla oluşturuldu!")
            return True
        except Exception as e:
            self.log(f"❌ commands.yml hatası: {e}")
            return False

    def deploy_essentials_guide(self):
        """Generates plugins/Essentials/info.txt multi-chapter interactive handbook."""
        ess_dir = os.path.join(self.plugins_dir, "Essentials")
        os.makedirs(ess_dir, exist_ok=True)
        info_path = os.path.join(ess_dir, "info.txt")
        content = """&6=====================================================
&e       ⚔️ SUNUCU REHBERİ & TÜRKÇE KOMUTLAR KİTABI ⚔️
&6=====================================================
&fAşağıdaki sayfalara göz atmak için &e/help <sayfa no>&f yazınız:
&e/help 1 &8- &aTemel Oyuncu Komutları & İletişim
&e/help 2 &8- &bAkçe, Ekonomi & Zenginlik Sistemi
&e/help 3 &8- &6Roller, Meslekler & Devlet Makamları
&e/help 4 &8- &dGüvenli Takas & Pazar Kuralları
&e/help 5 &8- &cArsa / Arazi Sahiplenme & Güvenlik
&6=====================================================

Chapter: 1
&6--- [ 1. SAYFA: TEMEL OYUNCU KOMUTLARI ] ---
&e/spawn &8- &fDoğuş noktasına ışınlanırsınız.
&e/sethome <isim> &8- &fBulunduğunuz yeri eviniz olarak kaydeder.
&e/home <isim> &8- &fKayıtlı evinize tek tıkla dönersiniz.
&e/tpa <oyuncu> &8- &fArkadaşınıza ışınlanma isteği yollar.
&e/tpaccept &8- &fGelen ışınlanma isteğini onaylar.
&e/kit &8- &fÜcretsiz başlangıç ve günlük hediyelerinizi listeler.
&e/msg <oyuncu> <mesaj> &8- &fÖzel fısıldama gönderir.

Chapter: 2
&6--- [ 2. SAYFA: AKÇE & EKONOMİ SİSTEMİ ] ---
&e/para &8veya &e/balance &8- &fCüzdanınızdaki mevcut Akçe miktarını gösterir.
&e/pay <oyuncu> <miktar> &8- &fArkadaşınıza güvenli elden para transferi yapar.
&e/baltop &8- &fSunucunun en zengin milyarderler sıralamasını listeler.
&e/market &8- &fOyun içi ürün alıp satabileceğiniz pazar menüsünü açar.
&aİpucu: &fHer 10 dakikada bir oyunda aktif kalan tüm vatandaşlarımıza devlet maaşı dağıtılır!

Chapter: 3
&6--- [ 3. SAYFA: ROLLER & DEVLET MAKAMLARI ] ---
&e/rol &8- &fMevcut mesleğinizi ve yetkilerinizi görüntüler.
&fSunucumuzda yer alan resmi makamlar:
&c👑 Cumhurbaşkanı &8- &fHalkın seçtiği en yüksek devlet başkanı.
&6🏡 Köy Muhtarı &8- &fBölgesel güvenliği sağlayan yetkili.
&9👮 Polis Memuru &8- &fAsayiş ve düzen koruyucusu.
&2🪖 Asker & Komutan &8- &fDevlet savunma gücü.
&c🩺 Doktor &8- &fŞifa ve iksir ustası.
&5⚖️ Ağır Ceza Hakimi &8- &fAdalet ve ceza dağıtıcısı.
&e💰 Büyük Tüccar &8- &fTicaret ve borsa lideri.
&a🌾 Baş Çiftçi &8- &fGıda ve hasat yöneticisi.

Chapter: 4
&6--- [ 4. SAYFA: GÜVENLİ TAKAS SİSTEMİ ] ---
&e/takas <oyuncu> &8veya &e/trade <oyuncu> &8- &fİki oyuncu arasında dolandırıcılığı imkansız kılan GUI penceresi açar.
&fHer iki taraf da eşyalarını koyduktan sonra yeşil butona basarak onaylar.
&cÖnemli: &fYere eşya atarak ticaret yapmak yasaktır; dolandırılmamak için daima &e/takas&f kullanın!

Chapter: 5
&6--- [ 5. SAYFA: ARSALAR & ARAZİ KORUMASI ] ---
&e/arsa &8veya &e/plot &8- &fArsa menüsünü açar.
&e/trust <oyuncu> &8- &fArsanıza arkadaşınızı ortak eder.
&e/untrust <oyuncu> &8- &fEklenen izni geri alır.
&e/containertrust <oyuncu> &8- &fYalnızca sandık açma izni verir.
&aTebrikler! Artık sunucunun tüm temel kurallarını öğrendiniz. İyi oyunlar dileriz!
"""
        try:
            with open(info_path, "w", encoding="utf-8") as f:
                f.write(content)
            self.log("✅ Çok sayfalı Türkçe rehber kitabı (plugins/Essentials/info.txt) oluşturuldu!")
            return True
        except Exception as e:
            self.log(f"❌ info.txt hatası: {e}")
            return False

    def configure_antixray_forge(self):
        """Generates config/antixray.toml with engineMode = 3 hiding all ores."""
        os.makedirs(self.config_dir, exist_ok=True)
        toml_path = os.path.join(self.config_dir, "antixray.toml")
        content = """# Anti-Xray Forge 1.20.1 Yapilandirmasi
# Otomatik Olarak En Ust Guvenlik Duzeyine (engineMode = 3) Ayarlanmistir.
engineMode = 3
updateRadius = 2
maxBlockHeight = 64
hiddenBlocks = [
    "minecraft:diamond_ore",
    "minecraft:deepslate_diamond_ore",
    "minecraft:ancient_debris",
    "minecraft:gold_ore",
    "minecraft:deepslate_gold_ore",
    "minecraft:iron_ore",
    "minecraft:deepslate_iron_ore",
    "minecraft:emerald_ore",
    "minecraft:deepslate_emerald_ore",
    "minecraft:lapis_ore",
    "minecraft:deepslate_lapis_ore",
    "minecraft:redstone_ore",
    "minecraft:deepslate_redstone_ore",
    "minecraft:copper_ore",
    "minecraft:deepslate_copper_ore",
    "minecraft:coal_ore",
    "minecraft:deepslate_coal_ore",
    "minecraft:nether_gold_ore",
    "minecraft:nether_quartz_ore"
]
replacementBlocks = [
    "minecraft:stone",
    "minecraft:deepslate",
    "minecraft:netherrack"
]
"""
        try:
            with open(toml_path, "w", encoding="utf-8") as f:
                f.write(content)
            self.log("✅ Anti-Xray motoru konfigüre edildi (config/antixray.toml, engineMode=3) ✔")
            return True
        except Exception as e:
            self.log(f"❌ antixray.toml hatası: {e}")
            return False

    def configure_tab_live_sync(self):
        """Configures plugins/TAB/config.yml for 200ms real-time economy & status sync."""
        tab_dir = os.path.join(self.plugins_dir, "TAB")
        os.makedirs(tab_dir, exist_ok=True)
        cfg_path = os.path.join(tab_dir, "config.yml")
        if os.path.exists(cfg_path):
            try:
                text = open(cfg_path, "r", encoding="utf-8", errors="ignore").read()
                # Ensure fast placeholder refresh
                if "placeholderapi-refresh-intervals:" in text:
                    text = text.replace("%vault_eco_balance%: 1000", "%vault_eco_balance%: 200")
                    text = text.replace("%vault_eco_balance_commas%: 1000", "%vault_eco_balance_commas%: 200")
                open(cfg_path, "w", encoding="utf-8").write(text)
                self.log("✅ TAB bakiye yenileme hızı 200ms canlı moda ayarlandı ✔")
                return True
            except Exception as e:
                self.log(f"TAB config ayar hatası: {e}")
        return False

    def install_preset(self, preset_key, progress_callback=None):
        """Installs all components of a chosen server preset."""
        preset = SERVER_PRESETS.get(preset_key)
        if not preset:
            self.log(f"❌ Geçersiz preset anahtarı: {preset_key}")
            return False

        self.log(f"======================================================")
        self.log(f"🚀 Hazır Paket Kuruluyor: {preset['title']}")
        self.log(f"======================================================")

        plugin_map = {p["id"]: p for p in POPULAR_PLUGINS}
        total_items = len(preset.get("plugins", [])) + len(preset.get("mods", []))
        done = 0

        # 1. Install plugins
        for pid in preset.get("plugins", []):
            pinfo = plugin_map.get(pid)
            if pinfo:
                self.install_plugin(pinfo)
            done += 1
            if progress_callback:
                progress_callback(int((done / max(1, total_items)) * 100), f"Kuruluyor: {pid}")

        # 2. Install mods
        for mid in preset.get("mods", []):
            minfo = plugin_map.get(mid)
            if minfo:
                self.install_plugin(minfo)
            done += 1
            if progress_callback:
                progress_callback(int((done / max(1, total_items)) * 100), f"Kuruluyor: {mid}")

        # 3. Post-install configurations
        if preset.get("deploy_commands"):
            self.deploy_turkish_commands()
        if preset.get("deploy_guide"):
            self.deploy_essentials_guide()
        if preset.get("deploy_antixray"):
            self.configure_antixray_forge()
        if preset.get("deploy_tab_sync"):
            self.configure_tab_live_sync()

        self.log(f"======================================================")
        self.log(f"✅ HAZIR SUNUCU PAKETİ BAŞARIYLA KURULDU!")
        self.log(f"======================================================")
        return True

