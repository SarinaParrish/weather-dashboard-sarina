import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import time

from features.current_conditions import create_current_conditions_frame, update_current_conditions
from features.weather_api import get_weather, get_user_city
from features.forecast import create_forecast_frame
from features.almanac import create_almanac_frame
from features.graph2_slide import create_graph2_frame
from features.user_settings import create_user_settings_frame, load_settings
from features.town_forecast import create_town_forecast_frame

root = tk.Tk()
root.title("WeatherStarr✨")
root.geometry("400x600")
root.resizable(False, False)
root.update_idletasks()
root.minsize(400, 600)
root.maxsize(400, 600)

bg_image = Image.open("assets/backgrounds/background_inspo_1.jpg").resize((400, 600), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
tk.Label(root, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

# === Top Header Frame ===
header_frame = tk.Frame(root, bg="#ffcde1", height=5)
header_frame.pack(side="top", fill="x")

header_content = tk.Frame(header_frame, bg="#ffcde1")
header_content.pack(fill="both", expand=True)

# Add the time
time_label = tk.Label(header_content, text="12:00 PM", font=("Courier", 11), bg="#ffcde1")
time_label.pack(side="right", padx=1)

# 🔁 Unit toggle goes here!
unit_var = tk.StringVar(value="imperial")  # default is °F

def toggle_units():
    current = unit_var.get()
    if current == "imperial":
        unit_var.set("metric")
        unit_toggle_btn.config(text="°C")
    else:
        unit_var.set("imperial")
        unit_toggle_btn.config(text="°F")
    
    print("Units set to:", unit_var.get())

    # 🔁 Re-fetch weather and rebuild all major slides
    city = location_entry.get().strip() or get_user_city()

    # Re-fetch current conditions
    weather_data = get_weather(city, units=unit_var.get())
    update_current_conditions(slides["current"], weather_data)

    # Rebuild forecast slide
    slides["forecast"].destroy()
    slides["forecast"] = create_forecast_frame(slide_container, city, units=unit_var.get())
    slides["forecast"].config(width=360, height=450, bg="#ffeaf5")
    slides["forecast"].grid(row=0, column=0, sticky="nsew")

    # Rebuild graph2 if it supports units
    slides["graph2"].destroy()
    slides["graph2"] = create_graph2_frame(slide_container, city, units=unit_var.get())
    slides["graph2"].config(width=360, height=450, bg="#ffeaf5")
    slides["graph2"].grid(row=0, column=0, sticky="nsew")

unit_toggle_btn = tk.Button(
    header_content,
    text="°F",
    font=("Courier", 10),
    command=toggle_units,
    width=4,
    bg="#ffddee",
    fg="#444",
    bd=2,
    relief="ridge"
)
unit_toggle_btn.pack(side="right", padx=10)  # 💥 THIS LINE ADDS IT TO THE SCREEN

logo_img = Image.open("assets/icons/weatherstarr_logo.png").resize((120, 75), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)
logo_label = tk.Label(header_frame, image=logo_photo, bg="#ffcde1")
logo_label.image = logo_photo
logo_label.pack(side="left", fill="y", padx=0)

location_frame = tk.Frame(root, bg="#ffdceb")
location_frame.pack(side="top", fill="x")

location_icon = tk.Label(location_frame, text="📍 Enter City", font=("Arial", 12), bg="#ffdceb")
location_icon.pack(side="left", padx=(10, 0), pady=5)

location_entry = ttk.Entry(location_frame, width=25)
location_entry.pack(side="left", padx=(5, 10), pady=5)

def clear_search():
    location_entry.delete(0, tk.END)

def search_city_weather():
    city = location_entry.get().strip()
    if city:
        print(f"📱 Requesting weather for: {city}")
        weather_data = get_weather(city)
        update_current_conditions(slides["current"], weather_data)
        slides["town"].update_town_forecast(city)

        slides["forecast"].destroy()
        slides["forecast"] = create_forecast_frame(slide_container, city)
        slides["forecast"].config(width=360, height=450, bg="#ffeaf5")
        slides["forecast"].grid(row=0, column=0, sticky="nsew")

        raise_slide("forecast")
    else:
        print("⚠️ No city entered.")

search_button = tk.Button(location_frame, text=" Search ", font=("Courier", 10), bg="#ffaad4", fg="#fff", bd=2, command=search_city_weather)
search_button.pack(side="left", padx=5)

clear_button = tk.Button(location_frame, text=" X ", font=("Courier", 10), bg="#ffaad4", fg="#fff", bd=2, command=clear_search)
clear_button.pack(side="left", padx=5)

style = ttk.Style()
style.configure("Custom.TFrame", background="#ffeaf5")

slide_container = tk.Frame(root, width=360, height=450)
slide_container.place(relx=0.5, y=140, anchor="n")
slide_container.grid_propagate(False)
slide_container.pack_propagate(False)
slide_container.grid_rowconfigure(0, weight=1)
slide_container.grid_columnconfigure(0, weight=1)

# Slide definitions
toc_frame = tk.Frame(slide_container, bg="#ffeaf5", width=360, height=450)
toc_frame.grid(row=0, column=0, sticky="nsew")

# Flying pig mascot image
pig_path = os.path.join("assets", "icons", "flying_pig_header_96px.png")
pig_image = Image.open(pig_path).resize((96, 96), Image.LANCZOS)
pig_photo = ImageTk.PhotoImage(pig_image)

mascot_label = tk.Label(toc_frame, image=pig_photo, bg="#ffeaf5")
mascot_label.image = pig_photo  # prevent garbage collection
mascot_label.pack(pady=10)

toc_title = tk.Label(toc_frame, text="★ Table of Contents ★", font=("Press Start 2P", 10), bg="#ffeaf5", fg="#ff69b4")
toc_title.pack(pady=5)

button_style = {
    "font": ("Courier", 12, "bold"),
    "width": 20,
    "padx": 10,
    "pady": 5,
    "bg": "#ffaad4",
    "fg": "#fff",
    "relief": "ridge",
    "bd": 3
}

def make_nav_button(label, key):
    return tk.Button(toc_frame, text=label, command=lambda: raise_slide(key), **button_style)

make_nav_button("Current Weather", "current").pack(pady=5)
make_nav_button("Forecast", "forecast").pack(pady=5)
make_nav_button("Graph", "graph2").pack(pady=5)
# make_nav_button("Display Mode", "almanac").pack(pady=5)  don't need it since i cant do static button
make_nav_button("Almanac", "graph").pack(pady=5)
make_nav_button("WeatherStarr Town", "town").pack(pady=5)

# Slide Frames
detected_city = load_settings().get("home_city", get_user_city())
slides = {
    "toc": toc_frame,
    "current": create_current_conditions_frame(slide_container),
    "forecast": create_forecast_frame(slide_container, detected_city),
    "graph": create_graph2_frame(slide_container),
    "almanac": create_almanac_frame(slide_container),
    "graph2": create_graph2_frame(slide_container),
    "town": create_town_forecast_frame(slide_container),
    "settings": create_user_settings_frame(slide_container)
}
for frame in slides.values():
    frame.config(width=360, height=450, bg="#ffeaf5")
    frame.grid(row=0, column=0, sticky="nsew")

slide_order = list(slides.keys())
current_slide_index = 0

def raise_slide(name):
    if name in slides:
        slides[name].tkraise()

        if hasattr(slides[name], "on_show"):
            slides[name].on_show()

        global current_slide_index
        current_slide_index = slide_order.index(name)
    else:
        print(f"Slide '{name}' not found")

def next_slide():
    global current_slide_index
    current_slide_index = (current_slide_index + 1) % len(slide_order)
    raise_slide(slide_order[current_slide_index])

def previous_slide():
    global current_slide_index
    current_slide_index = (current_slide_index - 1) % len(slide_order)
    raise_slide(slide_order[current_slide_index])

def play_slideshow():
    raise_slide("current")
    auto_cycle()

def auto_cycle():
    global current_slide_index
    next_index = (current_slide_index + 1) % len(slide_order)
    raise_slide(slide_order[next_index])
    root.after(4000, auto_cycle)

toolbar_frame = tk.Frame(root, bg="#ffccdd", height=40)
toolbar_frame.pack(side="bottom", fill="x")

toolbar_button_style = {
    "font": ("Courier", 14),
    "bg": "#ffaad4",
    "fg": "#fff",
    "width": 4,
    "relief": "raised",
    "bd": 2
}

tk.Button(toolbar_frame, text="☰", command=lambda: raise_slide("toc"), **toolbar_button_style).pack(side="left", padx=3, pady=2)
tk.Button(toolbar_frame, text="⏮", command=previous_slide, **toolbar_button_style).pack(side="left", padx=2)
tk.Button(toolbar_frame, text="▶", command=play_slideshow, **toolbar_button_style).pack(side="left", padx=2)
tk.Button(toolbar_frame, text="⏸", command=lambda: print("Pause clicked (coming soon)"), **toolbar_button_style).pack(side="left", padx=2)
tk.Button(toolbar_frame, text="🔊", command=lambda: print("Audio toggle (coming soon)"), **toolbar_button_style).pack(side="left", padx=2)
tk.Button(toolbar_frame, text="⚙️", command=lambda: raise_slide("settings"), **toolbar_button_style).pack(side="left", padx=2)
tk.Button(toolbar_frame, text="⏭", command=next_slide, **toolbar_button_style).pack(side="left", padx=2)

def update_time():
    current_time = time.strftime("%I:%M %p")
    time_label.config(text=current_time)
    root.after(1000, update_time)

update_time()
raise_slide("toc")
load_initial_weather = lambda: update_current_conditions(slides["current"], get_weather(get_user_city()))
load_initial_weather()

root.mainloop()
