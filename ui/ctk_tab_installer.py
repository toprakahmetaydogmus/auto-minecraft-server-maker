# -*- coding: utf-8 -*-
"""
Modern CustomTkinter Tab: Autonomous Server Installer & Launcher Pro
Incorporates all features from the official video:
- "RAKAMLARA BAK" 4-Metric Showcase Banner
- 10+ Server Flavors with 1-Click Pill Selector
- 1.7.10 -> 1.21.4 Complete Version Matrix
- Dynamic Java Compatibility Watcher & 1-Click Adoptium Java JRE Downloader
- macOS/Linux Style Developer Terminal with Live Progress Bar
- Glowing "SUNUCU ÇALIŞIYOR" Status Indicator
- "Yapay Zekâ Çökme Doktoru" (AI Crash Doctor)
- Bedrock & Console Crossplay (Geyser + Floodgate)
"""

import os
import time
import socket
import subprocess
import threading
import customtkinter as ctk
from tkinter import messagebox

from ui.modern_theme import *
from core.server_installer import ServerInstaller
from core.java_detector import JavaDetector

class CTkTabInstaller(ctk.CTkFrame):
    def __init__(self, master, config_manager, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.config_manager = config_manager
        self.server_process = None
        self.flavor_pills = {}

        self._build_ui()
        self._update_java_status()
        self._start_server_watcher()

    def _build_ui(self):
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=6)
        self.grid_rowconfigure(1, weight=1)

        # =====================================================================
        # ÜST BANNER: "RAKAMLARA BAK" (4-KART METRİK VİTRİNİ)
        # =====================================================================
        stats_banner = ctk.CTkFrame(self, fg_color=COLOR_BG_CARD, corner_radius=12, border_width=1, border_color=COLOR_BORDER)
        stats_banner.grid(row=0, column=0, columnspan=2, sticky="ew", padx=0, pady=(0, 10))

        # 4 Metrik Kartı Izgarası
        for col_idx in range(4):
            stats_banner.grid_columnconfigure(col_idx, weight=1)

        metrics = [
            ("10+ SUNUCU TÜRÜ", "Paper • Purpur • Fabric • Forge...", COLOR_ACCENT_GREEN),
            ("1.7 ➔ 1.21.4", "Tüm Sürümler (Eskiden Yeniye)", COLOR_ACCENT_CYAN),
            ("12 AI MOTORU", "Ollama: %100 Ücretsiz & Çevrimdışı", COLOR_ACCENT_PURPLE),
            ("380+ ADMİN KOMUTU", "300+ Blok • 16 Kategori Sekmesi", COLOR_ACCENT_GOLD),
        ]

        for idx, (title, sub, color) in enumerate(metrics):
            card = ctk.CTkFrame(stats_banner, fg_color=COLOR_BG_CARD_HOVER, corner_radius=8, border_width=1, border_color=color)
            card.grid(row=0, column=idx, padx=8, pady=8, sticky="nsew")

            ctk.CTkLabel(card, text=title, font=("Segoe UI", 11, "bold"), text_color=color).pack(anchor="center", pady=(6, 1))
            ctk.CTkLabel(card, text=sub, font=FONT_SMALL, text_color=COLOR_TEXT_MUTED).pack(anchor="center", pady=(0, 6))

        # =====================================================================
        # SOL KART: Kurulum Parametreleri & 1-Tıkla Pill Seçici
        # =====================================================================
        left_card = ctk.CTkScrollableFrame(self, fg_color=COLOR_BG_CARD, corner_radius=12, border_width=1, border_color=COLOR_BORDER)
        left_card.grid(row=1, column=0, sticky="nsew", padx=(0, 10), pady=0)

        ctk.CTkLabel(left_card, text="🚀 TEK TIKLA SUNUCU KURUCU", font=FONT_SUBTITLE, text_color=COLOR_ACCENT_CYAN).pack(anchor="w", pady=(4, 10))

        # 1. 10+ Sunucu Türü Pill Seçici
        ctk.CTkLabel(left_card, text="⚙️ Sunucu Yazılımı (10+ Tür):", font=FONT_BOLD, text_color=COLOR_TEXT_MAIN).pack(anchor="w", pady=(2, 4))
        
        pills_frame = ctk.CTkFrame(left_card, fg_color="transparent")
        pills_frame.pack(fill="x", pady=(0, 10))
        for p_col in range(3):
            pills_frame.grid_columnconfigure(p_col, weight=1)

        flavor_list = [
            ("PaperMC", "PaperMC (Yüksek Performans)"),
            ("Purpur", "Purpur (Optimize & Özellik Zengin)"),
            ("Fabric", "Fabric (Hafif & Hızlı Modlu)"),
            ("Arclight", "Arclight (Forge + Plugin Hibrit)"),
            ("Mohist", "Mohist (Forge + Bukkit Alternatif)"),
            ("Forge", "Forge (Klasik Modlu)"),
            ("NeoForge", "NeoForge (Yeni Nesil Modlu 1.20.4+)"),
            ("Velocity", "Velocity (Yeni Nesil Proxy)"),
            ("Vanilla", "Vanilla (Resmi Saf Mojang)")
        ]

        self.flavor_var = ctk.StringVar(value="PaperMC (Yüksek Performans)")

        for p_idx, (short_name, full_name) in enumerate(flavor_list):
            r = p_idx // 3
            c = p_idx % 3
            btn = ctk.CTkButton(
                pills_frame,
                text=short_name,
                font=FONT_SMALL,
                height=28,
                corner_radius=6,
                fg_color=COLOR_ACCENT_CYAN if p_idx == 0 else COLOR_BG_CARD_HOVER,
                text_color="#000000" if p_idx == 0 else COLOR_TEXT_MAIN,
                hover_color=COLOR_ACCENT_CYAN,
                command=lambda fn=full_name, sn=short_name: self._select_flavor(fn, sn)
            )
            btn.grid(row=r, column=c, padx=3, pady=3, sticky="ew")
            self.flavor_pills[short_name] = btn

        # 2. Minecraft Sürümü (1.7.10 -> 1.21.4)
        ctk.CTkLabel(left_card, text="📌 Minecraft Sürümü:", font=FONT_BOLD, text_color=COLOR_TEXT_MAIN).pack(anchor="w", pady=(2, 2))
        self.ver_var = ctk.StringVar(value="1.20.1")
        self.ver_menu = ctk.CTkOptionMenu(
            left_card,
            variable=self.ver_var,
            values=[
                "1.21.4", "1.21.3", "1.21.1", "1.20.6", "1.20.4", "1.20.2", "1.20.1",
                "1.19.4", "1.19.2", "1.18.2", "1.17.1", "1.16.5", "1.12.2", "1.8.9", "1.7.10"
            ],
            fg_color=COLOR_BG_CARD_HOVER,
            button_color=COLOR_ACCENT_CYAN,
            button_hover_color="#0284c7",
            command=lambda v: self._update_java_status()
        )
        self.ver_menu.pack(fill="x", pady=(0, 10))

        # 3. Java Durumu ve Uyuşmazlık Çözümü
        ctk.CTkLabel(left_card, text="☕ Java Uyumluluk Durumu:", font=FONT_BOLD, text_color=COLOR_TEXT_MAIN).pack(anchor="w", pady=(2, 2))
        self.java_badge_frame = ctk.CTkFrame(left_card, fg_color=COLOR_BG_CARD_HOVER, corner_radius=6)
        self.java_badge_frame.pack(fill="x", pady=(0, 10))

        self.lbl_java_info = ctk.CTkLabel(self.java_badge_frame, text="Kontrol ediliyor...", font=FONT_SMALL, text_color=COLOR_TEXT_MAIN)
        self.lbl_java_info.pack(side="left", padx=10, pady=6)

        self.btn_download_java = ctk.CTkButton(
            self.java_badge_frame,
            text="⚡ Java İndir",
            font=FONT_SMALL,
            width=90,
            height=24,
            fg_color=COLOR_ACCENT_GOLD,
            text_color="#000000",
            hover_color="#f59e0b",
            command=self._download_recommended_java
        )

        # 4. RAM Bellek Ayarı
        ctk.CTkLabel(left_card, text="💾 Bellek (RAM) Dağılımı:", font=FONT_BOLD, text_color=COLOR_TEXT_MAIN).pack(anchor="w", pady=(2, 2))
        ram_frame = ctk.CTkFrame(left_card, fg_color="transparent")
        ram_frame.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(ram_frame, text="Min:", font=FONT_SMALL, text_color=COLOR_TEXT_MUTED).pack(side="left", padx=(0, 4))
        self.min_ram_var = ctk.StringVar(value="4")
        self.min_ram_menu = ctk.CTkOptionMenu(ram_frame, variable=self.min_ram_var, values=["2", "4", "6", "8", "12", "16"], width=68, fg_color=COLOR_BG_CARD_HOVER)
        self.min_ram_menu.pack(side="left", padx=(0, 14))

        ctk.CTkLabel(ram_frame, text="Max:", font=FONT_SMALL, text_color=COLOR_TEXT_MUTED).pack(side="left", padx=(0, 4))
        self.max_ram_var = ctk.StringVar(value="6")
        self.max_ram_menu = ctk.CTkOptionMenu(ram_frame, variable=self.max_ram_var, values=["4", "6", "8", "10", "12", "16", "24", "32"], width=68, fg_color=COLOR_BG_CARD_HOVER)
        self.max_ram_menu.pack(side="left")

        # 5. Geyser Bedrock Crossplay Switch
        self.geyser_switch = ctk.CTkSwitch(
            left_card,
            text="📱 Mobil & Konsol Crossplay (Geyser + Floodgate)",
            font=FONT_BOLD,
            text_color=COLOR_ACCENT_GREEN,
            progress_color=COLOR_ACCENT_GREEN
        )
        self.geyser_switch.select()
        self.geyser_switch.pack(anchor="w", pady=(2, 14))

        # 6. Tek Tıkla Kurulum Butonu
        self.btn_install = ctk.CTkButton(
            left_card,
            text="⚡ TEK TIKLA İNDİR & KUR",
            font=FONT_TITLE,
            fg_color=COLOR_ACCENT_CYAN,
            text_color="#000000",
            hover_color="#38bdf8",
            height=44,
            corner_radius=8,
            command=self.start_installation
        )
        self.btn_install.pack(fill="x", pady=(0, 10))

        # 7. Başlat & Durdur Butonları
        ctrl_frame = ctk.CTkFrame(left_card, fg_color="transparent")
        ctrl_frame.pack(fill="x", pady=(0, 8))

        self.btn_start = ctk.CTkButton(
            ctrl_frame,
            text="▶️ Başlat",
            font=FONT_BOLD,
            fg_color=COLOR_ACCENT_GREEN,
            text_color="#000000",
            hover_color="#34d399",
            height=40,
            corner_radius=8,
            command=self.start_server
        )
        self.btn_start.pack(side="left", fill="x", expand=True, padx=(0, 4))

        self.btn_stop = ctk.CTkButton(
            ctrl_frame,
            text="⏹️ Durdur",
            font=FONT_BOLD,
            fg_color=COLOR_ACCENT_RED,
            text_color="#ffffff",
            hover_color="#dc2626",
            height=40,
            corner_radius=8,
            command=self.stop_server
        )
        self.btn_stop.pack(side="right", fill="x", expand=True, padx=(4, 0))

        # =====================================================================
        # SAĞ KART: macOS/Linux Stili Terminal & Canlı Konsol
        # =====================================================================
        right_card = ctk.CTkFrame(self, fg_color=COLOR_BG_CARD, corner_radius=12, border_width=1, border_color=COLOR_BORDER)
        right_card.grid(row=1, column=1, sticky="nsew", padx=0, pady=0)
        right_card.grid_columnconfigure(0, weight=1)
        right_card.grid_rowconfigure(2, weight=1)

        # Terminal Pencere Başlığı
        term_header = ctk.CTkFrame(right_card, fg_color="#0a0f1d", corner_radius=8)
        term_header.grid(row=0, column=0, sticky="ew", padx=12, pady=(12, 6))

        # Pencere Noktaları (Kırmızı, Sarı, Yeşil)
        dots_frame = ctk.CTkFrame(term_header, fg_color="transparent")
        dots_frame.pack(side="left", padx=10, pady=8)

        ctk.CTkLabel(dots_frame, text="●", font=("Segoe UI", 12), text_color="#ef4444").pack(side="left", padx=2)
        ctk.CTkLabel(dots_frame, text="●", font=("Segoe UI", 12), text_color="#f59e0b").pack(side="left", padx=2)
        ctk.CTkLabel(dots_frame, text="●", font=("Segoe UI", 12), text_color="#10b981").pack(side="left", padx=2)

        ctk.CTkLabel(term_header, text="auto-minecraft-server-maker", font=FONT_CODE, text_color=COLOR_TEXT_MUTED).pack(side="left", padx=6)

        # Sağ Aksiyonlar: AI Çökme Doktoru & Temizle
        btn_clear = ctk.CTkButton(
            term_header,
            text="Temizle",
            font=FONT_SMALL,
            width=60,
            height=24,
            fg_color=COLOR_BG_CARD_HOVER,
            hover_color=COLOR_BORDER,
            command=lambda: self.console.delete("1.0", "end")
        )
        btn_clear.pack(side="right", padx=(6, 8))

        btn_ai_doctor = ctk.CTkButton(
            term_header,
            text="🩺 AI Çökme Doktoru",
            font=FONT_SMALL,
            width=140,
            height=24,
            fg_color=COLOR_ACCENT_PURPLE,
            text_color="#ffffff",
            hover_color="#7c3aed",
            command=self.ai_heal_error
        )
        btn_ai_doctor.pack(side="right")

        # İndirme İlerleme Çubuğu ve Durumu (Progress Bar)
        prog_frame = ctk.CTkFrame(right_card, fg_color="transparent")
        prog_frame.grid(row=1, column=0, sticky="ew", padx=14, pady=(2, 6))

        self.dl_status_label = ctk.CTkLabel(prog_frame, text="Hazır • Sen sadece Başlat'a bas", font=FONT_SMALL, text_color=COLOR_ACCENT_CYAN, anchor="w")
        self.dl_status_label.pack(side="left", fill="x", expand=True)

        self.dl_progress = ctk.CTkProgressBar(prog_frame, height=8, corner_radius=4, progress_color=COLOR_ACCENT_CYAN)
        self.dl_progress.set(0.0)
        self.dl_progress.pack(side="right", fill="x", expand=True, padx=(10, 0))

        # Terminal Metin Kutusu
        self.console = ctk.CTkTextbox(
            right_card,
            fg_color="#030712",
            text_color="#e2e8f0",
            font=FONT_CODE,
            corner_radius=8,
            border_width=1,
            border_color=COLOR_BORDER
        )
        self.console.grid(row=2, column=0, sticky="nsew", padx=14, pady=(0, 10))

        # Alt Canlı Durum Rozeti (Video Stili: SUNUCU ÇALIŞIYOR)
        self.live_server_badge = ctk.CTkLabel(
            right_card,
            text="⚪ SUNUCU KAPALI",
            font=FONT_BOLD,
            text_color=COLOR_TEXT_MUTED,
            fg_color="#1e293b",
            corner_radius=6,
            height=32
        )
        self.live_server_badge.grid(row=3, column=0, sticky="ew", padx=14, pady=(0, 12))

        self.log("⚔️ Auto Minecraft Server Maker PRO (v3.2.0 Ultra) hazır.")
        self.log("> Tek tıkla. Sıfır dert.")
        self.log("> Kuruyor. Yönetiyor. Onarıyor.\n")

    def _select_flavor(self, full_name, short_name):
        self.flavor_var.set(full_name)
        for sname, btn in self.flavor_pills.items():
            if sname == short_name:
                btn.configure(fg_color=COLOR_ACCENT_CYAN, text_color="#000000")
            else:
                btn.configure(fg_color=COLOR_BG_CARD_HOVER, text_color=COLOR_TEXT_MAIN)

    def _update_java_status(self):
        mc_ver = self.ver_var.get().strip()
        req_java = JavaDetector.get_recommended_java_for_mc(mc_ver)
        sys_j = JavaDetector.get_system_java()

        if sys_j and sys_j["version"] > 0:
            cur_j = sys_j["version"]
            if cur_j >= req_java:
                self.lbl_java_info.configure(
                    text=f"✔ Java {cur_j} Algılandı (Gerekli: Java {req_java} LTS - Uyumlu)",
                    text_color=COLOR_ACCENT_GREEN
                )
                self.btn_download_java.pack_forget()
            else:
                self.lbl_java_info.configure(
                    text=f"⚠️ Java {req_java} Gerekli! (Sistemde Java {cur_j} var)",
                    text_color=COLOR_ACCENT_RED
                )
                self.btn_download_java.configure(text=f"⚡ Java {req_java} İndir")
                self.btn_download_java.pack(side="right", padx=10, pady=6)
        else:
            self.lbl_java_info.configure(
                text=f"⚠️ Java Bulunamadı! (Java {req_java} Gerekli)",
                text_color=COLOR_ACCENT_RED
            )
            self.btn_download_java.configure(text=f"⚡ Java {req_java} İndir")
            self.btn_download_java.pack(side="right", padx=10, pady=6)

    def _download_recommended_java(self):
        mc_ver = self.ver_var.get().strip()
        req_java = JavaDetector.get_recommended_java_for_mc(mc_ver)
        self.log(f"[*] Resmi Eclipse Temurin Java {req_java} indirme sayfası açılıyor...")
        JavaDetector.open_java_download_page(req_java)

    def log(self, text):
        self.console.insert("end", f"{text}\n")
        self.console.see("end")

    def _on_download_progress(self, pct, downloaded, total_size):
        def _update():
            frac = max(0.0, min(1.0, pct / 100.0))
            self.dl_progress.set(frac)
            if total_size > 0:
                mb_down = downloaded // (1024 * 1024)
                mb_tot = total_size // (1024 * 1024)
                self.dl_status_label.configure(text=f"İndiriliyor: %{pct} ({mb_down} MB / {mb_tot} MB)")
            else:
                self.dl_status_label.configure(text=f"İndiriliyor: {downloaded // (1024 * 1024)} MB")
        self.after(0, _update)

    def start_installation(self):
        cfg = self.config_manager.get_server_config()
        sdir = cfg.get("server_dir", os.path.join(os.getcwd(), "server"))

        ver = self.ver_var.get().strip()
        raw_flavor = self.flavor_var.get().split(" ")[0].lower()
        min_r = int(self.min_ram_var.get() or "4")
        max_r = int(self.max_ram_var.get() or "6")
        r_port = cfg.get("rcon_port", 25575)
        r_pass = cfg.get("rcon_password", "admin123")
        s_port = cfg.get("server_port", 25565)
        b_port = cfg.get("bedrock_port", 19132)
        geyser = self.geyser_switch.get() == 1

        self.btn_install.configure(state="disabled", text="⏳ Kuruluyor...")
        self.dl_progress.set(0.05)
        self.dl_status_label.configure(text=f"{raw_flavor.capitalize()} {ver} indiriliyor...")

        def _worker():
            installer = ServerInstaller(
                sdir,
                log_callback=lambda msg: self.after(0, self.log, msg),
                progress_callback=self._on_download_progress
            )
            success = installer.setup_server(
                server_type=raw_flavor,
                mc_version=ver,
                min_ram=min_r,
                max_ram=max_r,
                rcon_port=r_port,
                rcon_pass=r_pass,
                server_port=s_port,
                bedrock_port=b_port,
                install_geyser=geyser
            )
            def _finish():
                self.btn_install.configure(state="normal", text="⚡ TEK TIKLA İNDİR & KUR")
                if success:
                    self.dl_progress.set(1.0)
                    self.dl_status_label.configure(text="✅ Kurulum Tamamlandı! Başlat'a basabilirsiniz.")
                    self.log("\n🎉 Sunucu kurulumu başarıyla tamamlandı!")
                    self.log("Artık 'Başlat' butonuna basarak sunucunuzu açabilirsiniz.\n")
                    messagebox.showinfo("Kurulum Başarılı", f"✅ {ver} sunucusu hazırlandı!\nKonum: {sdir}")
                else:
                    self.dl_status_label.configure(text="❌ Kurulum Başarısız")
                    self.log("❌ Kurulum sırasında bir hata oluştu.")
                    messagebox.showerror("Hata", "Kurulum başarısız oldu. Konsol loglarını kontrol ediniz.")
            self.after(0, _finish)

        threading.Thread(target=_worker, daemon=True).start()

    def start_server(self):
        cfg = self.config_manager.get_server_config()
        sdir = cfg.get("server_dir", os.path.join(os.getcwd(), "server"))
        bat_file = os.path.join(sdir, "start.bat")
        if not os.path.exists(bat_file):
            messagebox.showerror("Hata", f"Başlatıcı dosyası bulunamadı:\n{bat_file}\nLütfen önce 'Tek Tıkla İndir & Kur' butonuna basınız.")
            return

        self.log(f"> Sunucu başlatılıyor: {bat_file}")
        self.live_server_badge.configure(text="⏳ SUNUCU BAŞLATILIYOR...", text_color=COLOR_ACCENT_GOLD, fg_color="#2a2312")
        threading.Thread(target=lambda: subprocess.Popen(["cmd.exe", "/c", "start", "", bat_file], cwd=sdir), daemon=True).start()

    def stop_server(self):
        cfg = self.config_manager.get_server_config()
        self.log("> Sunucu durdurma komutu gönderiliyor (/stop)...")
        from core.rcon_client import MinecraftRcon
        rcon = MinecraftRcon(
            host=cfg.get("rcon_host", "127.0.0.1"),
            port=cfg.get("rcon_port", 25575),
            password=cfg.get("rcon_password", "admin123")
        )
        def _stop():
            res = rcon.send_command("stop")
            self.after(0, self.log, f">> {res}")
        threading.Thread(target=_stop, daemon=True).start()

    def ai_heal_error(self):
        """Captures recent console logs and crash reports for instant AI diagnosis."""
        raw_text = self.console.get("1.0", "end").strip()
        lines = [line for line in raw_text.split("\n") if line.strip()]
        recent_logs = "\n".join(lines[-40:]) if lines else "Henüz log çıktısı yok."

        # Also check crash-reports folder if exists
        cfg = self.config_manager.get_server_config()
        sdir = cfg.get("server_dir", os.path.join(os.getcwd(), "server"))
        crash_dir = os.path.join(sdir, "crash-reports")
        crash_content = ""
        if os.path.exists(crash_dir):
            reports = sorted([os.path.join(crash_dir, f) for f in os.listdir(crash_dir) if f.endswith(".txt")], key=os.path.getmtime, reverse=True)
            if reports:
                try:
                    with open(reports[0], "r", encoding="utf-8", errors="ignore") as f:
                        crash_content = f"\n[EN SON CRASH RAPORU ({os.path.basename(reports[0])})]:\n" + f.read()[:2000]
                except Exception:
                    pass

        ver = self.ver_var.get()
        flavor = self.flavor_var.get()

        self.log("\n🤖 [Yapay Zekâ Çökme Doktoru] Hata ve çökme raporları analiz ediliyor...")
        def _worker():
            try:
                from core.ai_engineer import AIEngineer
                ai = AIEngineer(self.config_manager)
                full_context = f"{recent_logs}\n{crash_content}"
                solution = ai.analyze_log_error(full_context)
                self.after(0, self.log, f"\n🩺 [AI ÇÖKME DOKTORU TEŞHİS & ÇÖZÜM REÇETESİ]:\n{solution}\n")
            except Exception as e:
                self.after(0, self.log, f"❌ AI teşhis motoru hatası: {e}")
        threading.Thread(target=_worker, daemon=True).start()

    def _start_server_watcher(self):
        def _worker():
            while True:
                cfg = self.config_manager.get_server_config()
                port = cfg.get("server_port", 25565)
                is_online = False
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.5)
                    res = s.connect_ex(("127.0.0.1", port))
                    s.close()
                    is_online = (res == 0)
                except Exception:
                    is_online = False

                def _update():
                    if not self.winfo_exists():
                        return
                    if is_online:
                        self.live_server_badge.configure(
                            text=f"🟢 SUNUCU ÇALIŞIYOR (Port: {port}) • Arkadaşların Bağlanabilir!",
                            text_color=COLOR_ACCENT_GREEN,
                            fg_color="#064e3b"
                        )
                        self.btn_start.configure(state="disabled")
                        self.btn_stop.configure(state="normal")
                    else:
                        self.live_server_badge.configure(
                            text="⚪ SUNUCU KAPALI • Sen sadece Başlat'a bas",
                            text_color=COLOR_TEXT_MUTED,
                            fg_color="#1e293b"
                        )
                        self.btn_start.configure(state="normal")
                        self.btn_stop.configure(state="disabled")

                try:
                    self.after(0, _update)
                except Exception:
                    break
                time.sleep(2.5)

        threading.Thread(target=_worker, daemon=True).start()
