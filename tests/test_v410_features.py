# -*- coding: utf-8 -*-
"""
Automated Comprehensive Test Suite for Auto Minecraft Server Maker v4.1.0 Master
Validates:
1. PluginModHub presets and configuration generators
2. TabAdminPanel 24-category suite, 286+ buttons, and zero-leak privacy
3. ServerInstaller start script and server.properties generation
4. AIEngineer offline diagnostics engine
"""

import os
import sys
import shutil
import tempfile
import unittest

# Add project root to sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from core.plugin_mod_hub import PluginModHub, POPULAR_PLUGINS, SERVER_PRESETS
from core.server_installer import ServerInstaller
from core.ai_engineer import AIEngineer
import ui.tab_admin_panel as admin_panel_module


class TestV410Features(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp(prefix="mc_test_v410_")

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_popular_plugins_structure(self):
        """Validates all plugins have required fields and valid URLs."""
        self.assertGreater(len(POPULAR_PLUGINS), 15)
        for p in POPULAR_PLUGINS:
            self.assertIn("id", p)
            self.assertIn("name", p)
            self.assertIn("category", p)
            self.assertIn("url", p)
            self.assertIn("filename", p)
            self.assertTrue(p["url"].startswith("http"))

    def test_server_presets(self):
        """Validates server presets exist and contain valid plugin IDs."""
        self.assertIn("ultimate_rpg_crossplay", SERVER_PRESETS)
        self.assertIn("safe_crossplay_vanilla", SERVER_PRESETS)
        self.assertIn("hardcore_towny_economy", SERVER_PRESETS)

        plugin_ids = {p["id"] for p in POPULAR_PLUGINS}
        for preset_name, preset in SERVER_PRESETS.items():
            self.assertIn("title", preset)
            self.assertIn("desc", preset)
            for pid in preset.get("plugins", []):
                self.assertIn(pid, plugin_ids, f"Plugin {pid} in preset {preset_name} not found in POPULAR_PLUGINS")

    def test_deploy_turkish_commands(self):
        """Tests deployment of commands.yml with Turkish aliases."""
        hub = PluginModHub(self.test_dir)
        ok = hub.deploy_turkish_commands()
        self.assertTrue(ok)

        cmd_path = os.path.join(self.test_dir, "commands.yml")
        self.assertTrue(os.path.exists(cmd_path))
        with open(cmd_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("hewlp:", content)
        self.assertIn("yardim:", content)
        self.assertIn("takas:", content)
        self.assertIn("arsa:", content)
        self.assertIn("secim:", content)

    def test_deploy_essentials_guide(self):
        """Tests deployment of plugins/Essentials/info.txt multi-chapter book."""
        hub = PluginModHub(self.test_dir)
        ok = hub.deploy_essentials_guide()
        self.assertTrue(ok)

        info_path = os.path.join(self.test_dir, "plugins", "Essentials", "info.txt")
        self.assertTrue(os.path.exists(info_path))
        with open(info_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Chapter: 1", content)
        self.assertIn("Chapter: 5", content)
        self.assertIn("SUNUCU REHBERİ", content)

    def test_configure_antixray_forge(self):
        """Tests generation of config/antixray.toml with engineMode = 3."""
        hub = PluginModHub(self.test_dir)
        ok = hub.configure_antixray_forge()
        self.assertTrue(ok)

        toml_path = os.path.join(self.test_dir, "config", "antixray.toml")
        self.assertTrue(os.path.exists(toml_path))
        with open(toml_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("engineMode = 3", content)
        self.assertIn("diamond_ore", content)

    def test_admin_panel_tabs_and_privacy(self):
        """Validates the 24 tabs, 286+ buttons, and zero-leak privacy."""
        tabs_data = admin_panel_module.TABS_DATA
        self.assertEqual(len(tabs_data), 24, "TABS_DATA must have exactly 24 categories")

        total_buttons = 0
        for tab_name, buttons in tabs_data.items():
            self.assertGreater(len(buttons), 0, f"Tab {tab_name} must have at least one button")
            for item in buttons:
                self.assertEqual(len(item), 3, "Each button entry must be a 3-tuple (name, cmd, desc)")
                btn_name, cmd_tmpl, desc = item
                self.assertTrue(len(btn_name) > 0)
                self.assertTrue(len(cmd_tmpl) > 0)
                # Verify zero-leak privacy: NO hardcoded personal usernames or private LAN/VPN subnets
                for forbidden in ["192.168.", "10.0.", "26.92.", "mirkundaklayan"]:
                    self.assertNotIn(forbidden, cmd_tmpl.lower(), f"Privacy check failed in {btn_name}")
                total_buttons += 1

        self.assertGreaterEqual(total_buttons, 280)

    def test_server_installer_properties_and_start_script(self):
        """Tests generation of optimized server.properties and start.bat."""
        installer = ServerInstaller(self.test_dir)
        installer._write_server_properties(25565, 25575, "secret123")

        props_path = os.path.join(self.test_dir, "server.properties")
        self.assertTrue(os.path.exists(props_path))
        with open(props_path, "r", encoding="utf-8") as f:
            props_content = f.read()
        self.assertIn("view-distance=8", props_content)
        self.assertIn("simulation-distance=6", props_content)
        self.assertIn("server-port=25565", props_content)

        installer._write_start_script("server.jar", 2, 4, "1.20.1")
        bat_path = os.path.join(self.test_dir, "start.bat")
        self.assertTrue(os.path.exists(bat_path))
        with open(bat_path, "r", encoding="utf-8") as f:
            bat_content = f.read()
        self.assertIn("-XX:+UseG1GC", bat_content)
        self.assertIn("-Duser.timezone=Europe/Istanbul", bat_content)

    def test_ai_offline_diagnostics(self):
        """Validates AI engineer answers expert queries offline with zero keys."""
        ai = AIEngineer()
        
        # 1. Unsafe test
        resp_unsafe = ai._autonomous_expert_fallback("java 25 ensureclassinitialized crash")
        self.assertIn("sun.misc.Unsafe", resp_unsafe)
        self.assertIn("Java 17", resp_unsafe)

        # 2. Xray test
        resp_xray = ai._autonomous_expert_fallback("anti xray calismiyor")
        self.assertIn("antixray-forge", resp_xray)
        self.assertIn("engineMode = 3", resp_xray)

        # 3. Trade test
        resp_trade = ai._autonomous_expert_fallback("takas sistemi ve bakiye")
        self.assertIn("PlaceholderAPI", resp_trade)
        self.assertIn("200ms", resp_trade)

        # 4. Crossplay test
        resp_geyser = ai._autonomous_expert_fallback("bedrock geyser sunucuya baglanamiyor")
        self.assertIn("Geyser-Spigot", resp_geyser)
        self.assertIn("Floodgate", resp_geyser)


if __name__ == "__main__":
    unittest.main()
