import tkinter as tk
from PIL import Image, ImageTk
import os

class ForecastFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg="#ffeaf5")

        # Header
        tk.Label(self, text="★ Forecast ★", font=("Press Start 2P", 10),
                 bg="#ffeaf5", fg="#ff69b4").pack(pady=(10, 5))
        
        self.sparkle_label = tk.Label(self, text="✧ ✦ ✧ ✦", font=("Arial", 14), bg="#ffeaf5", fg="#ffb3da")
        self.sparkle_label.pack()

        # Container
        self.forecast_container = tk.Frame(self, bg="#ffeaf5")
        self.forecast_container.pack(pady=5)
        self.sparkles = ["✦", "✧", "✦", "✧", "✦"]
        
        sample_data = [
            ("Monday", "sunny_48.png", "75°F / 60°F"),
            ("Tuesday", "rainy_48.png", "68°F / 55°F"),
            ("Wednesday", "cloudy_48.png", "70°F / 58°F"),
            ("Thursday", "storm_48.png", "66°F / 52°F"),
            ("Friday", "partly_cloudy_48.png", "72°F / 57°F"),
        ]

        for day, icon_file, temps in sample_data:
            self.create_forecast_row(day, icon_file, temps)

    def create_forecast_row(self, day, icon_filename, temps):
        row = tk.Frame(self.forecast_container, bg="#ffd9ec")
        row.pack(fill="x", padx=20, pady=4)

        # Day label
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
        except:
            tk.Label(row, text="🌤️", font=("Arial", 16), bg="#ffd9ec").pack(side="left", padx=6)

        # Temps (THIS was misplaced!)
        tk.Label(row, text=temps, font=("Arial", 9), bg="#ffd9ec",
                fg="#333", anchor="w").pack(side="left", padx=(6, 8))

        condition = condition.lower()
        if "cloud" in condition:
            return "cloudy_48.png"
        if "rain" in condition:
            return "rainy_48.png"
        if "storm" in condition or "thunder" in condition:
            return "storm_48.png"
        if "sun" in condition or "clear" in condition:
            return "sunny_48.png"
        if "snow" in condition:
            return "snow_48.png"
        return "partly_cloudy_48.png"  # default fallback

        # Temps
        tk.Label(row, text=temps, font=("Arial", 9), bg="#ffd9ec",
                 fg="#333", anchor="w").pack(side="left", padx=(6, 8))

# Hook for main.py
def create_forecast_frame(parent):
    return ForecastFrame(parent)
