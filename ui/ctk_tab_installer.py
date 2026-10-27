# -*- coding: utf-8 -*-
"""
Modern CustomTkinter Tab: Autonomous Server Installer & Launcher
Supports 10+ server flavors, modern sliders, live console, and Aikar G1GC flags.
"""

import os
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

        self._build_ui()

    def _build_ui(self):
        # 2 Sütunlu Izgara Düzeni
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=6)
        self.grid_rowconfigure(0, weight=1)

        # SOL KART: Kurulum Parametreleri
        left_card = ctk.CTkScrollableFrame(self, fg_color=COLOR_BG_CARD, corner_radius=12, border_width=1, border_color=COLOR_BORDER)
        left_card.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=0)

        lbl_head = ctk.CTkLabel(left_card, text="🚀 OTOMATİK SUNUCU KURUCU", font=FONT_SUBTITLE, text_color=COLOR_ACCENT_CYAN)
        lbl_head.pack(anchor="w", pady=(4, 14))

        # 1. Minecraft Sürümü
        ctk.CTkLabel(left_card, text="📌 Minecraft Sürümü:", font=FONT_BOLD, text_color=COLOR_TEXT_MAIN).pack(anchor="w", pady=(2, 2))
        self.ver_var = ctk.StringVar(value="1.20.1")
        self.ver_menu = ctk.CTkOptionMenu(
            left_card,
            variable=self.ver_var,
            values=["1.21.4", "1.21.1", "1.20.4", "1.20.1", "1.19.4", "1.18.2", "1.16.5", "1.12.2", "1.8.9", "1.7.10"],
            fg_color=COLOR_BG_CARD_HOVER,
            button_color=COLOR_ACCENT_CYAN,
            button_hover_color="#0284c7"
        )
        self.ver_menu.pack(fill="x", pady=(0, 12))

        # 2. Sunucu Yazılımı (10+ Farklı Seçenek)
        ctk.CTkLabel(left_card, text="⚙️ Sunucu Yazılımı (Flavor):", font=FONT_BOLD, text_color=COLOR_TEXT_MAIN).pack(anchor="w", pady=(2, 2))
        self.flavor_var = ctk.StringVar(value="PaperMC (Yüksek Performans)")
        self.flavor_menu = ctk.CTkOptionMenu(
            left_card,
            variable=self.flavor_var,
            values=[
                "PaperMC (Yüksek Performans)",
                "Purpur (Optimize & Özellik Zengin)",
                "Fabric (Hafif & Hızlı Modlu)",
                "Arclight (Forge + Plugin Hibrit)",
                "Mohist (Forge + Bukkit Alternatif)",
                "Forge (Klasik Modlu)",
                "NeoForge (Yeni Nesil Modlu 1.20.4+)",
                "Velocity (Yeni Nesil Proxy)",
                "BungeeCord (Klasik Proxy)",
                "Vanilla (Resmi Saf Mojang)"
            ],
            fg_color=COLOR_BG_CARD_HOVER,
            button_color=COLOR_ACCENT_PURPLE,
            button_hover_color="#7c3aed"
        )
        self.flavor_menu.pack(fill="x", pady=(0, 12))

        # 3. RAM Ayarı
        ctk.CTkLabel(left_card, text="💾 Bellek (RAM) Dağılımı:", font=FONT_BOLD, text_color=COLOR_TEXT_MAIN).pack(anchor="w", pady=(2, 2))
        ram_frame = ctk.CTkFrame(left_card, fg_color="transparent")
        ram_frame.pack(fill="x", pady=(0, 12))

        ctk.CTkLabel(ram_frame, text="Min:", font=FONT_SMALL, text_color=COLOR_TEXT_MUTED).pack(side="left", padx=(0, 4))
        self.min_ram_var = ctk.StringVar(value="4")
        self.min_ram_menu = ctk.CTkOptionMenu(ram_frame, variable=self.min_ram_var, values=["2", "4", "6", "8", "12", "16"], width=64, fg_color=COLOR_BG_CARD_HOVER)
        self.min_ram_menu.pack(side="left", padx=(0, 14))

        ctk.CTkLabel(ram_frame, text="Max:", font=FONT_SMALL, text_color=COLOR_TEXT_MUTED).pack(side="left", padx=(0, 4))
        self.max_ram_var = ctk.StringVar(value="6")
        self.max_ram_menu = ctk.CTkOptionMenu(ram_frame, variable=self.max_ram_var, values=["4", "6", "8", "10", "12", "16", "24", "32"], width=64, fg_color=COLOR_BG_CARD_HOVER)
        self.max_ram_menu.pack(side="left")

        # 4. Geyser Bedrock Crossplay Switch
        self.geyser_switch = ctk.CTkSwitch(
            left_card,
            text="📱 Bedrock Crossplay (Geyser & Floodgate)",
            font=FONT_BOLD,
            text_color=COLOR_ACCENT_GREEN,
            progress_color=COLOR_ACCENT_GREEN
        )
        self.geyser_switch.select()
        self.geyser_switch.pack(anchor="w", pady=(4, 14))

        # 5. Algılanan Java Sürümü
        ctk.CTkLabel(left_card, text="☕ Sistemdeki Java Durumu:", font=FONT_BOLD, text_color=COLOR_TEXT_MAIN).pack(anchor="w", pady=(2, 2))
        sys_j = JavaDetector.get_system_java()
        j_text = f"Java {sys_j['version']} LTS Algılandı" if sys_j and sys_j['version'] > 0 else "Java Bulunamadı ⚠️"
        j_color = COLOR_ACCENT_GREEN if sys_j and sys_j['version'] >= 17 else COLOR_ACCENT_RED

        self.java_badge = ctk.CTkLabel(
            left_card,
            text=j_text,
            font=FONT_BOLD,
            text_color=j_color,
            fg_color=COLOR_BG_CARD_HOVER,
            corner_radius=6,
            height=30
        )
        self.java_badge.pack(fill="x", pady=(0, 18))

        # 6. Kurulum Butonu
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
        ctrl_frame.pack(fill="x", pady=(4, 6))

        self.btn_start = ctk.CTkButton(
            ctrl_frame,
            text="▶️ Başlat",
            font=FONT_BOLD,
            fg_color=COLOR_ACCENT_GREEN,
            text_color="#000000",
            hover_color="#34d399",
            height=38,
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
            height=38,
            corner_radius=8,
            command=self.stop_server
        )
        self.btn_stop.pack(side="right", fill="x", expand=True, padx=(4, 0))

        # SAĞ KART: Canlı Konsol ve Log Ekranı
        right_card = ctk.CTkFrame(self, fg_color=COLOR_BG_CARD, corner_radius=12, border_width=1, border_color=COLOR_BORDER)
        right_card.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        right_card.grid_columnconfigure(0, weight=1)
        right_card.grid_rowconfigure(1, weight=1)

        # Konsol Başlığı
        log_header = ctk.CTkFrame(right_card, fg_color="transparent")
        log_header.grid(row=0, column=0, sticky="ew", padx=14, pady=(12, 6))

        ctk.CTkLabel(log_header, text="📜 KURULUM & SUNUCU CANLI KONSOLU", font=FONT_SUBTITLE, text_color=COLOR_ACCENT_GOLD).pack(side="left")

        btn_clear = ctk.CTkButton(
            log_header,
            text="Temizle",
            font=FONT_SMALL,
            width=64,
            height=24,
            fg_color=COLOR_BG_CARD_HOVER,
            hover_color=COLOR_BORDER,
            command=lambda: self.console.delete("1.0", "end")
        )
        btn_clear.pack(side="right", padx=(6, 0))

        btn_ai_heal = ctk.CTkButton(
            log_header,
            text="🤖 AI ile Hatayı Çöz",
            font=FONT_SMALL,
            width=130,
            height=24,
            fg_color=COLOR_ACCENT_PURPLE,
            hover_color="#7c3aed",
            command=self.ai_heal_error
        )
        btn_ai_heal.pack(side="right")


        # Konsol Metin Kutusu
        self.console = ctk.CTkTextbox(
            right_card,
            fg_color="#030712",
            text_color="#e2e8f0",
            font=FONT_CODE,
            corner_radius=8,
            border_width=1,
            border_color=COLOR_BORDER
        )
        self.console.grid(row=1, column=0, sticky="nsew", padx=14, pady=(0, 14))

        self.log("⚡ Auto Minecraft Server Maker PRO hazır. Sürüm ve tür seçip 'Tek Tıkla İndir & Kur' butonuna basabilirsiniz.")

    def log(self, text):
        self.console.insert("end", f"{text}\n")
        self.console.see("end")

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

        def _worker():
            installer = ServerInstaller(sdir, log_callback=lambda msg: self.after(0, self.log, msg))
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
            self.after(0, lambda: self.btn_install.configure(state="normal", text="⚡ TEK TIKLA İNDİR & KUR"))
            if success:
                self.after(0, self.log, "🎉 Sunucu kurulumu başarıyla tamamlandı! Artık 'Başlat' butonuna basabilirsiniz.")
                self.after(0, messagebox.showinfo, "Kurulum Başarılı", f"✅ {ver} sunucusu hazırlandı!\nKonum: {sdir}")
            else:
                self.after(0, self.log, "❌ Kurulum sırasında bir hata oluştu.")
                self.after(0, messagebox.showerror, "Hata", "Kurulum başarısız oldu. Konsol loglarını kontrol ediniz.")

        threading.Thread(target=_worker, daemon=True).start()

    def start_server(self):
        cfg = self.config_manager.get_server_config()
        sdir = cfg.get("server_dir", os.path.join(os.getcwd(), "server"))
        bat_file = os.path.join(sdir, "start.bat")
        if not os.path.exists(bat_file):
            messagebox.showerror("Hata", f"Başlatıcı dosyası bulunamadı:\n{bat_file}\nLütfen önce sunucuyu kurunuz.")
            return

        self.log(f"[*] Sunucu başlatılıyor: {bat_file}")
        threading.Thread(target=lambda: subprocess.Popen(["cmd.exe", "/c", "start", "", bat_file], cwd=sdir), daemon=True).start()

    def ai_heal_error(self):
        """Captures recent console logs and sends to AI for instant diagnosis & fix."""
        raw_text = self.console.get("1.0", "end").strip()
        lines = [line for line in raw_text.split("\n") if line.strip()]
        recent_logs = "\n".join(lines[-40:]) if lines else "Henüz bir log çıktısı yok."

        ver = self.ver_var.get()
        flavor = self.flavor_var.get()

        self.log("\n🤖 [AI Otonom Teşhis] Konsol günlükleri inceleniyor, lütfen bekleyiniz...")
        def _worker():
            try:
                from core.ai_engineer import AIEngineer
                ai = AIEngineer(self.config_manager)
                solution = ai.diagnose_installation_error(flavor, ver, recent_logs)
                self.after(0, self.log, f"\n💡 [AI ÇÖZÜM REÇETESİ]:\n{solution}\n")
            except Exception as e:
                self.after(0, self.log, f"❌ AI teşhis motoru hatası: {e}")
        threading.Thread(target=_worker, daemon=True).start()

    def stop_server(self):
        cfg = self.config_manager.get_server_config()
        self.log("[*] Sunucu durdurma komutu gönderiliyor (stop)...")
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

