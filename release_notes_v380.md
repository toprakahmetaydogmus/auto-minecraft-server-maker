### ⚔️ Auto Minecraft Server Maker & AI Engineer Pro v3.8.0 Ultra

Tüm Minecraft tarihini kapsayan devasa sürüm matrisi (2026 Game Drops `26.4`-`26.1`, `1.21.11`'den `1.0.0`'a tüm adlandırılmış güncellemeler, `b1.8.1`-`b1.0` Betalar, `a1.2.6`-`a1.0.0` Alfalar ve Klasikler), 5 farklı küresel tünelleme motoru (Playit, Cloudflare, ngrok, Localtonet, UPnP), Canlı Sunucu & RCON Kontrol Merkezi ve 40.7 MB bağımsız tam paket standalone `.exe` ile yayınlandı!

---

### 🌟 Bu Sürümdeki Kritik Yenilikler & İyileştirmeler:

#### 1. 🚀 Eksiksiz Minecraft Tarih Matrisi (163+ Sürüm - 26.x'ten Classic 0.30'a)
- **🔥 2026 Game Drops:**
  - `26.4 (Fourth Drop 2026 - Beklenen)`
  - `26.3 (Wilderness Bound - Yaban Hayatı)`
  - `26.2 (Chaos Cubed - Küp Kaosu)`
  - `26.1 (Tiny Takeover - Küçük İstilacılar)`
- **⭐ Modern 1.21 Serisi:**
  - `1.21.11 (Mounts of Mayhem)`
  - `1.21.10 (The Copper Age)`
  - `1.21.9`, `1.21.8 (Chase the Skies)`, `1.21.7`, `1.21.6`
  - `1.21.5 (Spring to Life)`, `1.21.4 (The Garden Awakens)`, `1.21.3 (Bundles of Bravery)`, `1.21.2`, `1.21.1 (Tricky Trials)`, `1.21`
- **💎 Modern 1.20 Serisi:**
  - `1.20.6 (Trails & Tales)`, `1.20.5`, `1.20.4`, `1.20.3`, `1.20.2`, `1.20.1`, `1.20`
- **🌿 Altın Çağ (1.16 - 1.19):**
  - `1.19.4 - 1.19 (The Wild Update)`
  - `1.18.2 - 1.18 (Caves & Cliffs II)`
  - `1.17.1 - 1.17 (Caves & Cliffs I)`
  - `1.16.5 - 1.16 (Nether Update)`
- **🏰 Klasik Sürümler (1.0.0 - 1.15.2):**
  - 1.15 (Buzzy Bees), 1.14 (Village & Pillage), 1.13 (Update Aquatic), 1.12 (World of Color), 1.11 (Exploration), 1.10 (Frostburn), 1.9 (Combat), 1.8 (Bountiful), 1.7 (Changed The World), 1.6 (Horse), 1.5 (Redstone), 1.4 (Pretty Scary), 1.3 (Trading), 1.2 (Faithful), 1.1 (Spawn Egg), 1.0.1, 1.0.0 (Minecon Release).
- **🧪 Nostaljik Betalar & Alfalar:**
  - Betalar: `b1.8.1`, `b1.8`, `b1.7.3`, `b1.7.2`, `b1.7_01`, `b1.7`, `b1.6.6` - `b1.6`, `b1.5_02` - `b1.5`, `b1.4_01`, `b1.3_01`, `b1.2_02`, `b1.1_02`, `b1.0.2` - `b1.0`.
  - Alfalar: `a1.2.6 (Halloween Update)` - `a1.2.0`, `a1.1.2_01` - `a1.1.0 (Seecret Friday)`, `a1.0.17_04` - `a1.0.0`.
  - Infdev, Indev ve Classic: `Infdev 20100630`, `Infdev 20100618`, `Indev 20100223`, `Indev 0.31`, `c0.30 (Late Classic)`.

#### 2. 🌐 5 Farklı Tünelleme & Port Yönlendirme Motoru (Arkadaşlarınla Anında Oyna)
- **⚡ Playit.gg:** Sıfır yapılandırmalı, ücretsiz küresel Minecraft alan adı (`*.gl.at.ply.gg:port`).
- **☁️ Cloudflare Tunnel (cloudflared):** Cloudflare Zero Trust altyapısıyla güvenli, yüksek hızlı TCP tüneli (`trycloudflare.com`).
- **🚀 ngrok TCP:** Authtoken destekli ultra düşük gecikmeli TCP tüneli (`ngrok tcp 25565`).
- **🌐 Localtonet:** Gelişmiş TCP tünelleme istemcisi.
- **📡 Modem UPnP:** Otomatik SSDP/UPnP protokolüyle modemde anında 25565 port yönlendirme testi ve açma.
- **📋 Tek Tıkla Kopyala:** Üretilen bağlantı linkini tek tıkla panoya kopyalayan akıllı adres algılayıcı.

#### 3. 🛡️ Canlı Sunucu & RCON Kontrol Merkezi (WinError 10061 Kökten Çözüldü)
- Sunucu kapalıyken veya henüz başlatılırken oluşan `[WinError 10061] Hedef makine etkin olarak reddettiğinden...` hatası kökten giderildi.
- Admin Panelinin en üstüne entegre edilen **Canlı Sunucu Kontrol Çubuğu**:
  - `🚀 Sunucuyu Başlat`: Sunucuyu arka planda güvenle başlatır, açılışı izler ve dünya yüklendiğinde RCON'a otomatik bağlanır.
  - `⏹️ Sunucuyu Durdur`: RCON üzerinden `/stop` göndererek güvenli kapatma yapar.
  - `🔄 Yeniden Başlat`: Otomatik durdurup yeniden ayağa kaldırır.
  - `🔌 RCON Yenile`: Port 25575 hazır olduğunda tek tıkla bağlanır.
  - `👥 Oyuncu Listesi`: Anlık aktif oyuncuları listeler.
  - Durum Rozeti: `🔴 Kapalı` | `🟡 Başlatılıyor` | `🟢 Sunucu ve RCON Aktif!`.

#### 4. 💎 38.84 MB (40.7 MB) Doğrulanmış Standalone Windows Executable
- Boş veya eksik derleme yok! Python, CustomTkinter, PIL, Requests, Psutil, Darkdetect ve tüm arayüz kütüphaneleri eksiksiz tek bir Windows `.exe` içerisinde.

---

### 📦 Doğrulanmış Dosya Bilgileri:
- **Dosya Adı:** `Auto-Minecraft-Server-Maker-v3.8.0-Ultra.exe` (ve `Auto-Minecraft-Server-Maker.exe`)
- **Dosya Boyutu:** 38.84 MB (40,722,709 bayt)
- **SHA-256 Doğrulama Kodu:** `f914f75a505e962fd4720a3f7fc14da039f85c3f4eac94ee21ced875247833e7`
