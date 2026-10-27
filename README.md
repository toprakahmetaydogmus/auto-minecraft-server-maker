# ⚔️ Auto Minecraft Server Maker & AI Engineer Pro (v4.0.0 Master)

<div align="center">

![Version](https://img.shields.io/badge/Release-v4.0.0%20Master-00E5FF?style=for-the-badge&logo=github&logoColor=white)
![Python Version](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GUI Framework](https://img.shields.io/badge/GUI-CustomTkinter%20Cyberpunk-9333ea?style=for-the-badge&logo=windows11&logoColor=white)
![Minecraft](https://img.shields.io/badge/Minecraft-163%2B%20Versions%20(26.x%20%E2%86%92%20c0.30)-2E7D32?style=for-the-badge&logo=minecraft&logoColor=white)
![Local AI](https://img.shields.io/badge/Local%20AI-Ollama%201.5B%20%7C%20Zero--Key-FF6F00?style=for-the-badge&logo=ollama&logoColor=white)
![Modrinth](https://img.shields.io/badge/Modrinth-Autonomous%20Downloader-00AF5C?style=for-the-badge&logo=modrinth&logoColor=white)
![Security](https://img.shields.io/badge/Security-100%25%20Zero--Leak-00C853?style=for-the-badge&logo=shield&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-F57C00?style=for-the-badge)

**The Ultimate Autonomous Minecraft Server Orchestrator, Zero-API-Key Local AI Assistant, Modrinth Auto-Mod Downloader, Crash Doctor, Portless Tunneling & 380+ Command Master Administration Suite.**

[English Documentation](#-english-documentation) • [Türkçe Dokümantasyon](#-türkçe-dokümantasyon) • [Download Standalone .EXE](https://github.com/toprakahmetaydogmus/auto-minecraft-server-maker/releases/tag/v4.0.0)

</div>

---

## 🌟 What's New in v4.0.0 Master?

### 1. 🛡️ Java 25 & `sun.misc.Unsafe` Crash Prevention (Root-Level Fix)
* **The Problem:** Modern systems running Java 25 (`Temurin-25.0.3+9`) crashed immediately on Forge / Arclight 1.20.1 due to OpenJDK removing `sun.misc.Unsafe.ensureClassInitialized`.
* **The Solution:** 
  * Integrated autonomous runtime detection (`JavaDetector.ensure_compatible_java`).
  * Strictly forces **Java 17** for Minecraft 1.18 through 1.20.4, bypassing system Java 25.
  * Auto-provisions portable **Adoptium OpenJDK 17** (`tools/java/jre-17/bin/java.exe`).
  * Emits runtime-hardened `start.bat` with JVM reflection flags: `--add-opens java.base/sun.misc=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED`.

### 2. 🤖 100% Local AI by Default (Zero API Keys Needed!)
* **No API Key Required:** Defaults to `Ollama (Yerel/Ücretsiz)` and ultra-fast `qwen2.5:1.5b` (or `llama3.2:1b/3b`).
* **1-Click Local Setup:** Download Ollama and pull lightweight models with streaming progress directly from the UI.
* **Autonomous Offline Expert Engine:** Even without internet or Ollama, the built-in offline NLP engine analyzes prompt intents, diagnoses crash stack traces, and tunes server memory at **0 ms latency**.

### 3. 📦 Autonomous Mod Fetcher (Modrinth Public REST API)
* Just describe your theme (e.g. *"1.20.1 magic and swords forge server"*), and the engine:
  * Identifies the required loader (`Forge`, `Fabric`, `NeoForge`).
  * Directly queries Modrinth's official CDN for verified, safe `.jar` files.
  * Downloads mods like `Iron's Spells 'n Spellbooks`, `Simply Swords`, `Better Combat`, `JourneyMap`, `JEI`, and `FerriteCore` straight into `server/mods`.

### 4. 🌐 5-Engine Multi-Tunneling (Play Without Port Forwarding)
* **Playit.gg:** 1-Click zero-config global tunnel (`xyz.gl.at.ply.gg:port`).
* **Cloudflare Named Tunnels:** Enterprise-grade subdomains.
* **ngrok & Localtonet:** Custom token & endpoint support.
* **UPnP Autonomous Mapper:** Local router port mapper.

### 5. 📜 Complete 163+ Version History (2026 Game Drops down to Classic)
* **2026 Drops:** 26.4, 26.3 (Wilderness Bound), 26.2 (Chaos Cubed), 26.1 (Tiny Takeover).
* **Modern Releases:** 1.21.4 (The Garden Awakens), 1.21.1, 1.20.4, 1.20.1, 1.19.4.
* **Golden Age:** 1.16.5, 1.12.2, 1.8.9, 1.7.10.
* **Nostalgia & Betas:** Beta b1.8.1, b1.7.3, Alpha a1.2.6 Halloween, Infdev, Indev, and Classic c0.30.

---

## 🚀 Quick Start

### Option A: Standalone Windows Executable (Recommended)
1. Download **`Auto-Minecraft-Server-Maker-v4.0.0-Master.exe`** from [GitHub Releases](https://github.com/toprakahmetaydogmus/auto-minecraft-server-maker/releases/tag/v4.0.0).
2. Double-click to run — **zero installation, zero dependencies, 100% self-contained (38.87 MB)**.

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
| 🛡️ **Offline Expert** | Built-in Rule & Semantic Knowledge Engine | **None (Zero Token, Instant)** |
| 🔷 **Google Gemini** | `gemini-1.5-flash`, `gemini-1.5-pro` | Free Google AI Key |
| 🧠 **OpenAI** | `gpt-4o`, `gpt-4o-mini` | OpenAI API Key |
| 🪶 **Anthropic** | `claude-3-5-sonnet`, `claude-3-haiku` | Anthropic API Key |
| ⚡ **Groq** | `llama-3.3-70b-versatile` | Groq API Key |
| 🐋 **DeepSeek** | `deepseek-chat`, `deepseek-reasoner` | DeepSeek API Key |
| 🟢 **NVIDIA NIM** | `meta/llama-3.1-70b-instruct` | NVIDIA NIM API Key |
| 🌐 **OpenRouter** | 100+ Multi-Provider Models | OpenRouter API Key |

---

## 🇹🇷 Türkçe Dokümantasyon

### 🌟 Öne Çıkan Yetenekler:
1. **Sıfır Bilgiyle Sunucu Açma:** *"1.20.1 büyü kılıç modu ve harita kur"* yazın veya senaryo çipine tıklayın. AI motoru çekirdeği (Forge), belleği ve uyumlu modları Modrinth'ten otonom olarak kurar.
2. **Java 25 Çökme Koruması:** Forge 1.20.1 sunucularının Java 25 yüklü bilgisayarlarda verdiği `sun.misc.Unsafe` hatasını, taşınabilir **Adoptium Java 17** bağlayarak kökten çözer.
3. **Modemsiz & Port Açmadan Arkadaşlarla Oynama:** Playit.gg ve UPnP tünelleri sayesinde modem şifrenizi bilmeden tek tıkla arkadaşlarınızın girebileceği genel IP linki üretir.
4. **Çökmeyi Teşhis Et (Crash Doctor):** Sunucu çöktüğünde logları okur, hatanın kaynağını (çakışan mod, dolu port, yetersiz RAM) Türkçe olarak açıklar ve çözüm adımlarını listeler.
5. **Bedrock & Java Crossplay:** Geyser & Floodgate eklentilerini tek tıkla kurarak telefon, tablet ve konsoldaki oyuncuların sunucunuza bağlanmasını sağlar.

---

## 🔒 100% Zero-Leak Security Architecture
* Tüm API anahtarları, tünel token'ları ve yerel ayarlar yalnızca kullanıcının yerel makinesindeki `config.json` dosyasında tutulur.
* Repoda hiçbir kişisel veri, parola veya gizli anahtar commitlenmez.

---

## 📜 Lisans
Bu proje [MIT Lisansı](LICENSE) altında tamamen ücretsiz ve açık kaynaklıdır.
İstediğiniz gibi kullanabilir, özelleştirebilir ve dağıtabilirsiniz!
