import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from features.current_conditions import create_current_conditions_frame, update_current_conditions
from features.weather_api import get_weather, get_user_city
from features.forecast import create_forecast_frame
from features.graph_view import create_graph_frame
from features.almanac import AlmanacFrame
from features.town_forecast import create_town_forecast_frame
import os
import time

# Create main window
root = tk.Tk()
root.title("WeatherStarr✨")
root.geometry("400x600")
root.resizable(False, False)

# 🔒 Force size no matter what widgets try to do
root.update_idletasks()
root.minsize(400, 600)
root.maxsize(400, 600)


# BACKGROUND IMAGE
bg_image = Image.open("assets/backgrounds/background_inspo_1.jpg").resize((400, 600), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
tk.Label(root, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

# HEADER
header_frame = tk.Frame(root, bg="#ffcde1", height=5)
header_frame.pack(side="top", fill="x")

header_content = tk.Frame(header_frame, bg="#ffcde1")
header_content.pack(fill="both", expand=True)

time_label = tk.Label(header_content, text="12:00 PM", font=("Courier", 11), bg="#ffcde1")
time_label.pack(side="right", padx=1)

logo_img = Image.open("assets/icons/weatherstarr_logo.png").resize((120, 75), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)
logo_label = tk.Label(header_frame, image=logo_photo, bg="#ffcde1")
logo_label.image = logo_photo
logo_label.pack(side="left", fill="y", padx=0)

# LOCATION SEARCH BAR
location_frame = tk.Frame(root, bg="#ffdceb")
location_frame.pack(side="top", fill="x")

location_icon = tk.Label(location_frame, text="📍 Enter City", font=("Arial", 12), bg="#ffdceb")
location_icon.pack(side="left", padx=(10, 0), pady=5)

location_entry = ttk.Entry(location_frame, width=25)
location_entry.pack(side="left", padx=(5, 10), pady=5)

def search_city_weather():
    city = location_entry.get().strip()
    if city:
        print(f"📡 Requesting weather for: {city}")
        weather_data = get_weather(city)
        print("✅ API response received.")
        update_current_conditions(current_conditions_slide, weather_data)
        town_forecast_slide.update_town_forecast(city)
        raise_slide(1)
    else:
        print("⚠️ No city entered.")

search_button = tk.Button(location_frame, text=" Search ", font=("Courier", 10), bg="#ffaad4", fg="#fff", bd=2, command=search_city_weather)
search_button.pack(side="left", padx=5)

clear_button = tk.Button(location_frame, text=" X ", font=("Courier", 10), bg="#ffaad4", fg="#fff", bd=2)
clear_button.pack(side="left", padx=5)

# STYLES
style = ttk.Style()
style.configure("Custom.TFrame", background="#ffeaf5")

# SLIDE CONTAINER
slide_container = tk.Frame(root, width=360, height=450)
slide_container.place(relx=0.5, y=140, anchor="n")
slide_container.grid_propagate(False)
slide_container.pack_propagate(False)
slide_container.grid_rowconfigure(0, weight=1)
slide_container.grid_columnconfigure(0, weight=1)

# TOC Slide
toc_frame = tk.Frame(slide_container, bg="#ffeaf5", width=360, height=450)
toc_frame.grid(row=0, column=0, sticky="nsew")

mascot_label = tk.Label(toc_frame, text="(｡♥‿♥｡)", font=("Courier", 18), bg="#ffeaf5")
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

def make_nav_button(label, index):
    return tk.Button(toc_frame, text=label, command=lambda: raise_slide(index), **button_style)

make_nav_button("Current Weather", 1).pack(pady=5)
make_nav_button("Forecast", 2).pack(pady=5)
make_nav_button("Graph", 3).pack(pady=5)
make_nav_button("Display Mode", 0).pack(pady=5)
make_nav_button("Almanac", 4).pack(pady=5)
make_nav_button("WeatherStarr Town", 5).pack(pady=5)

# Slides
current_conditions_slide = create_current_conditions_frame(slide_container)
current_conditions_slide.config(width=360, height=450, bg="#ffeaf5")
current_conditions_slide.grid(row=0, column=0, sticky="nsew")

forecast_slide = create_forecast_frame(slide_container)
forecast_slide.config(width=360, height=450, bg="#ffeaf5")
forecast_slide.grid(row=0, column=0, sticky="nsew")

graph_slide = create_graph_frame(slide_container)
graph_slide.config(width=360, height=450)
graph_slide.grid(row=0, column=0, sticky="nsew")

almanac_slide = AlmanacFrame(slide_container)
almanac_slide.config(width=360, height=450, bg="#ffeaf5")
almanac_slide.grid(row=0, column=0, sticky="nsew")

town_forecast_slide = create_town_forecast_frame(slide_container)
town_forecast_slide.config(width=360, height=450, bg="#ffeaf5")
town_forecast_slide.grid(row=0, column=0, sticky="nsew")

slides = [toc_frame, current_conditions_slide, forecast_slide, graph_slide, almanac_slide, town_forecast_slide]
current_slide_index = 0

# Moon Friend
try:
    moon_path = os.path.join("assets", "its_just_a_phase.png")
    moon_img = Image.open(moon_path).resize((120, 120), Image.LANCZOS)
    moon_photo = ImageTk.PhotoImage(moon_img)

    moon_friend = tk.Label(root, image=moon_photo, bg="#ffeaf5", bd=0)
    moon_friend.place(x=20, y=600)
    moon_friend.lift()
except Exception as e:
    print("🚫 Moon friend failed to load:", e)
    moon_friend = None

def float_moon_friend():
    if moon_friend:
        current_y = moon_friend.winfo_y()
        target_y = 275
        if current_y > target_y:
            moon_friend.place_configure(y=current_y - 5)
            root.after(40, float_moon_friend)
        else:
            moon_friend.place_configure(y=target_y)

# Slide Navigation
def raise_slide(index):
    global current_slide_index
    current_slide_index = max(0, min(len(slides) - 1, index))
    slides[current_slide_index].tkraise()

    if index == 4 and hasattr(slides[index], "on_show"):
        slides[index].on_show()

def next_slide():
    raise_slide(current_slide_index + 1)

def previous_slide():
    raise_slide(current_slide_index - 1)

def play_slideshow():
    raise_slide(1)
    auto_cycle()

def auto_cycle():
    global current_slide_index
    next_index = (current_slide_index + 1) % len(slides)
    raise_slide(next_index)
    root.after(4000, auto_cycle)

# Toolbar
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

tk.Button(toolbar_frame, text="☰", command=lambda: raise_slide(0), **toolbar_button_style).pack(side="left", padx=3, pady=2)
tk.Button(toolbar_frame, text="⏮", command=previous_slide, **toolbar_button_style).pack(side="left", padx=2)
tk.Button(toolbar_frame, text="▶", command=play_slideshow, **toolbar_button_style).pack(side="left", padx=2)
tk.Button(toolbar_frame, text="⏸", command=lambda: print("Pause clicked (coming soon)"), **toolbar_button_style).pack(side="left", padx=2)
tk.Button(toolbar_frame, text="🔊", command=lambda: print("Audio toggle (coming soon)"), **toolbar_button_style).pack(side="left", padx=2)
tk.Button(toolbar_frame, text="📺", command=lambda: print("Static effect (coming soon)"), **toolbar_button_style).pack(side="left", padx=2)
tk.Button(toolbar_frame, text="⏭", command=next_slide, **toolbar_button_style).pack(side="left", padx=2)

# Time + Launch
def load_initial_weather():
    city = get_user_city()
    print(f"🌍 Detected location: {city}")
    data = get_weather(city)
    update_current_conditions(current_conditions_slide, data)

def update_time():
    current_time = time.strftime("%I:%M %p")
    time_label.config(text=current_time)
    root.after(1000, update_time)

update_time()
raise_slide(0)
load_initial_weather()
root.mainloop()
root.update_idletasks()
root.geometry("400x600")  # force the size again
