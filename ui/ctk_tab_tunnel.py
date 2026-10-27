# -*- coding: utf-8 -*-
"""
Modern CustomTkinter Tab: Global Tunnel & Port Forwarding (Playit.gg & UPnP)
Enables hassle-free multiplayer with friends without touching router settings.
"""

import threading
import customtkinter as ctk
from tkinter import messagebox

from ui.modern_theme import *
from core.tunnel_manager import TunnelManager

class CTkTabTunnel(ctk.CTkFrame):
    def __init__(self, master, config_manager, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.config_manager = config_manager
        self.tunnel = TunnelManager(log_callback=self._on_log)

        self._build_ui()

    def _build_ui(self):
        self.grid_columnconfigure(0, weight=1)

        # Kart 1: Playit.gg 1-Tıkla Global Tünel
        card1 = ctk.CTkFrame(self, fg_color=COLOR_BG_CARD, corner_radius=12, border_width=1, border_color=COLOR_BORDER)
        card1.pack(fill="x", padx=0, pady=(0, 12))

        c1_head = ctk.CTkFrame(card1, fg_color="transparent")
        c1_head.pack(fill="x", padx=16, pady=(12, 4))
        ctk.CTkLabel(c1_head, text="🌐 PLAYIT.GG GLOBAL TÜNEL (Modemsiz Arkadaş Oynatma)", font=FONT_SUBTITLE, text_color=COLOR_ACCENT_CYAN).pack(side="left")

        desc = (
            "Modem şifrenizi bilmiyorsanız veya CGNAT havuzundaysanız (port açamıyorsanız), "
            "Playit.gg arka planda ücretsiz ve güvenli bir genel tünel oluşturur.\n"
            "Arkadaşlarınıza verebileceğiniz 'ornek.gl.at.ply.gg:12345' şeklinde bir bağlantı adresi sağlar."
        )
        ctk.CTkLabel(card1, text=desc, font=FONT_REGULAR, text_color=COLOR_TEXT_MUTED, justify="left").pack(anchor="w", padx=16, pady=(0, 10))

        btn_row = ctk.CTkFrame(card1, fg_color="transparent")
        btn_row.pack(fill="x", padx=16, pady=(0, 14))

        self.btn_playit = ctk.CTkButton(
            btn_row,
            text="⚡ Playit.gg Tünelini Başlat",
            font=FONT_BOLD,
            fg_color=COLOR_ACCENT_GREEN,
            text_color="#000000",
            hover_color="#34d399",
            height=36,
            command=self._start_playit
        )
        self.btn_playit.pack(side="left", padx=(0, 10))

        btn_stop = ctk.CTkButton(
            btn_row,
            text="⏹️ Tüneli Durdur",
            font=FONT_BOLD,
            fg_color=COLOR_ACCENT_RED,
            hover_color="#dc2626",
            height=36,
            command=self._stop_tunnel
        )
        btn_stop.pack(side="left")

        # Kart 2: UPnP Port Yönlendirme
        card2 = ctk.CTkFrame(self, fg_color=COLOR_BG_CARD, corner_radius=12, border_width=1, border_color=COLOR_BORDER)
        card2.pack(fill="x", padx=0, pady=(0, 12))

        c2_head = ctk.CTkFrame(card2, fg_color="transparent")
        c2_head.pack(fill="x", padx=16, pady=(12, 4))
        ctk.CTkLabel(c2_head, text="📡 OTOMATİK MODEM UPNP PORT TESTİ", font=FONT_SUBTITLE, text_color=COLOR_ACCENT_GOLD).pack(side="left")

        ctk.CTkLabel(card2, text="Modeminizin UPnP özelliği açıksa, portları otomatik eşleyerek harici program olmadan doğrudan bağlanılmasını sağlar.", font=FONT_REGULAR, text_color=COLOR_TEXT_MUTED).pack(anchor="w", padx=16, pady=(0, 10))

        btn_upnp = ctk.CTkButton(
            card2,
            text="🔍 Modem UPnP Port Yönlendirmeyi Dene (Port 25565)",
            font=FONT_BOLD,
            fg_color=COLOR_BG_CARD_HOVER,
            hover_color=COLOR_BORDER,
            height=34,
            command=self._test_upnp
        )
        btn_upnp.pack(anchor="w", padx=16, pady=(0, 14))

        # Kart 3: Log Konsolu
        card3 = ctk.CTkFrame(self, fg_color=COLOR_BG_CARD, corner_radius=12, border_width=1, border_color=COLOR_BORDER)
        card3.pack(fill="both", expand=True, padx=0, pady=0)

        ctk.CTkLabel(card3, text="📜 TÜNEL VE BAĞLANTI DURUMU", font=FONT_BOLD, text_color=COLOR_TEXT_MAIN).pack(anchor="w", padx=16, pady=(10, 6))

        self.tunnel_log = ctk.CTkTextbox(card3, fg_color="#030712", text_color="#f8fafc", font=FONT_CODE, corner_radius=8)
        self.tunnel_log.pack(fill="both", expand=True, padx=16, pady=(0, 14))

        self._on_log("Tünel yöneticisi hazır. Modemsiz oynamak için 'Playit.gg Tünelini Başlat' butonuna basınız.")

    def _on_log(self, msg):
        self.after(0, lambda: self._insert_log(msg))

    def _insert_log(self, msg):
        self.tunnel_log.insert("end", f"{msg}\n")
        self.tunnel_log.see("end")

    def _start_playit(self):
        self.btn_playit.configure(state="disabled", text="⏳ Başlatılıyor...")
        def _worker():
            self.tunnel.start_playit()
            self.after(0, lambda: self.btn_playit.configure(state="normal", text="⚡ Playit.gg Tünelini Başlat"))
        threading.Thread(target=_worker, daemon=True).start()

    def _stop_tunnel(self):
        self.tunnel.stop_tunnel()
        messagebox.showinfo("Tünel", "Tünel servisi durduruldu.")

    def _test_upnp(self):
        cfg = self.config_manager.get_server_config()
        port = cfg.get("server_port", 25565)
        def _worker():
            self.tunnel.try_upnp_port_forward(port)
        threading.Thread(target=_worker, daemon=True).start()
