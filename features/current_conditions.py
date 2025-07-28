# features/current_conditions.py

import tkinter as tk
from tkinter import ttk

def create_current_conditions_frame(parent):
    frame = tk.Frame(parent, bg="#ffeaf5")

    font_title = ("Courier", 16, "bold")
    font_main = ("Courier", 26, "bold")
    font_info = ("Courier", 12)

    # --- LOCATION ---
    frame.location_label = tk.Label(frame, text="📍 Location", font=font_title, bg="#ffeaf5", fg="#d63384")
    frame.location_label.pack(pady=(20, 5))

    # --- TEMPERATURE ---
    frame.temp_label = tk.Label(frame, text="--°F", font=font_main, bg="#ffeaf5", fg="#000")
    frame.temp_label.pack(pady=(5, 5))

    # --- WEATHER CONDITION ---
    frame.condition_label = tk.Label(frame, text="☁️ Condition", font=font_info, bg="#ffeaf5")
    frame.condition_label.pack(pady=(5, 2))

    # --- HIGH / LOW ---
    frame.high_low_label = tk.Label(frame, text="H: --°F  L: --°F", font=font_info, bg="#ffeaf5")
    frame.high_low_label.pack(pady=(2, 2))

    # --- HUMIDITY ---
    frame.humidity_label = tk.Label(frame, text="💧 Humidity: --%", font=font_info, bg="#ffeaf5")
    frame.humidity_label.pack(pady=(2, 2))

    # --- WIND ---
    frame.wind_label = tk.Label(frame, text="🌬️ Wind: -- mph", font=font_info, bg="#ffeaf5")
    frame.wind_label.pack(pady=(2, 2))

    return frame

def get_emoji(condition):
    condition = condition.lower()
    if "cloud" in condition: return "☁️"
    if "rain" in condition: return "🌧️"
    if "sun" in condition or "clear" in condition: return "☀️"
    if "snow" in condition: return "❄️"
    return "🌈"

def update_current_conditions(frame, data):
    if not data:
        frame.location_label.config(text="⚠️ Unable to load weather")
        return
