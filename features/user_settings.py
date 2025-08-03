# features/user_settings.py

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import json

SETTINGS_FILE = "settings.json"

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return {"preferred_units": "Imperial (°F)", "home_city": "Largo"}

def save_settings(units, city):
    with open(SETTINGS_FILE, "w") as f:
        json.dump({
            "preferred_units": units,
            "home_city": city
        }, f, indent=2)
    print("✅ Settings saved to settings.json")

def create_user_settings_frame(parent):
    settings = load_settings()

    frame = tk.Frame(parent, width=400, height=600, bg="#ffeaf5")
    frame.pack_propagate(False)

    title = tk.Label(frame, text="User Settings", font=("Pixel", 20), bg="#ffeaf5")
    title.pack(pady=(20, 10))

    moon = tk.Label(frame, text="🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘", font=("Arial", 18), bg="#ffeaf5")
    moon.pack(pady=(20, 5))

    unit_label = tk.Label(frame, text="Preferred Units:", bg="#ffeaf5", font=("Courier", 12))
    unit_label.pack(pady=(10, 0))

    unit_choice = ttk.Combobox(frame, values=["Imperial (°F)", "Metric (°C)"])
    unit_choice.set(settings.get("preferred_units", "Imperial (°F)"))
    unit_choice.pack()

    city_label = tk.Label(frame, text="Home City:", bg="#ffeaf5", font=("Courier", 12))
    city_label.pack(pady=(20, 0))

    city_entry = tk.Entry(frame)
    city_entry.insert(0, settings.get("home_city", "Largo"))
    city_entry.pack()

    def on_save():
        units = unit_choice.get()
        city = city_entry.get().strip()
        save_settings(units, city)

    save_btn = tk.Button(frame, text="Save Settings", bg="#ffb3e6", command=on_save)
    save_btn.pack(pady=(30, 10))

    # Flying pig mascot
    pig_path = os.path.join("assets", "icons", "flying_pig_header_96px.png")
    pig_image = Image.open(pig_path).resize((96, 96), Image.LANCZOS)
    pig_photo = ImageTk.PhotoImage(pig_image)

    pig_label = tk.Label(frame, image=pig_photo, bg="#ffeaf5")
    pig_label.image = pig_photo
    pig_label.pack(pady=(10, 5))

    return frame
