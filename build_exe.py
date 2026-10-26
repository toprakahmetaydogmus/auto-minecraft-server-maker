# -*- coding: utf-8 -*-
"""
PyInstaller Build Script for Auto Minecraft Server Maker
Compiles the application into a standalone Windows .exe
"""

import os
import sys
import subprocess

def build():
    print("======================================================")
    print("   Building Auto Minecraft Server Maker Executable   ")
    print("======================================================")

    # Ensure pyinstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("[*] PyInstaller bulunamadı, yükleniyor...")
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
        print("\n✅ DERLEME BAŞARILI! Çıktı: dist/Auto-Minecraft-Server-Maker.exe")
    else:
        print(f"\n❌ Derleme hatası kodu: {ret}")

if __name__ == "__main__":
    build()
