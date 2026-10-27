# -*- coding: utf-8 -*-
"""
Interactive Beginner Onboarding Tutorial & Guide Modal (v4.1.0 Master)
Designed specifically for users with ZERO technical or Minecraft server knowledge.
Guides them through:
1. Understanding Server Presets and Turn-key solutions
2. 1-Click Installing with Automatic Java detection
3. Inviting friends globally with Portless Tunnels (Playit.gg / Cloudflare)
4. Admin Panel 24 Categories and 500+ Commands
5. Instant Quick-Setup action button
"""

import customtkinter as ctk
from ui.modern_theme import *
from core.i18n import t

TUTORIAL_STEPS = [
    {
        "step": 1,
        "badge": "ADIM 1 / 5 • BAŞLANGIÇ",
        "icon": "🎮",
        "title": "Minecraft Sunucusu Kurmak Artık Çok Kolay!",
        "subtitle": "Sıfır teknik bilgiyle 3 dakikada kendi dünyanı yarat",
        "desc": (
            "Eski usul karmaşık kodlarla, port açma dertleriyle, çöken Java sürümleriyle "
            "veya uyuşmayan eklentilerle uğraşmanıza hiç gerek yok.\n\n"
            "Bu program, dünya çapındaki en gelişmiş otonom Minecraft motorudur. "
            "Tek bir tıkla sunucunuzu hazırlar, optimize eder ve arkadaşlarınızla oynamaya hazır hale getirir."
        ),
        "bullets": [
            ("👑 1-Tıkla Hazır Sunucu Paketleri", "Eklentileri tek tek aramak yerine RPG, Crossplay veya Hayatta Kalma paketlerini tek tıkla kur."),
            ("📱 Telefon, Tablet ve PC Bir Arada", "Bedrock (Mobil/Konsol) ve Java oyuncuları aynı anda senin dünyana katılabilir."),
            ("🔒 %100 Güvenli ve Sıfır Veri Sızıntısı", "Tüm dosyalar bilgisayarında yerel çalışır, kişisel IP veya bilgiler asla sızdırılmaz.")
        ],
        "tip": "💡 Altın Tavsiye: Hiçbir ayara dokunmasanız bile 'Kurulumu Başlat' dediğinizde en iyi standartlarla sunucunuz hazır olur!"
    },
    {
        "step": 2,
        "badge": "ADIM 2 / 5 • KURULUM",
        "icon": "⚡",
        "title": "Sunucunu Seç, Kur ve Başlat",
        "subtitle": "Sunucu Kurucu sekmesinde 1-tıkla kurulum",
        "desc": (
            "Sol menüdeki 'Sunucu Kurucu' sekmesi sunucunuzun ana merkezidir.\n"
            "Burada yapmanız gereken adımlar oldukça basittir:"
        ),
        "bullets": [
            ("1. Sürümünü Seç", "Listeden dilediğin Minecraft sürümünü tıkla (Örn: 1.20.1 veya 1.21.4). Tüm 160+ sürüm mevcuttur."),
            ("2. RAM Miktarını Belirle", "Bilgisayarının gücüne göre 3GB - 6GB arası bir RAM seç. 3GB çoğu sunucu için gayet yeterlidir."),
            ("3. Crossplay'i Açık Bırak", "Arkadaşların telefon/tabletten girecekse 'Mobil ve Konsol Crossplay' anahtarı açık kalsın."),
            ("4. 'Sunucuyu Kur' Butonuna Bas", "Mavi butona bastığında program JAR dosyasını indirir, EULA'yı otomatik onaylar ve sunucuyu kurar.")
        ],
        "tip": "☕ Java Bilgisi Gerekmez: Sisteminizde Java yoksa veya sürümü eski ise program doğru Adoptium OpenJDK sürümünü otomatik algılar."
    },
    {
        "step": 3,
        "badge": "ADIM 3 / 5 • EKLENTİLER",
        "icon": "👑",
        "title": "1-Tıkla Hazır Sunucu Paketleri (Presets)",
        "subtitle": "Eklentiler ve Modlar sekmesinde hazır dünyalar",
        "desc": (
            "Saatlerce internetten eklenti (plugin) aramak, yapılandırmak veya komut çevirmekle vakit kaybetmeyin! "
            "'Eklentiler & Modlar' sekmesinde hazır anahtar teslim şablonlar bulunur:"
        ),
        "bullets": [
            ("👑 Ultimate Pro RPG ve Crossplay", "En popüler paket! Takas sistemi, GrimAC hilesiz oyun, 200ms anlık bakiye tablosu, madenleri koruyan Anti-Xray ve 24 devlet makamı hazır gelir."),
            ("🛡️ Sade Güvenli Crossplay", "Düşük sistemler için hafif, kasmayan, mobil destekli ve orijinal skinleri gösteren hayatta kalma sunucusu."),
            ("💰 Büyük Ekonomi ve Krallık", "GriefPrevention ile altın kürekli arazi sahiplenme (claim) ve pazar ekonomisi."),
            ("🇹🇷 Türkçe Komutlar ve Rehber", "Sunucu açıldığında /hewlp, /takas, /arsa, /para komutları ve 5 sayfalık interaktif Türkçe rehber kitapçığı otomatik yüklenir.")
        ],
        "tip": "📖 Oyun İçi Rehber: Oyundayken chat'e '/hewlp' veya '/komutlar' yazarak tüm komutları içeren rehber kitabını okuyabilirsiniz."
    },
    {
        "step": 4,
        "badge": "ADIM 4 / 5 • AĞ VE TÜNEL",
        "icon": "🌍",
        "title": "Port Açmadan Arkadaşlarını Davet Et!",
        "subtitle": "Tünel ve Ağ sekmesiyle dünya çapında bağlantı",
        "desc": (
            "Arkadaşlarınızla oynamak için modem arayüzlerine girip karmaşık port açma (Port Forwarding) "
            "işlemleriyle uğraşmanıza veya güvenlik riski almanıza hiç gerek yok!"
        ),
        "bullets": [
            ("1. 'Tünel ve Ağ' Sekmesine Geç", "Sol menüdeki tünel sekmesini aç."),
            ("2. 'Playit.gg' veya 'Cloudflare' Başlat", "Tek bir butona basarak portsuz küresel tüneli aktif et."),
            ("3. Adresi Arkadaşına Gönder", "Programın sana vereceği linki (Örn: 'benim-dunyasi.joinmc.link') arkadaşına at."),
            ("4. Doğrudan Bağlansınlar!", "Arkadaşın Minecraft'a girip Çok Oyunculu -> Sunucu Ekle kısmına bu adresi yapıştırarak anında dünyana katılır.")
        ],
        "tip": "🛡️ Güvenlik Garantisi: Evinizin gerçek IP adresi gizlenir, arkadaşlarınız güvenli tünel üzerinden bağlanır."
    },
    {
        "step": 5,
        "badge": "ADIM 5 / 5 • ADMİN PANELİ",
        "icon": "🎛️",
        "title": "24 Kategori Sekmeli Master Admin Paneli",
        "subtitle": "Oyun içi krallığını tek tıkla yönet",
        "desc": (
            "Sunucunuz açıldıktan sonra sol menüdeki 'Admin Paneli' sekmesine geçin. "
            "Burada 24 farklı kategoride 286'dan fazla buton parmaklarınızın ucundadır:"
        ),
        "bullets": [
            ("🏠 1-Tıkla Oto Ev Yapıcı", "2 katlı modern villa, dağ evi, ortaçağ şatosu, piramit veya tarım çiftliklerini tek tıkla inşa et."),
            ("🎭 Rol ve Makam Ribbon'ı", "Arkadaşına veya kendine tek tıkla Cumhurbaşkanı, Doktor, Muhtar, Polis rolü ve ses efektleri ata."),
            ("💰 Akçe ve Ekonomi", "Oyuncuya anında para ver, kes veya 10 dakikada bir otomatik devlet maaşı dağıt."),
            ("🛡️ Anti-Lag ve Canavar Temizliği", "Sunucuda lag olursa barışçıl geçişle tek tıkla yerdeki çöpleri ve yaratıkları temizle."),
            ("🎰 Şans Oyunları ve Sandıklar", "Kumarhaneler, şans kolları, milyarder madenci ve mimar sandıkları ver.")
        ],
        "tip": "🚀 Tebrikler! Artık tam donanımlı bir Minecraft Sunucu Yöneticisisiniz. Hemen aşağıdaki butona basarak ilk sunucunuzu başlatabilirsiniz!"
    }
]


class TutorialModal(ctk.CTkToplevel):
    def __init__(self, master, config_manager=None, on_quick_start=None):
        super().__init__(master)

        self.config_manager = config_manager
        self.on_quick_start = on_quick_start
        self.current_step_idx = 0

        self.title("🎓 Sıfırdan Başlayanlar İçin Minecraft Sunucu Rehberi")
        self.geometry("780x620")
        self.minsize(720, 560)
        self.configure(fg_color="#090d16")

        self.attributes("-topmost", True)
        self.transient(master)

        try:
            self.update_idletasks()
            master_x = master.winfo_x()
            master_y = master.winfo_y()
            master_w = master.winfo_width()
            master_h = master.winfo_height()
            w, h = 780, 620
            x = max(50, master_x + (master_w - w) // 2)
            y = max(50, master_y + (master_h - h) // 2)
            self.geometry(f"{w}x{h}+{x}+{y}")
        except Exception:
            pass

        self._build_ui()
        self._render_step(0)

    def _build_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ÜST HEADER
        header = ctk.CTkFrame(self, fg_color="#0f172a", corner_radius=0, height=70)
        header.grid(row=0, column=0, sticky="ew", padx=0, pady=0)

        left_box = ctk.CTkFrame(header, fg_color="transparent")
        left_box.pack(side="left", padx=16, pady=12)
        ctk.CTkLabel(left_box, text="🎓 BAŞLANGIÇ AKADEMİSİ", font=("Segoe UI", 12, "bold"), text_color=COLOR_ACCENT_CYAN).pack(anchor="w")
        ctk.CTkLabel(left_box, text="Sıfır Bilgiyle Minecraft Sunucu Kurma Kılavuzu", font=("Segoe UI", 9), text_color=COLOR_TEXT_MUTED).pack(anchor="w")

        self.dots_frame = ctk.CTkFrame(header, fg_color="transparent")
        self.dots_frame.pack(side="right", padx=16, pady=12)
        self.dot_labels = []
        for i in range(len(TUTORIAL_STEPS)):
            lbl = ctk.CTkLabel(self.dots_frame, text="●", font=("Segoe UI", 14), text_color="#334155")
            lbl.pack(side="left", padx=3)
            self.dot_labels.append(lbl)

        # ORTA KART
        self.card = ctk.CTkScrollableFrame(self, fg_color="#0f172a", corner_radius=12, border_width=1, border_color="#1e293b")
        self.card.grid(row=1, column=0, sticky="nsew", padx=16, pady=12)

        top_meta = ctk.CTkFrame(self.card, fg_color="transparent")
        top_meta.pack(fill="x", pady=(8, 4))

        self.lbl_step_badge = ctk.CTkLabel(
            top_meta,
            text="",
            font=("Segoe UI", 10, "bold"),
            text_color=COLOR_ACCENT_GOLD,
            fg_color="#2b200b",
            corner_radius=6,
            height=22,
            padx=8
        )
        self.lbl_step_badge.pack(side="left")

        title_box = ctk.CTkFrame(self.card, fg_color="transparent")
        title_box.pack(fill="x", pady=(6, 2))

        self.lbl_icon = ctk.CTkLabel(title_box, text="", font=("Segoe UI Emoji", 28))
        self.lbl_icon.pack(side="left", padx=(0, 10))

        text_title_col = ctk.CTkFrame(title_box, fg_color="transparent")
        text_title_col.pack(side="left", fill="x", expand=True)

        self.lbl_title = ctk.CTkLabel(text_title_col, text="", font=("Segoe UI", 16, "bold"), text_color=COLOR_TEXT_MAIN, anchor="w")
        self.lbl_title.pack(anchor="w")

        self.lbl_subtitle = ctk.CTkLabel(text_title_col, text="", font=("Segoe UI", 11), text_color=COLOR_ACCENT_CYAN, anchor="w")
        self.lbl_subtitle.pack(anchor="w")

        self.lbl_desc = ctk.CTkLabel(
            self.card,
            text="",
            font=("Segoe UI", 11),
            text_color=COLOR_TEXT_MAIN,
            justify="left",
            wraplength=680
        )
        self.lbl_desc.pack(anchor="w", pady=(8, 12))

        self.bullets_box = ctk.CTkFrame(self.card, fg_color="#131d31", corner_radius=10, border_width=1, border_color="#1e293b")
        self.bullets_box.pack(fill="x", pady=(0, 12), padx=2)

        self.tip_box = ctk.CTkFrame(self.card, fg_color="#18231c", corner_radius=8, border_width=1, border_color=COLOR_ACCENT_GREEN)
        self.tip_box.pack(fill="x", pady=(0, 8), padx=2)

        self.lbl_tip = ctk.CTkLabel(
            self.tip_box,
            text="",
            font=("Segoe UI", 10, "bold"),
            text_color=COLOR_ACCENT_GREEN,
            justify="left",
            wraplength=660
        )
        self.lbl_tip.pack(anchor="w", padx=10, pady=8)

        # ALT BAR
        bottom_bar = ctk.CTkFrame(self, fg_color="#0f172a", corner_radius=0, height=64)
        bottom_bar.grid(row=2, column=0, sticky="ew", padx=0, pady=0)

        self.dont_show_var = ctk.BooleanVar(value=False)
        self.chk_dont_show = ctk.CTkCheckBox(
            bottom_bar,
            text="Açılışta bu rehberi bir daha gösterme",
            variable=self.dont_show_var,
            font=("Segoe UI", 10),
            text_color=COLOR_TEXT_MUTED,
            border_color="#334155",
            checkmark_color="#000000",
            fg_color=COLOR_ACCENT_CYAN
        )
        self.chk_dont_show.pack(side="left", padx=16, pady=16)

        right_btns = ctk.CTkFrame(bottom_bar, fg_color="transparent")
        right_btns.pack(side="right", padx=16, pady=14)

        self.btn_prev = ctk.CTkButton(
            right_btns,
            text="◀ Önceki",
            font=FONT_BOLD,
            width=90,
            height=34,
            fg_color=COLOR_BG_CARD_HOVER,
            hover_color="#334155",
            command=self._prev_step
        )
        self.btn_prev.pack(side="left", padx=(0, 8))

        self.btn_next = ctk.CTkButton(
            right_btns,
            text="Sonraki ▶",
            font=FONT_BOLD,
            width=100,
            height=34,
            fg_color=COLOR_ACCENT_CYAN,
            text_color="#000000",
            hover_color="#38bdf8",
            command=self._next_step
        )
        self.btn_next.pack(side="left", padx=(0, 8))

        self.btn_quick_start = ctk.CTkButton(
            right_btns,
            text="🚀 İlk Sunucumu Hazırla",
            font=("Segoe UI", 11, "bold"),
            height=34,
            fg_color=COLOR_ACCENT_GREEN,
            text_color="#000000",
            hover_color="#34d399",
            command=self._on_finish_and_launch
        )
        self.btn_quick_start.pack(side="left")

    def _render_step(self, idx):
        self.current_step_idx = idx
        data = TUTORIAL_STEPS[idx]

        self.lbl_step_badge.configure(text=data["badge"])
        for i, dot in enumerate(self.dot_labels):
            if i == idx:
                dot.configure(text_color=COLOR_ACCENT_CYAN)
            elif i < idx:
                dot.configure(text_color=COLOR_ACCENT_GREEN)
            else:
                dot.configure(text_color="#334155")

        self.lbl_icon.configure(text=data["icon"])
        self.lbl_title.configure(text=data["title"])
        self.lbl_subtitle.configure(text=data["subtitle"])
        self.lbl_desc.configure(text=data["desc"])
        self.lbl_tip.configure(text=data["tip"])

        for w in self.bullets_box.winfo_children():
            w.destroy()

        for b_title, b_desc in data["bullets"]:
            row = ctk.CTkFrame(self.bullets_box, fg_color="transparent")
            row.pack(fill="x", padx=12, pady=5)

            ctk.CTkLabel(row, text="✔", font=("Segoe UI", 11, "bold"), text_color=COLOR_ACCENT_GREEN).pack(side="left", anchor="n", padx=(0, 8))
            text_col = ctk.CTkFrame(row, fg_color="transparent")
            text_col.pack(side="left", fill="x", expand=True)

            ctk.CTkLabel(text_col, text=b_title, font=("Segoe UI", 10, "bold"), text_color=COLOR_ACCENT_GOLD, anchor="w").pack(anchor="w")
            ctk.CTkLabel(text_col, text=b_desc, font=("Segoe UI", 9), text_color=COLOR_TEXT_MAIN, justify="left", wraplength=620, anchor="w").pack(anchor="w")

        if idx == 0:
            self.btn_prev.configure(state="disabled")
        else:
            self.btn_prev.configure(state="normal")

        if idx == len(TUTORIAL_STEPS) - 1:
            self.btn_next.configure(text="Tamamla ✔")
        else:
            self.btn_next.configure(text="Sonraki ▶")

    def _next_step(self):
        if self.current_step_idx < len(TUTORIAL_STEPS) - 1:
            self._render_step(self.current_step_idx + 1)
        else:
            self._on_finish_and_launch()

    def _prev_step(self):
        if self.current_step_idx > 0:
            self._render_step(self.current_step_idx - 1)

    def _save_preference_if_needed(self):
        if self.dont_show_var.get() and self.config_manager:
            try:
                cfg = self.config_manager.get_server_config()
                cfg["show_welcome_tutorial"] = False
                self.config_manager.save()
            except Exception:
                pass

    def _on_finish_and_launch(self):
        self._save_preference_if_needed()
        self.destroy()
        if callable(self.on_quick_start):
            self.on_quick_start()
