# -*- coding: utf-8 -*-
"""
PyInstaller Build Script for Auto Minecraft Server Maker (v3.6.0 Ultra)
Compiles the application into a standalone Windows .exe with icon and version metadata.
"""

import os
import sys
import shutil
import hashlib
import subprocess

# Ensure UTF-8 output if supported
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def compute_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def build():
    print("======================================================")
    print("   Building Auto Minecraft Server Maker (v4.1.0 Master)")
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
        "--icon=app_icon.ico",
        "--version-file=version_info.txt",
        "--collect-all=customtkinter",
        "--collect-all=PIL",
        "--collect-all=requests",
        "--collect-all=psutil",
        "--collect-all=darkdetect",
        "--hidden-import=PIL._tkinter_finder",
        "--add-data=ui;ui",
        "--add-data=core;core",
        "--add-data=app_icon.ico;.",
        "main.py"
    ]

    print(f"[*] Running PyInstaller with full assets and metadata...")
    ret = subprocess.call(cmd)
    if ret == 0:
        dist_exe = os.path.join("dist", "Auto-Minecraft-Server-Maker.exe")
        versioned_exe = os.path.join("dist", "Auto-Minecraft-Server-Maker-v4.1.0-Master.exe")
        if os.path.exists(dist_exe):
            shutil.copy2(dist_exe, versioned_exe)
            size_mb = os.path.getsize(dist_exe) / (1024 * 1024)
            sha = compute_sha256(dist_exe)
            print("\n" + "=" * 60)
            print("[SUCCESS] Build finished successfully!")
            print(f"  Primary:   {dist_exe} ({size_mb:.2f} MB)")
            print(f"  Versioned: {versioned_exe} ({size_mb:.2f} MB)")
            print(f"  SHA-256:   {sha}")
            print("=" * 60)
    else:
        print(f"\n[ERROR] Build failed with exit code: {ret}")
        sys.exit(ret)

if __name__ == "__main__":
    build()
