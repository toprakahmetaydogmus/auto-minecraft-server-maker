"""
Tab: Master Admin Control Panel & Universal Block Spawner Hub
Efsanevi Master Ekipmanlar, Gelişmiş Blok Dağıtım Merkezi ve 380+ Yönetici Komutu.
Completely sanitized of any personal names, IPs, or hardcoded passwords.
"""

import os
import subprocess
import time
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
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

CMD_SHULKER_VILLA = 'minecraft:give {p} white_shulker_box{display:{Name:\'{"text":"📦 SİHİRLİ VİLLA İNŞA SANDIĞI","color":"aqua","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"smooth_quartz",Count:64b},{Slot:1b,id:"smooth_quartz",Count:64b},{Slot:2b,id:"tinted_glass",Count:64b},{Slot:3b,id:"sea_lantern",Count:64b},{Slot:4b,id:"oak_door",Count:8b},{Slot:5b,id:"red_bed",Count:4b},{Slot:6b,id:"chest",Count:16b},{Slot:7b,id:"water_bucket",Count:4b},{Slot:8b,id:"smooth_stone",Count:64b}]}} 1'
CMD_SHULKER_CABIN = 'minecraft:give {p} brown_shulker_box{display:{Name:\'{"text":"📦 SİHİRLİ DAĞ EVİ SANDIĞI","color":"gold","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"spruce_log",Count:64b},{Slot:1b,id:"spruce_planks",Count:64b},{Slot:2b,id:"spruce_stairs",Count:64b},{Slot:3b,id:"glass_pane",Count:64b},{Slot:4b,id:"campfire",Count:8b},{Slot:5b,id:"bricks",Count:64b},{Slot:6b,id:"lantern",Count:32b},{Slot:7b,id:"barrel",Count:16b},{Slot:8b,id:"spruce_door",Count:8b}]}} 1'
CMD_SHULKER_CASTLE = 'minecraft:give {p} gray_shulker_box{display:{Name:\'{"text":"📦 SİHİRLİ KALE & SAVUNMA SANDIĞI","color":"dark_gray","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"deepslate_bricks",Count:64b},{Slot:1b,id:"stone_brick_wall",Count:64b},{Slot:2b,id:"iron_bars",Count:64b},{Slot:3b,id:"dispenser",Count:32b},{Slot:4b,id:"arrow",Count:64b},{Slot:5b,id:"lever",Count:16b},{Slot:6b,id:"iron_door",Count:8b},{Slot:7b,id:"sea_lantern",Count:32b},{Slot:8b,id:"tnt",Count:64b}]}} 1'
CMD_SHULKER_FARM = 'minecraft:give {p} green_shulker_box{display:{Name:\'{"text":"📦 SİHİRLİ OTOMATİK ÇİFTLİK SANDIĞI","color":"green","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"farmland",Count:64b},{Slot:1b,id:"water_bucket",Count:4b},{Slot:2b,id:"wheat_seeds",Count:64b},{Slot:3b,id:"carrot",Count:64b},{Slot:4b,id:"potato",Count:64b},{Slot:5b,id:"hopper",Count:16b},{Slot:6b,id:"chest",Count:16b},{Slot:7b,id:"bone_meal",Count:64b},{Slot:8b,id:"oak_fence",Count:64b}]}} 1'
CMD_SHULKER_MINE = 'minecraft:give {p} blue_shulker_box{display:{Name:\'{"text":"📦 SİHİRLİ MADENCİ & ASANSÖR SANDIĞI","color":"blue","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"netherite_pickaxe",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"efficiency",lvl:5s},{id:"fortune",lvl:3s}]}},{Slot:1b,id:"ladder",Count:64b},{Slot:2b,id:"ladder",Count:64b},{Slot:3b,id:"torch",Count:64b},{Slot:4b,id:"water_bucket",Count:4b},{Slot:5b,id:"soul_sand",Count:16b},{Slot:6b,id:"powered_rail",Count:64b},{Slot:7b,id:"rail",Count:64b},{Slot:8b,id:"chest_minecart",Count:8b}]}} 1'
CMD_SHULKER_MARKET_KIT = 'minecraft:give {p} yellow_shulker_box{display:{Name:\'{"text":"📦 SİHİRLİ TÜCCAR & MARKET SANDIĞI","color":"gold","bold":true}\'},BlockEntityTag:{Items:[{Slot:0b,id:"gold_ingot",Count:64b},{Slot:1b,id:"gold_ingot",Count:64b},{Slot:2b,id:"emerald",Count:64b},{Slot:3b,id:"emerald",Count:64b},{Slot:4b,id:"diamond",Count:64b},{Slot:5b,id:"villager_spawn_egg",Count:16b},{Slot:6b,id:"yellow_wool",Count:64b},{Slot:7b,id:"red_wool",Count:64b},{Slot:8b,id:"barrel",Count:16b}]}} 1'


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
    # -------------------------------------------------------------------------
    # 1. OTO İNŞAAT & EV YAPICI
    # -------------------------------------------------------------------------
    "🏠 OTO İNŞAAT & EV YAPICI": [
        ("🏡 2 Katlı Lüks Cam & Havuzlu Villa",
         "execute at {p} run fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 smooth_quartz && execute at {p} run fill ~-5 ~ ~-5 ~5 ~5 ~5 air && execute at {p} run fill ~-5 ~ ~-5 ~5 ~4 ~5 tinted_glass outline && execute at {p} run fill ~-5 ~5 ~-5 ~5 ~5 ~5 smooth_quartz && execute at {p} run fill ~-4 ~ ~-4 ~4 ~4 ~4 air && execute at {p} run setblock ~ ~-1 ~ sea_lantern && execute at {p} run setblock ~-4 ~-1 ~-4 sea_lantern && execute at {p} run setblock ~4 ~-1 ~4 sea_lantern && execute at {p} run setblock ~-3 ~ ~-4 chest && execute at {p} run setblock ~-2 ~ ~-4 crafting_table && execute at {p} run setblock ~-1 ~ ~-4 furnace && execute at {p} run setblock ~-4 ~ ~3 red_bed && execute at {p} run fill ~-1 ~ ~-5 ~1 ~1 ~-5 air && execute at {p} run setblock ~ ~ ~-5 oak_door[half=lower,facing=north] && execute at {p} run setblock ~ ~1 ~-5 oak_door[half=upper,facing=north] && execute at {p} run fill ~-3 ~-2 ~-9 ~3 ~-1 ~-6 smooth_stone && execute at {p} run fill ~-2 ~-2 ~-8 ~2 ~-1 ~-7 water && playsound minecraft:block.anvil.use master {p} ~ ~ ~ 1 1",
         "Kuvars zeminli, cam duvarlı, çift kişilik yataklı, fırınlı ve önünde havuzlu tam modern villa"),

        ("🪵 Dağ Kütük Evi (Şömineli & Bacalı)",
         "execute at {p} run fill ~-4 ~-1 ~-4 ~4 ~-1 ~4 cobblestone && execute at {p} run fill ~-4 ~ ~-4 ~4 ~5 ~4 air && execute at {p} run fill ~-4 ~ ~-4 ~4 ~3 ~4 spruce_planks outline && execute at {p} run fill ~-3 ~ ~-3 ~3 ~3 ~3 air && execute at {p} run fill ~-4 ~ ~-4 ~-4 ~3 ~-4 spruce_log && execute at {p} run fill ~4 ~ ~-4 ~4 ~3 ~-4 spruce_log && execute at {p} run fill ~-4 ~ ~4 ~-4 ~3 ~4 spruce_log && execute at {p} run fill ~4 ~ ~4 ~4 ~3 ~4 spruce_log && execute at {p} run setblock ~3 ~ ~3 bricks && execute at {p} run setblock ~3 ~1 ~3 bricks && execute at {p} run setblock ~3 ~2 ~3 bricks && execute at {p} run setblock ~3 ~3 ~3 campfire && execute at {p} run setblock ~3 ~4 ~3 cobblestone_wall && execute at {p} run setblock ~-3 ~ ~3 blue_bed && execute at {p} run setblock ~-3 ~ ~2 chest && execute at {p} run setblock ~-3 ~ ~1 crafting_table && execute at {p} run setblock ~ ~3 ~ lantern[hanging=true] && execute at {p} run setblock ~ ~ ~-4 spruce_door[half=lower,facing=north] && execute at {p} run setblock ~ ~1 ~-4 spruce_door[half=upper,facing=north] && playsound minecraft:block.wood.place master {p} ~ ~ ~ 1 1",
         "Ladin ağacından sıcacık dağ kulübesi, bacasından duman tüten tuğla şömine, yatak ve mobilyalar"),

        ("🏰 Ortaçağ Savunma Şatosu & Kalesi",
         "execute at {p} run fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 deepslate_bricks && execute at {p} run fill ~-5 ~ ~-5 ~5 ~6 ~5 air && execute at {p} run fill ~-5 ~ ~-5 ~5 ~5 ~5 deepslate_bricks outline && execute at {p} run fill ~-4 ~ ~-4 ~4 ~5 ~4 air && execute at {p} run fill ~-5 ~6 ~-5 ~5 ~6 ~5 stone_brick_wall outline && execute at {p} run setblock ~-5 ~6 ~-5 sea_lantern && execute at {p} run setblock ~5 ~6 ~-5 sea_lantern && execute at {p} run setblock ~-5 ~6 ~5 sea_lantern && execute at {p} run setblock ~5 ~6 ~5 sea_lantern && execute at {p} run fill ~-1 ~ ~-5 ~1 ~2 ~-5 air && execute at {p} run setblock ~ ~ ~-5 iron_door[half=lower,facing=north] && execute at {p} run setblock ~ ~1 ~-5 iron_door[half=upper,facing=north] && execute at {p} run setblock ~1 ~ ~-6 stone_button[face=wall,facing=north] && playsound minecraft:block.anvil.place master {p} ~ ~ ~ 1 1",
         "Derin kayraktan aşılmaz kale, mazgallı gözetleme surları, fenerler ve zırhlı demir kapı"),

        ("🛡️ Yeraltı Nükleer / Güvenli Sığınak",
         "execute at {p} run fill ~-4 ~-1 ~-4 ~4 ~-1 ~4 obsidian && execute at {p} run fill ~-4 ~ ~-4 ~4 ~4 ~4 reinforced_deepslate outline && execute at {p} run fill ~-3 ~ ~-3 ~3 ~3 ~3 air && execute at {p} run fill ~-4 ~4 ~-4 ~4 ~4 ~4 obsidian && execute at {p} run setblock ~ ~3 ~ redstone_lamp && execute at {p} run setblock ~ ~4 ~ redstone_block && execute at {p} run setblock ~-3 ~ ~-3 chest && execute at {p} run setblock ~-2 ~ ~-3 chest && execute at {p} run setblock ~-3 ~ ~3 respawn_anchor[charges=4] && execute at {p} run setblock ~-2 ~ ~3 enchanting_table && execute at {p} run setblock ~-1 ~ ~3 anvil",
         "Patlamaz obsidyen ve güçlendirilmiş derin kayraktan nükleer sığınak, kızıltaş lambaları, örs"),

        ("🌾 Otomatik Kızıltaş Hasat Çiftliği",
         "execute at {p} run fill ~-4 ~-1 ~-4 ~4 ~-1 ~4 dirt && execute at {p} run fill ~-4 ~ ~-4 ~4 ~2 ~4 air && execute at {p} run fill ~-4 ~-1 ~-4 ~4 ~-1 ~4 farmland && execute at {p} run setblock ~ ~-1 ~ water && execute at {p} run setblock ~ ~ ~ lily_pad && execute at {p} run fill ~-4 ~ ~-4 ~4 ~ ~4 wheat[age=7] && execute at {p} run fill ~-5 ~ ~-5 ~5 ~ ~5 oak_fence outline && execute at {p} run setblock ~ ~ ~-5 oak_fence_gate && execute at {p} run setblock ~-4 ~1 ~-4 torch && execute at {p} run setblock ~4 ~1 ~-4 torch",
         "Su kanallı, çit korumalı, hazır olgunlaşmış buğdaylarla dolu otomatik çiftlik tarlası"),

        ("🏙️ Modern Gökdelen & Seyir Kulesi (15 Blok)",
         "execute at {p} run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 smooth_quartz && execute at {p} run fill ~-3 ~ ~-3 ~3 ~15 ~3 tinted_glass outline && execute at {p} run fill ~-2 ~ ~-2 ~2 ~14 ~2 air && execute at {p} run fill ~-3 ~15 ~-3 ~3 ~15 ~3 smooth_quartz && execute at {p} run fill ~-3 ~16 ~-3 ~3 ~16 ~3 glass_pane outline && execute at {p} run setblock ~ ~15 ~ beacon && execute at {p} run fill ~ ~-1 ~ ~ ~14 ~ ladder[facing=north] && execute at {p} run fill ~-1 ~ ~-3 ~1 ~1 ~-3 air",
         "15 blok yüksekliğinde panaromik cam gökdelen, iç merdiven şaftı, teras feneri"),

        ("🌋 Nether Geçidi Mabedi",
         "execute at {p} run fill ~-3 ~-1 ~-2 ~3 ~-1 ~2 gilded_blackstone && execute at {p} run fill ~-2 ~ ~ ~2 ~4 ~ obsidian outline && execute at {p} run fill ~-1 ~1 ~ ~1 ~3 ~ nether_portal && execute at {p} run setblock ~-3 ~ ~-2 crying_obsidian && execute at {p} run setblock ~3 ~ ~-2 crying_obsidian && execute at {p} run setblock ~-3 ~ ~2 crying_obsidian && execute at {p} run setblock ~3 ~ ~2 crying_obsidian && execute at {p} run setblock ~-3 ~1 ~-2 soul_lantern && execute at {p} run setblock ~3 ~1 ~-2 soul_lantern && execute at {p} run setblock ~-2 ~-1 ~ gold_block && execute at {p} run setblock ~2 ~-1 ~ gold_block",
         "Yaldızlı karataş, ağlayan obsidyen ve ruh fenerleriyle donatılmış dev aktif Nether kapısı"),

        ("⛏️ Dikey Maden Asansörü (Y: -58'e Kadar)",
         "execute at {p} run fill ~-1 ~-1 ~-1 ~1 -58 ~1 air && execute at {p} run fill ~-2 ~-1 ~-2 ~2 -58 ~2 smooth_stone outline && execute at {p} run fill ~ ~-1 ~ ~ -57 ~ ladder[facing=north] && execute at {p} run setblock ~ ~-58 ~ water && execute at {p} run setblock ~ ~-58 ~1 sea_lantern",
         "Y:-58 elmas katmanına kadar tek tıkla inen merdivenli, aydınlatmalı ve su minderli maden şaftı"),

        ("⚔️ Gladyatör PvP Arenası",
         "execute at {p} run fill ~-7 ~-1 ~-7 ~7 ~-1 ~7 smooth_sandstone && execute at {p} run fill ~-7 ~ ~-7 ~7 ~3 ~7 air && execute at {p} run fill ~-7 ~ ~-7 ~7 ~ ~7 red_sandstone_wall outline && execute at {p} run setblock ~ ~-1 ~ redstone_block && execute at {p} run setblock ~-7 ~1 ~-7 torch && execute at {p} run setblock ~7 ~1 ~-7 torch && execute at {p} run setblock ~-7 ~1 ~7 torch && execute at {p} run setblock ~7 ~1 ~7 torch",
         "15x15 kumtaşı zeminli, kırmızı duvarlı, dövüşe hazır gladyatör arenası"),

        ("🌱 20x20 Arsa Düzleştirici & Temizleyici",
         "execute at {p} run fill ~-10 ~-1 ~-10 ~10 ~-1 ~10 grass_block && execute at {p} run fill ~-10 ~ ~-10 ~10 ~10 ~10 air && playsound minecraft:block.grass.break master {p} ~ ~ ~ 1 1",
         "Etraftaki tüm engelleri, dağları ve ağaçları silip 20x20 tertemiz yemyeşil inşaat alanı açar"),

        ("🛏️ Acil Durum Gece Barınağı (3x3)",
         "execute at {p} run fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 smooth_stone && execute at {p} run fill ~-1 ~ ~-1 ~1 ~2 ~1 cobblestone outline && execute at {p} run fill ~ ~ ~ ~ ~1 ~ air && execute at {p} run setblock ~ ~ ~ red_bed && execute at {p} run setblock ~ ~1 ~ torch && execute at {p} run setblock ~ ~ ~-1 oak_door[half=lower,facing=north] && execute at {p} run setblock ~ ~1 ~-1 oak_door[half=upper,facing=north]",
         "Gece canavarlarından saniyede korunmak için yataklı ve kapılı anında barınak"),

        ("🏊 7x7 Işıklı Lüks Havuz",
         "execute at {p} run fill ~-3 ~-3 ~-3 ~3 ~-1 ~3 smooth_quartz && execute at {p} run fill ~-2 ~-2 ~-2 ~2 ~-1 ~2 water && execute at {p} run setblock ~ ~-3 ~ sea_lantern",
         "Kuvars çerçeveli, dibinde deniz feneri parlayan berrak serinleme havuzu"),

        ("🏯 Japon Pagoda Tapınağı (Kiraz & Kavisli Çatı)",
         "execute at {p} run fill ~-4 ~-1 ~-4 ~4 ~-1 ~4 dark_oak_planks && execute at {p} run fill ~-4 ~ ~-4 ~4 ~6 ~4 air && execute at {p} run fill ~-3 ~ ~-3 ~3 ~4 ~3 stripped_cherry_wood outline && execute at {p} run fill ~-2 ~ ~-2 ~2 ~3 ~2 air && execute at {p} run fill ~-4 ~3 ~-4 ~4 ~3 ~4 cherry_planks && execute at {p} run fill ~-3 ~4 ~-3 ~3 ~4 ~3 cherry_slab && execute at {p} run setblock ~-4 ~3 ~-4 lantern && execute at {p} run setblock ~4 ~3 ~-4 lantern && execute at {p} run setblock ~-4 ~3 ~4 lantern && execute at {p} run setblock ~4 ~3 ~4 lantern && execute at {p} run setblock ~ ~ ~-3 cherry_door[half=lower,facing=north] && execute at {p} run setblock ~ ~1 ~-3 cherry_door[half=upper,facing=north]",
         "Geleneksel Japon kiraz ağacı mimarisi, kavisli saçaklar, asılı fenerler ve meditasyon odası"),

        ("🏜️ Antik Mısır Piramidi & Gizli Hazine Odası",
         "execute at {p} run fill ~-6 ~-1 ~-6 ~6 ~-1 ~6 sandstone && execute at {p} run fill ~-6 ~ ~-6 ~6 ~6 ~6 sandstone && execute at {p} run fill ~-5 ~1 ~-5 ~5 ~6 ~5 sandstone && execute at {p} run fill ~-4 ~2 ~-4 ~4 ~6 ~4 sandstone && execute at {p} run fill ~-3 ~3 ~-3 ~3 ~6 ~3 sandstone && execute at {p} run fill ~-2 ~4 ~-2 ~2 ~6 ~2 sandstone && execute at {p} run fill ~-1 ~5 ~-1 ~1 ~6 ~1 sandstone && execute at {p} run setblock ~ ~6 ~ gold_block && execute at {p} run fill ~-2 ~ ~-2 ~2 ~2 ~2 air && execute at {p} run setblock ~ ~ ~ chest && execute at {p} run setblock ~ ~-1 ~ gold_block && execute at {p} run fill ~ ~ ~-6 ~ ~1 ~-3 air",
         "Zirvesinde altın blok parlayan basamaklı kumtaşı piramit ve içinde gizli sandık mezar odası"),

        ("🌵 Otomatik Kaktüs & Kemik Unu Farmı",
         "execute at {p} run fill ~-4 ~-1 ~-4 ~4 ~-1 ~4 smooth_stone && execute at {p} run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 sand && execute at {p} run fill ~-4 ~ ~-4 ~4 ~3 ~4 glass outline && execute at {p} run fill ~-3 ~ ~-3 ~3 ~3 ~3 air && execute at {p} run setblock ~-2 ~ ~-2 cactus && execute at {p} run setblock ~2 ~ ~-2 cactus && execute at {p} run setblock ~-2 ~ ~2 cactus && execute at {p} run setblock ~2 ~ ~2 cactus && execute at {p} run setblock ~-2 ~1 ~-1 iron_bars && execute at {p} run setblock ~2 ~1 ~-1 iron_bars && execute at {p} run setblock ~-2 ~1 ~1 iron_bars && execute at {p} run setblock ~2 ~1 ~1 iron_bars && execute at {p} run setblock ~ ~-1 ~ hopper && execute at {p} run setblock ~ ~-2 ~ chest",
         "Cam korumalı, otomatik kırıcı demir çubuklu, hunili ve sandıklı sonsuz kaktüs hasat mekanizması"),

        ("🛸 Fütüristik Bilimkurgu Cyber Üssü",
         "execute at {p} run fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 smooth_quartz && execute at {p} run fill ~-5 ~ ~-5 ~5 ~4 ~5 light_blue_stained_glass outline && execute at {p} run fill ~-4 ~ ~-4 ~4 ~3 ~4 air && execute at {p} run fill ~-5 ~4 ~-5 ~5 ~4 ~5 smooth_quartz && execute at {p} run setblock ~ ~-1 ~ beacon && execute at {p} run setblock ~-4 ~-1 ~-4 sea_lantern && execute at {p} run setblock ~4 ~-1 ~-4 sea_lantern && execute at {p} run setblock ~-4 ~-1 ~4 sea_lantern && execute at {p} run setblock ~4 ~-1 ~4 sea_lantern && execute at {p} run fill ~-1 ~ ~-5 ~1 ~1 ~-5 air && execute at {p} run setblock ~ ~ ~ ender_chest",
         "Kuvars ve mavi lazer camdan ileri teknoloji sığınak, ortada fener ışını, Ender Sandığı"),

        ("☁️ Gökyüzü Skyblock Adası (Y: 150)",
         "execute at {p} run fill ~-4 148 ~-4 ~4 148 ~4 stone && execute at {p} run fill ~-3 147 ~-3 ~3 147 ~3 dirt && execute at {p} run fill ~-4 149 ~-4 ~4 149 ~4 grass_block && execute at {p} run setblock ~ 150 ~ oak_sapling && execute at {p} run setblock ~-2 150 ~-2 chest && execute at {p} run setblock ~2 150 ~2 water && tp {p} ~ 151 ~",
         "Y:150 irtifada süzülen çimenli Skyblock adası, fidan, sandık ve aşağı dökülen şelale")
    ],

    # -------------------------------------------------------------------------
    # 2. SİHİRLİ İNŞA SANDIKLARI
    # -------------------------------------------------------------------------
    "📦 SİHİRLİ İNŞA SANDIKLARI": [
        ("📦 Sihirli Villa Sandığı", CMD_SHULKER_VILLA, "Kuvars, Karartılmış Cam, Deniz Feneri, Meşe Kapılar, Su Kovası, Yatak, Sandık"),
        ("📦 Sihirli Dağ Evi Sandığı", CMD_SHULKER_CABIN, "Ladin Kütükleri, Tahtalar, Merdivenler, Şömine Tuğlaları, Kamp Ateşi, Fenerler"),
        ("📦 Sihirli Kale & Savunma Sandığı", CMD_SHULKER_CASTLE, "Derin Kayrak Tuğlası, Duvarlar, Demir Parmaklıklar, Fırlatıcılar, Oklar, TNT"),
        ("📦 Sihirli Otomatik Çiftlik Sandığı", CMD_SHULKER_FARM, "Tarla Bloğu, Su Kovaları, Tohumlar, Havuç, Patates, Huniler, Sandıklar, Kemik Tozu"),
        ("📦 Sihirli Madenci & Asansör Sandığı", CMD_SHULKER_MINE, "God Kazma, 128x Merdiven, 64x Meşale, Ruh Kumu, Güçlendirilmiş Raylar, Vagonlar"),
        ("📦 Sihirli Kızıltaş Fabrika Sandığı", CMD_SHULKER_REDSTONE, "TNT, Balçık, Bal Blokları, Yapışkan Pistonlar, Gözlemciler, Kızıltaş Blokları, Hedef"),
        ("📦 Full Admin & İllegal Blok Sandığı", CMD_SHULKER_ADMIN, "Bariyer, Komut Blokları, Görünmez Işık 15, Bedrock, Spawner, Sculk Shrieker"),
        ("📦 Sihirli Tüccar & Pazar Sandığı", CMD_SHULKER_MARKET_KIT, "Altın Külçeler, Zümrütler, Elmaslar, Köylü Yumurtaları, Renkli Yünler, Variller")
    ],

    # -------------------------------------------------------------------------
    # 3. AKÇE & EKONOMİ SİSTEMİ
    # -------------------------------------------------------------------------
    "💰 AKÇE & EKONOMİ SİSTEMİ": [
        ("🪙 Akçe Sistemini Kur & Başlat",
         "scoreboard objectives add akce dummy {\"text\":\"✦ AKÇE ✦\",\"color\":\"gold\",\"bold\":true} && scoreboard objectives setdisplay sidebar akce && scoreboard players add {p} akce 1000 && title {p} title {\"text\":\"🪙 AKÇE SİSTEMİ DEVREDE!\",\"color\":\"gold\",\"bold\":true} && title {p} subtitle {\"text\":\"1.000 Akçe Başlangıç Bakiyesi Yüklendi\",\"color\":\"yellow\"} && playsound minecraft:entity.player.levelup master {p}",
         "Scoreboard hedefini ekler, sağ tarafa şık altın paneli koyar ve oyuncuya 1000 akçe hediye eder"),

        ("👁️ Akçeyi Yan Ekranda Göster (Sidebar)", "scoreboard objectives setdisplay sidebar akce", "Ekranın sağındaki skor tablosunda gösterir"),
        ("📋 Akçeyi Oyuncu Listesinde Göster (Tab)", "scoreboard objectives setdisplay list akce", "Tab tuşuna basınca oyuncunun yanında gösterir"),
        ("👤 Akçeyi Oyuncu İsminin Altında Göster", "scoreboard objectives setdisplay belowName akce", "Oyuncunun kafasının üzerinde gösterir"),
        ("🙈 Akçe Tablosunu Gizle", "scoreboard objectives setdisplay sidebar", "Sağdaki skor tablosunu ekrandan kaldırır"),

        ("💰 +100 Akçe Yükle", "scoreboard players add {p} akce 100 && playsound minecraft:entity.experience_orb.pickup master {p}", "100 Akçe nakit ekler"),
        ("💰 +500 Akçe Yükle", "scoreboard players add {p} akce 500 && playsound minecraft:entity.experience_orb.pickup master {p}", "500 Akçe nakit ekler"),
        ("💰 +1.000 Akçe Yükle", "scoreboard players add {p} akce 1000 && playsound minecraft:entity.player.levelup master {p}", "1.000 Akçe yükler"),
        ("💰 +10.000 Akçe Yükle", "scoreboard players add {p} akce 10000 && playsound minecraft:entity.player.levelup master {p}", "10.000 Akçe yükler"),
        ("💰 +100.000 Akçe Milyarder Yüklemesi", "scoreboard players add {p} akce 100000 && title {p} title {\"text\":\"💎 MİLYARDER OLDUNUZ!\",\"color\":\"aqua\",\"bold\":true}", "100.000 Akçe zenginlik transferi"),
        ("💰 +1.000.000 İmparatorluk Hazinesi", "scoreboard players add {p} akce 1000000 && title {p} title {\"text\":\"👑 İMPARATORLUK HAZİNESİ!\",\"color\":\"gold\",\"bold\":true}", "1 Milyon Akçe hazine transferi"),

        ("💸 -500 Akçe Kes (Vergi/Harcama)", "scoreboard players remove {p} akce 500", "500 Akçe düşer"),
        ("💸 -5.000 Akçe Ceza Kes", "scoreboard players remove {p} akce 5000", "5.000 Akçe ceza keser"),
        ("🔄 Akçeyi Sıfırla (0 Yap)", "scoreboard players set {p} akce 0", "Hesaptaki tüm akçeyi silip sıfırlar"),
        ("📜 Bakiye Sorgula (Tellraw)", "tellraw {p} [{\"text\":\"[BANKA]: \",\"color\":\"gold\",\"bold\":true},{\"text\":\"Mevcut Akçe Bakiyeniz: \",\"color\":\"yellow\"},{\"score\":{\"name\":\"{p}\",\"objective\":\"akce\"},\"color\":\"green\",\"bold\":true},{\"text\":\" 🪙\",\"color\":\"gold\"}]", "Oyuncunun sohbetine tam bakiye raporu gönderir"),

        ("🪙 64x Fiziksel Bakır Akçe Ver", 'minecraft:give {p} iron_nugget{display:{Name:\'{"text":"🪙 1x Bakır Akçe","color":"yellow","bold":true}\',Lore:[\'{"text":"Temel harcama akçesi","color":"gray"}\']}} {qty}', "El ile tutulup takas yapılabilen bakır para"),
        ("💰 64x Fiziksel Gümüş Akçe Ver", 'minecraft:give {p} gold_nugget{display:{Name:\'{"text":"💰 10x Gümüş Akçe","color":"gold","bold":true}\',Lore:[\'{"text":"Tüccar gümüş akçesi","color":"gray"}\']}} {qty}', "10 Akçe değerinde gümüş sikke"),
        ("👑 64x Fiziksel Altın Akçe Ver", 'minecraft:give {p} gold_ingot{display:{Name:\'{"text":"👑 100x Altın Akçe","color":"yellow","bold":true}\',Lore:[\'{"text":"Değerli altın külçe akçe","color":"gray"}\']}} {qty}', "100 Akçe değerinde saf altın külçe"),
        ("💎 64x Zümrüt Kraliyet Akçesi", 'minecraft:give {p} emerald{display:{Name:\'{"text":"💎 1.000x Zümrüt Kraliyet Akçesi","color":"green","bold":true}\',Lore:[\'{"text":"Kraliyet zümrüt serveti","color":"gray"}\']}} {qty}', "1.000 Akçe değerinde zümrüt mücevher"),
        ("🌌 64x Elmas Milyarder Akçesi", 'minecraft:give {p} diamond{display:{Name:\'{"text":"🌌 10.000x Elmas Milyarder Akçesi","color":"aqua","bold":true}\',Lore:[\'{"text":"Milyarder elmas akçesi","color":"gray"}\']}} {qty}', "100.000 Akçe değerinde elmas birim"),
        ("🧱 64x Netherite İmparatorluk Külçesi", 'minecraft:give {p} netherite_ingot{display:{Name:\'{"text":"🧱 100.000x Netherite İmparatorluk Külçesi","color":"dark_purple","bold":true}\',Lore:[\'{"text":"Devasa imparatorluk serveti","color":"gray"}\']}} {qty}', "100.000 Akçe değerinde efsanevi külçe")
    ],

    # -------------------------------------------------------------------------
    # 4. MARKET & ÖZEL NPC TÜCCARLAR
    # -------------------------------------------------------------------------
    "🏪 MARKET & ÖZEL TÜCCARLAR": [
        ("🏛️ Büyük Ticaret Çarşısı İnşa Et",
         "execute at {p} run fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 polished_deepslate && execute at {p} run fill ~-5 ~ ~-5 ~5 ~4 ~5 air && execute at {p} run fill ~-5 ~3 ~-5 ~5 ~3 ~5 yellow_wool && execute at {p} run fill ~-4 ~3 ~-4 ~4 ~3 ~4 red_wool && execute at {p} run fill ~-5 ~ ~-5 ~-5 ~2 ~-5 spruce_fence && execute at {p} run fill ~5 ~ ~-5 ~5 ~2 ~-5 spruce_fence && execute at {p} run fill ~-5 ~ ~5 ~-5 ~2 ~5 spruce_fence && execute at {p} run fill ~5 ~ ~5 ~5 ~2 ~5 spruce_fence && execute at {p} run fill ~-3 ~ ~-3 ~3 ~ ~-3 barrel && execute at {p} run setblock ~-2 ~1 ~-3 lantern && execute at {p} run setblock ~2 ~1 ~-3 lantern && playsound minecraft:block.anvil.use master {p} ~ ~ ~ 1 1",
         "11x11 kapalı tente çatılı, varil tezgahlı ve fenerli devasa pazar yeri çarşısı inşa eder"),

        ("⚔️ Silah & Zırh Ustası Çağır",
         'execute at {p} run summon villager ~ ~ ~ {VillagerData:{profession:"weaponsmith",level:5,type:"plains"},NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,CustomName:\'{"text":"⚔️ Silah & Zırh Ustası","color":"gold","bold":true}\',CustomNameVisible:1b,Offers:{Recipes:[{buy:{id:"gold_ingot",Count:10b},sell:{id:"netherite_sword",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"sharpness",lvl:5s},{id:"fire_aspect",lvl:2s}]}},maxUses:9999999},{buy:{id:"gold_ingot",Count:15b},sell:{id:"netherite_pickaxe",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"efficiency",lvl:5s},{id:"fortune",lvl:3s}]}},maxUses:9999999},{buy:{id:"gold_ingot",Count:20b},sell:{id:"netherite_chestplate",Count:1b,tag:{Unbreakable:1b,Enchantments:[{id:"protection",lvl:4s},{id:"unbreaking",lvl:3s}]}},maxUses:9999999},{buy:{id:"gold_ingot",Count:5b},sell:{id:"totem_of_undying",Count:2b},maxUses:9999999}]}}',
         "Altın Akçe ile Netherite silah, zırh ve ölümsüzlük totemi satan ölümsüz sabit tüccar"),

        ("🏗️ Mimar & Lüks Blokçu Çağır",
         'execute at {p} run summon villager ~ ~ ~ {VillagerData:{profession:"mason",level:5,type:"plains"},NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,CustomName:\'{"text":"🏗️ Mimar & Lüks Blokçu","color":"aqua","bold":true}\',CustomNameVisible:1b,Offers:{Recipes:[{buy:{id:"gold_ingot",Count:1b},sell:{id:"smooth_quartz",Count:64b},maxUses:9999999},{buy:{id:"gold_ingot",Count:1b},sell:{id:"deepslate_bricks",Count:64b},maxUses:9999999},{buy:{id:"gold_ingot",Count:2b},sell:{id:"sea_lantern",Count:64b},maxUses:9999999},{buy:{id:"gold_ingot",Count:2b},sell:{id:"tinted_glass",Count:64b},maxUses:9999999},{buy:{id:"gold_ingot",Count:3b},sell:{id:"ochre_froglight",Count:64b},maxUses:9999999}]}}',
         "Kuvars, derin kayrak, fener ve özel mimari blokları istif halinde satan tüccar"),

        ("🪄 Baş Büyücü & Simyacı Çağır",
         'execute at {p} run summon villager ~ ~ ~ {VillagerData:{profession:"cleric",level:5,type:"plains"},NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,CustomName:\'{"text":"🪄 Baş Büyücü & Simyacı","color":"light_purple","bold":true}\',CustomNameVisible:1b,Offers:{Recipes:[{buy:{id:"gold_ingot",Count:5b},sell:{id:"enchanted_book",Count:1b,tag:{StoredEnchantments:[{id:"mending",lvl:1s}]}},maxUses:9999999},{buy:{id:"gold_ingot",Count:5b},sell:{id:"enchanted_book",Count:1b,tag:{StoredEnchantments:[{id:"sharpness",lvl:5s}]}},maxUses:9999999},{buy:{id:"gold_ingot",Count:5b},sell:{id:"enchanted_book",Count:1b,tag:{StoredEnchantments:[{id:"fortune",lvl:3s}]}},maxUses:9999999},{buy:{id:"gold_ingot",Count:4b},sell:{id:"enchanted_book",Count:1b,tag:{StoredEnchantments:[{id:"silk_touch",lvl:1s}]}},maxUses:9999999}]}}',
         "Tamir (Mending), Keskinlik V, Servet III ve İpeksi Dokunuş kitapları satan bilge büyücü"),

        ("🌾 Çiftçi & Gurme Aşçı Çağır",
         'execute at {p} run summon villager ~ ~ ~ {VillagerData:{profession:"farmer",level:5,type:"plains"},NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,CustomName:\'{"text":"🌾 Çiftçi & Gurme Aşçı","color":"green","bold":true}\',CustomNameVisible:1b,Offers:{Recipes:[{buy:{id:"gold_ingot",Count:1b},sell:{id:"golden_carrot",Count:64b},maxUses:9999999},{buy:{id:"gold_ingot",Count:3b},sell:{id:"enchanted_golden_apple",Count:8b},maxUses:9999999},{buy:{id:"gold_ingot",Count:1b},sell:{id:"cooked_beef",Count:64b},maxUses:9999999}]}}',
         "Altın havuç, Notch elması ve pişmiş et satan usta çiftçi"),

        ("⚙️ Kızıltaş Mühendisi Çağır",
         'execute at {p} run summon villager ~ ~ ~ {VillagerData:{profession:"armorer",level:5,type:"plains"},NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,CustomName:\'{"text":"⚙️ Kızıltaş Mühendisi","color":"red","bold":true}\',CustomNameVisible:1b,Offers:{Recipes:[{buy:{id:"gold_ingot",Count:2b},sell:{id:"tnt",Count:64b},maxUses:9999999},{buy:{id:"gold_ingot",Count:1b},sell:{id:"slime_block",Count:32b},maxUses:9999999},{buy:{id:"gold_ingot",Count:1b},sell:{id:"sticky_piston",Count:32b},maxUses:9999999},{buy:{id:"gold_ingot",Count:1b},sell:{id:"observer",Count:32b},maxUses:9999999}]}}',
         "TNT, balçık, yapışkan piston ve gözlemci satan sanayi mühendisi"),

        ("🕵️‍♂️ Gizli Karaborsacı Çağır",
         'execute at {p} run summon villager ~ ~ ~ {VillagerData:{profession:"nitwit",level:5,type:"swamp"},NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,CustomName:\'{"text":"🕵️‍♂️ Gizli Karaborsacı","color":"dark_red","bold":true}\',CustomNameVisible:1b,Offers:{Recipes:[{buy:{id:"gold_ingot",Count:10b},sell:{id:"barrier",Count:16b},maxUses:9999999},{buy:{id:"gold_ingot",Count:20b},sell:{id:"spawner",Count:1b},maxUses:9999999},{buy:{id:"gold_ingot",Count:15b},sell:{id:"light",Count:64b,tag:{BlockStateTag:{level:"15"}}},maxUses:9999999},{buy:{id:"gold_ingot",Count:25b},sell:{id:"elytra",Count:1b,tag:{Unbreakable:1b}},maxUses:9999999}]}}',
         "Bariyer, Spawner, Işık Bloğu ve Kırılmaz Elytra satan kaçakçı"),

        ("🧹 Çevredeki Tüccarları Temizle", "minecraft:kill @e[type=villager,distance=..15]", "15 blok içindeki çağrılan tüccarları temizler")
    ],

    # -------------------------------------------------------------------------
    # 5. EFSANEVİ SETLER & 32K SİLAHLAR
    # -------------------------------------------------------------------------
    "⚡ EFSANEVİ SETLER & 32K SİLAHLAR": [
        ("📦 FULL EFSANEVİ MASTER KİTİ (3 Sandık)", CMD_COMBO_FULL, "Zırh Sandığı + Silah Sandığı + İkmal Sandığı (Tek Tıkla Envantere)"),
        ("🛡️ Efsanevi Zırh Sandığı (Lvl 255)", CMD_BOX_ARMOR, "Netherite Kask, Göğüslük, Pantolon, Çizme, Elytra, Kalkan"),
        ("⚡ Efsanevi Silah & Alet Sandığı", CMD_BOX_WEAPONS, "Kılıç, Kazmalar, Balta, Kürek, Çapa, Yay, Arbalet, Mızrak"),
        ("💎 Efsanevi İkmal & Totem Sandığı", CMD_BOX_SUPPLIES, "128x Totem, 128x Notch Elma, Fişek, Kristal, Elmas Bloklar"),

        ("🗡️ Kıyamet Kılıcı (Tek Atan)",
         'minecraft:give {p} netherite_sword{Unbreakable:1b,Enchantments:[{id:"sharpness",lvl:255s},{id:"looting",lvl:255s},{id:"fire_aspect",lvl:255s},{id:"sweeping",lvl:255s},{id:"knockback",lvl:10s}]} 1',
         "Milyon hasar vuran, vurduğunu yakan ve yağmalayan efsanevi kılıç"),

        ("⛏️ Deprem Kazması (Lvl 255 Servet)",
         'minecraft:give {p} netherite_pickaxe{Unbreakable:1b,Enchantments:[{id:"efficiency",lvl:255s},{id:"fortune",lvl:255s}]} 1',
         "Blokları anında eritir ve 1 elmastan yüzlerce elmas düşürür"),

        ("💎 İpeksi Efsane Kazma",
         'minecraft:give {p} netherite_pickaxe{Unbreakable:1b,Enchantments:[{id:"efficiency",lvl:255s},{id:"silk_touch",lvl:1s}]} 1',
         "Blokları olduğu gibi kıran kırılmaz süper kazma"),

        ("🪓 Orman Baltası (Giga Hız)",
         'minecraft:give {p} netherite_axe{Unbreakable:1b,Enchantments:[{id:"efficiency",lvl:255s},{id:"sharpness",lvl:255s},{id:"fortune",lvl:255s}]} 1',
         "Ağaçları tek vuruşta devirir ve dev hasar verir"),

        ("🥄 Sismik Kürek",
         'minecraft:give {p} netherite_shovel{Unbreakable:1b,Enchantments:[{id:"efficiency",lvl:255s},{id:"fortune",lvl:255s}]} 1',
         "Toprak ve kumu 0.001 saniyede silip süpürür"),

        ("🏹 Nükleer Sonsuzluk Yayı",
         'minecraft:give {p} bow{Unbreakable:1b,Enchantments:[{id:"power",lvl:255s},{id:"flame",lvl:255s},{id:"punch",lvl:50s},{id:"infinity",lvl:1s}]} 1',
         "1 okla sonsuz nükleer alevli ok atar, hedefleri haritadan siler"),

        ("🎯 Makineli Hızlı Arbalet",
         'minecraft:give {p} crossbow{Unbreakable:1b,Enchantments:[{id:"quick_charge",lvl:5s},{id:"multishot",lvl:1s},{id:"piercing",lvl:255s}]} 1',
         "Anında gerilir, 3 lü delen mermi gibi ok saçar"),

        ("🔱 Zeus Fırtına Mızrağı",
         'minecraft:give {p} trident{Unbreakable:1b,Enchantments:[{id:"impaling",lvl:255s},{id:"loyalty",lvl:3s},{id:"channeling",lvl:1s}]} 1',
         "Geri dönen yıldırımlı efsanevi mızrak"),

        ("👑 Efsanevi Miğfer (Lvl 255)", 'minecraft:give {p} netherite_helmet{Unbreakable:1b,Enchantments:[{id:"protection",lvl:255s},{id:"unbreaking",lvl:255s},{id:"respiration",lvl:255s},{id:"thorns",lvl:255s}]} 1', "Ölümsüz kask"),
        ("🛡️ Efsanevi Göğüslük (Lvl 255)", 'minecraft:give {p} netherite_chestplate{Unbreakable:1b,Enchantments:[{id:"protection",lvl:255s},{id:"unbreaking",lvl:255s},{id:"blast_protection",lvl:255s},{id:"thorns",lvl:255s}]} 1', "Patlama geçirmez göğüslük"),
        ("🛡️ Efsanevi Pantolon (Lvl 255)", 'minecraft:give {p} netherite_leggings{Unbreakable:1b,Enchantments:[{id:"protection",lvl:255s},{id:"unbreaking",lvl:255s},{id:"fire_protection",lvl:255s},{id:"thorns",lvl:255s}]} 1', "Yanmaz pantolon"),
        ("👟 Efsanevi Çizmeler (Lvl 255)", 'minecraft:give {p} netherite_boots{Unbreakable:1b,Enchantments:[{id:"protection",lvl:255s},{id:"unbreaking",lvl:255s},{id:"feather_falling",lvl:255s},{id:"thorns",lvl:255s}]} 1', "Düşüş hasarı sıfır bot"),
        ("🪽 Sonsuz Master Elytra", 'minecraft:give {p} elytra{Unbreakable:1b,Enchantments:[{id:"unbreaking",lvl:255s},{id:"mending",lvl:1s}]} 1', "Asla yıpranmayan sonsuz kanat"),
        ("🛡️ Aşılmaz Master Kalkan", 'minecraft:give {p} shield{Unbreakable:1b,Enchantments:[{id:"unbreaking",lvl:255s},{id:"thorns",lvl:255s}]} 1', "Vuranı geri püskürten kalkan")
    ],

    # -------------------------------------------------------------------------
    # 6. BÜYÜ & EFEKT LABORATUVARI
    # -------------------------------------------------------------------------
    "🪄 BÜYÜ & EFEKT LABORATUVARI": [
        ("👑 MEGA ULTRA BUFF (Tüm Bufflar)",
         "effect give {p} resistance 99999 5 true && effect give {p} strength 99999 100 true && effect give {p} speed 99999 3 true && effect give {p} haste 99999 255 true && effect give {p} night_vision 99999 0 true && effect give {p} saturation 99999 255 true && effect give {p} fire_resistance 99999 0 true && effect give {p} absorption 99999 10 true && playsound minecraft:item.totem.use master {p}",
         "Tam ölümsüzlük, tek atma, süper koşu, ışık hızında kırma ve sonsuz tokluk"),

        ("⛏️ Çılgın Madenci Hızı (Haste 255)", "effect give {p} haste 99999 255 true", "Bloklara dokunduğun mikrosaniyede parçalar"),
        ("🛡️ Hasarsızlık (Resistance V)", "effect give {p} resistance 99999 5 true", "Darbe, patlama ve lavdan sıfır hasar alır"),
        ("💪 Titan Gücü (Strength 100)", "effect give {p} strength 99999 100 true", "Yumrukla dahi Ender Dragon'a tek atar"),
        ("🏃 Flaş Koşu Hızı (Speed 5)", "effect give {p} speed 99999 4 true", "Şimşek gibi yüksek koşu temposu"),
        ("👁️ Sonsuz Gece Görüşü (Night Vision)", "effect give {p} night_vision 99999 0 true", "Zifiri karanlığı gündüz yapar"),
        ("💖 Anında Can Yenilenmesi (Regen 255)", "effect give {p} regeneration 99999 255 true", "Can barı ışık hızında dolar"),
        ("🔥 Ateş Bağışıklığı (Fire Resistance)", "effect give {p} fire_resistance 99999 0 true", "Lav ve ateşte rahatça yüzme"),
        ("🌊 Sualtı Hâkimiyeti (Conduit Power)", "effect give {p} conduit_power 99999 0 true", "Suda sınırsız nefes, görüş ve kırma hızı"),
        ("🦘 Süper Zıplama (Jump Boost 5)", "effect give {p} jump_boost 99999 4 true", "10 blok yükseğe sıçrama"),
        ("👻 Tam Görünmezlik (Invisibility)", "effect give {p} invisibility 99999 0 true", "Moblar ve oyuncular göremez"),
        ("🪶 Yavaş Düşüş (Slow Falling)", "effect give {p} slow_falling 99999 0 true", "Tüy gibi süzülür, düşüş hasarı almaz"),
        ("🌟 Köyün Kahramanı (Hero of Village V)", "effect give {p} hero_of_the_village 99999 4 true", "Köylüler eşyaları bedavaya yakın verir"),
        ("🐬 Yunus Zarafeti (Dolphins Grace)", "effect give {p} dolphins_grace 99999 0 true", "Suda roket gibi yüzme hızı"),
        ("✨ Ekstra Can Barı (Absorption 10)", "effect give {p} absorption 99999 10 true", "40 ekstra altın kalp ekler"),
        ("🍖 Sonsuz Doygunluk (Saturation)", "effect give {p} saturation 99999 255 true", "Açlık barı asla düşmez"),
        ("🧹 TÜM EFEKTLERİ TEMİZLE", "effect clear {p}", "Tüm iksir ve büyü etkilerini anında sıfırlar"),

        ("🗡️ Eldeki Silaha: Keskinlik V", "enchant {p} sharpness 5", "Eldeki silaha Sharpness V basar"),
        ("🛡️ Eldeki Zırha: Koruma IV", "enchant {p} protection 4", "Eldeki zırha Protection IV basar"),
        ("⛏️ Eldeki Alete: Verimlilik V", "enchant {p} efficiency 5", "Eldeki alete Efficiency V basar"),
        ("💎 Eldeki Kazmaya: Servet III", "enchant {p} fortune 3", "Eldeki kazmaya Fortune III basar"),
        ("✨ Eldeki Kazmaya: İpeksi Dokunuş", "enchant {p} silk_touch 1", "Eldeki kazmaya Silk Touch basar"),
        ("🏹 Eldeki Yaya: Güç V (Power)", "enchant {p} power 5", "Eldeki yaya Power V basar"),
        ("♾️ Eldeki Yaya: Sonsuzluk (Infinity)", "enchant {p} infinity 1", "Eldeki yaya Infinity basar"),
        ("🔧 Eldeki Eşyaya: Tamir (Mending)", "enchant {p} mending 1", "Eldeki eşyaya Mending basar"),
        ("🔨 Eldeki Eşyaya: Kırılmazlık III", "enchant {p} unbreaking 3", "Eldeki eşyaya Unbreaking III basar")
    ],

    # -------------------------------------------------------------------------
    # 7. SUNUCU EVENTLERİ & BOSS
    # -------------------------------------------------------------------------
    "🎪 EVENT & ÖZEL ETKİNLİKLER": [
        ("☄️ Meteor Yağmuru Eventi Başlat",
         'execute at {p} run summon fireball ~ ~25 ~ {direction:[0.0,-1.0,0.0],ExplosionPower:4} && execute at {p} run summon tnt ~ ~20 ~ {Fuse:40} && title @a title {"text":"☄️ METEOR DÜŞÜYOR!","color":"red","bold":true} && title @a subtitle {"text":"Sığınaklara Kaçın!","color":"gold"} && playsound minecraft:entity.generic.explode master @a ~ ~ ~ 10 0.5',
         "Gökyüzünden patlayan meteor topları ve TNT indirir, dev sarsıntı yaratır"),

        ("💰 Altın & Akçe Yağmuru Eventi",
         'execute at {p} run summon item ~-1 ~5 ~ {Item:{id:"gold_ingot",Count:32b}} && execute at {p} run summon item ~1 ~5 ~ {Item:{id:"diamond",Count:16b}} && execute at {p} run summon item ~ ~6 ~1 {Item:{id:"emerald",Count:32b}} && title @a title {"text":"💰 ALTIN YAĞMURU!","color":"gold","bold":true} && title @a subtitle {"text":"Ganimetleri Toplayın!","color":"yellow"} && playsound minecraft:entity.player.levelup master @a',
         "Oyuncunun üzerine gökten külçeler, elmaslar ve zümrütler yağdırır"),

        ("🧟 Zombi Kıyameti Dalgası",
         'execute at {p} run summon zombie ~3 ~ ~ {HandItems:[{id:"iron_sword",Count:1b},{}],ArmorItems:[{},{},{id:"iron_chestplate",Count:1b},{id:"iron_helmet",Count:1b}]} && execute at {p} run summon zombie ~-3 ~ ~ {HandItems:[{id:"iron_sword",Count:1b},{}],ArmorItems:[{},{},{id:"iron_chestplate",Count:1b},{id:"iron_helmet",Count:1b}]} && execute at {p} run summon zombie ~ ~ ~3 {HandItems:[{id:"iron_sword",Count:1b},{}],ArmorItems:[{},{},{id:"iron_chestplate",Count:1b},{id:"iron_helmet",Count:1b}]} && title @a title {"text":"🧟 ZOMBİ KIYAMETİ!","color":"dark_red","bold":true}',
         "Oyuncuyu zırhlı ve kılıçlı zombi sürüsüyle kuşatır"),

        ("👹 Boss Savaşı: Warden Kralı",
         'execute at {p} run summon warden ~ ~ ~ {CustomName:\'{"text":"👹 KARANLIKLAR HÜKÜMDARI","color":"dark_purple","bold":true}\'} && title @a title {"text":"👹 BOSS DOĞDU!","color":"dark_purple","bold":true} && playsound minecraft:entity.warden.emerge master @a',
         "Özel isimli korkunç Warden bossu doğurur"),

        ("💀 Boss Savaşı: 3 Başlı Wither",
         'execute at {p} run summon wither ~ ~5 ~ {CustomName:\'{"text":"💀 KIYAMET WITHER\'I","color":"dark_red","bold":true}\'} && title @a title {"text":"💀 WITHER ÇAĞRILDI!","color":"dark_red","bold":true} && playsound minecraft:entity.wither.spawn master @a',
         "Gökyüzünde 3 başlı Wither bossu başlatır"),

        ("🎆 Görkemli Havai Fişek Festivali",
         'execute at {p} run summon firework_rocket ~ ~ ~ {LifeTime:20,FireworksItem:{Flight:2,Explosions:[{Type:1,Colors:[I;16711680,65280,255],FadeColors:[I;16776960]}]}} && execute at {p} run summon firework_rocket ~2 ~ ~ {LifeTime:25,FireworksItem:{Flight:2,Explosions:[{Type:2,Colors:[I;16776960,16711935],FadeColors:[I;65535]}]}} && execute at {p} run summon firework_rocket ~-2 ~ ~ {LifeTime:30,FireworksItem:{Flight:3,Explosions:[{Type:4,Colors:[I;65535,16711680],FadeColors:[I;16777215]}]}} && title @a actionbar {"text":"🎆 KUTLAMA VE ŞÖLEN BAŞLADI!","color":"gold","bold":true}',
         "Çok renkli patlayan roketlerle gökyüzü festivali yapar"),

        ("⚡ 15'li Şimşek Kasırgası",
         "execute at {p} run summon lightning_bolt ~2 ~ ~ && execute at {p} run summon lightning_bolt ~-2 ~ ~ && execute at {p} run summon lightning_bolt ~ ~ ~2 && execute at {p} run summon lightning_bolt ~ ~ ~-2 && execute at {p} run summon lightning_bolt ~3 ~ ~3 && execute at {p} run summon lightning_bolt ~-3 ~ ~-3",
         "Hedefin etrafını dev yıldırımlarla bombalar")
    ],

    # -------------------------------------------------------------------------
    # 8. TROLL & OYUNCU YÖNETİMİ
    # -------------------------------------------------------------------------
    "🤡 TROLL & OYUNCU YÖNETİMİ": [
        ("🚀 Uzaya Fırlat (Y: 500)", "tp {p} ~ 500 ~", "Oyuncuyu stratosfere ışınlar, serbest düşüşe bırakır"),
        ("🕳️ Yerin Dibine Göm (Y: -58)", "tp {p} ~ -58 ~", "Katman kayasının dibine hapseder"),
        ("🧊 Cam Kafese Hapset", "execute at {p} run fill ~-1 ~ ~-1 ~1 ~2 ~1 glass outline", "Oyuncunun etrafına hava alamaz cam kafes örer"),
        ("⬛ Obsidyen Hücreye Kapat", "execute at {p} run fill ~-1 ~-1 ~-1 ~1 ~2 ~1 obsidian outline", "Kırılması imkansız obsidyen hücre"),
        ("🕸️ Örümcek Ağına Göm", "execute at {p} run fill ~-1 ~ ~-1 ~1 ~2 ~1 cobweb replace air", "Hareket edemeyecek şekilde ağlara dolar"),
        ("🔨 Kafasına Örs Düşür", "execute at {p} run setblock ~ ~4 ~ anvil", "Doğrudan kafasına 4 blok yukarıdan örs bırakır"),
        ("🔥 Ayaklarının Altını Yak", "execute at {p} run setblock ~ ~ ~ fire", "Ayağını ateşe verir"),
        ("🌊 Kafasından Lav Boşalt", "execute at {p} run setblock ~ ~2 ~ lava", "Kafasından aşağı kızgın lav akıtır"),
        ("💧 Kafasından Su Dök", "execute at {p} run setblock ~ ~2 ~ water", "Kafasından su boşaltır"),
        ("🤢 Aşırı Bulantı (Nausea 255)", "effect give {p} nausea 30 255 true", "Ekranı fırıl fırıl döndürüp midesini bulandırır"),
        ("🕶️ Körlük & Zifiri Karanlık", "effect give {p} blindness 30 255 true && effect give {p} darkness 30 255 true", "1 santim önünü bile göremez"),
        ("🥶 Dondur / Felç Et (Slowness 255)", "effect give {p} slowness 30 255 true", "Adım dahi atamaz, kaskatı kesilir"),
        ("🎈 Sonsuz Havaya Yükselt (Levitation)", "effect give {p} levitation 15 5 true", "Balon gibi gökyüzüne uçurur"),
        ("🍖 Açlık Krizine Sok", "effect give {p} hunger 30 255 true", "Açlık barını 1 saniyede sıfıra indirir"),
        ("🔊 Creeper Tıslaması (Jumpscare)", "playsound minecraft:entity.creeper.primed master {p} ~ ~ ~ 10 1", "Arkasında creeper patlayacakmış gibi ses çalar"),
        ("👹 Warden Çığlığı (Jumpscare)", "playsound minecraft:entity.warden.emerge master {p} ~ ~ ~ 10 1", "Korkunç Warden çıkış çığlığı ile korkutur"),
        ("🐲 Ejderha Kükremesi", "playsound minecraft:entity.ender_dragon.growl master {p} ~ ~ ~ 10 1", "Kulağında dev ejderha kükremesi patlatır"),
        ("🎒 Envanterini Tamamen Boşalt", "clear {p}", "Tüm envanterini ve zırhlarını siler"),
        ("🧲 Baş Aşağı Çevir (Dinnerbone)", 'minecraft:give {p} name_tag{display:{Name:\'{"text":"Dinnerbone"}\'}} 1', "Dinnerbone isim etiketi verir")
    ],

    # -------------------------------------------------------------------------
    # 9. IŞINLANMA & WARP NOKTALARI
    # -------------------------------------------------------------------------
    "📍 IŞINLANMA & WARP NOKTALARI": [
        ("🌳 Overworld Spawn'a Işınla (0, 100, 0)", "execute in minecraft:overworld run tp {p} 0 100 0", "Dünya ana doğma noktasına gönderir"),
        ("🌋 Nether Boyutuna Gönder (0, 70, 0)", "execute in minecraft:the_nether run tp {p} 0 70 0", "Cehennem boyutuna güvenli kata ışınlar"),
        ("🔮 The End Boyutuna Gönder (0, 70, 0)", "execute in minecraft:the_end run tp {p} 0 70 0", "Ejderha dünyasına ışınlar"),
        ("👥 Herkesi Bana Çek (TP All)", "tp @a {p}", "Tüm online oyuncuları bu oyuncunun yanına çeker"),
        ("🛏️ Doğma Noktası Ayarla (Spawnpoint)", "spawnpoint {p}", "Oyuncunun yeniden doğma noktasını burası yapar"),
        ("💎 Derin Maden Katına İn (Y: -55)", "tp {p} ~ -55 ~", "Doğrudan elmas seviyesine ışınlar"),
        ("☁️ Gökyüzü Kulesine Çık (Y: 200)", "tp {p} ~ 200 ~", "Bulutların üzerine ışınlar"),
        ("🧭 0, 0 Merkezine Git", "tp {p} 0 ~ 0", "X=0, Z=0 dünya merkezine ışınlar"),
        ("📍 1000 Blok İleri Işınla", "tp {p} ~1000 ~ ~", "Doğuya 1000 blok keşfe gönderir")
    ],

    # -------------------------------------------------------------------------
    # 10. DÜNYA, HAVA & ANTİ-LAG
    # -------------------------------------------------------------------------
    "⚙️ DÜNYA, HAVA & ANTİ-LAG": [
        ("🧹 LAG TEMİZLİĞİ: Yerdeki Çöpleri Sil", "minecraft:kill @e[type=item]", "Yerde biriken tüm item çöplerini silip lagı önler"),
        ("🧹 LAG TEMİZLİĞİ: Canavarları Sil", "difficulty peaceful && difficulty normal", "Tüm zararlı yaratık ve canavarları anında temizler"),
        ("🏹 Yerdeki Okları Temizle", "minecraft:kill @e[type=arrow]", "Saplanan okları temizler"),
        ("⚡ Full Lag & Çöp Temizliği (Eşyalar + Oklar + Küreler)", "minecraft:kill @e[type=item] && minecraft:kill @e[type=arrow] && minecraft:kill @e[type=experience_orb]", "Tüm yerdeki çöpleri, okları ve küreleri tek seferde temizler"),

        ("☀️ Sabah Yap (Day)", "time set day", "Güneş doğar"),
        ("🕛 Öğle Yap (Noon)", "time set noon", "Tam tepede güneş"),
        ("🌇 Gün Batımı (Sunset)", "time set 12000", "Romantik akşam batımı"),
        ("🌙 Gece Yap (Night)", "time set night", "Gece başlar"),

        ("☀️ Güneşli Hava (Clear)", "weather clear", "Yağmuru keser"),
        ("🌧️ Yağmur Yağdır (Rain)", "weather rain", "Yağmur başlatır"),
        ("⛈️ Fırtına & Şimşek (Thunder)", "weather thunder", "Yıldırımlı fırtına"),

        ("🛡️ Eşyalar Düşmesin (KeepInv AÇ)", "gamerule keepInventory true", "Ölünce eşyalar envanterde kalır"),
        ("❌ Eşyalar Düşsün (KeepInv KAPAT)", "gamerule keepInventory false", "Ölünce eşyalar saçılır"),
        ("🚫 Creeper / Mob Hasarını Kapat", "gamerule mobGriefing false", "Creeper patlayınca bloklar kırılmaz"),
        ("💥 Mob Hasarını Aç", "gamerule mobGriefing true", "Creeper blokları patlatabilir"),
        ("🧯 Yangın Yayılmasını Kapat", "gamerule doFireTick false", "Ateş yayılmaz"),
        ("⏸️ Zaman Akışını Sabitle", "gamerule doDaylightCycle false", "Saat durur"),
        ("▶️ Zaman Akışını Başlat", "gamerule doDaylightCycle true", "Saat ilerler"),

        ("🕊️ Zorluk: Barışçıl", "difficulty peaceful", "Canavarlar doğmaz"),
        ("⚔️ Zorluk: Normal", "difficulty normal", "Standart zorluk"),
        ("💀 Zorluk: Zor (Hard)", "difficulty hard", "Maksimum canavar gücü"),
        ("💾 Dünyayı Şimdi Kaydet (Flush)", "save-all flush", "Tüm dünya bloklarını diske kalıcı yazar"),
        ("📢 Sunucuya Altın Başlık Bas", 'title @a title {"text":"Toprakkk","color":"gold","bold":true}', "Ekrana dev altın yazı"),
        ("💬 Kurucu Duyurusu Geç", "say [KURUCU]: Sunucumuza Hos Geldiniz!", "Sohbete duyuru geçer")
    ],

    # -------------------------------------------------------------------------
    # 11. MOB & CANLI ÇAĞIRICI
    # -------------------------------------------------------------------------
    "🐉 MOB & CANLI ÇAĞIRICI": [
        ("🐲 Ender Ejderhası Çağır", "summon ender_dragon ~ ~5 ~", "Ender Dragon oluşturur"),
        ("💀 Wither Boss Çağır", "summon wither ~ ~2 ~", "3 Başlı Wither çağırır"),
        ("👹 Warden Çağır", "summon warden ~ ~ ~", "Karanlık derinlik bekçisi Warden"),
        ("🤖 Demir Golem Çağır", "summon iron_golem ~ ~ ~", "Korumacı Demir Golem"),
        ("🐎 Eyerli Evcil At Çağır", 'summon horse ~ ~ ~ {Tame:1b,SaddleItem:{id:"saddle",Count:1b}}', "Binmeye hazır evcil at"),
        ("🐕 Sadık Evcil Kurt", "summon wolf ~ ~ ~ {Tame:1b}", "Sadık kurt"),
        ("🐈 Evcil Kedi", "summon cat ~ ~ ~ {Tame:1b}", "Creeper kaçıran kedi"),
        ("🧨 Patlayan TNT Çağır", "summon tnt ~ ~ ~ {Fuse:40}", "2 saniye sonra patlar"),
        ("⚡ Yıldırım Çarptır", "summon lightning_bolt ~ ~ ~", "Yıldırım indirir"),
        ("🧟 Zombi Sürüsü (5x)", "summon zombie ~ ~ ~ && summon zombie ~ ~ ~ && summon zombie ~ ~ ~ && summon zombie ~ ~ ~ && summon zombie ~ ~ ~", "5 adet zombi basar"),
        ("💀 İskelet Sürüsü (5x)", "summon skeleton ~ ~ ~ && summon skeleton ~ ~ ~ && summon skeleton ~ ~ ~ && summon skeleton ~ ~ ~ && summon skeleton ~ ~ ~", "5 adet iskelet basar")
    ],

    # -------------------------------------------------------------------------
    # 12. YETKİ & MOD YÖNETİMİ
    # -------------------------------------------------------------------------
    "👑 YETKİ & OYUNCU MODLARI": [
        ("👑 OP Yetkisi Ver", "op {p}", "Oyuncuyu yönetici (OP) yapar"),
        ("🚫 OP Yetkisini Al", "deop {p}", "OP yetkisini kaldırır"),
        ("💖 Canı & Açlığı Fulle (Heal)", "effect give {p} instant_health 1 255 true && effect give {p} saturation 1 255 true", "Can ve açlık barını anında doldurur"),
        ("🏕️ Hayatta Kalma (Survival)", "gamemode survival {p}", "Survival moduna geçirir"),
        ("🎨 Yaratıcı Mod (Creative)", "gamemode creative {p}", "Creative moduna geçirir"),
        ("👻 İzleyici Modu (Spectator)", "gamemode spectator {p}", "Duvarlardan geçen hayalet modu"),
        ("🧭 Macera Modu (Adventure)", "gamemode adventure {p}", "Blok kıramaz macera modu"),
        ("🌟 +100 Level Deneyim (XP)", "xp add {p} 100 levels", "100 Seviye XP yükler"),
        ("✨ +1000 Puan Deneyim (XP)", "xp add {p} 1000 points", "1000 Deneyim puanı verir"),
        ("👢 Sunucudan At (Kick)", "kick {p} Sunucudan cikarildiniz", "Oyuncuyu oyundan atar"),
        ("⛔ Oyuncuyu Yasakla (Ban)", "ban {p} Sunucudan yasaklandiniz", "Sunucudan banlar"),
        ("🔓 Banı Aç (Pardon)", "pardon {p}", "Yasağını kaldırır"),
        ("☠️ Oyuncuyu Öldür", "kill {p}", "Anında öldürür")
    ],

    # -------------------------------------------------------------------------
    # 13. 🏡 ARSA & ARAZİ YÖNETİMİ (GriefPrevention)
    # -------------------------------------------------------------------------
    "🏡 ARSA & ARAZİ YÖNETİMİ": [
        ("⛏️ Arsa Kapatma Altın Küreği Ver", 'minecraft:give {p} golden_shovel{display:{Name:\'{"text":"🏡 Arsa Kapatma & Koruma Küreği","color":"gold","bold":true}\',Lore:[\'{"text":"İki çapraz köşeye sağ tıklayarak arsa kapat","color":"yellow"}\',\'{"text":"Sandıkların ve evlerin patlamaya karşı korunur!","color":"green"}\']}} 1', "Sağ tıklayarak sınırları çizip arsayı sahiplenme küreği"),
        ("📜 Oyuncunun Arsalarını Listele", "claimslist {p}", "Oyuncunun sahip olduğu tüm arsaları ve kalan blok hakkını listeler"),
        ("🛡️ +500 Bonus Arsa Bloğu Hediye Et", "adjustbonusclaimblocks {p} 500", "Oyuncuya 500 blokluk ekstra arsa genişletme hakkı verir"),
        ("🛡️ +2.000 Bonus Arsa Bloğu Hediye Et", "adjustbonusclaimblocks {p} 2000", "Oyuncuya 2.000 blokluk devasa arsa alanı verir"),
        ("🛡️ +10.000 Bonus Arsa Bloğu (Dev Şehir)", "adjustbonusclaimblocks {p} 10000", "Oyuncuya 10.000 blokluk krallık/şehir arsa hakkı verir"),
        ("💥 Arsa Patlama Korumasını Aç / Kapat", "sudo {p} claimexplosions", "Arsa içinde TNT/Creeper patlama hasarını açar veya kapatır"),
        ("🤝 Arsayı Arkadaşa Aç (Güven Ver - Trust)", "sudo {p} trust @r", "Seçilen oyuncuya arsa içinde inşa ve sandık izni verir"),
        ("🚫 Arsa Güvenini Kaldır (Untrust)", "sudo {p} untrust @r", "Arsa iznini geri alır"),
        ("📦 Sandık ve Eşya Güveni Ver (ContainerTrust)", "sudo {p} containertrust @r", "Yalnızca sandık ve fırınları açma izni verir"),
        ("🚪 Giriş & Buton Güveni Ver (AccessTrust)", "sudo {p} accesstrust @r", "Kapıları ve şalterleri kullanma izni verir"),
        ("🏰 Admin Koruma Alanı Oluştur (AdminClaim)", "sudo {p} adminclaims", "Sunucu doğma alanı veya pazar yeri için kırılmaz admin arsası"),
        ("🧹 Oyuncunun Tüm Arsalarını Sil", "deleteallclaims {p}", "Oyuncunun dünyadaki tüm arsalarını serbest bırakır"),
        ("📖 Arsa Kılavuz Kitabı Ver", "claimbook {p}", "Oyuncuya nasıl arsa kapatacağını anlatan renkli rehber kitap verir")
    ],

    # -------------------------------------------------------------------------
    # 14. 🛒 OYUN İÇİ MARKET & TAKAS (EconomyShopGUI & Trade)
    # -------------------------------------------------------------------------
    "🛒 OYUN İÇİ MARKET & TAKAS": [
        ("🛒 Oyuncuya Market Menüsünü Aç (/shop)", "sudo {p} shop", "Ekrana eşyalar alıp satabileceği renkli GUI marketi açar"),
        ("🏷️ Hızlı Eşya Satış Menüsünü Aç (/sellgui)", "sudo {p} sellgui", "Envanterdeki eşyaları sürükleyip anında Akçeye çevirir"),
        ("💰 Tüm Eşyaları Sat & Akçe Kazan (/sellall)", "sudo {p} sellall", "Envanterdeki satılabilir tüm maden ve tarım ürünlerini satar"),
        ("🧭 Sunucu & Market Pusulası Ver", 'minecraft:give {p} compass{display:{Name:\'{"text":"🧭 Sunucu & Market Menüsü","color":"gold","bold":true}\',Lore:[\'{"text":"Sağ tıkla veya /n yaz: Marketi aç!","color":"yellow"}\',\'{"text":"Akçenle eşya alıp satabilirsin!","color":"green"}\']}} 1', "Eline sağ tıklayınca market menüsünü açan özel pusula verir"),
        ("🤝 İki Oyuncu Arasında Takas Başlat", "sudo {p} trade @r", "Güvenli dolandırıcılıksız eşya ve Akçe takas penceresi açar"),
        ("🪙 +1.000 Akçe Gönder (/eco give)", "eco give {p} 1000", "Oyuncunun Vault Essentials hesabına 1.000 Akçe yükler"),
        ("🪙 +10.000 Akçe Gönder (/eco give)", "eco give {p} 10000", "Oyuncunun Vault Essentials hesabına 10.000 Akçe yükler"),
        ("🪙 +100.000 Milyarder Akçesi Yükle", "eco give {p} 100000", "Oyuncuya 100.000 Akçe yükler"),
        ("💸 -500 Akçe Kes (/eco take)", "eco take {p} 500", "Oyuncunun hesabından 500 Akçe çeker"),
        ("🎯 Akçe Bakiyesini Sabitle (/eco set)", "eco set {p} 5000", "Oyuncunun Akçesini 5.000 olarak ayarlar"),
        ("🏆 En Zenginler Sıralaması (/baltop)", "baltop", "Sunucunun en zengin oyuncularını listeler"),
        ("🔄 Market Fiyatlarını Yenile (/eshop reload)", "eshop reload", "EconomyShopGUI ayarlarını ve fiyat listesini yeniler")
    ],

    # -------------------------------------------------------------------------
    # 15. 🛡️ ANTICHEAT & GÜVENLİK (GrimAC & AntiXray)
    # -------------------------------------------------------------------------
    "🛡️ ANTICHEAT & GÜVENLİK": [
        ("🛡️ GrimAC Durumunu Kontrol Et", "grim reload", "Grim AntiCheat motorunu kontrol eder ve kuralları tazeler"),
        ("🔍 Canlı Hile İhlal Bildirimleri (/grim verbose)", "grim verbose", "Hile şüphelilerini konsolda ve sohbette anlık takip eder"),
        ("👁️ Anti-Xray Engelleyici Durumu", "say [GÜVENLİK]: Spigot Anti-Xray Aktif! Madenler gizleniyor.", "X-Ray maden hilelerinin engellendiğini onaylar"),
        ("🧊 Hile Şüphelisini Dondur & Kitle", "effect give {p} slowness 60 255 true && effect give {p} mining_fatigue 60 255 true && title {p} title {\"text\":\"⚠️ KONTROL EDİLİYORSUNUZ\",\"color\":\"red\",\"bold\":true}", "Şüpheli oyuncuyu 60 saniye kilitler, hareketini ve kazmasını durdurur"),
        ("🔥 Buzu Çöz / Serbest Bırak", "effect clear {p} slowness && effect clear {p} mining_fatigue", "Oyuncunun dondurmasını kaldırır"),
        ("🏃 Hileciden Tüm Eşyaları Al & Temizle", "clear {p}", "Envanterini tamamen siler"),
        ("⚡ Yere Çak (Uçan Hileciyi İndir)", "effect give {p} levitation 1 255 true", "Fly açan oyuncuyu anında yere çiviler")
    ],

    # -------------------------------------------------------------------------
    # 16. ⛺ EVLER & HIZLI IŞINLANMA (EssentialsX)
    # -------------------------------------------------------------------------
    "⛺ EVLER & HIZLI IŞINLANMA": [
        ("⛺ Oyuncunun Evine Işınlan (/home)", "sudo {p} home", "Oyuncuyu kaydettiği güvenli evine ışınlar"),
        ("📍 Burayı Ev Olarak Kaydet (/sethome)", "sudo {p} sethome", "Oyuncunun durduğu yeri /home noktası olarak kaydeder"),
        ("🏛️ Başlangıç Spawn Alanına Git (/spawn)", "sudo {p} spawn", "Oyuncuyu güvenli sunucu başlangıç merkezine ışınlar"),
        ("🔮 Işınlanma İsteği Gönder (/tpa)", "sudo {p} tpa @r", "Arkadaşına ışınlanma daveti yollar"),
        ("✅ Işınlanma İsteğini Kabul Et (/tpaccept)", "sudo {p} tpaccept", "Gelen ışınlanma davetini onaylar"),
        ("🏃 Önceki Konuma / Öldüğün Yere Dön (/back)", "sudo {p} back", "Ölüm veya önceki ışınlanma noktasına geri döner")
    ],

    # -------------------------------------------------------------------------
    # 17. 🎁 KİTLER & SUNUCU EKRANI (Kits, Scoreboard & Hologram)
    # -------------------------------------------------------------------------
    "🎁 KİTLER & EKRAN": [
        ("🎁 Oyuncuya Başlangıç Kiti Ver (/kit baslangic)", "kit baslangic {p}", "Taş aletler, altın arsa küreği, yiyecek, meşale ve 100 Akçe"),
        ("⭐ Oyuncuya Günlük Hediye Kiti Ver (/kit gunluk)", "kit gunluk {p}", "Altın elma, demir külçeler, ekmek, roket ve 500 Akçe ödülü"),
        ("⛏️ Oyuncuya Madenci Kiti Ver (/kit madenci)", "kit madenci {p}", "Verimlilik I demir kazma, 64 meşale, su kovası ve ekmek"),
        ("⚔️ Oyuncuya Savaşçı Kiti Ver (/kit savasci)", "kit savasci {p}", "Keskinlik I demir kılıç, kalkan, yay ve 32 ok"),
        ("📊 Scoreboard'u Aç/Kapat (/sb)", "sudo {p} sb", "Sağ taraftaki Akçe ve ping bilgi tablosunu açıp kapatır"),
        ("🌌 Spawn Rehber Hologramını Yenile (/dh reload)", "dh reload", "Spawn alanındaki rehber ve bilgi hologramını yeniler"),
        ("📢 Sohbette Market Duyurusu Geç", "broadcast &8[&6Duyuru&8] &e/n &7veya &e/shop &ayazarak Akçe marketini açabilirsiniz!", "Tüm sunucuya market duyurusu atar"),
        ("📢 Sohbette Arsa Duyurusu Geç", "broadcast &8[&6Duyuru&8] &eAltın Kürek &aile iki köşeye tıklayarak patlamaz arsanızı kapatın!", "Tüm sunucuya arsa duyurusu atar"),
        ("📢 Sohbette Takas Duyurusu Geç", "broadcast &8[&6Duyuru&8] &e/takas <oyuncu> &aile güvenli ticaret yapabilirsiniz!", "Tüm sunucuya takas duyurusu atar")
    ],

    # -------------------------------------------------------------------------
    # 18. 👑 ROLLER & MESLEK YÖNETİMİ
    # -------------------------------------------------------------------------
    "👑 ROLLER & MESLEKLER": [
        ("🏛️ Cumhurbaşkanı Rolü Ata", "team join cumhurbaskani {p} && tab player {p} tabprefix &c&l[Baskan] &e && tab player {p} tagprefix &c&l[Baskan] &e && title {p} title {\"text\":\"👑 CUMHURBAŞKANI SEÇİLDİNİZ!\",\"color\":\"red\",\"bold\":true} && broadcast &8[&4Devlet&8] &c{p} &4Cumhurbaskani makamina atandi!", "Oyuncuyu en yüksek devlet makamı olan Cumhurbaşkanı yapar"),
        ("🏡 Köy Muhtarı Rolü Ata", "team join muhtar {p} && tab player {p} tabprefix &6&l[Muhtar] &f && tab player {p} tagprefix &6&l[Muhtar] &f && title {p} title {\"text\":\"🏡 KÖY MUHTARI OLDUNUZ!\",\"color\":\"gold\",\"bold\":true} && broadcast &8[&6Duyuru&8] &e{p} &6Koy Muhtari secildi!", "Oyuncuyu köyün yöneticisi ve arsa temsilcisi Muhtar yapar"),
        ("👮 Polis Memuru Ata", "team join polis {p} && tab player {p} tabprefix &9&l[Polis] &b && tab player {p} tagprefix &9&l[Polis] &b && title {p} title {\"text\":\"👮 POLİS MEMURU OLDUNUZ!\",\"color\":\"blue\",\"bold\":true} && broadcast &8[&9Emniyet&8] &b{p} &9Polis Teskilatina katildi!", "Asayişi ve huzuru sağlamak için polis unvanı verir"),
        ("🪖 Asker & Komutan Ata", "team join asker {p} && tab player {p} tabprefix &2&l[Asker] &a && tab player {p} tagprefix &2&l[Asker] &a && title {p} title {\"text\":\"🪖 ASKER OLDUNUZ!\",\"color\":\"dark_green\",\"bold\":true} && broadcast &8[&2Ordu&8] &a{p} &2Milli Savunma Ordusuna katildi!", "Vatan savunması ve sınır güvenliği için asker unvanı verir"),
        ("🩺 Başhekim / Doktor Ata", "team join doktor {p} && tab player {p} tabprefix &c&l[Doktor] &f && tab player {p} tagprefix &c&l[Doktor] &f && title {p} title {\"text\":\"🩺 DOKTOR OLDUNUZ!\",\"color\":\"red\",\"bold\":true} && broadcast &8[&cSaglik&8] &f{p} &cDoktor gorevine basladi!", "Oyuncuları iyileştiren sağlık görevlisi unvanı verir"),
        ("⚖️ Ağır Ceza Hakimi Ata", "team join hakim {p} && tab player {p} tabprefix &5&l[Hakim] &d && tab player {p} tagprefix &5&l[Hakim] &d && title {p} title {\"text\":\"⚖️ HAKİM OLDUNUZ!\",\"color\":\"dark_purple\",\"bold\":true} && broadcast &8[&5Adalet&8] &d{p} &5Hakim olarak divana gecti!", "Oyuncular arası davaları çözen adalet hakimi yapar"),
        ("🏗️ Baş Mimar Ata", "team join mimar {p} && tab player {p} tabprefix &3&l[Mimar] &b && tab player {p} tagprefix &3&l[Mimar] &b && title {p} title {\"text\":\"🏗️ BAŞ MİMAR OLDUNUZ!\",\"color\":\"dark_aqua\",\"bold\":true} && broadcast &8[&3Imar&8] &b{p} &3Bas Mimar unvanini kazandi!", "Şehir yapılarını tasarlayan baş mimar yapar"),
        ("💰 Büyük Tüccar Ata", "team join tuccar {p} && tab player {p} tabprefix &e&l[Tuccar] &6 && tab player {p} tagprefix &e&l[Tuccar] &6 && title {p} title {\"text\":\"💰 BÜYÜK TÜCCAR OLDUNUZ!\",\"color\":\"yellow\",\"bold\":true} && broadcast &8[&eTicaret&8] &e{p} &6Buyuk Tuccar oldu!", "Pazarda ticaret yapan tüccar unvanı verir"),
        ("⛏️ Usta Madenci Ata", "team join madenci {p} && tab player {p} tabprefix &8&l[Madenci] &7 && tab player {p} tagprefix &8&l[Madenci] &7 && title {p} title {\"text\":\"⛏️ MADENCİ OLDUNUZ!\",\"color\":\"gray\",\"bold\":true}", "Yeraltı madenlerini işleten madenci unvanı verir"),
        ("🌾 Baş Çiftçi Ata", "team join ciftci {p} && tab player {p} tabprefix &a&l[Ciftci] &2 && tab player {p} tagprefix &a&l[Ciftci] &2 && title {p} title {\"text\":\"🌾 ÇİFTÇİ OLDUNUZ!\",\"color\":\"green\",\"bold\":true}", "Tarlaları ekip biçen çiftçi unvanı verir"),
        ("⚔️ Kraliyet Şövalyesi Ata", "team join sovalye {p} && tab player {p} tabprefix &1&l[Sovalye] &9 && tab player {p} tagprefix &1&l[Sovalye] &9 && title {p} title {\"text\":\"⚔️ KRALİYET ŞÖVALYESİ OLDUNUZ!\",\"color\":\"dark_blue\",\"bold\":true}", "Kralın özel muhafız şövalyesi yapar"),
        ("👑 Sunucu Kurucusu / Kral Yap", "team join kurucu {p} && tab player {p} tabprefix &4&l[Kurucu] &c && tab player {p} tagprefix &4&l[Kurucu] &c && title {p} title {\"text\":\"👑 SUNUCU KURUCUSU / KRAL!\",\"color\":\"dark_red\",\"bold\":true}", "En üst düzey Kurucu ve Hükümdar yetki unvanı verir"),
        ("❌ Rolü Sıfırla (Standart Vatandaş Yap)", "team join vatandas {p} && tab player {p} tabprefix &7[Vatandas] &f && tab player {p} tagprefix &7[Vatandas] &f && title {p} title {\"text\":\"Standart Vatandaş Yapıldınız\",\"color\":\"white\"}", "Özel rolü kaldırıp normal oyuncu/vatandaş seviyesine çeker")
    ],

    # -------------------------------------------------------------------------
    # 19. 🎰 CASİNO & ŞANS OYUNLARI
    # -------------------------------------------------------------------------
    "🎰 CASİNO & ŞANS OYUNLARI": [
        ("🕹️ ÇALIŞAN KOLLU SLOT MAKİNESİ (Lever/Kollu İn-Game Oyna)",
         "execute at {p} run fill ~-1 ~-1 ~2 ~1 ~-1 ~2 polished_blackstone && execute at {p} run fill ~-1 ~ ~2 ~1 ~3 ~2 polished_blackstone && execute at {p} run fill ~-1 ~1 ~2 ~1 ~1 ~2 gold_block && execute at {p} run setblock ~ ~1 ~2 sea_lantern && execute at {p} run setblock ~ ~ ~1 dropper[facing=south]{Items:[{Slot:0b,id:\"diamond\",Count:16b},{Slot:1b,id:\"emerald\",Count:32b},{Slot:2b,id:\"gold_ingot\",Count:64b},{Slot:3b,id:\"gold_nugget\",Count:64b},{Slot:4b,id:\"paper\",Count:5b,tag:{display:{Name:'{\"text\":\"💰 500 Akçe Çeki\",\"color\":\"gold\",\"bold\":true}'}}}]} && execute at {p} run setblock ~ ~1 ~1 lever[face=floor] && execute at {p} run setblock ~ ~-1 ~1 note_block && execute at {p} run setblock ~ ~2 ~1 oak_wall_sign[facing=north]{front_text:{messages:['{\"text\":\"🎰 KOLLU SLOT 🎰\",\"bold\":true,\"color\":\"gold\"}','{\"text\":\"Kolu İndir!\",\"color\":\"yellow\"}','{\"text\":\"Elmas & Akçe\",\"color\":\"aqua\"}','{\"text\":\"Kazan!\",\"color\":\"green\"}']}} && playsound minecraft:block.anvil.use master {p} ~ ~ ~ 1 1",
         "Hedef oyuncunun önüne kolu (lever) indirildiğinde zili çalan ve haznesinden elmas/akçe fırlatan fiziksel slot makinesi kurar"),

        ("🏰 Las Vegas Kumarhanesi & Casino Binası İnşa Et",
         "execute at {p} run fill ~-6 ~-1 ~-6 ~6 ~-1 ~6 polished_blackstone && execute at {p} run fill ~-6 ~ ~-6 ~6 ~4 ~6 air && execute at {p} run fill ~-6 ~ ~-6 ~6 ~3 ~6 red_concrete outline && execute at {p} run fill ~-5 ~ ~-5 ~5 ~3 ~5 air && execute at {p} run fill ~-6 ~4 ~-6 ~6 ~4 ~6 gold_block outline && execute at {p} run fill ~-5 ~4 ~-5 ~5 ~4 ~5 sea_lantern && execute at {p} run fill ~-4 ~-1 ~-4 ~4 ~-1 ~4 green_wool && execute at {p} run setblock ~ ~-1 ~ emerald_block && execute at {p} run setblock ~ ~ ~ jukebox && execute at {p} run setblock ~-3 ~ ~-3 chest && execute at {p} run setblock ~3 ~ ~-3 chest && execute at {p} run setblock ~ ~ ~-6 oak_door[half=lower,facing=north] && execute at {p} run setblock ~ ~1 ~-6 oak_door[half=upper,facing=north] && playsound minecraft:block.bell.use master {p} ~ ~ ~ 1 1",
         "13x13 kırmızı betonlu, altın çatılı, zümrüt masalı ve lüks zeminli kumarhane binası"),

        ("🎲 Zar At (1-6 Şans & 1.000 Akçe Ödülü)",
         "playsound minecraft:block.note_block.bell master {p} ~ ~ ~ 1 1.5 && tellraw {p} [{\"text\":\"🎲 [CASİNO]: \",\"color\":\"gold\",\"bold\":true},{\"text\":\"Zar atıldı... Gelen Sayı: \",\"color\":\"yellow\"},{\"text\":\"6! 🎯 BÜYÜK KAZANÇ!\",\"color\":\"green\",\"bold\":true}] && eco give {p} 1000 && playsound minecraft:entity.player.levelup master {p} ~ ~ ~ 1 1",
         "Zar atar, oyuncunun ekranında sesli ve renkli zar sonucu gösterip 1.000 Akçe kazandırır"),

        ("🎰 Slot Makinesi Çevir (Jackpot: 💎💎💎)",
         "title {p} title {\"text\":\"🎰 [ 💎 | 💎 | 💎 ]\",\"color\":\"aqua\",\"bold\":true} && title {p} subtitle {\"text\":\"🎉 MEGA JACKPOT! +5.000 Akçe Kazandınız!\",\"color\":\"gold\"} && eco give {p} 5000 && playsound minecraft:ui.toast.challenge_complete master {p} ~ ~ ~ 1 1 && execute at {p} run summon firework_rocket ~ ~1 ~ {FireworksItem:{id:\"firework_rocket\",Count:1b,tag:{Fireworks:{Flight:2b,Explosions:[{Type:1,Colors:[I;16766720,65535]}]}}}}",
         "3'lü elmas slot jackpotu vurur, dev havai fişek patlatır ve 5.000 Akçe kazandırır"),

        ("🎡 Rulet Çarkı Çevir (Kırmızı 32 Kazandı!)",
         "title {p} title {\"text\":\"🎡 RULET DÖNÜYOR...\",\"color\":\"yellow\"} && tellraw {p} [{\"text\":\"🎡 [RULET]: \",\"color\":\"red\",\"bold\":true},{\"text\":\"Top Kırmızı 32'de durdu! +2.500 Akçe Kazandınız!\",\"color\":\"gold\"}] && eco give {p} 2500 && playsound minecraft:entity.experience_orb.pickup master {p} ~ ~ ~ 1 1",
         "Rulet masasında dönen top kazandırır ve 2.500 Akçe verir"),

        ("🪙 Yazı Tura Bahsi (Tura Geldi!)",
         "title {p} title {\"text\":\"🪙 TURA GELDİ!\",\"color\":\"gold\",\"bold\":true} && tellraw {p} [{\"text\":\"🪙 [YAZI-TURA]: \",\"color\":\"yellow\",\"bold\":true},{\"text\":\"Tura geldi! Bahsi kazandınız: +500 Akçe!\",\"color\":\"green\"}] && eco give {p} 500 && playsound minecraft:entity.experience_orb.pickup master {p}",
         "Yazı tura atar ve 500 Akçe kazandırır"),

        ("🎁 Gizemli Jackpot Şans Sandığı Ver",
         'minecraft:give {p} purple_shulker_box{display:{Name:\'{"text":"🎰 GİZEMLİ JACKPOT ŞANS KASASI","color":"gold","bold":true}\',Lore:[\'{"text":"İçinde 100x Elmas, Zümrüt ve Kraliyet Akçeleri var!","color":"yellow"}\',\'{"text":"Aç ve şansını dene!","color":"green"}\']},BlockEntityTag:{Items:[{Slot:0b,id:"diamond",Count:64b},{Slot:1b,id:"emerald",Count:64b},{Slot:2b,id:"gold_ingot",Count:64b},{Slot:3b,id:"netherite_ingot",Count:16b},{Slot:4b,id:"enchanted_golden_apple",Count:16b}]}} 1',
         "Açıldığında içinden yüzlerce elmas, zümrüt ve külçe fışkıran gizemli zenginlik kasası"),

        ("💣 Patlayan Şakacı Kumar Kasası (Troll)",
         "execute at {p} run summon tnt ~ ~ ~ && playsound minecraft:entity.creeper.primed master {p} ~ ~ ~ 1 1 && title {p} title {\"text\":\"💣 KASA PATLADI!\",\"color\":\"red\",\"bold\":true}",
         "Şakacı tuzaklı kumar kasası, oyuncunun önünde patlayan zararsız TNT şovu yapar"),

        ("🎆 Devasa Casino Kutlama & Havai Fişek Şovu",
         "execute at {p} run summon firework_rocket ~ ~1 ~ {FireworksItem:{id:\"firework_rocket\",Count:1b,tag:{Fireworks:{Flight:1b,Explosions:[{Type:1,Colors:[I;16711680,65280,255]}]}}}} && execute at {p} run summon firework_rocket ~2 ~1 ~ {FireworksItem:{id:\"firework_rocket\",Count:1b,tag:{Fireworks:{Flight:2b,Explosions:[{Type:2,Colors:[I;16766720]}]}}}} && broadcast &8[&6Casino&8] &e{p} &aCasino Jackpotunu vurdu!",
         "Tüm sunucuya renkli havai fişeklerle kutlama duyurusu geçer")
    ],

    # -------------------------------------------------------------------------
    # 20. 🗳️ SEÇİM & DEMOKRASİ SİSTEMİ
    # -------------------------------------------------------------------------
    "🗳️ SEÇİM & DEMOKRASİ": [
        ("👑 Cumhurbaşkanlığı Seçimlerini Başlat",
         "broadcast &e&l======================================== && broadcast &6&l👑 RESMİ CUMHURBAŞKANLIĞI SEÇİMLERİ BAŞLADI! && broadcast &eOyunuzu vermek için sandığa gidiniz veya &a/oy <aday> &eyazınız! && broadcast &e&l======================================== && title @a title {\"text\":\"👑 CUMHURBAŞKANLIĞI SEÇİMİ!\",\"color\":\"gold\",\"bold\":true} && title @a subtitle {\"text\":\"Vatandaşlar sandık başına!\",\"color\":\"yellow\"} && playsound minecraft:ui.toast.challenge_complete master @a",
         "Tüm sunucuda Cumhurbaşkanlığı seçim sürecini başlatır, duyuru geçer ve oyuncuları oy vermeye davet eder"),

        ("🏡 Köy Muhtarlığı Seçimlerini Başlat",
         "broadcast &e&l======================================== && broadcast &6&l🏡 RESMİ KÖY MUHTARLIĞI SEÇİMLERİ BAŞLADI! && broadcast &eKöyünüzün yeni Muhtarını seçmek için &a/oy <aday> &eyazınız! && broadcast &e&l======================================== && title @a title {\"text\":\"🏡 MUHTARLIK SEÇİMİ!\",\"color\":\"green\",\"bold\":true} && title @a subtitle {\"text\":\"Köyün yeni Muhtarını seçin!\",\"color\":\"yellow\"} && playsound minecraft:entity.player.levelup master @a",
         "Köy Muhtarlığı seçimlerini başlatır, /oy komutunu hatırlatır"),

        ("🗳️ Seçim Sandığı & Oy Kabini İnşa Et",
         "execute at {p} run fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 smooth_stone && execute at {p} run fill ~-2 ~ ~-2 ~2 ~3 ~2 air && execute at {p} run fill ~-2 ~ ~-2 ~2 ~2 ~2 dark_oak_planks outline && execute at {p} run fill ~-1 ~ ~-2 ~1 ~1 ~-2 air && execute at {p} run setblock ~ ~ ~ barrel && execute at {p} run setblock ~ ~1 ~ oak_wall_sign[facing=south]{front_text:{messages:['{\"text\":\"🗳️ SEÇİM SANDIĞI\",\"bold\":true,\"color\":\"dark_blue\"}','{\"text\":\"Oyları buraya\",\"color\":\"black\"}','{\"text\":\"bırakınız.\",\"color\":\"black\"}','{\"text\":\"Gizli Oy Açık Tasnif\",\"color\":\"dark_red\"}']}} && execute at {p} run setblock ~-1 ~1 ~ torch && execute at {p} run setblock ~1 ~1 ~ torch && playsound minecraft:block.wood.place master {p}",
         "Oyuncunun bulunduğu yere resmi mühürlü Seçim Sandığı (fıçı) ve ahşap Oy Kabini inşa eder"),

        ("📜 Resmi Oy Pusulası & Mühür Dağıt",
         "minecraft:give {p} paper{display:{Name:'{\"text\":\"🗳️ Resmi Seçim Oy Pusulası\",\"color\":\"gold\",\"bold\":true}',Lore:['{\"text\":\"Adayınızın adını üzerine yazıp\",\"color\":\"yellow\"}','{\"text\":\"Seçim Sandığına bırakın veya /oy kullanın.\",\"color\":\"gray\"}']}} 1 && minecraft:give {p} feather{display:{Name:'{\"text\":\"✅ EVET / TERCİH MÜHRÜ\",\"color\":\"green\",\"bold\":true}',Lore:['{\"text\":\"Demokrasinin kutsal mührü.\",\"color\":\"yellow\"}']}} 1",
         "Hedef oyuncuya imzalı seçim pusulası ve EVET mührü verir"),

        ("☀️ Gündüz Olsun mu? Oylaması Başlat",
         "broadcast &8[&eOylama&8] &6Gündüz yapılsın mı? &aEvet için zıplayın, Hayır için eğilin! && playsound minecraft:block.note_block.bell master @a",
         "Halk oylaması ile havanın gündüz yapılması için oylama başlatır"),

        ("🌧️ Güneşli Hava (Yağmur Dursun) Oylaması",
         "broadcast &8[&bOylama&8] &bYağmur dursun mu? &a/weather clear &eyapılsın mı? && playsound minecraft:block.note_block.bell master @a",
         "Yağmurun dindirilmesi için sunucu genelinde oylama başlatır"),

        ("🏆 Seçim Sonucu: {p} Cumhurbaşkanı Seçildi!",
         "team join cumhurbaskani {p} && tab player {p} tabprefix &c&l[Baskan] &e && tab player {p} tagprefix &c&l[Baskan] &e && title @a title {\"text\":\"👑 YENİ CUMHURBAŞKANI SEÇİLDİ!\",\"color\":\"gold\",\"bold\":true} && title @a subtitle {\"text\":\"Tebrikler {p}!\",\"color\":\"yellow\"} && broadcast &8[&4Seçim Sonucu&8] &eHalkın hür iradesiyle &c&l{p} &eyeni &4&lCumhurbaşkanı &eseçilmiştir! Kutlarız! && playsound minecraft:ui.toast.challenge_complete master @a",
         "Seçim sonucunu açıklar, oyuncuyu resmi Cumhurbaşkanı ilan eder ve tabelasını/tagını verir"),

        ("🏡 Seçim Sonucu: {p} Köy Muhtarı Seçildi!",
         "team join muhtar {p} && tab player {p} tabprefix &6&l[Muhtar] &f && tab player {p} tagprefix &6&l[Muhtar] &f && title @a title {\"text\":\"🏡 YENİ KÖY MUHTARI SEÇİLDİ!\",\"color\":\"green\",\"bold\":true} && title @a subtitle {\"text\":\"Tebrikler {p}!\",\"color\":\"yellow\"} && broadcast &8[&6Seçim Sonucu&8] &eKöy halkının oylarıyla &6&l{p} &eyeni &a&lKöy Muhtarı &eseçilmiştir! && playsound minecraft:entity.player.levelup master @a",
         "Seçim sonucunu açıklar, oyuncuyu resmi Köy Muhtarı ilan eder"),

        ("🎁 Tüm Vatandaşlara 500 Akçe Seçim Teşvik Yardımı",
         "eco give @a 500 && broadcast &a[Hazine] Seçimlere katılan tüm vatandaşlarımızın hesabına 500 Akçe yatırılmıştır! && playsound minecraft:entity.experience_orb.pickup master @a",
         "Tüm online oyuncuların banka hesabına 500 Akçe seçim katılım ödülü aktarır"),

        ("🔒 Seçimleri Tamamla & Sandıkları Kilitle",
         "broadcast &c&l[SEÇİM] Oy verme süresi sona ermiştir. Sandıklar kilitlenmiştir! && playsound minecraft:block.chest.locked master @a",
         "Seçimleri resmen kapatır ve sandıkları mühürler")
    ],

    # -------------------------------------------------------------------------
    # 21. AİRDROP & GÖKTEN KASA EVENTİ
    # -------------------------------------------------------------------------
    "🪂 AİRDROP & GÖKTEN KASA": [
        ("🪂 Hedef Konuma Airdrop İndir (İşaret Fişeği + Lüks Sandık)",
         "execute at {p} run setblock ~ ~-1 ~ beacon && execute at {p} run fill ~-1 ~-2 ~-1 ~1 ~-2 ~1 iron_block && execute at {p} run setblock ~ ~ ~ barrel{CustomName:'{\"text\":\"🪂 EFSANEVİ AİRDROP KASASI\",\"color\":\"gold\",\"bold\":true}',Items:[{Slot:0b,id:\"diamond_block\",Count:16b},{Slot:1b,id:\"netherite_ingot\",Count:8b},{Slot:2b,id:\"golden_apple\",Count:32b},{Slot:3b,id:\"totem_of_undying\",Count:2b},{Slot:4b,id:\"emerald_block\",Count:32b},{Slot:5b,id:\"experience_bottle\",Count:64b}]} && execute at {p} run summon firework_rocket ~ ~2 ~ {FireworksItem:{id:\"firework_rocket\",Count:1,tag:{Fireworks:{Flight:2,Explosions:[{Type:1,Flicker:1,Trail:1,Colors:[I;16711680,16766720],FadeColors:[I;16777215]}]}}}} && broadcast &e&l======================================== && broadcast &c&l🪂 [AİRDROP] GÖKTEN ZENGİNLİK KASASI DÜŞTÜ! && broadcast &6📍 Işın sütunu ve havai fişekler patlatıldı! İlk açan ganimeti kapar! && broadcast &e&l======================================== && playsound minecraft:ui.toast.challenge_complete master @a",
         "Hedef oyuncunun yanına ışın sütunu ve içinde 16 elmas blok, 8 netherite ve 32 altın elma olan Airdrop kasası indirir"),

        ("💥 Küçük Hızlı Airdrop Düşür (Hazine Sandığı)",
         "execute at {p} run setblock ~ ~ ~ chest{CustomName:'{\"text\":\"🎁 HIZLI AİRDROP\",\"color\":\"aqua\",\"bold\":true}',Items:[{Slot:0b,id:\"diamond\",Count:32b},{Slot:1b,id:\"emerald\",Count:64b},{Slot:2b,id:\"iron_ingot\",Count:64b},{Slot:3b,id:\"cooked_beef\",Count:64b}]} && execute at {p} run summon firework_rocket ~ ~1 ~ && broadcast &b[Airdrop] Yakınına hızlı yardım sandığı indi! && playsound minecraft:entity.player.levelup master {p}",
         "Oyuncunun hemen önüne orta boy elmas ve zümrüt airdrop sandığı bırakır"),

        ("💎 5.000 Akçe Airdrop Hediye Çeki Bırak",
         "minecraft:give {p} paper{display:{Name:'{\"text\":\"💰 5.000 AKÇE AİRDROP ÇEKİ\",\"color\":\"gold\",\"bold\":true}',Lore:['{\"text\":\"Bankaya götürerek veya admin\",\"color\":\"yellow\"}','{\"text\":\"paneli ile 5000 Akçeye çevrilir!\",\"color\":\"gray\"}']}} 1 && playsound minecraft:entity.experience_orb.pickup master {p}",
         "Hedef oyuncuya resmi airdrop altın hediye çeki verir"),

        ("🎆 Devasa Airdrop Kutlama Şovu Başlat",
         "execute at {p} run summon firework_rocket ~ ~1 ~ {FireworksItem:{id:\"firework_rocket\",Count:1,tag:{Fireworks:{Flight:3,Explosions:[{Type:2,Colors:[I;16711680,65280,255]}]}}}} && execute at {p} run summon firework_rocket ~3 ~1 ~ {FireworksItem:{id:\"firework_rocket\",Count:1,tag:{Fireworks:{Flight:2,Explosions:[{Type:1,Colors:[I;16776960]}]}}}} && broadcast &a[Airdrop] Gökyüzünde kutlama fişekleri patlatıldı! && playsound minecraft:entity.firework_rocket.blast master @a",
         "Renkli gökyüzü havai fişekleri fırlatır"),

        ("🎁 Tüm Sunucuya Airdrop Katılım Bonusu (+500 Akçe)",
         "eco give @a 500 && broadcast &6[Airdrop] Tüm vatandaşlarımıza 500 Akçe etkinlik primi dağıtıldı! && playsound minecraft:entity.player.levelup master @a",
         "Sunucudaki herkese 500 Akçe etkinlik bonusu verir")
    ],

    # -------------------------------------------------------------------------
    # 22. BOSS ZİNDANI & KANLI AY EVENTİ
    # -------------------------------------------------------------------------
    "⚔️ BOSS ZİNDANI & KANLI AY": [
        ("🩸 KANLI AY EVENTİ BAŞLAT (Zombiler Güçlenir)",
         "time set 18000 && weather thunder && broadcast &4&l======================================== && broadcast &c&l🩸 [KANLI AY] GÖKYÜZÜ KAN KIZILINA BÜRÜNDÜ! && broadcast &4Tüm zombiler ve canavarlar uyandı! Kendinizi koruyun! && broadcast &4&l======================================== && title @a title {\"text\":\"🩸 KANLI AY BAŞLADI!\",\"color\":\"dark_red\",\"bold\":true} && title @a subtitle {\"text\":\"Sığınaklarınıza çekilin!\",\"color\":\"red\"} && playsound minecraft:entity.wither.spawn master @a",
         "Geceyi kan kırmızısı yapar, yıldırımlar düşürür ve tüm oyunculara acil savunma alarmı çalar"),

        ("☀️ Kanlı Ayı Sonlandır & Güneş Doğsun",
         "time set day && weather clear && broadcast &a&l[HUZUR] Kanlı Ay sona erdi. Güneş yeniden doğdu! && title @a title {\"text\":\"☀️ GÜNEŞ DOĞDU\",\"color\":\"gold\",\"bold\":true} && playsound minecraft:ui.toast.challenge_complete master @a",
         "Kanlı Ayı bitirir, gökyüzünü açar ve güneşi doğurur"),

        ("🏰 Antik Boss Zindanı İnşa Et (11x11 Taş Tapınak)",
         "execute at {p} run fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 mossy_stone_bricks && execute at {p} run fill ~-5 ~ ~-5 ~5 ~4 ~5 cracked_stone_bricks outline && execute at {p} run fill ~-4 ~ ~-4 ~4 ~3 ~4 air && execute at {p} run fill ~-1 ~ ~-5 ~1 ~2 ~-5 iron_bars && execute at {p} run setblock ~ ~ ~ spawner{SpawnData:{entity:{id:\"minecraft:zombie\"}}} && execute at {p} run setblock ~ ~ ~ chest{CustomName:'{\"text\":\"🏆 ZİNDAN HAZİNESİ\",\"color\":\"gold\",\"bold\":true}',Items:[{Slot:0b,id:\"diamond\",Count:32b},{Slot:1b,id:\"netherite_scrap\",Count:4b},{Slot:2b,id:\"enchanted_golden_apple\",Count:4b}]} && execute at {p} run setblock ~-4 ~2 ~-4 soul_torch && execute at {p} run setblock ~4 ~2 ~4 soul_torch && playsound minecraft:block.stone.place master {p}",
         "Oyuncunun bulunduğu yere yosunlu taşlardan antik bir zindan odası, spawner ve hazine sandığı inşa eder"),

        ("👑 Zindan Lordu Boss'u Çağır (Netherite Zırhlı & Keskin Kılıç)",
         "execute at {p} run summon zombie ~ ~ ~ {CustomName:'{\"text\":\"👑 ZİNDAN LORDU (BOSS)\",\"color\":\"dark_red\",\"bold\":true}',CustomNameVisible:1b,Health:150f,Attributes:[{Name:\"generic.max_health\",Base:150f},{Name:\"generic.attack_damage\",Base:12f},{Name:\"generic.movement_speed\",Base:0.32f}],HandItems:[{id:\"netherite_sword\",Count:1b,tag:{Enchantments:[{id:\"sharpness\",lvl:5s}]}},{}],ArmorItems:[{id:\"netherite_boots\",Count:1b},{id:\"netherite_leggings\",Count:1b},{id:\"netherite_chestplate\",Count:1b},{id:\"diamond_helmet\",Count:1b}]} && broadcast &4[BOSS] Zindan Lordu uyandı! && playsound minecraft:entity.ender_dragon.growl master @a",
         "150 cana sahip, özel zırhlı ve elmas miğferli güçlü bir zindan bossu çağırır"),

        ("🧟 Elit Zombi Baskını Çağır (6 Zombi)",
         "execute at {p} run summon zombie ~2 ~ ~ {HandItems:[{id:\"iron_sword\",Count:1b},{}]} && execute at {p} run summon zombie ~-2 ~ ~ {HandItems:[{id:\"iron_sword\",Count:1b},{}]} && execute at {p} run summon zombie ~ ~ ~2 {HandItems:[{id:\"iron_axe\",Count:1b},{}]} && execute at {p} run summon zombie ~ ~ ~-2 && playsound minecraft:entity.zombie.ambient master {p}",
         "Hedef oyuncunun etrafına 4 silahlı zombi muhafız çağırır"),

        ("🏹 Alevli İskelet Okçu Timi Çağır",
         "execute at {p} run summon skeleton ~3 ~ ~ {HandItems:[{id:\"bow\",Count:1b,tag:{Enchantments:[{id:\"flame\",lvl:1s}]}},{}]} && execute at {p} run summon skeleton ~-3 ~ ~ {HandItems:[{id:\"bow\",Count:1b,tag:{Enchantments:[{id:\"power\",lvl:3s}]}},{}]} && playsound minecraft:entity.skeleton.ambient master {p}",
         "Alev okları atan 2 iskelet nişancı çağırır"),

        ("🏆 Zindan Zaferi & Boss Ödülü (+2.000 Akçe)",
         "eco give @a 2000 && broadcast &6&l🏆 [ZAFER] Zindan Boss'u devrildi! Tüm savaşçılara 2.000 Akçe ödül verildi! && playsound minecraft:ui.toast.challenge_complete master @a",
         "Boss'u yenen tüm oyunculara 2.000 Akçe zafer ödülü dağıtır")
    ],

    # -------------------------------------------------------------------------
    # 23. KLANLAR & KRALLIK SAVAŞLARI
    # -------------------------------------------------------------------------
    "🏰 KLANLAR & KRALLIK SAVAŞLARI": [
        ("🚩 Kızıl Bayrak Klanını Kur",
         "team add klan_kizil \"Kızıl Bayrak Klanı\" && team modify klan_kizil prefix \"&c[Kızıl] \" && team modify klan_kizil color red && team modify klan_kizil friendlyFire false && broadcast &c[Klan] Kızıl Bayrak Klanı resmen kuruldu! && playsound minecraft:entity.player.levelup master @a",
         "Kızıl Bayrak adında kırmızı renkli ve dost ateşi kapalı bir klan kurar"),

        ("🐺 Kurtlar Hanedanı Klanını Kur",
         "team add klan_kurtlar \"Kurtlar Hanedanı\" && team modify klan_kurtlar prefix \"&6[Kurtlar] \" && team modify klan_kurtlar color gold && team modify klan_kurtlar friendlyFire false && broadcast &6[Klan] Kurtlar Hanedanı klanı kuruldu! && playsound minecraft:entity.player.levelup master @a",
         "Altın sarısı renkli Kurtlar Hanedanı klanını kurar"),

        ("🦅 Kartal Krallığı Klanını Kur",
         "team add klan_kartal \"Kartal Krallığı\" && team modify klan_kartal prefix \"&9[Kartal] \" && team modify klan_kartal color blue && team modify klan_kartal friendlyFire false && broadcast &9[Klan] Kartal Krallığı klanı kuruldu! && playsound minecraft:entity.player.levelup master @a",
         "Mavi renkli Kartal Krallığı klanını kurar"),

        ("➕ {p} Oyuncusunu Kızıl Bayrak Klanına Ekle",
         "team join klan_kizil {p} && broadcast &c[Klan] {p} Kızıl Bayrak klanına katıldı! && playsound minecraft:entity.experience_orb.pickup master {p}",
         "Seçili oyuncuyu Kızıl Bayrak klanına üye yapar"),

        ("➕ {p} Oyuncusunu Kurtlar Hanedanına Ekle",
         "team join klan_kurtlar {p} && broadcast &6[Klan] {p} Kurtlar Hanedanına katıldı! && playsound minecraft:entity.experience_orb.pickup master {p}",
         "Seçili oyuncuyu Kurtlar Hanedanına üye yapar"),

        ("➕ {p} Oyuncusunu Kartal Krallığına Ekle",
         "team join klan_kartal {p} && broadcast &9[Klan] {p} Kartal Krallığına katıldı! && playsound minecraft:entity.experience_orb.pickup master {p}",
         "Seçili oyuncuyu Kartal Krallığına üye yapar"),

        ("❌ {p} Oyuncusunu Klandan Çıkar",
         "team leave {p} && broadcast &7[Klan] {p} klanından ayrıldı. && playsound minecraft:block.anvil.land master {p}",
         "Oyuncuyu bulunduğu klandan çıkarır"),

        ("⚔️ BÜYÜK KLAN SAVAŞI BAŞLAT! (PvP Meydanı)",
         "broadcast &4&l======================================== && broadcast &c&l⚔️ KRALLIKLAR ARASI BÜYÜK KLAN SAVAŞI BAŞLADI! && broadcast &eTüm klanlar PvP Arenasında kozlarını paylaşıyor! && broadcast &4&l======================================== && title @a title {\"text\":\"⚔️ KLAN SAVAŞI BAŞLADI!\",\"color\":\"red\",\"bold\":true} && playsound minecraft:entity.ender_dragon.growl master @a",
         "Sunucu genelinde klanlar arası büyük meydan savaşı başlatır"),

        ("💰 Klan Hazinesi Bonusu Ver (+10.000 Akçe)",
         "eco give {p} 10000 && broadcast &e[Hazine] {p} klan hazinesine 10.000 Akçe aktarıldı! && playsound minecraft:entity.player.levelup master {p}",
         "Klan liderine klanı büyütmesi için 10.000 Akçe verir")
    ],

    # -------------------------------------------------------------------------
    # 24. HOLOGRAMLAR & LİDERLİK TABLOSU
    # -------------------------------------------------------------------------
    "🏆 HOLOGRAMLAR & LİDERLİK TABLOSU": [
        ("🏆 Liderlik Kürsüsü Hologramını Buraya Taşı",
         "execute at {p} run dh movehere liderlik_tablosu && playsound minecraft:entity.player.levelup master {p}",
         "En zengin oyuncular liderlik tablosunu hedef oyuncunun tam karşısına taşır"),

        ("📜 Sunucu Rehber Hologramını Buraya Taşı",
         "execute at {p} run dh movehere spawn_rehber && playsound minecraft:entity.player.levelup master {p}",
         "Sunucu kuralları ve başlangıç rehberi hologramını hedef oyuncunun yanına taşır"),

        ("🔄 Tüm Hologramları Yenile (/dh reload)",
         "dh reload && playsound minecraft:entity.experience_orb.pickup master {p}",
         "DecentHolograms eklentisini ve canlı tabloları günceller"),

        ("✨ Günlük Görevler & Ödül Dağıt (+500 Akçe & 5 Elmas)",
         "eco give {p} 500 && minecraft:give {p} diamond 5 && minecraft:give {p} cooked_beef 32 && broadcast &a[Görev] {p} bugünkü görevlerini tamamlayıp ödülünü aldı! && playsound minecraft:ui.toast.challenge_complete master {p}",
         "Hedef oyuncuya günlük görev ödül paketini (+500 Akçe, 5 Elmas, 32 Pişmiş Biftek) verir"),

        ("🌟 Tüm Sunucuya Görev Teşvik Bonusu Dağıt (+250 Akçe)",
         "eco give @a 250 && broadcast &e[Görevler] Günlük görevlere katılan tüm oyunculara 250 Akçe prim dağıtıldı! && playsound minecraft:entity.experience_orb.pickup master @a",
         "Online olan herkese 250 Akçe görev tamamlama primi dağıtır")
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
        self._check_initial_rcon()

    def _check_initial_rcon(self):
        def _worker():
            if self.rcon and self.rcon.connect():
                self.parent.after(0, lambda: self.lbl_server_status.configure(text="🟢 Sunucu ve RCON Aktif! (25565 / 25575)", fg="#34d399"))
            else:
                self.parent.after(0, lambda: self.lbl_server_status.configure(text="🔴 Sunucu: Beklemede | RCON: Bağlı Değil", fg="#f87171"))
        threading.Thread(target=_worker, daemon=True).start()

    def _init_rcon(self):
        cfg = self.config_manager.get_server_config()
        self.rcon = MinecraftRcon(
            host=cfg.get("rcon_host", "127.0.0.1"),
            port=cfg.get("rcon_port", 25575),
            password=cfg.get("rcon_password", "admin123")
        )

    def _build_ui(self):
        # 0. CANLI SUNUCU & RCON KONTROL ÇUBUĞU
        srv_bar = tk.Frame(self.frame, bg="#0b1120", height=38, padx=12, pady=4)
        srv_bar.pack(fill=tk.X, side=tk.TOP)

        self.lbl_server_status = tk.Label(srv_bar, text="🔴 Sunucu: Beklemede | RCON: Bağlı Değil", font=("Segoe UI", 8, "bold"), fg="#f87171", bg="#0b1120")
        self.lbl_server_status.pack(side=tk.LEFT, padx=(0, 10))

        self.btn_srv_start = tk.Button(srv_bar, text="🚀 Sunucuyu Başlat", font=("Segoe UI", 8, "bold"), bg=ACCENT_GREEN, fg="#000", relief=tk.FLAT, padx=8, command=self._start_server)
        self.btn_srv_start.pack(side=tk.LEFT, padx=3)

        self.btn_srv_stop = tk.Button(srv_bar, text="⏹️ Sunucuyu Durdur", font=("Segoe UI", 8, "bold"), bg="#dc2626", fg="#fff", relief=tk.FLAT, padx=8, command=self._stop_server)
        self.btn_srv_stop.pack(side=tk.LEFT, padx=3)

        self.btn_srv_restart = tk.Button(srv_bar, text="🔄 Yeniden Başlat", font=("Segoe UI", 8, "bold"), bg="#d97706", fg="#fff", relief=tk.FLAT, padx=8, command=self._restart_server)
        self.btn_srv_restart.pack(side=tk.LEFT, padx=3)

        self.btn_rcon_reconnect = tk.Button(srv_bar, text="🔌 RCON Yenile", font=("Segoe UI", 8, "bold"), bg="#0284c7", fg="#fff", relief=tk.FLAT, padx=8, command=self._reconnect_rcon)
        self.btn_rcon_reconnect.pack(side=tk.LEFT, padx=3)

        self.btn_list_players = tk.Button(srv_bar, text="👥 Oyuncu Listesi", font=("Segoe UI", 8, "bold"), bg="#6366f1", fg="#fff", relief=tk.FLAT, padx=8, command=self._list_players)
        self.btn_list_players.pack(side=tk.LEFT, padx=3)

        # 1. HEDEF, ROL & ADET ŞERİDİ
        ribbon = tk.Frame(self.frame, bg="#0d1424", height=44, padx=12, pady=4)
        ribbon.pack(fill=tk.X, side=tk.TOP)

        tk.Label(ribbon, text="🎯 Hedef:", font=("Segoe UI", 9, "bold"), fg=TEXT_COLOR, bg="#0d1424").pack(side=tk.LEFT, padx=(0, 4))
        self.player_var = tk.StringVar(value="@p")
        self.player_entry = ttk.Combobox(ribbon, textvariable=self.player_var, font=("Segoe UI", 9, "bold"), width=15, values=["@p", "@a", "@r"])
        self.player_entry.pack(side=tk.LEFT, padx=(0, 2))

        btn_refresh_p = tk.Button(
            ribbon,
            text="🔄",
            font=("Segoe UI", 8, "bold"),
            bg="#1e293b",
            fg="#38bdf8",
            activebackground="#334155",
            activeforeground="#38bdf8",
            relief=tk.FLAT,
            padx=5,
            pady=1,
            command=lambda: threading.Thread(target=self.update_player_dropdown, daemon=True).start()
        )
        btn_refresh_p.pack(side=tk.LEFT, padx=(0, 8))

        tk.Label(ribbon, text="🔢 Adet:", font=("Segoe UI", 9, "bold"), fg=TEXT_COLOR, bg="#0d1424").pack(side=tk.LEFT, padx=(0, 4))
        self.qty_var = tk.StringVar(value="64")
        self.qty_entry = ttk.Combobox(ribbon, textvariable=self.qty_var, font=("Segoe UI", 9, "bold"), width=5, values=["1", "16", "32", "64", "128", "256", "576"])
        self.qty_entry.pack(side=tk.LEFT, padx=(0, 8))

        # Hızlı Rol Verme Bölümü
        tk.Label(ribbon, text="🎭 Rol:", font=("Segoe UI", 9, "bold"), fg=ACCENT_GOLD, bg="#0d1424").pack(side=tk.LEFT, padx=(2, 4))
        self.roles_dict = {
            "👑 Cumhurbaşkanı": ("cumhurbaskani", "&c&l[Baskan] &e", "👑 CUMHURBAŞKANI SEÇİLDİNİZ!"),
            "🏡 Köy Muhtarı": ("muhtar", "&6&l[Muhtar] &f", "🏡 KÖY MUHTARI OLDUNUZ!"),
            "👮 Polis Memuru": ("polis", "&9&l[Polis] &b", "👮 POLİS MEMURU OLDUNUZ!"),
            "🪖 Asker & Komutan": ("asker", "&2&l[Asker] &a", "🪖 ASKER OLDUNUZ!"),
            "🩺 Doktor / Hekim": ("doktor", "&c&l[Doktor] &f", "🩺 DOKTOR OLDUNUZ!"),
            "⚖️ Ağır Ceza Hakimi": ("hakim", "&5&l[Hakim] &d", "⚖️ HAKİM OLDUNUZ!"),
            "🏗️ Baş Mimar": ("mimar", "&3&l[Mimar] &b", "🏗️ BAŞ MİMAR OLDUNUZ!"),
            "💰 Büyük Tüccar": ("tuccar", "&e&l[Tuccar] &6", "💰 BÜYÜK TÜCCAR OLDUNUZ!"),
            "⛏️ Usta Madenci": ("madenci", "&8&l[Madenci] &7", "⛏️ MADENCİ OLDUNUZ!"),
            "🌾 Baş Çiftçi": ("ciftci", "&a&l[Ciftci] &2", "🌾 ÇİFTÇİ OLDUNUZ!"),
            "⚔️ Kraliyet Şövalyesi": ("sovalye", "&1&l[Sovalye] &9", "⚔️ KRALİYET ŞÖVALYESİ OLDUNUZ!"),
            "👑 Kurucu / Kral": ("kurucu", "&4&l[Kurucu] &c", "👑 SUNUCU KURUCUSU / KRAL!"),
            "❌ Vatandaş (Sıfırla)": ("vatandas", "&7[Vatandas] &f", "Standart Vatandaş")
        }
        self.role_var = tk.StringVar(value=list(self.roles_dict.keys())[0])
        self.role_combo = ttk.Combobox(
            ribbon,
            textvariable=self.role_var,
            font=("Segoe UI", 8, "bold"),
            width=15,
            values=list(self.roles_dict.keys()),
            state="readonly"
        )
        self.role_combo.pack(side=tk.LEFT, padx=(0, 2))

        btn_assign_role = tk.Button(
            ribbon,
            text="👑 Rolü Ata",
            font=("Segoe UI", 8, "bold"),
            bg="#f59e0b",
            fg="#000000",
            relief=tk.FLAT,
            padx=6,
            pady=1,
            command=self.assign_selected_role
        )
        btn_assign_role.pack(side=tk.LEFT, padx=(0, 8))

        tk.Label(ribbon, text="🔍 Arama:", font=("Segoe UI", 9, "bold"), fg=ACCENT_CYAN, bg="#0d1424").pack(side=tk.LEFT, padx=(0, 4))
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self._on_search_change)
        search_entry = tk.Entry(ribbon, textvariable=self.search_var, font=("Segoe UI", 9), bg=BG_CARD, fg="#ffffff", relief=tk.FLAT, width=12)
        search_entry.pack(side=tk.LEFT, padx=(0, 6), ipady=2)

        btn_heal = tk.Button(ribbon, text="💖 Can Fulle", font=("Segoe UI", 8, "bold"), bg="#0284c7", fg="white", relief=tk.FLAT, padx=6, command=lambda: self.run_template("effect give {p} instant_health 1 255 true && effect give {p} saturation 1 255 true"))
        btn_heal.pack(side=tk.LEFT, padx=2)

        btn_buff = tk.Button(ribbon, text="⚡ ULTRA BUFF", font=("Segoe UI", 8, "bold"), bg="#7c3aed", fg="white", relief=tk.FLAT, padx=6, command=lambda: self.run_template("effect give {p} resistance 99999 5 true && effect give {p} strength 99999 100 true && effect give {p} speed 99999 3 true && effect give {p} haste 99999 255 true && effect give {p} night_vision 99999 0 true && effect give {p} saturation 99999 255 true"))
        btn_buff.pack(side=tk.LEFT, padx=2)

        btn_box = tk.Button(ribbon, text="📦 3'LÜ MASTER KİT", font=("Segoe UI", 8, "bold"), bg="#b45309", fg="white", relief=tk.FLAT, padx=6, command=lambda: self.run_template(CMD_COMBO_FULL))
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

    def _start_server(self):
        cfg = self.config_manager.get_server_config()
        sdir = cfg.get("server_dir", os.path.join(os.getcwd(), "server"))
        bat_path = os.path.join(sdir, "start.bat")

        if not os.path.exists(sdir):
            os.makedirs(sdir, exist_ok=True)

        if not os.path.exists(bat_path):
            self.log(f"[Uyarı] {bat_path} bulunamadı. Lütfen önce 'Kurulum' sekmesinden sunucunuzu kurunuz.\n", "err")
            return

        self.lbl_server_status.configure(text="🟡 Sunucu Başlatılıyor...", fg="#fbbf24")
        self.log(f"[Sistem] Sunucu başlatılıyor ({bat_path})...\n", "cmd")

        try:
            if sys.platform == "win32":
                subprocess.Popen(["cmd.exe", "/c", "start", "Minecraft Server", bat_path], cwd=sdir)
            else:
                subprocess.Popen(["bash", bat_path], cwd=sdir)
            self._poll_rcon_auto()
        except Exception as e:
            self.log(f"[Hata] Sunucu başlatılamadı: {e}\n", "err")
            self.lbl_server_status.configure(text="🔴 Başlatma Hatası", fg="#ef4444")

    def _poll_rcon_auto(self, max_attempts=45):
        def _poll():
            for _ in range(max_attempts):
                time.sleep(2)
                if self.rcon and self.rcon.connect():
                    self.parent.after(0, self._on_server_ready)
                    return
            self.parent.after(0, lambda: self.lbl_server_status.configure(text="🟡 Sunucu Açık (RCON bekleniyor)", fg="#fbbf24"))

        threading.Thread(target=_poll, daemon=True).start()

    def _on_server_ready(self):
        self.lbl_server_status.configure(text="🟢 Sunucu ve RCON Aktif! (25565 / 25575)", fg="#34d399")
        self.log("======================================================\n", "ok")
        self.log("[Sistem] ✅ Minecraft Sunucusu ve RCON başarıyla bağlandı!\n", "ok")
        self.log("Artık tüm admin butonlarını ve komutları sorunsuz kullanabilirsiniz.\n", "ok")
        self.log("======================================================\n", "ok")

    def _stop_server(self):
        self.log("[Sistem] Sunucu durdurma komutu gönderiliyor (/stop)...\n", "cmd")
        def _worker():
            resp = self.rcon.send_command("stop")
            self.parent.after(0, self.log, f"[Yanıt] {resp}\n", "ok")
            self.parent.after(0, lambda: self.lbl_server_status.configure(text="🔴 Sunucu: Kapalı", fg="#f87171"))
        threading.Thread(target=_worker, daemon=True).start()

    def _restart_server(self):
        self.log("[Sistem] Sunucu yeniden başlatılıyor...\n", "cmd")
        def _worker():
            self.rcon.send_command("stop")
            time.sleep(4)
            self.parent.after(0, self._start_server)
        threading.Thread(target=_worker, daemon=True).start()

    def _reconnect_rcon(self):
        self.log("[Sistem] RCON bağlantısı test ediliyor...\n", "cmd")
        def _worker():
            if self.rcon and self.rcon.connect():
                self.parent.after(0, lambda: self.lbl_server_status.configure(text="🟢 RCON Bağlandı ✔", fg="#34d399"))
                self.parent.after(0, self.log, "[Sistem] ✅ RCON bağlantısı başarılı!\n", "ok")
            else:
                self.parent.after(0, lambda: self.lbl_server_status.configure(text="🔴 RCON Bağlantısı Yok", fg="#f87171"))
                self.parent.after(0, self.log, "[Sistem] ❌ RCON portuna (25575) bağlanılamadı. Sunucu kapalı veya başlatılıyor olabilir.\n", "err")
        threading.Thread(target=_worker, daemon=True).start()

    def _list_players(self):
        self.run_template("list")

    def assign_selected_role(self):
        target = self.player_var.get().strip() or "@p"
        role_label = self.role_var.get()
        if not target or role_label not in getattr(self, "roles_dict", {}):
            return
        team_name, prefix, title_text = self.roles_dict[role_label]
        cmd = f"team join {team_name} {target} && tab player {target} tabprefix {prefix} && tab player {target} tagprefix {prefix} && title {target} title {{\"text\":\"{title_text}\",\"color\":\"gold\",\"bold\":true}} && broadcast &8[&6Devlet&8] &e{target} &fartık resmi &6{role_label}&f makamına atandı! && playsound minecraft:ui.toast.challenge_complete master @a"
        self.log(f">> [Rol Atandı] {target} -> {role_label}\n", "ok")
        self.run_template(cmd)

    def update_player_dropdown(self):
        """
        usercache.json ve aktif sunucudaki tüm oyuncuları dinamik olarak çeker ve hedef açılır listesine ekler.
        """
        import json
        import re
        all_players = set()
        online_players = []

        cfg = self.config_manager.get_server_config()
        sdir = cfg.get("server_dir", os.path.join(os.getcwd(), "server"))

        # 1. usercache.json'dan kayıtlı tüm oyuncuları oku
        cache_file = os.path.join(sdir, "usercache.json")
        if os.path.exists(cache_file):
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for entry in data:
                        p_name = entry.get("name")
                        if p_name and re.match(r'^[a-zA-Z0-9_]{3,16}$', p_name):
                            all_players.add(p_name)
            except Exception:
                pass

        # 2. RCON üzerinden aktif oyuncuları sorgula
        try:
            res = self.rcon.send_command("minecraft:list")
            if not res or "online" not in res.lower():
                res = self.rcon.send_command("list")
            if res:
                words = re.findall(r'[a-zA-Z0-9_]{3,16}', res)
                ignore = {"there", "are", "players", "online", "max", "sunucuda", "aktif", "oyuncu", "cevrimici", "default", "kurucu", "oyuncular"}
                for w in words:
                    if w.lower() not in ignore:
                        all_players.add(w)
                        if w not in online_players:
                            online_players.append(w)
        except Exception:
            pass

        ordered_list = []
        for p in online_players:
            if p not in ordered_list:
                ordered_list.append(p)
        for p in sorted(all_players):
            if p not in ordered_list:
                ordered_list.append(p)
        for s in ["@a", "@p", "@r"]:
            if s not in ordered_list:
                ordered_list.append(s)

        if not ordered_list:
            ordered_list = ["@p", "@a", "@r"]

        def _apply():
            curr = self.player_var.get().strip()
            self.player_entry.configure(values=ordered_list)
            if not curr or curr == "@p":
                first_p = [x for x in ordered_list if not x.startswith("@")]
                if first_p:
                    self.player_var.set(first_p[0])

        self.parent.after(0, _apply)


