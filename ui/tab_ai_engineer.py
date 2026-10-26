# -*- coding: utf-8 -*-
"""
Tab: AI Server Engineer & Crash Diagnostics (12+ Providers)
"""

import os
import glob
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from ui.theme import *
from core.ai_engineer import AIEngineer

class TabAIEngineer:
    def __init__(self, parent, config_manager):
        self.parent = parent
        self.config_manager = config_manager
        self.ai = AIEngineer(config_manager)
        self.frame = tk.Frame(parent, bg=BG_DARK)

        self._build_ui()

    def _build_ui(self):
        # ÜST BAR: Sağlayıcı ve Model Seçimi
        top_bar = tk.Frame(self.frame, bg=BG_PANEL, padx=14, pady=10)
        top_bar.pack(fill=tk.X, side=tk.TOP, pady=(0, 6))

        lbl_prov = tk.Label(top_bar, text="🤖 AI Sağlayıcısı (12 Farklı Motor):", font=("Segoe UI", 9, "bold"), fg=ACCENT_GOLD, bg=BG_PANEL)
        lbl_prov.pack(side=tk.LEFT, padx=(0, 6))

        ai_cfg = self.config_manager.get_ai_config()
        providers = list(ai_cfg.get("providers", {}).keys())

        self.prov_var = tk.StringVar(value=ai_cfg.get("active_provider", "Ollama (Yerel/Ücretsiz)"))
        self.prov_combo = ttk.Combobox(
            top_bar,
            textvariable=self.prov_var,
            font=("Segoe UI", 9, "bold"),
            values=providers,
            width=22,
            state="readonly"
        )
        self.prov_combo.pack(side=tk.LEFT, padx=(0, 14))
        self.prov_combo.bind("<<ComboboxSelected>>", self._on_provider_change)

        lbl_mod = tk.Label(top_bar, text="🧠 Model:", font=("Segoe UI", 9, "bold"), fg=ACCENT_CYAN, bg=BG_PANEL)
        lbl_mod.pack(side=tk.LEFT, padx=(0, 6))

        self.model_var = tk.StringVar(value=ai_cfg.get("active_model", "llama3"))
        self.model_entry = tk.Entry(
            top_bar,
            textvariable=self.model_var,
            font=("Consolas", 9),
            bg=BG_CARD,
            fg="#ffffff",
            relief=tk.FLAT,
            width=26
        )
        self.model_entry.pack(side=tk.LEFT, padx=(0, 14), ipady=2)

        # Hızlı Teşhis Butonları
        btn_diag = tk.Button(
            top_bar,
            text="🚨 Son Hatayı / Çökmeyi Teşhis Et",
            font=("Segoe UI", 8, "bold"),
            bg="#dc2626",
            fg="white",
            activebackground="#b91c1c",
            relief=tk.FLAT,
            padx=10,
            command=self.diagnose_last_crash
        )
        btn_diag.pack(side=tk.RIGHT, padx=3)

        btn_opt = tk.Button(
            top_bar,
            text="⚡ Performans Optimizasyonu",
            font=("Segoe UI", 8, "bold"),
            bg="#7c3aed",
            fg="white",
            relief=tk.FLAT,
            padx=10,
            command=self.optimize_config
        )
        btn_opt.pack(side=tk.RIGHT, padx=3)

        # ORTA ALAN: AI Sohbet ve Çıktı Ekranı
        chat_frame = tk.Frame(self.frame, bg=BG_PANEL, padx=14, pady=10)
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=6, pady=4)

        head = tk.Frame(chat_frame, bg=BG_PANEL)
        head.pack(fill=tk.X, pady=(0, 6))
        tk.Label(head, text="💬 AI SUNUCU MÜHENDİSİ DANIŞMA PANELİ", font=("Segoe UI", 9, "bold"), fg=ACCENT_GREEN, bg=BG_PANEL).pack(side=tk.LEFT)

        btn_clear = tk.Button(head, text="Temizle", font=("Segoe UI", 7), bg=BG_CARD, fg=TEXT_MUTED, relief=tk.FLAT, padx=6, command=lambda: self.chat_area.delete("1.0", tk.END))
        btn_clear.pack(side=tk.RIGHT)

        self.chat_area = scrolledtext.ScrolledText(
            chat_frame,
            bg="#030712",
            fg="#e2e8f0",
            insertbackground=ACCENT_CYAN,
            font=("Segoe UI", 10),
            wrap=tk.WORD,
            relief=tk.FLAT
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True, pady=(0, 8))

        self.chat_area.tag_config("user", foreground=ACCENT_CYAN, font=("Segoe UI", 10, "bold"))
        self.chat_area.tag_config("ai", foreground="#f8fafc", font=("Segoe UI", 10))
        self.chat_area.tag_config("system", foreground=ACCENT_GOLD, font=("Segoe UI", 9, "italic"))

        self.append_chat("🤖 Merhaba! Ben AI Minecraft Sunucu Mühendisi. 12 farklı sağlayıcı üzerinden sunucunu kurmana, hataları çözmene ve lag optimizasyonu yapmana yardımcı olabilirim.\n", "ai")

        # ALT BAR: Mesaj Girişi
        input_bar = tk.Frame(self.frame, bg=BG_PANEL, padx=14, pady=10)
        input_bar.pack(fill=tk.X, side=tk.BOTTOM)

        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(
            input_bar,
            textvariable=self.input_var,
            font=("Segoe UI", 10),
            bg=BG_CARD,
            fg="#ffffff",
            insertbackground="#ffffff",
            relief=tk.FLAT
        )
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8), ipady=4)
        self.input_entry.bind("<Return>", lambda e: self.send_user_message())

        btn_send = tk.Button(
            input_bar,
            text="Gönder (Enter)",
            font=("Segoe UI", 9, "bold"),
            bg=ACCENT_CYAN,
            fg="#000000",
            activebackground="#0284c7",
            relief=tk.FLAT,
            padx=16,
            command=self.send_user_message
        )
        btn_send.pack(side=tk.RIGHT)

    def _on_provider_change(self, event=None):
        prov = self.prov_var.get()
        ai_cfg = self.config_manager.get_ai_config()
        providers_dict = ai_cfg.get("providers", {})
        if prov in providers_dict:
            def_model = providers_dict[prov].get("default_model", "")
            self.model_var.set(def_model)
            ai_cfg["active_provider"] = prov
            ai_cfg["active_model"] = def_model
            self.config_manager.save()

    def append_chat(self, text, tag="ai"):
        self.chat_area.insert(tk.END, text + "\n", tag)
        self.chat_area.see(tk.END)

    def send_user_message(self):
        msg = self.input_var.get().strip()
        if not msg:
            return
        self.input_var.set("")
        self.append_chat(f"\n👤 Siz: {msg}", "user")
        self.append_chat("🤖 Düşünüyor...", "system")

        prov = self.prov_var.get()
        model = self.model_var.get()

        def _worker():
            resp = self.ai.ask(msg, provider_name=prov, model=model)
            self.parent.after(0, self._render_response, resp)

        threading.Thread(target=_worker, daemon=True).start()

    def _render_response(self, response_text):
        # Remove thinking notice
        content = self.chat_area.get("1.0", tk.END)
        if "🤖 Düşünüyor..." in content:
            idx = content.rfind("🤖 Düşünüyor...")
            self.chat_area.delete(f"1.0 + {idx} chars", f"1.0 + {idx + len('🤖 Düşünüyor...')} chars")
        self.append_chat(f"🤖 AI Mühendis:\n{response_text}\n", "ai")

    def diagnose_last_crash(self):
        cfg = self.config_manager.get_server_config()
        sdir = cfg.get("server_dir", os.path.join(os.getcwd(), "server"))

        # Check crash-reports first, then latest.log
        crash_dir = os.path.join(sdir, "crash-reports")
        log_file = os.path.join(sdir, "logs", "latest.log")

        snippet = ""
        src_name = ""

        if os.path.exists(crash_dir):
            crashes = glob.glob(os.path.join(crash_dir, "*.txt"))
            if crashes:
                crashes.sort(key=os.path.getmtime, reverse=True)
                latest_crash = crashes[0]
                src_name = os.path.basename(latest_crash)
                with open(latest_crash, "r", encoding="utf-8", errors="replace") as f:
                    snippet = f.read()[-3500:]

        if not snippet and os.path.exists(log_file):
            src_name = "latest.log"
            with open(log_file, "r", encoding="utf-8", errors="replace") as f:
                lines = f.readlines()
                snippet = "".join(lines[-150:])

        if not snippet:
            messagebox.showinfo("Bilgi", "İncelenecek bir çökme raporu veya hata logu bulunamadı.")
            return

        self.append_chat(f"\n🚨 [Sistem] {src_name} dosyası incelenmek üzere AI Sağlayıcısına iletiliyor...", "system")
        prov = self.prov_var.get()

        def _worker():
            resp = self.ai.analyze_log_error(snippet, provider_name=prov)
            self.parent.after(0, self._render_response, resp)

        threading.Thread(target=_worker, daemon=True).start()

    def optimize_config(self):
        cfg = self.config_manager.get_server_config()
        ver = cfg.get("mc_version", "1.20.1")
        stype = cfg.get("server_type", "Paper")
        ram = cfg.get("max_ram_gb", 6)

        self.append_chat(f"\n⚡ [Sistem] {ver} ({stype}, {ram}GB RAM) için optimizasyon kuralları oluşturuluyor...", "system")
        prov = self.prov_var.get()

        def _worker():
            resp = self.ai.optimize_server(player_count=20, ram_gb=ram, server_type=stype, mc_version=ver)
            self.parent.after(0, self._render_response, resp)

        threading.Thread(target=_worker, daemon=True).start()
