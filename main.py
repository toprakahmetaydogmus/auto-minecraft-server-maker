# -*- coding: utf-8 -*-
"""
⚔️ AUTO MINECRAFT SERVER MAKER & AI ENGINEER PRO (v3.0 ULTRA)
===================================================================================
- Autonomous Minecraft Server Creator (10+ Flavors: Paper, Purpur, Fabric, Forge, NeoForge, Arclight, Mohist, Velocity, Vanilla, BDS)
- 12+ AI Engines Integrated (NVIDIA NIM, OpenRouter, OpenAI, Claude, Gemini, Groq, Mistral, Together, Perplexity, Cohere, DeepSeek, Ollama)
- Autonomous Local Offline AI Hub (1-Click Ollama Setup & Streaming Model Puller)
- 1-Click Global Tunnel (Playit.gg & UPnP - Play with friends without port forwarding)
- 1-Click Plugin & Mod Hub (20+ High-Performance Plugins)
- Visual server.properties Editor
- World Backup & 1-Click Restore Manager
- Master Admin Control Panel (380+ Commands, Universal Block Hub, Themed Shulker Kits)
- Live CPU, RAM & Server Process Telemetry
- 100% Zero-Leak Security Architecture (Isolated Local Vault)
"""

import os
import sys
import time
import socket
import threading

# 1. Autonomous Dependency Bootstrap (Self-installs missing packages on any PC)
try:
    from core.dependency_bootstrap import ensure_dependencies
    ensure_dependencies()
except Exception:
    pass

# 2. Critical protection for PyInstaller --noconsole where stdout/stderr are None
class NullWriter:
    def write(self, s):
        pass
    def flush(self):
        pass

if sys.stdout is None:
    sys.stdout = NullWriter()
if sys.stderr is None:
    sys.stderr = NullWriter()

import customtkinter as ctk
from tkinter import messagebox

from ui.modern_theme import *
from core.config_manager import ConfigManager
from core.lan_broadcaster import LanBroadcaster
from core.hardware_monitor import HardwareMonitor

from ui.ctk_tab_installer import CTkTabInstaller
from ui.ctk_tab_ai_engineer import CTkTabAIEngineer
from ui.ctk_tab_tunnel import CTkTabTunnel
from ui.ctk_tab_plugins import CTkTabPlugins
from ui.ctk_tab_properties import CTkTabProperties
from ui.ctk_tab_backup import CTkTabBackup
from ui.ctk_tab_admin_panel import CTkTabAdminPanel
from ui.ctk_tab_settings import CTkTabSettings

# Configure CustomTkinter Global Theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class AutoMinecraftServerMakerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("⚔️ Auto Minecraft Server Maker & AI Engineer Pro (v3.0)")
        self.geometry("1340x940")
        self.minsize(1160, 780)
        self.configure(fg_color=COLOR_BG_DARK)

        self.config_manager = ConfigManager()
        self.lan_broadcaster = None
        self.active_tab_btn = None

        self._build_layout()
        self._start_background_workers()

    def _build_layout(self):
        # Ana Izgara: Sol Sidebar (260px) + Sağ İçerik Alanı
        self.grid_columnconfigure(0, weight=0, minsize=260)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 1. SOL SIDEBAR
        self.sidebar = ctk.CTkFrame(self, fg_color=COLOR_BG_SIDEBAR, corner_radius=0, width=260)
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.sidebar.grid_propagate(False)

        # Sidebar Logo / Başlık
        logo_f = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        logo_f.pack(fill="x", padx=16, pady=(16, 14))

        ctk.CTkLabel(
            logo_f,
            text="⚡ SERVER MAKER PRO",
            font=FONT_TITLE,
            text_color=COLOR_ACCENT_CYAN,
            anchor="w"
        ).pack(anchor="w")

        ctk.CTkLabel(
            logo_f,
            text="v3.0 Ultra • 100% Zero-Leak",
            font=FONT_SMALL,
            text_color=COLOR_TEXT_MUTED,
            anchor="w"
        ).pack(anchor="w")

        # Canlı Sunucu Durumu Rozeti
        self.status_badge = ctk.CTkLabel(
            self.sidebar,
            text="● KONTROL EDILIYOR...",
            font=FONT_BOLD,
            text_color=COLOR_ACCENT_GOLD,
            fg_color="#2a2312",
            corner_radius=6,
            height=30
        )
        self.status_badge.pack(fill="x", padx=14, pady=(0, 14))

        # Navigasyon Butonları Listesi
        self.nav_btns = {}
        nav_items = [
            ("installer", "🚀 Sunucu Kurucu", self._show_installer),
            ("ai", "🤖 AI Mühendisi & Teşhis", self._show_ai),
            ("tunnel", "🌐 Global Tünel (Playit)", self._show_tunnel),
            ("plugins", "🔌 1-Tıkla Eklenti Hub", self._show_plugins),
            ("properties", "⚙️ Görsel server.prop", self._show_properties),
            ("backup", "💾 Dünya Yedekleme", self._show_backup),
            ("admin", "🎮 Master Admin Paneli", self._show_admin),
            ("settings", "🔑 Ayarlar & API Kasası", self._show_settings)
        ]

        for key, text, cmd in nav_items:
            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                font=FONT_BOLD,
                anchor="w",
                height=38,
                corner_radius=8,
                fg_color="transparent",
                text_color=COLOR_TEXT_MAIN,
                hover_color=COLOR_BG_CARD_HOVER,
                command=cmd
            )
            btn.pack(fill="x", padx=12, pady=2)
            self.nav_btns[key] = btn

        # Alt Telemetri ve Donanım Barı
        tele_card = ctk.CTkFrame(self.sidebar, fg_color=COLOR_BG_CARD, corner_radius=10, border_width=1, border_color=COLOR_BORDER)
        tele_card.pack(side="bottom", fill="x", padx=12, pady=14)

        ctk.CTkLabel(tele_card, text="📊 DONANIM TELEMETRİSİ", font=FONT_SMALL, text_color=COLOR_ACCENT_GOLD).pack(anchor="w", padx=10, pady=(8, 4))

        self.lbl_cpu = ctk.CTkLabel(tele_card, text="CPU: %0", font=FONT_SMALL, text_color=COLOR_TEXT_MAIN)
        self.lbl_cpu.pack(anchor="w", padx=10, pady=1)

        self.lbl_ram = ctk.CTkLabel(tele_card, text="RAM: 0GB / 0GB", font=FONT_SMALL, text_color=COLOR_TEXT_MAIN)
        self.lbl_ram.pack(anchor="w", padx=10, pady=1)

        self.ram_progress = ctk.CTkProgressBar(tele_card, height=6, progress_color=COLOR_ACCENT_GREEN)
        self.ram_progress.set(0.3)
        self.ram_progress.pack(fill="x", padx=10, pady=(4, 8))

        # 2. SAĞ İÇERİK ALANI
        self.content_area = ctk.CTkFrame(self, fg_color="transparent")
        self.content_area.grid(row=0, column=1, sticky="nsew", padx=16, pady=14)
        self.content_area.grid_columnconfigure(0, weight=1)
        self.content_area.grid_rowconfigure(0, weight=1)

        # Sekme Örnekleri
        self.tabs = {
            "installer": CTkTabInstaller(self.content_area, self.config_manager),
            "ai": CTkTabAIEngineer(self.content_area, self.config_manager),
            "tunnel": CTkTabTunnel(self.content_area, self.config_manager),
            "plugins": CTkTabPlugins(self.content_area, self.config_manager),
            "properties": CTkTabProperties(self.content_area, self.config_manager),
            "backup": CTkTabBackup(self.content_area, self.config_manager),
            "admin": CTkTabAdminPanel(self.content_area, self.config_manager),
            "settings": CTkTabSettings(self.content_area, self.config_manager)
        }

        # Varsayılan sekme: Sunucu Kurucu
        self._show_installer()

    def _switch_tab(self, key):
        for k, view in self.tabs.items():
            if k == key:
                view.grid(row=0, column=0, sticky="nsew")
                self.nav_btns[k].configure(fg_color=COLOR_ACCENT_CYAN, text_color="#000000")
            else:
                view.grid_forget()
                self.nav_btns[k].configure(fg_color="transparent", text_color=COLOR_TEXT_MAIN)

    def _show_installer(self): self._switch_tab("installer")
    def _show_ai(self): self._switch_tab("ai")
    def _show_tunnel(self): self._switch_tab("tunnel")
    def _show_plugins(self): self._switch_tab("plugins")
    def _show_properties(self): self._switch_tab("properties")
    def _show_backup(self): self._switch_tab("backup")
    def _show_admin(self): self._switch_tab("admin")
    def _show_settings(self): self._switch_tab("settings")

    def _start_background_workers(self):
        # 1. LAN Broadcaster (Yerel ağ ve VPN - Radmin/Hamachi otomatik yayın)
        srv_cfg = self.config_manager.get_server_config()
        self.lan_broadcaster = LanBroadcaster(port=srv_cfg.get("server_port", 25565))
        self.lan_broadcaster.start()

        # 2. Donanım & Sunucu Durum İzleyici Worker
        threading.Thread(target=self._telemetry_worker, daemon=True).start()

    def _telemetry_worker(self):
        while True:
            srv_cfg = self.config_manager.get_server_config()
            port = srv_cfg.get("server_port", 25565)

            # Check server port
            is_online = False
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                res = s.connect_ex(("127.0.0.1", port))
                s.close()
                is_online = (res == 0)
            except Exception:
                is_online = False

            # Check hardware metrics
            m = HardwareMonitor.get_system_metrics()

            def _update_ui():
                if is_online:
                    self.status_badge.configure(text=f"● SUNUCU AKTİF ({port})", text_color=COLOR_ACCENT_GREEN, fg_color="#064e3b")
                else:
                    self.status_badge.configure(text="● SUNUCU KAPALI", text_color=COLOR_ACCENT_RED, fg_color="#450a0a")

                self.lbl_cpu.configure(text=f"CPU: %{m['cpu_percent']}")
                self.lbl_ram.configure(text=f"RAM: {m['ram_used_gb']}GB / {m['ram_total_gb']}GB")
                self.ram_progress.set(m['ram_percent'] / 100.0)

            self.after(0, _update_ui)
            time.sleep(2.5)


def main():
    try:
        app = AutoMinecraftServerMakerApp()
        app.mainloop()
    except Exception as e:
        import traceback
        err_msg = f"Uygulama çalışırken beklenmedik bir hata oluştu:\n\n{e}\n\nDetay:\n{traceback.format_exc()}"
        try:
            messagebox.showerror("Kritik Hata", err_msg)
        except Exception:
            pass
        sys.exit(1)

if __name__ == "__main__":
    main()
