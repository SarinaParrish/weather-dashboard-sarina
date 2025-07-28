import tkinter as tk
from PIL import Image, ImageTk
from features.weather_api import get_forecast

# Defer image loading until root window is ready
SUN_ICON = None
RAIN_ICON = None
CLOUD_ICON = None

# Emoji fallback (for undefined types)
WEATHER_EMOJIS = {
    "Thunderstorm": "⚡",
    "Drizzle": "🌦️",
    "Snow": "❄️",
    "Mist": "🌫️"
}

def create_town_forecast_frame(parent):
    global SUN_ICON, RAIN_ICON, CLOUD_ICON

    # Load icons now that root exists
    if SUN_ICON is None:
        SUN_ICON = ImageTk.PhotoImage(Image.open("assets/icons/kawaii_sun_64px.png").resize((48, 48), Image.LANCZOS))
    if RAIN_ICON is None:
        RAIN_ICON = ImageTk.PhotoImage(Image.open("assets/icons/kawaii_rain_64px.png").resize((48, 48), Image.LANCZOS))
    if CLOUD_ICON is None:
        CLOUD_ICON = ImageTk.PhotoImage(Image.open("assets/icons/kawaii_cloud_64px.png").resize((48, 48), Image.LANCZOS))

    frame = tk.Frame(parent, width=360, height=450, bg="#ffeaf5")
    frame.pack_propagate(False)

    # Title
    title = tk.Label(
        frame,
        text="★ Coming Up Next ★",
        font=("Press Start 2P", 10),
        bg="#ffeaf5",
        fg="#ff69b4"
    )
    title.pack(pady=(12, 4))

    # Forecast container
    forecast_container = tk.Frame(frame, bg="#ffeaf5")
    forecast_container.pack(pady=(10, 5))

    # Day blocks with nicer style
    blocks = []
    for i in range(3):
        card = tk.Frame(forecast_container, width=100, height=130, bg="#ffd6ec", bd=0, highlightbackground="#ffaad4", highlightthickness=2)
        card.grid(row=0, column=i, padx=6, pady=5)
        card.pack_propagate(False)

        day_label = tk.Label(card, text="Day", font=("Courier", 10, "bold"), bg="#ffd6ec", fg="#ff69b4")
        day_label.pack(pady=(10, 0))

        icon_label = tk.Label(card, text="☁️", font=("Arial", 32), bg="#ffd6ec")
        icon_label.pack(pady=(5, 10))

        blocks.append((day_label, icon_label))

    # Moon Friend
    moon = tk.Label(frame, text="(｡♥‿♥｡)", font=("Courier", 20), bg="#ffeaf5")
    moon.pack(pady=(15, 5))

    moon_msg = tk.Label(frame, text="See you soon!", font=("Courier", 10), bg="#ffeaf5", fg="#5f5f5f")
    moon_msg.pack()

    def update_town_forecast(city):
        data = get_forecast(city)
        if not data:
            print("⚠️ No forecast data.")
            return

        for i in range(min(3, len(data))):
            forecast_day = data[i]
            name = forecast_day.get("day", f"Day {i+1}")
            condition = forecast_day.get("main", "Clear")

            blocks[i][0].config(text=name)

            if condition == "Clear":
                blocks[i][1].config(image=SUN_ICON, text="")
                blocks[i][1].image = SUN_ICON
            elif condition == "Rain":
                blocks[i][1].config(image=RAIN_ICON, text="")
                blocks[i][1].image = RAIN_ICON
            elif condition == "Clouds":
                blocks[i][1].config(image=CLOUD_ICON, text="")
                blocks[i][1].image = CLOUD_ICON
            else:
                emoji = WEATHER_EMOJIS.get(condition, "❓")
                blocks[i][1].config(text=emoji, image="")

        moon_msg.config(text=f"Wow! {city} looks {condition.lower()}!")

    frame.update_town_forecast = update_town_forecast
    return frame
