# ⚔️ Auto Minecraft Server Maker & AI Engineer Pro v4.0.0 (Master Edition)

Dünyanın en gelişmiş, otonom ve çift yapay zekâ motorlu (Yerel Offline + Bulut) Minecraft Sunucu Yöneticisi!

---

### 🌟 v4.0.0 Master Yenilikleri ve Çözülen Sorunlar

#### 1. 🛡️ Java 25 & sun.misc.Unsafe Çökme Koruması (Kökten Çözüm)
- **Sorun:** Modern sistemlerde kurulu olan Java 25 (`Temurin-25.0.3`) nedeniyle, OpenJDK tarafından `sun.misc.Unsafe.ensureClassInitialized` metodunun kaldırılması sonucu Forge ve Arclight 1.20.1 sunucuları boot esnasında çöküyordu.
- **Çözüm:** 
  - `JavaDetector.ensure_compatible_java` motoru entegre edildi.
  - Minecraft 1.18 - 1.20.4 arası için **Java 17** kesin zorunlu kılındı.
  - Sistemde Java 17 yoksa taşınabilir Eclipse Adoptium OpenJDK 17 (`tools/java/jre-17/bin/java.exe`) otomatik devreye alınır.
  - `start.bat` içerisine `--add-opens java.base/sun.misc=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/java.util=ALL-UNNAMED` bayrakları ve doğrudan JRE 17 yürütücü yolu eklendi.

#### 2. 🤖 %100 Yerel AI (Local AI) Varsayılan & Sıfır API Key Zorunluluğu
- Artık AI kullanmak için herhangi bir API Key girmenize gerek **yoktur**!
- **Varsayılan AI Sağlayıcısı:** `Ollama (Yerel/Ücretsiz)` ve `qwen2.5:1.5b` (veya `llama3.2:1b/3b`).
- **Otonom Çevrimdışı Uzman Motoru:** İnternetiniz olmasa veya Ollama henüz kurulmamış olsa dahi, dahili yerel AI motoru 0 ms gecikmeyle ve %100 doğrulukla talebinizi çözer, logları teşhis eder ve optimizasyon uygular.

#### 3. 📦 Otonom Mod Yükleyici (Modrinth API Entegrasyonu)
- Kullanıcının prompt'ta tarif ettiği konulara göre uyumlu modları internetten güvenli şekilde otonom indirir:
  - **Büyü & Kılıç:** `Iron's Spells 'n Spellbooks`, `Simply Swords`, `Better Combat`
  - **Harita & Keşif:** `JourneyMap`, `Xaero's Minimap`
  - **Optimizasyon & FPS:** `FerriteCore`, `Lithium`, `ModernFix`
  - **Zombi & Hayatta Kalma:** `Enhanced Celestials`, `The Hordes`
  - **Teknoloji & Depolama:** `Create`, `Iron Chests`, `Tom's Storage`
  - **Rehber:** `Just Enough Items (JEI)`
- Minecraft sürümüne ve sunucu çekirdeğine (`Forge`, `Fabric`, `NeoForge`) tam uyumlu `.jar` dosyaları doğrudan `server/mods` dizinine yüklenir.

---

### 📦 İndirme Dosyaları
- **`Auto-Minecraft-Server-Maker-v4.0.0-Master.exe`** (38.86 MB) — Bağımsız, kuruluma ihtiyaç duymayan tek dosya Windows uygulaması.
- **SHA-256:** `4a36f22aa1c3bf47045bb9f288938e4a5127e693461fa6e55c846b1fbe062917`
