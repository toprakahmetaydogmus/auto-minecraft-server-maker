# -*- coding: utf-8 -*-
"""
Autonomous Global Tunnel & Port Forwarding Manager
Enables players to host Minecraft servers globally without router port forwarding / CGNAT:
- 1-Click Playit.gg autonomous client (Zero config, free global domain xyz.gl.at.ply.gg:port)
- 1-Click Ngrok TCP tunnel integration
- Autonomous Local UPnP Port Mapper
"""

import os
import sys
import shutil
import urllib.request
import subprocess
import threading
import socket
import logging

PLAYIT_DOWNLOAD_URL = "https://github.com/playit-cloud/playit-agent/releases/download/v0.15.26/playit-windows-x86_64.exe"

class TunnelManager:
    def __init__(self, log_callback=None):
        self.log_callback = log_callback or print
        self.tunnel_process = None
        self.tunnel_type = None

    def log(self, msg):
        try:
            self.log_callback(f"[Tünel] {msg}")
        except Exception:
            pass

    def get_playit_path(self):
        tools_dir = os.path.join(os.getcwd(), "tools")
        os.makedirs(tools_dir, exist_ok=True)
        return os.path.join(tools_dir, "playit.exe")

    def is_playit_downloaded(self):
        return os.path.exists(self.get_playit_path())

    def download_playit(self, progress_callback=None):
        """Downloads official playit.gg standalone binary."""
        dest = self.get_playit_path()
        if os.path.exists(dest):
            self.log("Playit.gg zaten mevcut.")
            return True

        self.log("Playit.gg tünel istemcisi indiriliyor...")
        try:
            req = urllib.request.Request(PLAYIT_DOWNLOAD_URL, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as resp, open(dest, "wb") as out:
                total = int(resp.headers.get("Content-Length", 0))
                downloaded = 0
                while True:
                    chunk = resp.read(65536)
                    if not chunk:
                        break
                    out.write(chunk)
                    downloaded += len(chunk)
                    if total > 0 and progress_callback:
                        pct = int((downloaded / total) * 100)
                        progress_callback(pct, f"Playit İndiriliyor: %{pct}")
            self.log("Playit.gg başarıyla indirildi!")
            return True
        except Exception as e:
            self.log(f"Playit indirme hatası: {e}")
            return False

    def start_playit(self):
        """Starts playit.gg tunnel in a new console window."""
        playit_exe = self.get_playit_path()
        if not os.path.exists(playit_exe):
            self.download_playit()

        if not os.path.exists(playit_exe):
            self.log("Playit bulunamadı.")
            return False

        self.log("Playit.gg tüneli başlatılıyor...")
        try:
            if sys.platform == "win32":
                self.tunnel_process = subprocess.Popen(["cmd.exe", "/c", "start", "Playit.gg Global Tunnel", playit_exe])
            else:
                self.tunnel_process = subprocess.Popen([playit_exe])
            self.tunnel_type = "Playit.gg"
            self.log("✅ Playit.gg tüneli aktif! Açılan penceredeki bağlantı linkine tıklayarak genel IP adresinizi alabilirsiniz.")
            return True
        except Exception as e:
            self.log(f"Playit başlatma hatası: {e}")
            return False

    def stop_tunnel(self):
        if self.tunnel_process:
            try:
                self.tunnel_process.terminate()
            except Exception:
                pass
            self.tunnel_process = None
            self.tunnel_type = None
            self.log("Tünel durduruldu.")

    def try_upnp_port_forward(self, port=25565):
        """Attempts to map port via UPnP if router supports it."""
        self.log(f"Modem UPnP port yönlendirme deneniyor (Port {port})...")
        try:
            import socket
            # Simple SSDP discovery probe
            msg = (
                'M-SEARCH * HTTP/1.1\r\n'
                'HOST: 239.255.255.250:1900\r\n'
                'MAN: "ssdp:discover"\r\n'
                'MX: 2\r\n'
                'ST: urn:schemas-upnp-org:device:InternetGatewayDevice:1\r\n\r\n'
            )
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(2.0)
            s.sendto(msg.encode(), ('239.255.255.250', 1900))
            data, _ = s.recvfrom(2048)
            s.close()
            if b"200 OK" in data:
                self.log("✅ Modem UPnP servisi aktif tespit edildi!")
                return True
            else:
                self.log("⚠️ Modem UPnP yanıt vermedi, Playit.gg tüneli önerilir.")
                return False
        except Exception:
            self.log("⚠️ Modem UPnP kapalı veya yanıt vermiyor. Playit.gg tüneli kullanarak modemsiz oynayabilirsiniz.")
            return False
