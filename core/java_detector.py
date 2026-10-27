# -*- coding: utf-8 -*-
"""
Java Environment Detector
Detects installed Java JDK/JRE runtimes and matches them with Minecraft version requirements:
- Minecraft <= 1.16.5: Java 8
- Minecraft 1.17 - 1.17.1: Java 16
- Minecraft 1.18 - 1.20.4: Java 17 (or Java 21 LTS)
- Minecraft 1.20.5+: Java 21
"""

import os
import sys
import re
import subprocess
import logging

class JavaDetector:
    @staticmethod
    def _get_creationflags():
        return 0x08000000 if sys.platform == "win32" else 0

    @staticmethod
    def get_system_java():
        """Checks default 'java' in PATH."""
        try:
            res = subprocess.run(
                ["java", "-version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=5,
                creationflags=JavaDetector._get_creationflags()
            )
            raw = res.stderr or res.stdout
            ver = JavaDetector._parse_version(raw)
            return {"path": "java", "version": ver, "raw": raw.strip()}
        except Exception:
            return None

    @staticmethod
    def find_all_javas():
        """Searches common Windows directories for Java executables."""
        candidates = []
        sys_j = JavaDetector.get_system_java()
        if sys_j:
            candidates.append(sys_j)

        search_dirs = [
            os.environ.get("JAVA_HOME", ""),
            r"C:\Program Files\Java",
            r"C:\Program Files\Eclipse Adoptium",
            r"C:\Program Files\Microsoft",
            r"C:\Program Files\BellSoft",
            r"C:\Program Files\Zulu",
            r"C:\Program Files (x86)\Java",
        ]

        found_paths = set()
        for root in search_dirs:
            if not root or not os.path.exists(root):
                continue
            if os.path.isfile(root) and root.lower().endswith("java.exe"):
                found_paths.add(root)
                continue

            for dirpath, _, filenames in os.walk(root):
                if "java.exe" in [f.lower() for f in filenames]:
                    jpath = os.path.join(dirpath, "java.exe")
                    if jpath not in found_paths:
                        found_paths.add(jpath)

        for p in found_paths:
            try:
                res = subprocess.run(
                    [p, "-version"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=5,
                    creationflags=JavaDetector._get_creationflags()
                )
                raw = res.stderr or res.stdout
                ver = JavaDetector._parse_version(raw)
                candidates.append({"path": p, "version": ver, "raw": raw.strip()})
            except Exception:
                pass

        # Deduplicate by version
        unique = []
        seen = set()
        for c in candidates:
            if c["path"] not in seen:
                seen.add(c["path"])
                unique.append(c)

        return unique

    @staticmethod
    def _parse_version(raw_str):
        # Matches "1.8.0_...", "17.0.2", "21.0.7"
        match = re.search(r'version "(1\.[0-8]|[0-9]+)(\.[0-9]+)*', raw_str)
        if match:
            v = match.group(1)
            if v.startswith("1."):
                return int(v.split(".")[1])
            return int(v)
        return 0

    @staticmethod
    def get_recommended_java_for_mc(mc_version):
        v = str(mc_version).lower().strip()
        # All Beta and Alpha versions require Java 8
        if v.startswith("b") or v.startswith("a") or v.startswith("c") or v.startswith("rd"):
            return 8
        try:
            parts = [int(p) for p in re.findall(r'\d+', v)]
            if len(parts) >= 2:
                major, minor = parts[0], parts[1]
                if major == 1:
                    if minor <= 16:
                        return 8
                    elif minor == 17:
                        return 16
                    elif 18 <= minor <= 20:
                        if minor == 20 and len(parts) >= 3 and parts[2] >= 5:
                            return 21
                        return 17
                    else:
                        return 21
                elif major > 1:
                    return 21
        except Exception:
            pass
        return 17

    @staticmethod
    def get_recommended_java_version(mc_version):
        """Unified alias for get_recommended_java_for_mc."""
        return JavaDetector.get_recommended_java_for_mc(mc_version)

    @staticmethod
    def get_java_download_url(version=21):
        """Returns direct official Eclipse Adoptium Temurin MSI installer URL for Windows x64."""
        if version == 21:
            return "https://api.adoptium.net/v3/installer/latest/21/ga/windows/x64/jdk/hotspot/normal/eclipse"
        elif version == 17:
            return "https://api.adoptium.net/v3/installer/latest/17/ga/windows/x64/jdk/hotspot/normal/eclipse"
        elif version == 8:
            return "https://api.adoptium.net/v3/installer/latest/8/ga/windows/x64/jdk/hotspot/normal/eclipse"
        return "https://adoptium.net/temurin/releases/"

    @staticmethod
    def open_java_download_page(version=21):
        import webbrowser
        url = JavaDetector.get_java_download_url(version)
        webbrowser.open(url)
