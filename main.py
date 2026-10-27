# -*- coding: utf-8 -*-
"""
⚔️ AUTO MINECRAFT SERVER MAKER & AI ENGINEER PRO (v3.2.0 ULTRA)
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
import traceback

# 1. Critical protection for PyInstaller --noconsole where stdout/stderr are None
class NullWriter:
    def write(self, s):
        pass
    def flush(self):
        pass

if sys.stdout is None:
    sys.stdout = NullWriter()
if sys.stderr is None:
    sys.stderr = NullWriter()

# 2. Global Uncaught Exception Hook for Reliable Debugging
def fatal_excepthook(exc_type, exc_value, exc_traceback):
    err = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    try:
        base = os.path.dirname(sys.executable) if getattr(sys, "frozen", False) else os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(base, "app_crash.log"), "w", encoding="utf-8") as f:
            f.write(err)
    except Exception:
        pass
    try:
        from tkinter import messagebox
        messagebox.showerror("Kritik Hata", f"Uygulama çalıştırılırken beklenmeyen bir hata oluştu:\n\n{exc_value}\n\nDetaylar app_crash.log dosyasına kaydedildi.")
    except Exception:
        pass

sys.excepthook = fatal_excepthook

# 3. Single-Instance Mutex Socket (Prevents duplicate instances from choking the PC)
_single_instance_socket = None
def acquire_single_instance_lock():
    global _single_instance_socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1", 49152))
        s.listen(1)
        _single_instance_socket = s
        return True
    except OSError:
        return False

# 4. Autonomous Dependency Bootstrap (Self-installs missing packages in dev mode only)
try:
    from core.dependency_bootstrap import ensure_dependencies
    ensure_dependencies()
except Exception:
    pass

import customtkinter as ctk
from tkinter import messagebox

from ui.modern_theme import *
from ui.theme import apply_global_theme
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

        self.title("⚔️ Auto Minecraft Server Maker & AI Engineer Pro (v3.2.0 Ultra)")
        self.geometry("1360x920")
        self.minsize(1180, 780)
        self.configure(fg_color=COLOR_BG_DARK)

        apply_global_theme(self)

        self.config_manager = ConfigManager()
        self.lan_broadcaster = None
        self.active_tab_btn = None
        self.tabs = {}

        self._build_layout()
        self._start_background_workers()

    def _build_layout(self):
        # Ana Izgara: Sol Sidebar (270px) + Sağ İçerik Alanı
        self.grid_columnconfigure(0, weight=0, minsize=270)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 1. SOL SIDEBAR
        self.sidebar = ctk.CTkFrame(self, fg_color=COLOR_BG_SIDEBAR, corner_radius=0, width=270)
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.sidebar.grid_propagate(False)

        # Sidebar Logo / Başlık Kartı
        logo_f = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        logo_f.pack(fill="x", padx=16, pady=(16, 10))

        ctk.CTkLabel(
            logo_f,
            text="⚡ AUTO MINECRAFT",
            font=FONT_TITLE,
            text_color=COLOR_ACCENT_CYAN,
            anchor="w"
        ).pack(anchor="w")

        ctk.CTkLabel(
            logo_f,
            text="SERVER MAKER PRO",
            font=("Segoe UI", 12, "bold"),
            text_color=COLOR_TEXT_MAIN,
            anchor="w"
        ).pack(anchor="w")

        ctk.CTkLabel(
            logo_f,
            text="v3.2.0 ULTRA • Tek tıkla. Sıfır dert.",
            font=FONT_SMALL,
            text_color=COLOR_ACCENT_GREEN,
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
            height=32
        )
        self.status_badge.pack(fill="x", padx=14, pady=(0, 12))

        # Navigasyon Butonları & Kategorileri
        self.nav_btns = {}
        nav_structure = [
            ("⚡ SUNUCU & YÖNETİM", [
                ("installer", "🚀 Sunucu Kurucu", self._show_installer),
                ("admin", "🎮 Master Admin Paneli", self._show_admin),
                ("properties", "⚙️ server.properties", self._show_properties),
            ]),
            ("🌐 GLOBAL AĞ & EKLENTİ", [
                ("tunnel", "🌍 Global Tünel (Playit)", self._show_tunnel),
                ("plugins", "🔌 1-Tıkla Eklenti Hub", self._show_plugins),
                ("backup", "💾 Dünya & Yedekleme", self._show_backup),
            ]),
            ("🧠 YAPAY ZEKA & AYARLAR", [
                ("ai", "🩺 AI Çökme Doktoru & Mühendis", self._show_ai),
                ("settings", "🔑 API Kasası & Ayarlar", self._show_settings)
            ])
        ]

        for section_title, items in nav_structure:
            ctk.CTkLabel(
                self.sidebar,
                text=section_title,
                font=("Segoe UI", 9, "bold"),
                text_color=COLOR_ACCENT_GOLD,
                anchor="w"
            ).pack(fill="x", padx=16, pady=(10, 2))

            for key, text, cmd in items:
                btn = ctk.CTkButton(
                    self.sidebar,
                    text=text,
                    font=FONT_BOLD,
                    anchor="w",
                    height=36,
                    corner_radius=8,
                    fg_color="transparent",
                    text_color=COLOR_TEXT_MAIN,
                    hover_color=COLOR_BG_CARD_HOVER,
                    command=cmd
                )
                btn.pack(fill="x", padx=12, pady=2)
                self.nav_btns[key] = btn

        # Alt Donanım Telemetrisi Kartı
        tele_card = ctk.CTkFrame(self.sidebar, fg_color=COLOR_BG_CARD, corner_radius=10, border_width=1, border_color=COLOR_BORDER)
        tele_card.pack(side="bottom", fill="x", padx=12, pady=14)

        ctk.CTkLabel(tele_card, text="📊 CANLI DONANIM TELEMETRİSİ", font=FONT_SMALL, text_color=COLOR_ACCENT_CYAN).pack(anchor="w", padx=10, pady=(8, 4))

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

        # Varsayılan sekme: Sunucu Kurucu
        self._show_installer()

    def _switch_tab(self, key):
        # Lazy Loading: Sadece tıklandığında sekme örneğini oluştur
        if key not in self.tabs:
            tab_factories = {
                "installer": lambda: CTkTabInstaller(self.content_area, self.config_manager),
                "ai": lambda: CTkTabAIEngineer(self.content_area, self.config_manager),
                "tunnel": lambda: CTkTabTunnel(self.content_area, self.config_manager),
                "plugins": lambda: CTkTabPlugins(self.content_area, self.config_manager),
                "properties": lambda: CTkTabProperties(self.content_area, self.config_manager),
                "backup": lambda: CTkTabBackup(self.content_area, self.config_manager),
                "admin": lambda: CTkTabAdminPanel(self.content_area, self.config_manager),
                "settings": lambda: CTkTabSettings(self.content_area, self.config_manager)
            }
            if key in tab_factories:
                self.tabs[key] = tab_factories[key]()

        for k, view in self.tabs.items():
            if k == key:
                view.grid(row=0, column=0, sticky="nsew")
                if k in self.nav_btns:
                    self.nav_btns[k].configure(fg_color=COLOR_ACCENT_CYAN, text_color="#000000")
            else:
                view.grid_forget()
                if k in self.nav_btns:
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
                if not self.winfo_exists():
                    return
                if is_online:
                    self.status_badge.configure(text=f"● SUNUCU AKTİF (Port: {port})", text_color=COLOR_ACCENT_GREEN, fg_color="#064e3b")
                else:
                    self.status_badge.configure(text="● SUNUCU KAPALI", text_color=COLOR_ACCENT_RED, fg_color="#450a0a")

                self.lbl_cpu.configure(text=f"CPU: %{m['cpu_percent']}")
                self.lbl_ram.configure(text=f"RAM: {m['ram_used_gb']}GB / {m['ram_total_gb']}GB")
                self.ram_progress.set(m['ram_percent'] / 100.0)

            try:
                self.after(0, _update_ui)
            except Exception:
                break
            time.sleep(2.5)


def main():
    # Enforce Single-Instance Mutex
    if not acquire_single_instance_lock():
        try:
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo(
                "Zaten Çalışıyor",
                "Auto Minecraft Server Maker zaten arka planda veya görev çubuğunda çalışıyor!\nLütfen açık olan pencereyi kullanın."
            )
            root.destroy()
        except Exception:
            pass
        sys.exit(0)

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

