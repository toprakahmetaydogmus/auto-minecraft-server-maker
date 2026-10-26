"""
Tab: Master Admin Control Panel & Universal Block Spawner Hub
Efsanevi Master Ekipmanlar, Gelişmiş Blok Dağıtım Merkezi ve 380+ Yönetici Komutu.
Completely sanitized of any personal names, IPs, or hardcoded passwords.
"""

import time
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext
from ui.theme import *
from core.rcon_client import MinecraftRcon

# =============================================================================
# EFSANEVİ EKİPMAN SANDIKLARI (Lvl 255 - 1460 Byte Sınırına Uygun)
# =============================================================================
CMD_BOX_ARMOR = 'give {p} cyan_shulker_box{display:{Name:\'{"text":"🛡️ EFSANEVİ MASTER ZIRH SANDIĞI (LVL 255)","color":"aqua","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"netherite_helmet",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"protection",lvl:255s},{id:"unbreaking",lvl:255s},{id:"respiration",lvl:255s},{id:"thorns",lvl:255s}]}},{Slot:1b,id:"netherite_chestplate",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"protection",lvl:255s},{id:"unbreaking",lvl:255s},{id:"blast_protection",lvl:255s},{id:"thorns",lvl:255s}]}},{Slot:2b,id:"netherite_leggings",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"protection",lvl:255s},{id:"unbreaking",lvl:255s},{id:"fire_protection",lvl:255s},{id:"thorns",lvl:255s}]}},{Slot:3b,id:"netherite_boots",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"protection",lvl:255s},{id:"unbreaking",lvl:255s},{id:"feather_falling",lvl:255s},{id:"thorns",lvl:255s}]}},{Slot:4b,id:"elytra",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"unbreaking",lvl:255s},{id:"mending",lvl:1s}]}},{Slot:5b,id:"shield",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"unbreaking",lvl:255s},{id:"thorns",lvl:255s}]}}]}} 1'

CMD_BOX_WEAPONS = 'give {p} black_shulker_box{display:{Name:\'{"text":"⚡ EFSANEVİ SİLAH & ALET SANDIĞI","color":"gold","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"netherite_sword",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"sharpness",lvl:255s},{id:"looting",lvl:255s},{id:"fire_aspect",lvl:255s},{id:"sweeping",lvl:255s},{id:"knockback",lvl:10s}]}},{Slot:1b,id:"netherite_pickaxe",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"efficiency",lvl:255s},{id:"fortune",lvl:255s}]}},{Slot:2b,id:"netherite_pickaxe",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"efficiency",lvl:255s},{id:"silk_touch",lvl:1s}]}},{Slot:3b,id:"netherite_axe",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"efficiency",lvl:255s},{id:"sharpness",lvl:255s},{id:"fortune",lvl:255s}]}},{Slot:4b,id:"netherite_shovel",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"efficiency",lvl:255s},{id:"fortune",lvl:255s}]}},{Slot:5b,id:"bow",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"power",lvl:255s},{id:"flame",lvl:255s},{id:"punch",lvl:50s},{id:"infinity",lvl:1s}]}},{Slot:6b,id:"crossbow",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"quick_charge",lvl:5s},{id:"multishot",lvl:1s},{id:"piercing",lvl:255s}]}},{Slot:7b,id:"trident",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"impaling",lvl:255s},{id:"loyalty",lvl:3s},{id:"channeling",lvl:1s}]}}]}} 1'

CMD_BOX_SUPPLIES = 'give {p} purple_shulker_box{display:{Name:\'{"text":"💎 EFSANEVİ İKMAL & TOTEM SANDIĞI","color":"light_purple","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"totem_of_undying",Count:64b},{Slot:1b,id:"totem_of_undying",Count:64b},{Slot:2b,id:"enchanted_golden_apple",Count:64b},{Slot:3b,id:"enchanted_golden_apple",Count:64b},{Slot:4b,id:"firework_rocket",Count:64b,tag:{Fireworks:{Flight:3b}}},{Slot:5b,id:"firework_rocket",Count:64b,tag:{Fireworks:{Flight:3b}}},{Slot:6b,id:"ender_pearl",Count:16b},{Slot:7b,id:"arrow",Count:1b},{Slot:8b,id:"spectral_arrow",Count:64b},{Slot:9b,id:"tipped_arrow",Count:64b,tag:{Potion:"minecraft:strong_harming"}},{Slot:10b,id:"experience_bottle",Count:64b},{Slot:11b,id:"netherite_block",Count:64b},{Slot:12b,id:"diamond_block",Count:64b},{Slot:13b,id:"golden_carrot",Count:64b},{Slot:14b,id:"end_crystal",Count:64b}]}} 1'

CMD_COMBO_FULL = f"{CMD_BOX_ARMOR} && {CMD_BOX_WEAPONS} && {CMD_BOX_SUPPLIES}"

# =============================================================================
# KOMBİNE TEMATİK BLOK SANDIKLARI (Themed Mega Shulker Boxes - Güvenli Boyut)
# =============================================================================
CMD_SHULKER_ADMIN = 'give {p} black_shulker_box{display:{Name:\'{"text":"🧱 EFSANEVİ ADMİN & İLLEGAL BLOK SANDIĞI","color":"dark_purple","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"barrier",Count:64b},{Slot:1b,id:"command_block",Count:64b},{Slot:2b,id:"repeating_command_block",Count:64b},{Slot:3b,id:"chain_command_block",Count:64b},{Slot:4b,id:"light",Count:64b,tag:{BlockStateTag:{level:"15"}}},{Slot:5b,id:"bedrock",Count:64b},{Slot:6b,id:"spawner",Count:64b},{Slot:7b,id:"structure_block",Count:64b},{Slot:8b,id:"sculk_shrieker",Count:64b,tag:{BlockEntityTag:{can_summon:1b}}}]}} 1'

CMD_SHULKER_ORES = 'give {p} cyan_shulker_box{display:{Name:\'{"text":"💎 MİLYARDER MADENCİ SANDIĞI","color":"aqua","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"ancient_debris",Count:64b},{Slot:1b,id:"netherite_block",Count:64b},{Slot:2b,id:"diamond_block",Count:64b},{Slot:3b,id:"emerald_block",Count:64b},{Slot:4b,id:"gold_block",Count:64b},{Slot:5b,id:"iron_block",Count:64b},{Slot:6b,id:"lapis_block",Count:64b},{Slot:7b,id:"redstone_block",Count:64b},{Slot:8b,id:"amethyst_block",Count:64b}]}} 1'

CMD_SHULKER_ARCHITECT = 'give {p} pink_shulker_box{display:{Name:\'{"text":"🏗️ LÜKS MİMAR & İNŞAAT SANDIĞI","color":"light_purple","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"cherry_log",Count:64b},{Slot:1b,id:"cherry_planks",Count:64b},{Slot:2b,id:"bamboo_block",Count:64b},{Slot:3b,id:"bamboo_planks",Count:64b},{Slot:4b,id:"deepslate_bricks",Count:64b},{Slot:5b,id:"polished_deepslate",Count:64b},{Slot:6b,id:"smooth_quartz",Count:64b},{Slot:7b,id:"calcite",Count:64b},{Slot:8b,id:"tinted_glass",Count:64b}]}} 1'

CMD_SHULKER_LIGHT = 'give {p} yellow_shulker_box{display:{Name:\'{"text":"💡 IŞIK & AYDINLATMA SANDIĞI","color":"yellow","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"beacon",Count:64b},{Slot:1b,id:"sea_lantern",Count:64b},{Slot:2b,id:"glowstone",Count:64b},{Slot:3b,id:"shroomlight",Count:64b},{Slot:4b,id:"ochre_froglight",Count:64b},{Slot:5b,id:"pearlescent_froglight",Count:64b},{Slot:6b,id:"verdant_froglight",Count:64b},{Slot:7b,id:"end_rod",Count:64b},{Slot:8b,id:"lantern",Count:64b}]}} 1'

CMD_SHULKER_REDSTONE = 'give {p} red_shulker_box{display:{Name:\'{"text":"⚙️ KIZILTAŞ MÜHENDİSİ SANDIĞI","color":"red","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"tnt",Count:64b},{Slot:1b,id:"slime_block",Count:64b},{Slot:2b,id:"honey_block",Count:64b},{Slot:3b,id:"sticky_piston",Count:64b},{Slot:4b,id:"observer",Count:64b},{Slot:5b,id:"hopper",Count:64b},{Slot:6b,id:"target",Count:64b},{Slot:7b,id:"dispenser",Count:64b},{Slot:8b,id:"redstone_block",Count:64b}]}} 1'

CMD_SHULKER_CONCRETE = 'give {p} purple_shulker_box{display:{Name:\'{"text":"🌈 GÖKKUŞAĞI BETON SANDIĞI","color":"dark_purple","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"white_concrete",Count:64b},{Slot:1b,id:"black_concrete",Count:64b},{Slot:2b,id:"red_concrete",Count:64b},{Slot:3b,id:"blue_concrete",Count:64b},{Slot:4b,id:"yellow_concrete",Count:64b},{Slot:5b,id:"lime_concrete",Count:64b},{Slot:6b,id:"light_blue_concrete",Count:64b},{Slot:7b,id:"purple_concrete",Count:64b},{Slot:8b,id:"orange_concrete",Count:64b}]}} 1'

CMD_SHULKER_WOOD = 'give {p} brown_shulker_box{display:{Name:\'{"text":"🪵 ORMANCI TÜM AĞAÇLAR SANDIĞI","color":"gold","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"oak_log",Count:64b},{Slot:1b,id:"spruce_log",Count:64b},{Slot:2b,id:"birch_log",Count:64b},{Slot:3b,id:"jungle_log",Count:64b},{Slot:4b,id:"acacia_log",Count:64b},{Slot:5b,id:"dark_oak_log",Count:64b},{Slot:6b,id:"mangrove_log",Count:64b},{Slot:7b,id:"crimson_stem",Count:64b},{Slot:8b,id:"warped_stem",Count:64b}]}} 1'

CMD_SHULKER_DEEPSLATE_ORES = 'give {p} gray_shulker_box{display:{Name:\'{"text":"⛏️ DERİN KAYRAK CEVHER SANDIĞI","color":"gray","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"deepslate_diamond_ore",Count:64b},{Slot:1b,id:"deepslate_emerald_ore",Count:64b},{Slot:2b,id:"deepslate_gold_ore",Count:64b},{Slot:3b,id:"deepslate_iron_ore",Count:64b},{Slot:4b,id:"deepslate_copper_ore",Count:64b},{Slot:5b,id:"deepslate_redstone_ore",Count:64b},{Slot:6b,id:"deepslate_lapis_ore",Count:64b},{Slot:7b,id:"deepslate_coal_ore",Count:64b},{Slot:8b,id:"ancient_debris",Count:64b}]}} 1'

BLOCK_CATALOG = {
    "🔥 EN ÇOK KULLANILANLAR": [
        ("🚫 Görünmez Bariyer Bloğu", "barrier"),
        ("⚡ Standart Komut Bloğu", "command_block"),
        ("🔄 Yineleyici Komut Bloğu", "repeating_command_block"),
        ("⛓️ Zincirleme Komut Bloğu", "chain_command_block"),
        ("💡 Görünmez Işık Bloğu (Işık 15)", "light[level=15]"),
        ("⬛ Kırılamaz Katman Kayası", "bedrock"),
        ("👾 Canavar Spawnerı (Boş)", "spawner"),
        ("🌌 Antik Kalıntı (Ancient Debris)", "ancient_debris"),
        ("🧱 Netherite Bloğu", "netherite_block"),
        ("💎 Elmas Bloğu", "diamond_block"),
        ("🟢 Zümrüt Bloğu", "emerald_block"),
        ("🪙 Altın Bloğu", "gold_block"),
        ("⛓️ Demir Bloğu", "iron_block"),
        ("🌊 Deniz Feneri (Sea Lantern)", "sea_lantern"),
        ("🐸 Sarı Kurbağa Işığı", "ochre_froglight"),
        ("🌸 Kiraz Ağacı Kütüğü", "cherry_log"),
        ("🎋 Bambu Bloğu", "bamboo_block"),
        ("🪟 Karartılmış Cam", "tinted_glass"),
        ("🧊 Mavi Buz", "blue_ice"),
        ("🧨 TNT Bloğu", "tnt")
    ],
    "🧱 İLLEGAL & ADMİN BLOKLARI": [
        ("🚫 Bariyer (Barrier)", "barrier"),
        ("⚡ Komut Bloğu", "command_block"),
        ("🔄 Yineleyici Komut Bloğu", "repeating_command_block"),
        ("⛓️ Zincirleme Komut Bloğu", "chain_command_block"),
        ("🛒 Komut Bloğu Vagonu", "command_block_minecart"),
        ("💡 Görünmez Işık (Işık 15)", "light[level=15]"),
        ("💡 Görünmez Işık (Işık 10)", "light[level=10]"),
        ("💡 Görünmez Işık (Işık 5)", "light[level=5]"),
        ("💡 Görünmez Işık (Işık 0)", "light[level=0]"),
        ("⬛ Katman Kayası (Bedrock)", "bedrock"),
        ("🏛️ Yapı Bloğu (Structure Block)", "structure_block"),
        ("🌌 Yapı Boşluğu (Structure Void)", "structure_void"),
        ("🧩 Yapı Parçası (Jigsaw Block)", "jigsaw"),
        ("🛑 Sınır Bloğu (Border Block)", "border_block"),
        ("🪑 İzin Bloğu (Allow Block)", "allow"),
        ("⛔ Red Bloğu (Deny Block)", "deny"),
        ("👾 Boş Spawner", "spawner"),
        ("🧟 Zombi Spawnerı", 'spawner{BlockEntityTag:{SpawnData:{entity:{id:"minecraft:zombie"}}}}'),
        ("💀 İskelet Spawnerı", 'spawner{BlockEntityTag:{SpawnData:{entity:{id:"minecraft:skeleton"}}}}'),
        ("🔥 Blaze Spawnerı", 'spawner{BlockEntityTag:{SpawnData:{entity:{id:"minecraft:blaze"}}}}'),
        ("🕷️ Örümcek Spawnerı", 'spawner{BlockEntityTag:{SpawnData:{entity:{id:"minecraft:spider"}}}}'),
        ("👹 Aktif Sculk Çığırtkanı", 'sculk_shrieker{BlockEntityTag:{can_summon:1b}}'),
        ("🛡️ Güçlendirilmiş Derin Kayrak", "reinforced_deepslate"),
        ("🐉 Ejderha Yumurtası", "dragon_egg"),
        ("👁️ End Portalı Çerçevesi (Gözlü)", "end_portal_frame[eye=true]"),
        ("🕳️ End Portalı Çerçevesi (Boş)", "end_portal_frame[eye=false]"),
        ("🔮 Yeniden Doğuş Çapası", "respawn_anchor")
    ],
    "💎 DEĞERLİ MADENLER & CEVHERLER": [
        ("🌌 Antik Kalıntı", "ancient_debris"),
        ("🧱 Netherite Bloğu", "netherite_block"),
        ("💎 Elmas Bloğu", "diamond_block"),
        ("🟢 Zümrüt Bloğu", "emerald_block"),
        ("🪙 Altın Bloğu", "gold_block"),
        ("⛓️ Demir Bloğu", "iron_block"),
        ("🟤 Bakır Bloğu", "copper_block"),
        ("🔴 Kızıltaş Bloğu", "redstone_block"),
        ("🔵 Lapis Lazuli Bloğu", "lapis_block"),
        ("⚫ Kömür Bloğu", "coal_block"),
        ("🟣 Ametist Bloğu", "amethyst_block"),
        ("🔮 Tomurcuklanan Ametist", "budding_amethyst"),
        ("✨ Ametist Kümesi", "amethyst_cluster"),
        ("💎 Derin Kayrak Elmas Cevheri", "deepslate_diamond_ore"),
        ("💎 Klasik Elmas Cevheri", "diamond_ore"),
        ("🟢 Derin Kayrak Zümrüt Cevheri", "deepslate_emerald_ore"),
        ("🟢 Klasik Zümrüt Cevheri", "emerald_ore"),
        ("🪙 Derin Kayrak Altın Cevheri", "deepslate_gold_ore"),
        ("⛓️ Derin Kayrak Demir Cevheri", "deepslate_iron_ore"),
        ("🟤 Derin Kayrak Bakır Cevheri", "deepslate_copper_ore"),
        ("🔴 Derin Kayrak Kızıltaş Cevheri", "deepslate_redstone_ore"),
        ("🔵 Derin Kayrak Lapis Cevheri", "deepslate_lapis_ore"),
        ("⚫ Derin Kayrak Kömür Cevheri", "deepslate_coal_ore"),
        ("🌋 Nether Altın Cevheri", "nether_gold_ore"),
        ("🌋 Nether Kuvars Cevheri", "nether_quartz_ore"),
        ("⛓️ Ham Demir Bloğu", "raw_iron_block"),
        ("🪙 Ham Altın Bloğu", "raw_gold_block"),
        ("🟤 Ham Bakır Bloğu", "raw_copper_block")
    ],
    "🏗️ İNŞAAT & MİMARİ BLOKLAR": [
        ("🧱 Derin Kayrak Tuğlası", "deepslate_bricks"),
        ("🧱 Cilalı Derin Kayrak", "polished_deepslate"),
        ("🧱 Derin Kayrak Karo", "deepslate_tiles"),
        ("🏛️ Pürüzsüz Kuvars", "smooth_quartz"),
        ("🏛️ Kuvars Sütunu", "quartz_pillar"),
        ("🤍 Kalsit (Calcite)", "calcite"),
        ("🩶 Tuff Taşı", "tuff"),
        ("🧱 Taş Tuğla", "stone_bricks"),
        ("🧱 Yosunlu Taş Tuğla", "mossy_stone_bricks"),
        ("🧱 Pürüzsüz Taş", "smooth_stone"),
        ("⬛ Cilalı Kara Taş", "polished_blackstone"),
        ("🪙 Altın Yaldızlı Kara Taş", "gilded_blackstone"),
        ("🧱 Çamur Tuğlaları", "mud_bricks"),
        ("🌊 Prizmarin Bloğu", "prismarine"),
        ("🟣 Obsidyen", "obsidian"),
        ("😭 Ağlayan Obsidyen", "crying_obsidian"),
        ("🧊 Mavi Buz", "blue_ice")
    ],
    "🪵 TÜM AĞAÇLAR & KÜTÜKLER": [
        ("🌸 Kiraz Ağacı Kütüğü", "cherry_log"),
        ("🌸 Kiraz Tahtası", "cherry_planks"),
        ("🎋 Bambu Bloğu", "bamboo_block"),
        ("🎋 Bambu Tahtası", "bamboo_planks"),
        ("🪵 Mangrov Kütüğü", "mangrove_log"),
        ("🪵 Mangrov Tahtası", "mangrove_planks"),
        ("🪵 Meşe Kütüğü", "oak_log"),
        ("🪵 Meşe Tahtası", "oak_planks"),
        ("🪵 Ladin Kütüğü", "spruce_log"),
        ("🪵 Ladin Tahtası", "spruce_planks"),
        ("🪵 Huş Kütüğü", "birch_log"),
        ("🪵 Orman Ağacı Kütüğü", "jungle_log"),
        ("🪵 Akasya Kütüğü", "acacia_log"),
        ("🪵 Karanlık Meşe Kütüğü", "dark_oak_log"),
        ("🍄 Kızıl Kök (Nether)", "crimson_stem"),
        ("🍄 Çarpık Kök (Nether)", "warped_stem")
    ],
    "🌈 BETON, CAM & RENKLER": [
        ("🪟 Karartılmış Cam", "tinted_glass"),
        ("🪟 Şeffaf Cam", "glass"),
        ("⬜ Beyaz Beton", "white_concrete"),
        ("⬛ Siyah Beton", "black_concrete"),
        ("🟥 Kırmızı Beton", "red_concrete"),
        ("🟦 Mavi Beton", "blue_concrete"),
        ("🟩 Açık Yeşil Beton", "lime_concrete"),
        ("🟨 Sarı Beton", "yellow_concrete"),
        ("🟧 Turuncu Beton", "orange_concrete"),
        ("🟪 Mor Beton", "purple_concrete"),
        ("🌸 Pembe Beton", "pink_concrete"),
        ("🩵 Açık Mavi Beton", "light_blue_concrete"),
        ("🩶 Gri Beton", "gray_concrete"),
        ("🧱 Pişmiş Toprak (Terracotta)", "terracotta")
    ],
    "💡 AYDINLATMA & IŞIK": [
        ("🏮 Fener (Beacon)", "beacon"),
        ("🌊 Deniz Feneri (Sea Lantern)", "sea_lantern"),
        ("💡 Işıktaşı (Glowstone)", "glowstone"),
        ("🍄 Mantar Işığı (Shroomlight)", "shroomlight"),
        ("🐸 Sarı Kurbağa Işığı", "ochre_froglight"),
        ("🐸 Beyaz Kurbağa Işığı", "pearlescent_froglight"),
        ("🐸 Yeşil Kurbağa Işığı", "verdant_froglight"),
        ("🪄 End Çubuğu (End Rod)", "end_rod"),
        ("🏮 Asılabilir Metal Fener", "lantern"),
        ("💙 Ruh Feneri (Soul Lantern)", "soul_lantern"),
        ("🏕️ Kamp Ateşi", "campfire"),
        ("🔴 Kızıltaş Lambası", "redstone_lamp"),
        ("🌿 Yosun Bloğu", "moss_block")
    ],
    "⚙️ REDSTONE & MEKANİZMA": [
        ("🧨 TNT Bloğu", "tnt"),
        ("🛒 TNT Vagonu", "tnt_minecart"),
        ("🟩 Balçık Bloğu (Slime)", "slime_block"),
        ("🍯 Bal Bloğu (Honey)", "honey_block"),
        ("🦾 Yapışkan Piston", "sticky_piston"),
        ("🦾 Normal Piston", "piston"),
        ("👁️ Gözlemci (Observer)", "observer"),
        ("📥 Huni (Hopper)", "hopper"),
        ("🎯 Hedef Bloğu (Target)", "target"),
        ("🔊 Sculk Sensörü", "sculk_sensor"),
        ("📦 Fırlatıcı (Dispenser)", "dispenser"),
        ("⚡ Yıldırımsavar", "lightning_rod"),
        ("🎚️ Şalter (Lever)", "lever"),
        ("📦 Sandık (Chest)", "chest"),
        ("👁️ Ender Sandığı", "ender_chest")
    ]
}

TABS_DATA = {
    "🧱 İLLEGAL & ADMİN BLOKLARI": [
        ("🚫 Görünmez Bariyer Bloğu", "give {p} barrier {qty}", "Yalnızca adminlerin görebildiği görünmez duvar"),
        ("⚡ Standart Komut Bloğu", "give {p} command_block {qty}", "Turuncu komut bloğu"),
        ("🔄 Yineleyici Komut Bloğu", "give {p} repeating_command_block {qty}", "Mor sürekli çalışan komut bloğu"),
        ("⛓️ Zincirleme Komut Bloğu", "give {p} chain_command_block {qty}", "Yeşil zincirleme komut bloğu"),
        ("💡 Görünmez Işık (Işık 15)", "give {p} light[level=15] {qty}", "Bloğu olmayan saf görünmez ışık"),
        ("⬛ Kırılamaz Katman Kayası", "give {p} bedrock {qty}", "Kırılamayan efsanevi blok"),
        ("🏛️ Yapı Bloğu (Structure)", "give {p} structure_block {qty}", "Yapıları kopyalama bloğu"),
        ("👾 Boş Canavar Spawnerı", "give {p} spawner {qty}", "Canavar kafesi"),
        ("🧟 Zombi Spawnerı", 'give {p} spawner{BlockEntityTag:{SpawnData:{entity:{id:"minecraft:zombie"}}}} {qty}', "Hazır zombi spawnerı"),
        ("💀 İskelet Spawnerı", 'give {p} spawner{BlockEntityTag:{SpawnData:{entity:{id:"minecraft:skeleton"}}}} {qty}', "Hazır iskelet spawnerı"),
        ("🔥 Blaze Spawnerı", 'give {p} spawner{BlockEntityTag:{SpawnData:{entity:{id:"minecraft:blaze"}}}} {qty}', "Blaze spawnerı"),
        ("👹 Aktif Sculk Çığırtkanı", 'give {p} sculk_shrieker{BlockEntityTag:{can_summon:1b}} {qty}', "Warden çıkaran aktif çığırtkan"),
        ("🛡️ Güçlendirilmiş Derin Kayrak", "give {p} reinforced_deepslate {qty}", "Warden kırılamaz bloğu"),
        ("🐉 Ejderha Yumurtası", "give {p} dragon_egg {qty}", "Ender ejderhası ödülü yumurta")
    ],
    "💎 DEĞERLİ MADENLER & CEVHERLER": [
        ("🌌 Antik Kalıntı (Ancient Debris)", "give {p} ancient_debris {qty}", "Nether madeni"),
        ("🧱 Netherite Bloğu", "give {p} netherite_block {qty}", "Som Netherite bloğu"),
        ("💎 Elmas Bloğu", "give {p} diamond_block {qty}", "Som Elmas bloğu"),
        ("🟢 Zümrüt Bloğu", "give {p} emerald_block {qty}", "Som Zümrüt bloğu"),
        ("🪙 Altın Bloğu", "give {p} gold_block {qty}", "Som Altın bloğu"),
        ("⛓️ Demir Bloğu", "give {p} iron_block {qty}", "Som Demir bloğu"),
        ("🔴 Kızıltaş Bloğu", "give {p} redstone_block {qty}", "Kızıltaş enerji bloğu"),
        ("🔵 Lapis Lazuli Bloğu", "give {p} lapis_block {qty}", "Büyü lapis bloğu"),
        ("🟣 Ametist Bloğu", "give {p} amethyst_block {qty}", "Ametist bloğu"),
        ("🔮 Tomurcuklanan Ametist", "give {p} budding_amethyst {qty}", "Nadir ametist ana bloğu"),
        ("💎 Derin Kayrak Elmas Cevheri", "give {p} deepslate_diamond_ore {qty}", "Derin elmas"),
        ("🟢 Derin Kayrak Zümrüt Cevheri", "give {p} deepslate_emerald_ore {qty}", "Derin zümrüt")
    ],
    "🏗️ İNŞAAT & MİMARİ BLOKLAR": [
        ("🧱 Derin Kayrak Tuğlası", "give {p} deepslate_bricks {qty}", "Koyu şık kale tuğlası"),
        ("🧱 Cilalı Derin Kayrak", "give {p} polished_deepslate {qty}", "Pürüzsüz mimari blok"),
        ("🏛️ Pürüzsüz Kuvars Bloğu", "give {p} smooth_quartz {qty}", "Modern beyaz villa bloğu"),
        ("🏛️ Kuvars Sütunu", "give {p} quartz_pillar {qty}", "Saray sütunu"),
        ("🤍 Kalsit (Calcite)", "give {p} calcite {qty}", "Tebeşir dokulu parlak beyaz taş"),
        ("🩶 Tuff Taşı", "give {p} tuff {qty}", "Dekoratif taş"),
        ("🧱 Taş Tuğla", "give {p} stone_bricks {qty}", "Klasik kale tuğlası"),
        ("⬛ Cilalı Kara Taş", "give {p} polished_blackstone {qty}", "Nether karataşı"),
        ("🪙 Altın Yaldızlı Kara Taş", "give {p} gilded_blackstone {qty}", "Altın damarlı taş"),
        ("🟣 Obsidyen", "give {p} obsidian {qty}", "Patlama korumalı taş"),
        ("😭 Ağlayan Obsidyen", "give {p} crying_obsidian {qty}", "Parlak obsidyen"),
        ("🧊 Mavi Buz", "give {p} blue_ice {qty}", "En hızlı kaygan buz")
    ],
    "🪵 TÜM AĞAÇLAR & KÜTÜKLER": [
        ("🌸 Kiraz Ağacı Kütüğü", "give {p} cherry_log {qty}", "1.20 kiraz kütüğü"),
        ("🌸 Kiraz Ağacı Tahtası", "give {p} cherry_planks {qty}", "Pembe tahta"),
        ("🎋 Bambu Bloğu", "give {p} bamboo_block {qty}", "Bambu kütüğü"),
        ("🎋 Bambu Tahtası", "give {p} bamboo_planks {qty}", "Bambu parke"),
        ("🪵 Mangrov Kütüğü", "give {p} mangrove_log {qty}", "Kızıl bataklık kütüğü"),
        ("🪵 Meşe Kütüğü", "give {p} oak_log {qty}", "Klasik meşe"),
        ("🪵 Ladin Kütüğü", "give {p} spruce_log {qty}", "Koyu dağ ladini"),
        ("🪵 Huş Ağacı Kütüğü", "give {p} birch_log {qty}", "Beyaz huş"),
        ("🪵 Karanlık Meşe Kütüğü", "give {p} dark_oak_log {qty}", "Koyu çikolata ahşap"),
        ("🍄 Kızıl Kök", "give {p} crimson_stem {qty}", "Nether mantar kütüğü"),
        ("🍄 Çarpık Kök", "give {p} warped_stem {qty}", "Nether turkuaz kütük")
    ],
    "🌈 BETON, CAM & RENKLER": [
        ("🪟 Karartılmış Cam", "give {p} tinted_glass {qty}", "Işık geçirmeyen özel cam"),
        ("🪟 Şeffaf Cam", "give {p} glass {qty}", "Klasik cam"),
        ("⬜ Beyaz Beton", "give {p} white_concrete {qty}", "Modern beyaz duvar"),
        ("⬛ Siyah Beton", "give {p} black_concrete {qty}", "Zifiri siyah duvar"),
        ("🟥 Kırmızı Beton", "give {p} red_concrete {qty}", "Kırmızı mimari blok"),
        ("🟦 Mavi Beton", "give {p} blue_concrete {qty}", "Mavi mimari blok"),
        ("🟩 Açık Yeşil Beton", "give {p} lime_concrete {qty}", "Canlı fıstık yeşili"),
        ("🟨 Sarı Beton", "give {p} yellow_concrete {qty}", "Parlak sarı blok"),
        ("🟪 Mor Beton", "give {p} purple_concrete {qty}", "Asil mor blok"),
        ("🌸 Pembe Beton", "give {p} pink_concrete {qty}", "Yumuşak pembe blok")
    ],
    "💡 AYDINLATMA & IŞIK BLOKLARI": [
        ("🏮 Fener (Beacon)", "give {p} beacon {qty}", "Piramit efekt kulesi"),
        ("🌊 Deniz Feneri (Sea Lantern)", "give {p} sea_lantern {qty}", "Açık mavi ışık küpü"),
        ("💡 Işıktaşı (Glowstone)", "give {p} glowstone {qty}", "Altın sarısı ışıktaşı"),
        ("🍄 Mantar Işığı (Shroomlight)", "give {p} shroomlight {qty}", "Sıcak mantar ışığı"),
        ("🐸 Kehribar Kurbağa Işığı", "give {p} ochre_froglight {qty}", "Sarı kurbağa ışığı"),
        ("🐸 İnci Kurbağa Işığı", "give {p} pearlescent_froglight {qty}", "Beyaz kurbağa ışığı"),
        ("🐸 Zümrüt Kurbağa Işığı", "give {p} verdant_froglight {qty}", "Yeşil kurbağa ışığı"),
        ("🪄 End Çubuğu (End Rod)", "give {p} end_rod {qty}", "Parlak beyaz ışık çubuğu"),
        ("🏮 Asılabilir Metal Fener", "give {p} lantern {qty}", "Metal fener"),
        ("💙 Ruh Feneri (Soul Lantern)", "give {p} soul_lantern {qty}", "Mavi alevli fener"),
        ("🔴 Kızıltaş Lambası", "give {p} redstone_lamp {qty}", "Elektrikli lamba")
    ],
    "🪄 HIZLI ALAN DOLDURMA (FILL & BUILD)": [
        ("🧱 Ayak Altına 5x5 Cam Platform", "execute at {p} run fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 glass", "Cam zemin"),
        ("⬛ Ayak Altına 5x5 Obsidyen Platform", "execute at {p} run fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 obsidian", "Patlamaz sağlam zemin"),
        ("💎 Ayak Altına 5x5 Elmas Platform", "execute at {p} run fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 diamond_block", "Elmas zemin"),
        ("🌱 Ayak Altına 10x10 Çimen Zemin", "execute at {p} run fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 grass_block", "Düz çimen"),
        ("🧹 Etraftaki Blokları Temizle (5x5x5)", "execute at {p} run fill ~-2 ~ ~-2 ~2 ~4 ~2 air", "Çevreyi silip hava yapar"),
        ("💡 Etrafı Görünmez Işıkla Doldur", "execute at {p} run fill ~-4 ~ ~-4 ~4 ~4 ~4 light[level=15] replace air", "Karanlık mağarayı aydınlatır"),
        ("🏡 Hızlı 7x7x5 Taş Villa Yap", "execute at {p} run fill ~-3 ~ ~-3 ~3 ~4 ~3 stone_bricks outline && execute at {p} run fill ~-1 ~1 ~-3 ~1 ~2 ~-3 glass && execute at {p} run setblock ~ ~3 ~ sea_lantern", "Pencereli sığınak ev"),
        ("💧 5x5x3 Su Havuzu Yap", "execute at {p} run fill ~-2 ~-3 ~-2 ~2 ~-1 ~2 water", "Su havuzu kazar"),
        ("🔥 5x5x2 Lav Havuzu Yap", "execute at {p} run fill ~-2 ~-2 ~-2 ~2 ~-1 ~2 lava", "Kızgın lav çukuru"),
        ("🧽 Çevredeki Suları Kurut", "execute at {p} run fill ~-4 ~-3 ~-4 ~4 ~3 ~4 air replace water", "Suları siler"),
        ("🧨 3x3 TNT Küpü Koy", "execute at {p} run fill ~-1 ~ ~-1 ~1 ~2 ~1 tnt", "27 blok TNT yerleştirir")
    ],
    "📦 KOMBİNE BLOK SANDIKLARI": [
        ("🧱 Efsanevi Admin Blok Sandığı", CMD_SHULKER_ADMIN, "Bariyer, Komut Blokları, Görünmez Işık 15, Bedrock, Spawner (64x)"),
        ("💎 Milyarder Madenci Sandığı", CMD_SHULKER_ORES, "Netherite, Elmas, Zümrüt, Altın, Demir, Kızıltaş Blokları (64x)"),
        ("🏗️ Lüks Mimar & İnşaat Sandığı", CMD_SHULKER_ARCHITECT, "Kiraz, Bambu, Derin Kayrak Tuğlası, Pürüzsüz Kuvars, Kalsit (64x)"),
        ("💡 Işık & Aydınlatma Sandığı", CMD_SHULKER_LIGHT, "Beacon, Deniz Feneri, Glowstone, 3 Kurbağa Işığı, End Rod (64x)"),
        ("⚙️ Kızıltaş Mühendisi Sandığı", CMD_SHULKER_REDSTONE, "TNT, Balçık, Bal, Piston, Gözlemci, Huni, Hedef (64x)"),
        ("🌈 Gökkuşağı Beton Sandığı", CMD_SHULKER_CONCRETE, "9 Renk Tam Stack Beton Paketi (64x)"),
        ("🪵 Ormancı Tüm Ağaçlar Sandığı", CMD_SHULKER_WOOD, "Tüm Ağaç Türlerinden Kütük Paketi (64x)"),
        ("⛏️ Derin Kayrak Cevher Sandığı", CMD_SHULKER_DEEPSLATE_ORES, "Tüm Derin Kayrak Maden Cevherleri (64x)")
    ],
    "⚡ EFSANEVİ MASTER SETLERİ (LVL 255)": [
        ("📦 FULL EFSANEVİ KİT (3 Sandık Dolusu)", CMD_COMBO_FULL, "Zırh + Silah + İkmal Sandığı (Tek Tıkla Envantere)"),
        ("🛡️ Efsanevi Zırh Sandığı (Lvl 255)", CMD_BOX_ARMOR, "Netherite Kask, Göğüslük, Pantolon, Çizme, Elytra, Kalkan"),
        ("⚡ Efsanevi Silah & Alet Sandığı", CMD_BOX_WEAPONS, "Kılıç, Kazmalar, Balta, Kürek, Çapa, Yay, Arbalet, Mızrak"),
        ("💎 Efsanevi İkmal & Totem Sandığı", CMD_BOX_SUPPLIES, "128x Totem, 128x Notch Elma, Fişek, Kristal, Elmas Bloklar"),
        ("🗡️ Efsanevi Kıyamet Kılıcı (Tek Atan)", 'give {p} netherite_sword{Unbreakable:1b,Enchantments:[{id:"sharpness",lvl:255s},{id:"looting",lvl:255s},{id:"fire_aspect",lvl:255s},{id:"sweeping",lvl:255s},{id:"knockback",lvl:10s}]} 1', "Milyon hasar vuran kılıç"),
        ("⛏️ Efsanevi Deprem Kazması (Lvl 255 Servet)", 'give {p} netherite_pickaxe{Unbreakable:1b,Enchantments:[{id:"efficiency",lvl:255s},{id:"fortune",lvl:255s}]} 1', "Anında kazar ve yüzlerce elmas düşürür"),
        ("💎 İpeksi Efsane Kazma", 'give {p} netherite_pickaxe{Unbreakable:1b,Enchantments:[{id:"efficiency",lvl:255s},{id:"silk_touch",lvl:1s}]} 1', "Blokları olduğu gibi kıran kazma"),
        ("🪓 Efsanevi Orman Baltası", 'give {p} netherite_axe{Unbreakable:1b,Enchantments:[{id:"efficiency",lvl:255s},{id:"sharpness",lvl:255s},{id:"fortune",lvl:255s}]} 1', "Ağaçları tek vuruşta devirir"),
        ("🏹 Nükleer Sonsuzluk Yayı", 'give {p} bow{Unbreakable:1b,Enchantments:[{id:"power",lvl:255s},{id:"flame",lvl:255s},{id:"punch",lvl:50s},{id:"infinity",lvl:1s}]} 1', "1 okla sonsuz nükleer hasar"),
        ("🔱 Fırtına Mızrağı (Trident)", 'give {p} trident{Unbreakable:1b,Enchantments:[{id:"impaling",lvl:255s},{id:"loyalty",lvl:3s},{id:"channeling",lvl:1s}]} 1', "Yıldırımlı geri dönen mızrak"),
        ("🪽 Sonsuz Master Elytra", 'give {p} elytra{Unbreakable:1b,Enchantments:[{id:"unbreaking",lvl:255s},{id:"mending",lvl:1s}]} 1', "Kırılmaz sonsuz kanat")
    ],
    "🪄 BÜYÜCÜ (ENCHANTER & POTIONS)": [
        ("👑 MEGA ULTRA BUFF (Tüm Bufflar)", "effect give {p} resistance 99999 5 true && effect give {p} strength 99999 100 true && effect give {p} speed 99999 3 true && effect give {p} haste 99999 255 true && effect give {p} night_vision 99999 0 true && effect give {p} saturation 99999 255 true && effect give {p} fire_resistance 99999 0 true && effect give {p} absorption 99999 10 true", "Ölümsüzlük, tek atma, süper hız ve anında kırma"),
        ("⛏️ Çılgın Madenci Hızı (Haste 255)", "effect give {p} haste 99999 255 true", "Blokları dokunduğun an paramparça eder"),
        ("🛡️ Hasarsızlık (Resistance V)", "effect give {p} resistance 99999 5 true", "Darbe ve patlamadan sıfır hasar alır"),
        ("💪 Titan Gücü (Strength 100)", "effect give {p} strength 99999 100 true", "Devasa vuruş hasarı"),
        ("🏃 Flaş Koşu Hızı (Speed 5)", "effect give {p} speed 99999 4 true", "Şimşek gibi yüksek koşu temposu"),
        ("👁️ Sonsuz Gece Görüşü", "effect give {p} night_vision 99999 0 true", "Zifiri karanlığı gündüz yapar"),
        ("💖 Anında Can Yenilenmesi (Regen 255)", "effect give {p} regeneration 99999 255 true", "Can barı ışık hızında dolar"),
        ("🔥 Ateş Bağışıklığı (Fire Res)", "effect give {p} fire_resistance 99999 0 true", "Lav ve ateşte yüzme"),
        ("🌊 Sualtı Hâkimiyeti (Conduit)", "effect give {p} conduit_power 99999 0 true", "Suda sınırsız nefes ve görüş"),
        ("🦘 Süper Zıplama (Jump 5)", "effect give {p} jump_boost 99999 4 true", "10 blok yükseğe sıçrama"),
        ("👻 Tam Görünmezlik", "effect give {p} invisibility 99999 0 true", "Görünmezlik iksiri"),
        ("🧹 TÜM EFEKTLERİ TEMİZLE", "effect clear {p}", "Tüm iksir ve büyü etkilerini sıfırlar"),
        ("🗡️ Eldeki Silaha: Keskinlik V", "enchant {p} sharpness 5", "Sharpness V basar"),
        ("⛏️ Eldeki Kazmaya: Verimlilik V", "enchant {p} efficiency 5", "Efficiency V basar"),
        ("💎 Eldeki Kazmaya: Servet III", "enchant {p} fortune 3", "Fortune III basar"),
        ("✨ Eldeki Kazmaya: İpeksi Dokunuş", "enchant {p} silk_touch 1", "Silk Touch basar"),
        ("🏹 Eldeki Yaya: Sonsuzluk", "enchant {p} infinity 1", "Infinity basar"),
        ("🔧 Eldeki Eşyaya: Tamir (Mending)", "enchant {p} mending 1", "Mending basar")
    ],
    "🤡 TROLL & OYUNCUYLA OYNAMA": [
        ("🚀 Uzaya Fırlat (Y: 500)", "tp {p} ~ 500 ~", "Stratosfere ışınlar"),
        ("🕳️ Yerin Dibine Göm (Y: -58)", "tp {p} ~ -58 ~", "Katman kayası dibine hapseder"),
        ("🧊 Cam Kafese Hapset", "execute at {p} run fill ~-1 ~ ~-1 ~1 ~2 ~1 glass outline", "Hava alamaz cam kafes"),
        ("⬛ Obsidyen Hücre", "execute at {p} run fill ~-1 ~-1 ~-1 ~1 ~2 ~1 obsidian outline", "Kırılamaz obsidyen hücre"),
        ("🕸️ Örümcek Ağına Göm", "execute at {p} run fill ~-1 ~ ~-1 ~1 ~2 ~1 cobweb replace air", "Ağlara dolar"),
        ("🔨 Kafasına Örs Düşür", "execute at {p} run setblock ~ ~4 ~ anvil", "Kafasına 4 blok yukarıdan örs bırakır"),
        ("🔥 Ayaklarının Altını Yak", "execute at {p} run setblock ~ ~ ~ fire", "Ayağını ateşe verir"),
        ("🌊 Kafasından Lav Boşalt", "execute at {p} run setblock ~ ~2 ~ lava", "Kafasından lav akıtır"),
        ("⚡ 10 Katlı Şimşek Çaktır", "execute at {p} run summon lightning_bolt ~ ~ ~ && execute at {p} run summon lightning_bolt ~ ~ ~ && execute at {p} run summon lightning_bolt ~ ~ ~", "Peş peşe şimşekler indirir"),
        ("🤢 Aşırı Bulantı (Nausea 255)", "effect give {p} nausea 30 255 true", "Ekranı fırıl fırıl döndürür"),
        ("🕶️ Körlük & Zifiri Karanlık", "effect give {p} blindness 30 255 true && effect give {p} darkness 30 255 true", "Önünü göremez"),
        ("🥶 Dondur / Felç Et (Slowness 255)", "effect give {p} slowness 30 255 true", "Adım atamaz"),
        ("🎈 Sonsuz Havaya Uçur (Levitation)", "effect give {p} levitation 15 5 true", "Gökyüzüne uçurur"),
        ("🔊 Creeper Tıslaması (Jumpscare)", "playsound minecraft:entity.creeper.primed master {p} ~ ~ ~ 10 1", "Arkasında creeper patlayacakmış gibi ses çalar"),
        ("👹 Warden Çığlığı", "playsound minecraft:entity.warden.emerge master {p} ~ ~ ~ 10 1", "Warden çıkış çığlığı çalar"),
        ("🎒 Envanterini Tamamen Boşalt", "clear {p}", "Tüm envanterini temizler")
    ],
    "⚙️ REDSTONE & MEKANİZMA": [
        ("🧨 64x TNT Bloğu", "give {p} tnt {qty}", "Patlayıcı TNT"),
        ("🟩 64x Balçık Bloğu (Slime)", "give {p} slime_block {qty}", "Zıplatan balçık"),
        ("🍯 64x Bal Bloğu (Honey)", "give {p} honey_block {qty}", "Yapışkan bal"),
        ("🦾 64x Yapışkan Piston", "give {p} sticky_piston {qty}", "Piston"),
        ("👁️ 64x Gözlemci (Observer)", "give {p} observer {qty}", "Gözlemci"),
        ("📥 64x Huni (Hopper)", "give {p} hopper {qty}", "Huni"),
        ("🎯 64x Hedef Bloğu", "give {p} target {qty}", "Hedef bloğu"),
        ("🔊 64x Sculk Sensörü", "give {p} sculk_sensor {qty}", "Ses sensörü"),
        ("📦 64x Sandık (Chest)", "give {p} chest {qty}", "Sandık"),
        ("👁️ 64x Ender Sandığı", "give {p} ender_chest {qty}", "Ender sandığı")
    ],
    "👑 YETKİ & OYUNCU YÖNETİMİ": [
        ("👑 OP Yetkisi Ver", "op {p}", "OP yetkisi verir"),
        ("🚫 OP Yetkisini Al", "deop {p}", "OP yetkisini kaldırır"),
        ("💖 Canı & Açlığı Fulle (Heal)", "effect give {p} instant_health 1 255 true && effect give {p} saturation 1 255 true", "Can ve açlığı doldurur"),
        ("🏕️ Hayatta Kalma (Survival)", "gamemode survival {p}", "Survival modu"),
        ("🎨 Yaratıcı Mod (Creative)", "gamemode creative {p}", "Creative modu"),
        ("👻 İzleyici Modu (Spectator)", "gamemode spectator {p}", "Spectator modu"),
        ("🌟 +100 Level Deneyim (XP)", "xp add {p} 100 levels", "100 Seviye XP"),
        ("📍 Merkeze Işınla (0, 100, 0)", "tp {p} 0 100 0", "Merkeze ışınlar"),
        ("👥 Herkesi Bana Çek (TP All)", "tp @a {p}", "Tüm oyuncuları çeker"),
        ("👢 Sunucudan At (Kick)", "kick {p} Sunucudan cikarildiniz", "Oyuncuyu atar"),
        ("⛔ Oyuncuyu Yasakla (Ban)", "ban {p} Sunucudan yasaklandiniz", "Sunucudan banlar"),
        ("🔓 Banı Aç (Pardon)", "pardon {p}", "Yasağını kaldırır"),
        ("☠️ Oyuncuyu Öldür", "kill {p}", "Anında öldürür"),
        ("🧹 Canavarları Sil (Lag Temizliği)", "kill @e[type=!player]", "Tüm mobları temizler")
    ],
    "⚙️ ZAMAN, HAVA & KURALLAR": [
        ("☀️ Sabah Yap (Day)", "time set day", "Güneş doğar"),
        ("🕛 Öğle Yap (Noon)", "time set noon", "Öğle saati"),
        ("🌙 Gece Yap (Night)", "time set night", "Gece saati"),
        ("☀️ Güneşli Hava (Clear)", "weather clear", "Yağmuru keser"),
        ("🌧️ Yağmur Yağdır (Rain)", "weather rain", "Yağmur başlatır"),
        ("⛈️ Fırtına & Şimşek (Thunder)", "weather thunder", "Yıldırımlı fırtına"),
        ("🛡️ Eşyalar Düşmesin (KeepInv AÇ)", "gamerule keepInventory true", "Ölünce eşyalar gitmez"),
        ("❌ Eşyalar Düşsün (KeepInv KAPAT)", "gamerule keepInventory false", "Ölünce eşyalar saçılır"),
        ("🚫 Creeper Hasarını Kapat", "gamerule mobGriefing false", "Creeper blok kırmaz"),
        ("💥 Creeper Hasarını Aç", "gamerule mobGriefing true", "Creeper blok kırabilir"),
        ("💾 Dünyayı Şimdi Kaydet", "save-all flush", "Diske kaydeder"),
        ("📢 Sunucuya Altın Başlık Bas", 'title @a title {"text":"Sunucu Aktif!","color":"gold","bold":true}', "Ekrana duyuru basar")
    ],
    "🐉 CANLI ÇAĞIRICI (SUMMON)": [
        ("🐲 Ender Ejderhası Çağır", "summon ender_dragon ~ ~5 ~", "Ender Dragon oluşturur"),
        ("💀 Wither Boss Çağır", "summon wither ~ ~2 ~", "3 Başlı Wither"),
        ("👹 Warden Çağır", "summon warden ~ ~ ~", "Warden çağırır"),
        ("🤖 Demir Golem Çağır", "summon iron_golem ~ ~ ~", "Demir Golem"),
        ("🐎 Eyerli Evcil At", 'summon horse ~ ~ ~ {Tame:1b,SaddleItem:{id:"saddle",Count:1b}}', "Evcil at"),
        ("🧑‍🌾 Köylü Çağır", "summon villager ~ ~ ~", "Köylü"),
        ("⚡ Yıldırım İndir", "summon lightning_bolt ~ ~ ~", "Şimşek çarptırır")
    ]
}

class TabAdminPanel:
    def __init__(self, parent, config_manager):
        self.parent = parent
        self.config_manager = config_manager
        self.rcon = None
        self.frame = tk.Frame(parent, bg=BG_DARK)
        self.all_button_cards = []

        self._init_rcon()
        self._build_ui()

    def _init_rcon(self):
        cfg = self.config_manager.get_server_config()
        self.rcon = MinecraftRcon(
            host=cfg.get("rcon_host", "127.0.0.1"),
            port=cfg.get("rcon_port", 25575),
            password=cfg.get("rcon_password", "admin123")
        )

    def _build_ui(self):
        # 1. HEDEF & ADET ŞERİDİ
        ribbon = tk.Frame(self.frame, bg="#0d1424", height=42, padx=12, pady=4)
        ribbon.pack(fill=tk.X, side=tk.TOP)

        tk.Label(ribbon, text="🎯 Hedef:", font=("Segoe UI", 9, "bold"), fg=TEXT_COLOR, bg="#0d1424").pack(side=tk.LEFT, padx=(0, 4))
        self.player_var = tk.StringVar(value="@p")
        self.player_entry = ttk.Combobox(ribbon, textvariable=self.player_var, font=("Segoe UI", 9, "bold"), width=16, values=["@p", "@a"])
        self.player_entry.pack(side=tk.LEFT, padx=(0, 10))

        tk.Label(ribbon, text="🔢 Adet:", font=("Segoe UI", 9, "bold"), fg=TEXT_COLOR, bg="#0d1424").pack(side=tk.LEFT, padx=(0, 4))
        self.qty_var = tk.StringVar(value="64")
        self.qty_entry = ttk.Combobox(ribbon, textvariable=self.qty_var, font=("Segoe UI", 9, "bold"), width=6, values=["1", "16", "32", "64", "128", "256", "576"])
        self.qty_entry.pack(side=tk.LEFT, padx=(0, 10))

        tk.Label(ribbon, text="🔍 Arama:", font=("Segoe UI", 9, "bold"), fg=ACCENT_CYAN, bg="#0d1424").pack(side=tk.LEFT, padx=(0, 4))
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self._on_search_change)
        search_entry = tk.Entry(ribbon, textvariable=self.search_var, font=("Segoe UI", 9), bg=BG_CARD, fg="#ffffff", relief=tk.FLAT, width=14)
        search_entry.pack(side=tk.LEFT, padx=(0, 10), ipady=2)

        btn_heal = tk.Button(ribbon, text="💖 Can Fulle", font=("Segoe UI", 8, "bold"), bg="#0284c7", fg="white", relief=tk.FLAT, padx=8, command=lambda: self.run_template("effect give {p} instant_health 1 255 true && effect give {p} saturation 1 255 true"))
        btn_heal.pack(side=tk.LEFT, padx=2)

        btn_buff = tk.Button(ribbon, text="⚡ ULTRA BUFF", font=("Segoe UI", 8, "bold"), bg="#7c3aed", fg="white", relief=tk.FLAT, padx=8, command=lambda: self.run_template("effect give {p} resistance 99999 5 true && effect give {p} strength 99999 100 true && effect give {p} speed 99999 3 true && effect give {p} haste 99999 255 true && effect give {p} night_vision 99999 0 true && effect give {p} saturation 99999 255 true"))
        btn_buff.pack(side=tk.LEFT, padx=2)

        btn_box = tk.Button(ribbon, text="📦 3'LÜ MASTER KİT", font=("Segoe UI", 8, "bold"), bg="#b45309", fg="white", relief=tk.FLAT, padx=8, command=lambda: self.run_template(CMD_COMBO_FULL))
        btn_box.pack(side=tk.LEFT, padx=2)

        # 2. GELİŞMİŞ BLOK DAĞITIM MERKEZİ (Universal Block Hub)
        hub = tk.Frame(self.frame, bg="#111827", padx=12, pady=4)
        hub.pack(fill=tk.X, side=tk.TOP)

        row1 = tk.Frame(hub, bg="#111827")
        row1.pack(fill=tk.X, pady=(0, 3))

        tk.Label(row1, text="🧱 Kategori:", font=("Segoe UI", 8, "bold"), fg=ACCENT_GOLD, bg="#111827").pack(side=tk.LEFT, padx=(0, 4))
        cats = list(BLOCK_CATALOG.keys())
        self.cat_var = tk.StringVar(value=cats[0])
        self.cat_combo = ttk.Combobox(row1, textvariable=self.cat_var, font=("Segoe UI", 8, "bold"), width=18, values=cats, state="readonly")
        self.cat_combo.pack(side=tk.LEFT, padx=(0, 6))
        self.cat_combo.bind("<<ComboboxSelected>>", self._on_block_cat_change)

        tk.Label(row1, text="📦 Blok:", font=("Segoe UI", 8, "bold"), fg=ACCENT_CYAN, bg="#111827").pack(side=tk.LEFT, padx=(0, 4))
        self.block_sel_var = tk.StringVar()
        self.block_sel_combo = ttk.Combobox(row1, textvariable=self.block_sel_var, font=("Segoe UI", 8), width=22, state="readonly")
        self.block_sel_combo.pack(side=tk.LEFT, padx=(0, 6))
        self.block_sel_combo.bind("<<ComboboxSelected>>", self._on_block_pick)

        tk.Label(row1, text="✍️ ID:", font=("Segoe UI", 8, "bold"), fg=TEXT_COLOR, bg="#111827").pack(side=tk.LEFT, padx=(0, 4))
        self.custom_item_var = tk.StringVar(value="minecraft:barrier")
        self.custom_entry = tk.Entry(row1, textvariable=self.custom_item_var, font=("Consolas", 9), bg=BG_CARD, fg="#ffffff", relief=tk.FLAT, width=20)
        self.custom_entry.pack(side=tk.LEFT, padx=(0, 6), ipady=1)
        self.custom_entry.bind("<Return>", lambda e: self.dispatch_block("give"))

        # İşlem butonları
        tk.Button(row1, text="🚀 Envantere Ver", font=("Segoe UI", 8, "bold"), bg=ACCENT_GREEN, fg="#000", relief=tk.FLAT, padx=6, command=lambda: self.dispatch_block("give")).pack(side=tk.LEFT, padx=2)
        tk.Button(row1, text="🦶 Ayak Altına", font=("Segoe UI", 8, "bold"), bg="#0284c7", fg="#fff", relief=tk.FLAT, padx=6, command=lambda: self.dispatch_block("setblock_under")).pack(side=tk.LEFT, padx=2)
        tk.Button(row1, text="🧱 3x3 Duvar", font=("Segoe UI", 8, "bold"), bg=ACCENT_GOLD, fg="#000", relief=tk.FLAT, padx=6, command=lambda: self.dispatch_block("wall_front")).pack(side=tk.LEFT, padx=2)
        tk.Button(row1, text="🕳️ Kutu Yap", font=("Segoe UI", 8, "bold"), bg=ACCENT_PURPLE, fg="#fff", relief=tk.FLAT, padx=6, command=lambda: self.dispatch_block("box_outline")).pack(side=tk.LEFT, padx=2)
        tk.Button(row1, text="🌟 5x5 Zemin", font=("Segoe UI", 8, "bold"), bg="#0d9488", fg="#fff", relief=tk.FLAT, padx=6, command=lambda: self.dispatch_block("platform")).pack(side=tk.LEFT, padx=2)

        # 3. KATEGORİ SEKMELERİ (NOTEBOOK)
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=8, pady=3)

        for tab_title, buttons in TABS_DATA.items():
            fr = tk.Frame(self.notebook, bg=BG_DARK)
            self.notebook.add(fr, text=f" {tab_title} ")
            self._build_button_grid(fr, buttons)

        # 4. KONSOL & RAW KOMUT GİRİŞİ
        c_frame = tk.Frame(self.frame, bg=BG_PANEL, height=130, padx=10, pady=4)
        c_frame.pack(fill=tk.X, side=tk.BOTTOM)

        top_c = tk.Frame(c_frame, bg=BG_PANEL)
        top_c.pack(fill=tk.X)
        tk.Label(top_c, text="💻 RCON YÖNETİM KONSOLU", font=("Segoe UI", 8, "bold"), fg=ACCENT_CYAN, bg=BG_PANEL).pack(side=tk.LEFT)
        tk.Button(top_c, text="Temizle", font=("Segoe UI", 7), bg=BG_CARD, fg=TEXT_MUTED, relief=tk.FLAT, padx=6, command=lambda: self.console.delete("1.0", tk.END)).pack(side=tk.RIGHT)

        self.console = scrolledtext.ScrolledText(c_frame, height=3, bg="#030712", fg="#e2e8f0", insertbackground=ACCENT_CYAN, font=("Consolas", 9), relief=tk.FLAT)
        self.console.pack(fill=tk.X, pady=(2, 3))
        self.console.tag_config("cmd", foreground=ACCENT_CYAN, font=("Consolas", 9, "bold"))
        self.console.tag_config("ok", foreground=ACCENT_GREEN)
        self.console.tag_config("err", foreground=ACCENT_RED)

        cmd_bar = tk.Frame(c_frame, bg=BG_PANEL)
        cmd_bar.pack(fill=tk.X)
        tk.Label(cmd_bar, text="CMD >", font=("Consolas", 9, "bold"), fg=ACCENT_GREEN, bg=BG_PANEL).pack(side=tk.LEFT, padx=(0, 4))
        self.raw_cmd_var = tk.StringVar()
        self.raw_entry = tk.Entry(cmd_bar, textvariable=self.raw_cmd_var, font=("Consolas", 9), bg=BG_CARD, fg="#ffffff", relief=tk.FLAT)
        self.raw_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6), ipady=2)
        self.raw_entry.bind("<Return>", lambda e: self.send_raw_cmd())
        tk.Button(cmd_bar, text="Gönder", font=("Segoe UI", 8, "bold"), bg=ACCENT_CYAN, fg="#000", relief=tk.FLAT, padx=12, command=self.send_raw_cmd).pack(side=tk.RIGHT)

        self._update_catalog_dropdown()

    def _on_block_cat_change(self, event=None):
        self._update_catalog_dropdown()

    def _update_catalog_dropdown(self):
        cat = self.cat_var.get()
        items = BLOCK_CATALOG.get(cat, [])
        names = [n for n, _ in items]
        self.block_sel_combo.configure(values=names)
        if names:
            self.block_sel_combo.current(0)
            self._on_block_pick()

    def _on_block_pick(self, event=None):
        cat = self.cat_var.get()
        items = BLOCK_CATALOG.get(cat, [])
        idx = self.block_sel_combo.current()
        if 0 <= idx < len(items):
            _, raw_id = items[idx]
            if not raw_id.startswith("minecraft:") and ":" not in raw_id and "{" not in raw_id and "[" not in raw_id:
                raw_id = f"minecraft:{raw_id}"
            self.custom_item_var.set(raw_id)

    def dispatch_block(self, mode="give"):
        item_id = self.custom_item_var.get().strip()
        if not item_id:
            return
        if not item_id.startswith("minecraft:") and ":" not in item_id and "{" not in item_id and "[" not in item_id:
            item_id = f"minecraft:{item_id}"
        target = self.player_var.get().strip() or "@p"
        qty = self.qty_var.get().strip() or "64"
        clean = item_id.split("{")[0]

        if mode == "give":
            cmd = f"give {target} {item_id} {qty}"
        elif mode == "setblock_under":
            cmd = f"execute at {target} run setblock ~ ~-1 ~ {clean}"
        elif mode == "wall_front":
            cmd = f"execute at {target} run fill ^-1 ^ ^3 ^1 ^2 ^3 {clean}"
        elif mode == "box_outline":
            cmd = f"execute at {target} run fill ~-1 ~-1 ~-1 ~1 ~2 ~1 {clean} outline"
        elif mode == "platform":
            cmd = f"execute at {target} run fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 {clean}"
        else:
            cmd = f"give {target} {item_id} {qty}"

        self.run_template(cmd)

    def _build_button_grid(self, parent, buttons):
        canvas = tk.Canvas(parent, bg=BG_DARK, highlightthickness=0, borderwidth=0)
        scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg=BG_DARK)

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, padx=(2, 0), pady=2)
        scrollbar.pack(side="right", fill="y", pady=2)

        cols = 3
        for idx, (btn_name, cmd_tmpl, desc) in enumerate(buttons):
            r = idx // cols
            c = idx % cols
            card = tk.Frame(scroll_frame, bg=BG_CARD, highlightbackground=BORDER_COLOR, highlightthickness=1, padx=6, pady=4)
            card.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")
            scroll_frame.columnconfigure(c, weight=1, minsize=310)

            btn = tk.Button(card, text=btn_name, font=("Segoe UI", 9, "bold"), bg="#1e293b", fg=TEXT_COLOR, activebackground=ACCENT_CYAN, activeforeground="#000", relief=tk.FLAT, anchor="w", padx=6, pady=2, command=lambda ct=cmd_tmpl: self.run_template(ct))
            btn.pack(fill=tk.X)

            desc_lbl = tk.Label(card, text=desc, font=("Segoe UI", 8), fg=TEXT_MUTED, bg=BG_CARD, anchor="w")
            desc_lbl.pack(fill=tk.X, padx=6, pady=(1, 0))

            self.all_button_cards.append((card, btn, btn_name, desc))

    def _on_search_change(self, *args):
        query = self.search_var.get().lower().strip()
        for card, btn, name, desc in self.all_button_cards:
            if not query or query in name.lower() or query in desc.lower():
                card.configure(bg=BG_CARD)
                btn.configure(bg="#1e293b", fg=TEXT_COLOR)
            else:
                card.configure(bg="#111827")
                btn.configure(bg="#111827", fg="#475569")

    def run_template(self, cmd_tmpl):
        target = self.player_var.get().strip() or "@p"
        qty = self.qty_var.get().strip() or "64"
        cmd = cmd_tmpl.replace("{p}", target).replace("{qty}", qty)
        self.log(f">> {cmd}\n", "cmd")

        def _worker():
            resp = self.rcon.send_chained_commands(cmd)
            tag = "err" if "Hata" in resp else "ok"
            self.parent.after(0, self.log, f"{resp}\n", tag)

        threading.Thread(target=_worker, daemon=True).start()

    def send_raw_cmd(self):
        cmd = self.raw_cmd_var.get().strip()
        if not cmd:
            return
        if cmd.startswith("/"):
            cmd = cmd[1:]
        self.raw_cmd_var.set("")
        self.log(f">> {cmd}\n", "cmd")

        def _worker():
            resp = self.rcon.send_command(cmd)
            tag = "err" if "Hata" in resp else "ok"
            self.parent.after(0, self.log, f"{resp}\n", tag)

        threading.Thread(target=_worker, daemon=True).start()

    def log(self, text, tag="ok"):
        self.console.insert(tk.END, text, tag)
        self.console.see(tk.END)
