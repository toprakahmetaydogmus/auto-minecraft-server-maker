# ⚔️ Auto Minecraft Server Maker & AI Engineer Pro (v4.1.0 Master)

<div align="center">

![Version](https://img.shields.io/badge/Release-v4.1.0%20Master-00E5FF?style=for-the-badge&logo=github&logoColor=white)
![Python Version](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GUI Framework](https://img.shields.io/badge/GUI-CustomTkinter%20Cyberpunk-9333ea?style=for-the-badge&logo=windows11&logoColor=white)
![Admin Suite](https://img.shields.io/badge/Admin%20Panel-24%20Tabs%20%7C%20500%2B%20Commands-FFD700?style=for-the-badge&logo=gnometerminal&logoColor=white)
![Minecraft](https://img.shields.io/badge/Minecraft-163%2B%20Versions%20(26.x%20%E2%86%92%20c0.30)-2E7D32?style=for-the-badge&logo=minecraft&logoColor=white)
![Local AI](https://img.shields.io/badge/Local%20AI-Ollama%201.5B%20%7C%20Zero--Key-FF6F00?style=for-the-badge&logo=ollama&logoColor=white)
![Security](https://img.shields.io/badge/Security-100%25%20Zero--Leak-00C853?style=for-the-badge&logo=shield&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-F57C00?style=for-the-badge)

**The Ultimate Autonomous Minecraft Server Orchestrator, 1-Click Server Presets, 24-Tab Admin Suite, Zero-API-Key Local AI Assistant, Modrinth Auto-Mod Downloader, Crash Doctor, Portless Tunneling & Anti-Xray Security Engine.**

[English Documentation](#-english-documentation) • [Türkçe Dokümantasyon](#-türkçe-dokümantasyon) • [Download Standalone .EXE](https://github.com/toprakahmetaydogmus/auto-minecraft-server-maker/releases)

</div>

---

## 🌟 What's New in v4.1.0 Master?

### 1. 👑 1-Click Ready Server Presets (Hazır Sunucu Şablonları)
No more spending hours configuring plugins, permissions, and complex command alias mappings! Install turnkey, fully-tuned server suites with a single click:
* **👑 Ultimate Pro RPG, Survival & Crossplay:**
  * **Bedrock & Java Crossplay:** Geyser + Floodgate configured for seamless Android, iOS, Xbox, PlayStation, and PC play.
  * **GrimAC Next-Gen AntiCheat:** Packet-level 0 false-positive exploit and movement security.
  * **Live TAB & Scoreboard:** 200ms ultra-low latency real-time currency, health bar, and prefix syncing.
  * **Economy Suite:** EssentialsX, Vault, and PlaceholderAPI.
  * **Anti-Xray Forge 1.20.1 Engine:** Masks all ores as stone/deepslate (`engineMode = 3`) to eliminate X-ray cheating.
  * **Turkish Command System:** Pre-mapped `commands.yml` (`/hewlp`, `/hlp`, `/yardim`, `/komutlar`, `/takas`, `/arsa`, `/doyur`, `/para`, `/secim`, `/oy`) and interactive 5-page `/hewlp` guidebook (`plugins/Essentials/info.txt`).
* **🛡️ Safe Vanilla Crossplay (Bedrock + Java):**
  * Lightweight, ultra-high TPS Purpur/Paper setup with ViaVersion (all client versions supported) and SkinsRestorer.
* **💰 Grand Economy & Kingdom Towny:**
  * GriefPrevention land claiming, LuckPerms permissions, and dynamic marketplace economy.

### 2. 🎛️ 24-Category & 500+ Command Master Admin Suite
The Admin Panel features 24 dedicated category tabs with over 286+ verified, one-click action cards:
| Tab Category | Description & Capabilities |
|---|---|
| 🏠 **Oto İnşaat & Ev Yapıcı** | 1-Click Luxury modern villas, log cabins, medieval castles, Japanese pagodas, pyramids, and automated wheat/cactus farms. |
| 📦 **Sihirli İnşa Sandıkları** | Themed Lvl 255 God shulker boxes (Admin blocks, Billionaire ores, Architect timbers, Redstone engineers). |
| 💰 **Akçe & Ekonomi Sistemi** | Instant balance granting/deducting and automated 10-minute citizen salary broadcaster. |
| 🎭 **Hızlı Rol & Makam Atayıcı** | Ribbon dropdown assigning official titles (President, Village Mayor, Police Officer, Army Commander, Doctor, Judge, Royal Knight). |
| 🔄 **Dinamik Oyuncu Senkronizasyonu** | Live sync button pulling all joined friends and active players from `usercache.json` and RCON. |
| ⚡ **Efsanevi 32K Tanrı Setleri** | Lvl 255 Netherite armor, Apocalypse Swords, Nuclear Bows, and Machine Crossbows. |
| 🛡️ **Anti-Lag & Canavar Temizliği** | Peaceful difficulty toggle for zero-lag instant monster wipes and ground item clearing. |
| 🎰 **Casino & Şans Oyunları** | Lucky levers, slot machine generators, and lottery dispensers. |
| 🗳️ **Seçim & Demokrasi** | Democratic player election polls, ballot boxes, and voting systems. |
| 🪂 **Airdrop & Gökten Kasa** | Random supply drops, parachute crates, and server gift showers. |
| ⚔️ **Boss Zindanı & Kanlı Ay** | Wither, Warden, Blood Moon invasions, and custom mob arenas. |

### 3. ⚡ 3GB RAM & Aikar G1GC Peak TPS Optimization
Designed to run with a rock-solid **20.0 TPS** even on budget hardware or VPS machines with 3GB to 4GB of RAM:
* `server.properties`: `view-distance=8`, `simulation-distance=6`, `network-compression-threshold=256` reduces chunk loading overhead by ~40%.
* `start.bat`: Modern Aikar G1GC flags, parallel reference processing, and local timezone lock (`-Duser.timezone=Europe/Istanbul`).

### 4. 🛡️ Java 25 & `sun.misc.Unsafe` Crash Shield
* **The Root Fix:** OpenJDK 25 removed `sun.misc.Unsafe.ensureClassInitialized`, causing Forge/Arclight 1.20.1 to crash during boot.
* **Autonomous Resolution:** Auto Minecraft Server Maker detects Java 25 and auto-provisions portable **Adoptium OpenJDK 17** (`tools/java/jre-17/bin/java.exe`), ensuring 100% crash-free server startups.

### 5. 🎓 Zero-Knowledge Interactive Beginner Academy (Sıfırdan Başlayanlar İçin Rehber)
* **Interactive 5-Step Visual Wizard:** Pops up automatically on first launch (or anytime via the prominent sidebar `🎓 Sıfırdan Başla Rehberi` button).
* **Demystifying Servers:** Explains Turn-key Presets, Java version matching, Portless Global Tunnels (Playit.gg / Cloudflare), and Admin Panel controls in plain language.
* **1-Click Quick Launcher:** Beginners can click `🚀 İlk Sunucumu Hazırla` to automatically populate the gold standard (1.20.1 Paper, 3GB RAM, Bedrock Crossplay) and immediately start playing with friends.

---

## 🚀 Quick Start

### Option A: Standalone Windows Executable (Recommended)
1. Download the latest **`Auto-Minecraft-Server-Maker.exe`** from [GitHub Releases](https://github.com/toprakahmetaydogmus/auto-minecraft-server-maker/releases).
2. Double-click to launch — **zero installation, zero dependencies, 100% self-contained portable executable**.

### Option B: Python / PyPI Package
```bash
# Clone the repository
git clone https://github.com/toprakahmetaydogmus/auto-minecraft-server-maker.git
cd auto-minecraft-server-maker

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

---

## 🤖 12+ AI Engines & Local Models

| Provider | Model Family | Key Requirement |
|---|---|---|
| 🦙 **Ollama (Default)** | `qwen2.5:1.5b`, `llama3.2:3b`, `mistral:7b` | **None (%100 Free & Offline)** |
| 🛡️ **Offline Expert** | Built-in Rule & Semantic Knowledge Engine | **None (Zero Token, Instant 0ms)** |
| 🔷 **Google Gemini** | `gemini-1.5-flash`, `gemini-1.5-pro` | Free Google AI Key |
| 🧠 **OpenAI** | `gpt-4o`, `gpt-4o-mini` | OpenAI API Key |
| 🪶 **Anthropic** | `claude-3-5-sonnet`, `claude-3-haiku` | Anthropic API Key |
| ⚡ **Groq** | `llama-3.3-70b-versatile` | Groq API Key |
| 🐋 **DeepSeek** | `deepseek-chat`, `deepseek-reasoner` | DeepSeek API Key |
| 🟢 **NVIDIA NIM** | `meta/llama-3.1-70b-instruct` | NVIDIA NIM API Key |
| 🌐 **OpenRouter** | 100+ Multi-Provider Models | OpenRouter API Key |

---

## 🇹🇷 Türkçe Dokümantasyon

### 🌟 Öne Çıkan Süper Yetenekler:
1. **1-Tıkla Hazır Sunucu Paketleri:** İster telefon-konsol crossplay'li tam RPG sunucusu, ister sade hayatta kalma sunucusu seçin; tüm eklentiler, Türkçe komut haritaları (`commands.yml`) ve rehber kitapçığı otomatik kurulur.
2. **24 Kategori & 500+ Yönetici Butonu:** Otomatik villa inşası, 32K tanrı silahları, hava durumu, oyuncu troll komutları, anlık rol ve makam atama şeridi ile tam hakimiyet.
3. **Dinamik Arkadaş Listesi (🔄 Butonu):** Sunucunuza katılan tüm arkadaşları ve kayıtlı oyuncuları RCON ve `usercache.json` üzerinden anında algılayıp hedef listesine ekler.
4. **Anti-Xray Forge Koruma Motoru:** Madenleri yeraltında taş ve derin kayrak olarak maskeleyerek X-ray hilecilerini tamamen etkisiz hale getirir.
5. **Modemsiz & Port Açmadan Oynama:** Playit.gg ve UPnP tünelleri sayesinde modem şifrenizi bilmeden tek tıkla arkadaşlarınızın girebileceği genel bağlantı üretir.
6. **Çökmeyi Teşhis Et (Crash Doctor):** Sunucu çöktüğünde logları okur, hatanın kaynağını Türkçe açıklar ve anında uygulanabilir çözüm önerir.

---

## 🔒 100% Zero-Leak Security Architecture
* **Sıfır Sızıntı Garantisi:** Kod tabanında, şablonlarda veya yapılandırma dosyalarında hiçbir kişisel IP, kullanıcı adı, parola veya özel token yer almaz.
* Tüm yerel ayarlar yalnızca kullanıcının kendi makinesindeki `config.json` dosyasında tutulur ve `.gitignore` ile korunur.

---

## 📜 Lisans
Bu proje [MIT Lisansı](LICENSE) altında tamamen ücretsiz ve açık kaynaklıdır.
İstediğiniz gibi kullanabilir, özelleştirebilir ve dağıtabilirsiniz!
