# -*- coding: utf-8 -*-
"""
⚔️ AUTO MINECRAFT SERVER MAKER & AI ENGINEER PRO
===================================================================================
- Autonomous Minecraft Server Maker (Any Version, Any Flavor)
- 12+ AI Providers Integrated (NVIDIA NIM, OpenRouter, OpenAI, Anthropic, Gemini,
  Groq, Mistral, Together, Perplexity, Cohere, DeepSeek, Ollama)
- Master Admin Control Panel (380+ Commands, Universal Block Hub, Themed Shulker Kits)
- 100% Zero-Leak Security Architecture (No hardcoded keys/secrets)
"""

import os
import sys
import time
import socket
import threading
import tkinter as tk
from tkinter import ttk, messagebox

from ui.theme import *
from core.config_manager import ConfigManager
from core.lan_broadcaster import LanBroadcaster
from ui.tab_installer import TabInstaller
from ui.tab_ai_engineer import TabAIEngineer
from ui.tab_admin_panel import TabAdminPanel
from ui.tab_settings import TabSettings

class AutoMinecraftServerMakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⚔️ Auto Minecraft Server Maker & AI Engineer Pro")
        self.root.geometry("1300x920")
        self.root.minsize(1120, 760)

        self.config_manager = ConfigManager()
        self.lan_broadcaster = None

        apply_global_theme(self.root)
        self._build_header()
        self._build_tabs()

        self._start_background_workers()

    def _build_header(self):
        header = tk.Frame(self.root, bg=BG_PANEL, height=50, padx=16, pady=8)
        header.pack(fill=tk.X, side=tk.TOP)

        title_lbl = tk.Label(
            header,
            text="⚡ AUTO MINECRAFT SERVER MAKER & AI ENGINEER",
            font=("Segoe UI", 12, "bold"),
            fg=ACCENT_GOLD,
            bg=BG_PANEL
        )
        title_lbl.pack(side=tk.LEFT)

        self.status_lbl = tk.Label(
            header,
            text="● KONTROL EDILIYOR...",
            font=("Segoe UI", 8, "bold"),
            fg=ACCENT_GOLD,
            bg="#2a2312",
            padx=8,
            pady=3
        )
        self.status_lbl.pack(side=tk.LEFT, padx=12)

        srv_cfg = self.config_manager.get_server_config()
        port = srv_cfg.get("server_port", 25565)
        ip_lbl = tk.Label(
            header,
            text=f"🌐 Port: {port} | Bedrock: {srv_cfg.get('bedrock_port', 19132)} | RCON: {srv_cfg.get('rcon_port', 25575)}",
            font=("Segoe UI", 8, "bold"),
            fg=ACCENT_CYAN,
            bg=BG_PANEL
        )
        ip_lbl.pack(side=tk.LEFT, padx=6)

        ver_lbl = tk.Label(
            header,
            text="v2.5 Pro | 100% Zero-Leak",
            font=("Segoe UI", 8),
            fg=TEXT_MUTED,
            bg=BG_PANEL
        )
        ver_lbl.pack(side=tk.RIGHT, padx=6)

    def _build_tabs(self):
        self.main_notebook = ttk.Notebook(self.root)
        self.main_notebook.pack(fill=tk.BOTH, expand=True, padx=8, pady=4)

        # Tab 1: Otomatik Kurucu
        self.tab_inst = TabInstaller(self.main_notebook, self.config_manager)
        self.main_notebook.add(self.tab_inst.frame, text="  🚀 Otomatik Sunucu Kurucu  ")

        # Tab 2: AI Sunucu Mühendisi
        self.tab_ai = TabAIEngineer(self.main_notebook, self.config_manager)
        self.main_notebook.add(self.tab_ai.frame, text="  🤖 AI Sunucu Mühendisi (12 Motor)  ")

        # Tab 3: Master Admin Paneli
        self.tab_admin = TabAdminPanel(self.main_notebook, self.config_manager)
        self.main_notebook.add(self.tab_admin.frame, text="  🎮 Master Admin Paneli & Blok Hub  ")

        # Tab 4: Ayarlar & API Anahtarları
        self.tab_sett = TabSettings(self.main_notebook, self.config_manager)
        self.main_notebook.add(self.tab_sett.frame, text="  ⚙️ Ayarlar & API Kasası  ")

    def _start_background_workers(self):
        # LAN Broadcast
        srv_cfg = self.config_manager.get_server_config()
        self.lan_broadcaster = LanBroadcaster(port=srv_cfg.get("server_port", 25565))
        self.lan_broadcaster.start()

        # Status Checker
        threading.Thread(target=self._status_worker, daemon=True).start()

    def _status_worker(self):
        while True:
            srv_cfg = self.config_manager.get_server_config()
            port = srv_cfg.get("server_port", 25565)
            is_online = False
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.6)
                res = s.connect_ex(("127.0.0.1", port))
                s.close()
                is_online = (res == 0)
            except Exception:
                is_online = False

            if is_online:
                self.root.after(0, lambda: self.status_lbl.configure(text=f"● SUNUCU AKTİF (Port {port})", fg=ACCENT_GREEN, bg="#064e3b"))
            else:
                self.root.after(0, lambda: self.status_lbl.configure(text="● SUNUCU KAPALI", fg=ACCENT_RED, bg="#450a0a"))

            time.sleep(3)


def main():
    root = tk.Tk()
    app = AutoMinecraftServerMakerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
