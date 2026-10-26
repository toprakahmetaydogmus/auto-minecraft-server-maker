# ⚔️ Auto Minecraft Server Maker & AI Engineer Pro

<div align="center">

![Python Version](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Minecraft](https://img.shields.io/badge/Minecraft-All%20Versions%20(1.7.x--1.21.x)-2E7D32?style=for-the-badge&logo=minecraft&logoColor=white)
![AI Providers](https://img.shields.io/badge/AI%20Providers-12%20Engines%20Supported-7B1FA2?style=for-the-badge&logo=openai&logoColor=white)
![Security](https://img.shields.io/badge/Security-100%25%20Zero--Leak-00C853?style=for-the-badge&logo=shield&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-F57C00?style=for-the-badge)

**The Ultimate Autonomous Minecraft Server Creation, AI-Powered Crash Diagnostics, and 380+ Command Master Administration Suite.**

[English](#-english-documentation) • [Türkçe Dokümantasyon](#-türkçe-dokümantasyon)

</div>

---

## 🌟 Highlights & Key Features

### 1. 🚀 Autonomous Server Creator (Her Sürüm & Her Tür)
- **One-Click Installation**: Automatically downloads official server binaries, generates `server.properties`, auto-accepts EULA (`eula=true`), and configures Aikar's high-performance G1GC flags in `start.bat`.
- **Supported Server Flavors**:
  - ⚡ **PaperMC**: Ultra-high performance Spigot fork.
  - 🟣 **Purpur**: Feature-packed, customizable Paper fork.
  - 🧵 **Fabric**: Modern, lightweight, fast modded loader.
  - 🏹 **Arclight (Forge + Bukkit)**: Full hybrid supporting Forge mods + Spigot plugins simultaneously.
  - 📦 **Vanilla**: Official pure Mojang server software.
- **Crossplay Ready**: Built-in 1-click **Geyser** support for seamless Java & Bedrock (Mobile/Xbox/PS/PC) crossplay.
- **Intelligent Java Detector**: Automatically scans and detects Java 8, 16, 17, and 21 across your system, matching the exact requirement of the target Minecraft version.

---

### 2. 🤖 AI Server Engineer & Crash Diagnostics (12+ AI Engines)
Never struggle with cryptic stack traces, mod conflicts, or chunk corruption again! Supports 12 leading AI engines:

| AI Provider | Description & Models |
|---|---|
| 🟢 **NVIDIA NIM** | Meta Llama 3.1 70B/405B, Mixtral via NVIDIA NIM API |
| 🌐 **OpenRouter** | 100+ models including Claude 3.5 Sonnet, DeepSeek & Free Llama 3 |
| 🧠 **OpenAI** | GPT-4o, GPT-4o-mini |
| 🪶 **Anthropic** | Claude 3.5 Sonnet, Claude 3 Haiku |
| 🔷 **Google Gemini** | Gemini 1.5 Pro, Gemini 1.5 Flash |
| ⚡ **Groq** | Blazing-fast real-time inference (Llama 3.3 70B) |
| 🌪️ **Mistral AI** | Mistral Large, Codestral |
| 🤝 **Together AI** | Meta Llama 3.1 Turbo |
| 🔍 **Perplexity** | Real-time web-grounded Sonar AI |
| 💬 **Cohere** | Command R+ |
| 🐋 **DeepSeek** | DeepSeek V3, DeepSeek R1 |
| 🦙 **Ollama (Local)** | **100% Free & Offline** (Llama 3, Qwen, Mistral - Zero API keys required!) |

**AI Capabilities:**
- 🚨 **Autonomous Crash Diagnosis**: Analyzes `crash-reports/` and `logs/latest.log` to pinpoint exact mod ID conflicts, missing dependencies, or corrupted configs.
- ⚡ **Lag-Free Server Optimizer**: Generates custom JVM flags and config recommendations tailored to your RAM and player count.
- 💬 **Live Chat & Command Generator**: Generates complex NBT commands, `/fill` structures, and plugin setup guides.

---

### 3. 🎮 Master Admin Control Panel & Universal Block Hub
Embedded control center with **380+ commands** categorized across 16 tabs:

- 🧱 **Universal Block Hub**:
  - Interactive catalog with 300+ Minecraft blocks.
  - **5 Placement Modes**:
    1. 🚀 **Inventory Delivery** (`give {p} {block} {qty}`)
    2. 🦶 **Under Feet** (`execute at {p} run setblock ~ ~-1 ~ {block}`)
    3. 🧱 **3x3 Front Wall** (`execute at {p} run fill ^-1 ^ ^3 ^1 ^2 ^3 {block}`)
    4. 🕳️ **Box Caging** (`execute at {p} run fill ~-1 ~-1 ~-1 ~1 ~2 ~1 {block} outline`)
    5. 🌟 **5x5 Platform** (`execute at {p} run fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 {block}`)
  - Flexible quantities: `1x`, `16x`, `32x`, `64x` (1 stack), `128x`, `256x`, `576x` (Full Inventory).
- 📦 **Themed Mega Shulker Box Kits** (Strictly sized below Minecraft's 1460-byte RCON limit):
  - 🧱 Legendary Admin Box (Barrier, Command Blocks, Light Lvl 15, Bedrock, Spawner)
  - 💎 Billionaire Miner Box (Netherite, Diamond, Emerald, Ancient Debris)
  - 🏗️ Luxury Architect Box (Cherry, Bamboo, Deepslate, Quartz, Tinted Glass)
  - 💡 Ultimate Lighting Box (Beacon, Sea Lantern, 3 Froglights, End Rod)
  - ⚙️ Redstone Engineer Box (TNT, Slime, Honey, Pistons, Observers, Hoppers)
  - 🌈 Rainbow Concrete Box (All 9 vibrant full-stack concretes)
  - 🪵 Wood Master Box (All 9 tree species logs)
  - ⛏️ Deepslate Ore Box (All deepslate ores)
- ⚡ **Legendary Master Equipment Sets (Lvl 255)**:
  - Apocalypse Sword, Seismic Pickaxe, Silk Touch Pickaxe, Forest Axe, Nuclear Bow, Lightning Trident, Master Armor, Infinite Elytra.
- 🤡 **Troll & Player Fun Suite**: Space Launch (Y:500), Bury (Y:-58), Glass/Obsidian cages, Anvil drop, Nausea 255, Blindness, Warden scream jumpscare.
- 🪄 **Enchanter & 30+ Potion Buffs**: MEGA ULTRA BUFF, Haste 255, Resistance V, Strength 100, Speed 5, Night Vision.
- 🌐 **Multi-Interface LAN Broadcaster**: Broadcasts UDP discovery (`224.0.2.60:4445`) across WiFi, Ethernet, and VPN adapters (Radmin VPN, Hamachi, ZeroTier).

---

### 4. 🔒 100% Zero-Leak Security Architecture
- **No hardcoded API keys, tokens, or personal identifiers.**
- API keys and configurations are saved exclusively to local `config.json` (strictly covered in `.gitignore`).
- Sanitized `config.example.json` provided for clean onboarding.

---

## 📥 Installation & Download

### 🚀 Direct Download (No Python Required)
You can directly download the ready-to-use Windows `.exe` from our GitHub Releases:
👉 **[Download Latest Auto-Minecraft-Server-Maker.exe](https://github.com/toprakahmetaydogmus/auto-minecraft-server-maker/releases/latest)**

---

### Option A: Run from Source (Python 3.9+)

```bash
# 1. Clone repository
git clone https://github.com/toprakahmetaydogmus/auto-minecraft-server-maker.git
cd auto-minecraft-server-maker

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch application
python main.py
```

### Option B: Build Windows Standalone `.exe` Locally

```bash
# Run the 1-click compiler
build_exe.bat
# Output executable will be in: dist/Auto-Minecraft-Server-Maker.exe
```

---

## 🇹🇷 Türkçe Dokümantasyon

### Genel Bakış
Auto Minecraft Server Maker, her Minecraft sürümü için (1.7.x - 1.21.x) tek tıkla otomatik sunucu kuran, 12 farklı yapay zekâ motoruyla ve **%100 Çevrimdışı / Ücretsiz Yerel AI (Ollama)** desteğiyle sunucu çökmelerini ve log hatalarını anında teşhis eden, 380+ komutluk gelişmiş Master Admin Paneli içeren profesyonel bir sunucu yönetim merkezidir.

### Temel Özellikler
1. **Tek Tıkla Kurulum**: Paper, Purpur, Fabric, Arclight (Forge+Plugin) ve Vanilla sunucuları otomatik indirir, EULA'yı onaylar, `server.properties` ve optimize `start.bat` dosyalarını üretir.
2. **Bedrock Crossplay**: Geyser eklentisiyle mobil (iOS/Android) ve konsol oyuncularının sunucuya bağlanmasını sağlar.
3. **🛡️ 1-Tıkla Yerel AI Hub (Offline & Ücretsiz)**: API anahtarı gerekmeden tek tıkla Ollama kurulumu (`OllamaSetup.exe`), arka planda servis başlatma (`ollama serve`) ve canlı progress bar ile model indirme (`qwen2.5:1.5b`, `llama3.2:3b`, `phi3:mini`, `mistral:7b`).
4. **12 AI Motoru**: NVIDIA NIM, OpenRouter, OpenAI, Claude, Gemini, Groq, Mistral, Together, Perplexity, Cohere, DeepSeek ve Ollama ile çökme raporlarını okur, mod uyumsuzluklarını tespit edip adım adım çözüm sunar.
5. **Gelişmiş Blok & Eşya Merkezi**: 300+ bloğu envantere verme, ayak altına koyma, önüne 3x3 duvar örme veya platform yapma özellikleri.
6. **Efsanevi Master Setler**: Lvl 255 kırılmaz zırhlar, tek atan kılıçlar ve tematik Shulker sandıkları (1460 byte RCON sınırına tam uyumlu).
7. **100% Zero-Leak Güvenlik**: API anahtarlarınız ve kişisel verileriniz asla repoya veya üçüncü taraflara aktarılmaz.

---

## 🤝 Contributing & License
Contributions, feature requests, and PRs are welcome!
Licensed under the [MIT License](LICENSE).

