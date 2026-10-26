@echo off
title Auto Minecraft Server Maker - EXE Derleyici
chcp 65001 >nul
cls
echo =====================================================================
echo       AUTO MINECRAFT SERVER MAKER - WINDOWS EXE DERLEYICI
echo =====================================================================
echo.
echo [*] Python ortami kontrol ediliyor...
python -m pip install -r requirements.txt
echo.
echo [*] Standalone Tek Dosya EXE Derleniyor...
python build_exe.py
echo.
pause
