# features/almanac.py

import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Load combined team CSV
TEAM_DATA = pd.read_csv("assets/data/team_weather_data.csv")  # Adjust path if needed

# Group by city for faster access
CITY_DATA = {city: df for city, df in TEAM_DATA.groupby("city")}

def create_almanac_frame(parent):
    frame = tk.Frame(parent, bg="#ffeaf5", width=360, height=450)
    frame.pack_propagate(False)

    title = tk.Label(frame, text="★ Almanac ★", font=("Press Start 2P", 12), bg="#ffeaf5", fg="#ff69b4")
    title.pack(pady=(10, 5))

    # City buttons container
    button_frame = tk.Frame(frame, bg="#ffeaf5")
    button_frame.pack(side="left", padx=(10, 5), pady=10)

    # Graph display area
    graph_container = tk.Frame(frame, bg="#ffeaf5")
    graph_container.pack(side="right", padx=(5, 10), pady=10)

    canvas_holder = {}

    def plot_city_graph(city):
        # Clear previous canvas if any
        if "canvas" in canvas_holder:
            canvas_holder["canvas"].get_tk_widget().destroy()

        df = CITY_DATA[city]
        dates = pd.to_datetime(df["date"])
        max_temps = df["max_temp"]
        min_temps = df["min_temp"]


        fig, ax = plt.subplots(figsize=(3.5, 3), dpi=100)

        # Plot lines
        ax.plot(dates, max_temps, label="Max Temp", color="#ff69b4", linewidth=1.5)
        ax.plot(dates, min_temps, label="Min Temp", color="#a39dff", linewidth=1.5)

        # Clean title and labels
        ax.set_title(f"{city} Temps (2024)", fontsize=9)
        ax.set_ylabel("Temperature (°C)", fontsize=5)

        # Clean ticks
        ax.tick_params(axis='x', labelrotation=45, labelsize=7)
        ax.tick_params(axis='y', labelsize=7)

        # Format Y-axis numbers (no decimals unless needed)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.1f}".rstrip('0').rstrip('.')))

        # Legend
        ax.legend(fontsize=8, loc="upper right")

        canvas = FigureCanvasTkAgg(fig, master=graph_container)
        canvas.draw()
        canvas.get_tk_widget().pack()
        canvas_holder["canvas"] = canvas

    # Create buttons for each city
    for city in CITY_DATA:
        ttk.Button(button_frame, text=city, command=lambda c=city: plot_city_graph(c)).pack(pady=3)

    return frame
