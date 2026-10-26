# -*- coding: utf-8 -*-
"""
PyInstaller Build Script for Auto Minecraft Server Maker
Compiles the application into a standalone Windows .exe
"""

import os
import sys
import subprocess

# Ensure UTF-8 output if supported
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def build():
    print("======================================================")
    print("   Building Auto Minecraft Server Maker Executable   ")
    print("======================================================")

    # Ensure pyinstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("[*] PyInstaller not found, installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--name=Auto-Minecraft-Server-Maker",
        "--onefile",
        "--noconsole",
        "--clean",
        "--add-data=ui;ui",
        "--add-data=core;core",
        "main.py"
    ]

    print(f"[*] Running: {' '.join(cmd)}")
    ret = subprocess.call(cmd)
    if ret == 0:
        print("\n[SUCCESS] Build finished successfully! Output: dist/Auto-Minecraft-Server-Maker.exe")
    else:
        print(f"\n[ERROR] Build failed with exit code: {ret}")
        sys.exit(ret)

if __name__ == "__main__":
    build()
