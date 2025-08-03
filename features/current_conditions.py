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

def update_current_conditions(frame, data):
    if not data:
        frame.location_label.config(text="⚠️ Weather Unavailable")
        return

    try:
        city = data.get("name", "Unknown")
        temp = round(data["main"]["temp"])
        condition = data["weather"][0]["main"]
        high = round(data["main"]["temp_max"])
        low = round(data["main"]["temp_min"])
        humidity = data["main"]["humidity"]
        wind = round(data["wind"]["speed"])

        frame.location_label.config(text=f"📍 {city}")
        frame.temp_label.config(text=f"{temp}°F")
        frame.condition_label.config(text=f"{condition}")
        frame.high_low_label.config(text=f"H: {high}°F  L: {low}°F")
        frame.humidity_label.config(text=f"💧 Humidity: {humidity}%")
        frame.wind_label.config(text=f"🌬️ Wind: {wind} mph")

    except Exception as e:
        print("❌ Failed to update current conditions:", e)
        frame.location_label.config(text="⚠️ Error loading weather")
