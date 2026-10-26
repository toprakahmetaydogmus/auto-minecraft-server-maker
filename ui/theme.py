# -*- coding: utf-8 -*-
"""
Modern Cyberpunk / Deep Slate Theme Tokens
"""

import tkinter as tk
from tkinter import ttk

BG_DARK = "#090d16"
BG_PANEL = "#0f172a"
BG_CARD = "#1e293b"
BG_HOVER = "#334155"
BORDER_COLOR = "#334155"
TEXT_COLOR = "#f8fafc"
TEXT_MUTED = "#94a3b8"

ACCENT_CYAN = "#38bdf8"
ACCENT_GREEN = "#10b981"
ACCENT_GOLD = "#f59e0b"
ACCENT_PURPLE = "#a855f7"
ACCENT_RED = "#ef4444"

def apply_global_theme(root):
    root.configure(bg=BG_DARK)
    style = ttk.Style()
    style.theme_use("clam")

    # Notebook Tabs
    style.configure("TNotebook", background=BG_DARK, borderwidth=0)
    style.configure("TNotebook.Tab", background=BG_CARD, foreground=TEXT_COLOR,
                    padding=[12, 6], font=("Segoe UI", 9, "bold"), borderwidth=0)
    style.map("TNotebook.Tab",
              background=[("selected", ACCENT_CYAN), ("active", BG_HOVER)],
              foreground=[("selected", "#000000"), ("active", "#ffffff")])

    # Comboboxes
    style.configure("TCombobox", fieldbackground=BG_CARD, background=BG_CARD,
                    foreground=TEXT_COLOR, arrowcolor=ACCENT_CYAN, borderwidth=0)

    # Progressbar
    style.configure("Horizontal.TProgressbar", background=ACCENT_CYAN, troughcolor=BG_CARD, borderwidth=0)
