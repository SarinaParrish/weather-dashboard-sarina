import tkinter as tk
from PIL import Image, ImageTk
import os
from features.weather_api import get_forecast

class ForecastFrame(tk.Frame):
    def __init__(self, parent, city="New York", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg="#ffeaf5")

        # Header
        tk.Label(self, text="⛅ Forecast ⛅", font=("Press Start 2P", 10),
                 bg="#ffeaf5", fg="#ff69b4").pack(pady=(10, 5))

        self.sparkle_label = tk.Label(self, text="✦ ✧ ✦ ✧", font=("Arial", 14),
                                      bg="#ffeaf5", fg="#ffb3da")
        self.sparkle_label.pack()

        # Container for forecast rows
        self.forecast_container = tk.Frame(self, bg="#ffeaf5")
        self.forecast_container.pack(pady=5)

        # Pull forecast data for selected city
        forecast_data = get_forecast(city)

        if forecast_data:
            for entry in forecast_data:
                day = entry["day"]
                main = entry["main"]
                desc = entry["desc"]
                high = entry["high"]
                low = entry["low"]
                icon_file = self.get_weather_icon(main)
                temps = f"{high}°F / {low}°F"
                self.create_forecast_row(day, icon_file, temps)
                self.add_description(desc)
        else:
            tk.Label(self.forecast_container, text="❌ Forecast unavailable",
                     font=("Arial", 9), fg="red", bg="#ffeaf5").pack(pady=10)

    def get_weather_icon(self, condition):
        condition = condition.lower()
        if "cloud" in condition:
            return "kawaii_cloud_64px.png"
        if "rain" in condition:
            return "kawaii_rain_64px.png"
        if "storm" in condition or "thunder" in condition:
            return "kawaii_rain_64px.png"
        if "sun" in condition or "clear" in condition:
            return "kawaii_sun_64px.png"
        if "snow" in condition:
            return "snow.png"
        return "kawaii_cloud_64px.png"  # default fallback

    def create_forecast_row(self, day, icon_filename, temps):
        row = tk.Frame(self.forecast_container, bg="#ffd9ec")
        row.pack(fill="x", padx=20, pady=4)

        # Day
        tk.Label(row, text=day, font=("Press Start 2P", 7),
                 bg="#ffd9ec", fg="#d63384", width=12, anchor="w").pack(side="left", padx=(6, 4), pady=4)

        # Weather Icon
        icon_path = os.path.join("assets", "icons", icon_filename)
        try:
            img = Image.open(icon_path).resize((32, 32))
            icon = ImageTk.PhotoImage(img)
            icon_label = tk.Label(row, image=icon, bg="#ffd9ec")
            icon_label.image = icon
            icon_label.pack(side="left", padx=6)
        except Exception as e:
            print(f"🚫 Could not load icon {icon_filename}: {e}")
            tk.Label(row, text="🌤️", font=("Arial", 16), bg="#ffd9ec").pack(side="left", padx=6)

        # Temps
        tk.Label(row, text=temps, font=("Arial", 9),
                 bg="#ffd9ec", fg="#333", anchor="w").pack(side="left", padx=(6, 8))

    def add_description(self, desc):
        tk.Label(self.forecast_container, text=desc.capitalize(), font=("Arial", 8, "italic"),
                 bg="#ffeaf5", fg="#aa88aa", anchor="w").pack(fill="x", padx=30, pady=(0, 6))

# Entry point from main.py
def create_forecast_frame(parent, city="New York"):
    return ForecastFrame(parent, city=city)
