# -*- coding: utf-8 -*-
"""
Modern CustomTkinter Tab: Global Tunnel & Multiplayer Hub (Playit.gg & UPnP)
Matches Video Feature 1/4:
"ARKADAŞLARIN ANINDA GİRSİN: Playit.gg tüneli + otomatik UPnP. Port açma yok, modem şifresi yok."
"""

import re
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
        self.extracted_address = None

        self._build_ui()

    def _build_ui(self):
        self.grid_columnconfigure(0, weight=1)

        # 1. Video Banner: "ARKADAŞLARIN ANINDA GİRSİN"
        hero_card = ctk.CTkFrame(self, fg_color=COLOR_BG_CARD, corner_radius=12, border_width=1, border_color=COLOR_ACCENT_CYAN)
        hero_card.pack(fill="x", padx=0, pady=(0, 10))

        h_inner = ctk.CTkFrame(hero_card, fg_color="transparent")
        h_inner.pack(fill="x", padx=16, pady=10)

        ctk.CTkLabel(h_inner, text="🌐 ARKADAŞLARIN ANINDA GİRSİN", font=FONT_TITLE, text_color=COLOR_ACCENT_CYAN).pack(anchor="w")
        ctk.CTkLabel(
            h_inner,
            text="Playit.gg tüneli + otomatik UPnP port yönlendirme • Port açma yok, modem şifresi yok.",
            font=FONT_REGULAR,
            text_color=COLOR_TEXT_MAIN
        ).pack(anchor="w", pady=(2, 0))

        # 2. Hızlı Bağlantı Adresi ve Kopyalama Kutusu
        addr_card = ctk.CTkFrame(self, fg_color=COLOR_BG_CARD_HOVER, corner_radius=10, border_width=1, border_color=COLOR_BORDER)
        addr_card.pack(fill="x", padx=0, pady=(0, 10))

        addr_row = ctk.CTkFrame(addr_card, fg_color="transparent")
        addr_row.pack(fill="x", padx=14, pady=10)

        ctk.CTkLabel(addr_row, text="🔗 Sunucu Paylaşım Adresi:", font=FONT_BOLD, text_color=COLOR_ACCENT_GOLD).pack(side="left", padx=(0, 10))

        self.lbl_address = ctk.CTkEntry(
            addr_row,
            font=FONT_CODE,
            height=32,
            fg_color="#030712",
            text_color=COLOR_ACCENT_GREEN,
            border_color=COLOR_BORDER
        )
        self.lbl_address.insert(0, "Tünel başlatıldığında adres burada belirecektir (örn: ornek.gl.at.ply.gg:12345)")
        self.lbl_address.configure(state="readonly")
        self.lbl_address.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.btn_copy = ctk.CTkButton(
            addr_row,
            text="📋 Adresi Kopyala",
            font=FONT_BOLD,
            width=130,
            height=32,
            fg_color=COLOR_ACCENT_CYAN,
            text_color="#000000",
            hover_color="#38bdf8",
            command=self._copy_address
        )
        self.btn_copy.pack(side="right")

        # 3. Kontrol Butonları Kartı
        ctrl_card = ctk.CTkFrame(self, fg_color=COLOR_BG_CARD, corner_radius=12, border_width=1, border_color=COLOR_BORDER)
        ctrl_card.pack(fill="x", padx=0, pady=(0, 10))

        ctrl_inner = ctk.CTkFrame(ctrl_card, fg_color="transparent")
        ctrl_inner.pack(fill="x", padx=16, pady=10)

        self.btn_playit = ctk.CTkButton(
            ctrl_inner,
            text="⚡ Playit.gg Tünelini Başlat",
            font=FONT_BOLD,
            fg_color=COLOR_ACCENT_GREEN,
            text_color="#000000",
            hover_color="#34d399",
            height=38,
            command=self._start_playit
        )
        self.btn_playit.pack(side="left", padx=(0, 10))

        self.btn_stop = ctk.CTkButton(
            ctrl_inner,
            text="⏹️ Tüneli Kapat",
            font=FONT_BOLD,
            fg_color=COLOR_ACCENT_RED,
            hover_color="#dc2626",
            height=38,
            command=self._stop_tunnel
        )
        self.btn_stop.pack(side="left", padx=(0, 14))

        self.btn_upnp = ctk.CTkButton(
            ctrl_inner,
            text="📡 Modem UPnP Test Et (Port 25565)",
            font=FONT_BOLD,
            fg_color=COLOR_BG_CARD_HOVER,
            hover_color=COLOR_BORDER,
            height=38,
            command=self._test_upnp
        )
        self.btn_upnp.pack(side="left")

        # 4. Canlı Tünel Konsolu
        log_card = ctk.CTkFrame(self, fg_color=COLOR_BG_CARD, corner_radius=12, border_width=1, border_color=COLOR_BORDER)
        log_card.pack(fill="both", expand=True, padx=0, pady=0)

        ctk.CTkLabel(log_card, text="📜 TÜNEL VE BAĞLANTI DURUM LOGLARI", font=FONT_BOLD, text_color=COLOR_TEXT_MAIN).pack(anchor="w", padx=16, pady=(10, 6))

        self.tunnel_log = ctk.CTkTextbox(log_card, fg_color="#030712", text_color="#f8fafc", font=FONT_CODE, corner_radius=8)
        self.tunnel_log.pack(fill="both", expand=True, padx=16, pady=(0, 14))

        self._on_log("🌐 Tünel yöneticisi hazır.")
        self._on_log("> Modemsiz arkadaşlarınızla oynamak için 'Playit.gg Tünelini Başlat' butonuna basınız.")

    def _on_log(self, msg):
        self.after(0, lambda: self._insert_log(msg))

    def _insert_log(self, msg):
        self.tunnel_log.insert("end", f"{msg}\n")
        self.tunnel_log.see("end")

        # Otomatik bağlantı adresi yakalama (ornek.ply.gg:12345)
        match = re.search(r'([a-zA-Z0-9\.\-]+\.(?:ply\.gg|playit\.gg)(?::\d+)?)', msg)
        if match:
            addr = match.group(1)
            self.extracted_address = addr
            self.lbl_address.configure(state="normal")
            self.lbl_address.delete(0, "end")
            self.lbl_address.insert(0, addr)
            self.lbl_address.configure(state="readonly")

    def _copy_address(self):
        text = self.lbl_address.get()
        if "ornek" not in text and text.strip():
            self.clipboard_clear()
            self.clipboard_append(text.strip())
            messagebox.showinfo("Kopyalandı", f"✅ Tünel bağlantı adresi panoya kopyalandı:\n\n{text.strip()}\n\nArkadaşlarınıza bu IP'yi gönderebilirsiniz!")
        else:
            messagebox.showwarning("Uyarı", "Lütfen önce tüneli başlatıp bağlantı adresinin oluşmasını bekleyiniz.")

    def _start_playit(self):
        self.btn_playit.configure(state="disabled", text="⏳ Başlatılıyor...")
        def _worker():
            self.tunnel.start_playit()
            self.after(0, lambda: self.btn_playit.configure(state="normal", text="⚡ Playit.gg Tünelini Başlat"))
        threading.Thread(target=_worker, daemon=True).start()

    def _stop_tunnel(self):
        self.tunnel.stop_tunnel()
        self.lbl_address.configure(state="normal")
        self.lbl_address.delete(0, "end")
        self.lbl_address.insert(0, "Tünel kapatıldı.")
        self.lbl_address.configure(state="readonly")
        messagebox.showinfo("Tünel", "Tünel servisi durduruldu.")

    def _test_upnp(self):
        cfg = self.config_manager.get_server_config()
        port = cfg.get("server_port", 25565)
        def _worker():
            self.tunnel.try_upnp_port_forward(port)
        threading.Thread(target=_worker, daemon=True).start()
