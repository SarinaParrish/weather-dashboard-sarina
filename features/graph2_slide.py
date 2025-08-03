# features/graph2_slide.py

import tkinter as tk
import matplotlib
matplotlib.use("Agg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from features.weather_api import get_forecast

def create_graph2_frame(parent, city="Clearwater"):
    # Get API forecast data
    forecast_data = get_forecast(city)

    if not forecast_data:
        return tk.Label(parent, text="Forecast unavailable", bg="#ffeaf5", fg="red")

    days = [entry["day"] for entry in forecast_data]
    max_temps = [entry["high"] for entry in forecast_data]
    min_temps = [entry["low"] for entry in forecast_data]
    precips = [0 for _ in forecast_data]  # <-- optional placeholder

    frame = tk.Frame(parent, width=360, height=450, bg="#ffeaf5")
    frame.grid_propagate(False)
    frame.pack_propagate(False)
    frame.place(x=0, y=0)

    title_text = f"★ Forecast Trends: {city.title()} ★"
    title_label = tk.Label(frame, text=title_text, font=("Press Start 2P", 8), bg="#ffeaf5", fg="#ff69b4")
    title_label.pack(pady=(12, 2))

    fig, ax1 = plt.subplots(figsize=(4.8, 2.5), dpi=100)

    ax1.bar(days, precips, color="#a2e4f8", label="Precipitation (in)")
    ax1.set_ylabel("Precip (in)", color="#0093b5")
    ax1.tick_params(axis='y', labelcolor="#0093b5")

    ax2 = ax1.twinx()
    ax2.plot(days, max_temps, marker="o", color="#ff69b4", label="Max Temp")
    ax2.plot(days, min_temps, marker="o", color="#bb7af3", label="Min Temp")
    ax2.set_ylabel("Temp (°F)", color="#a70094")
    ax2.tick_params(axis='y', labelcolor="#a70094")

    fig.tight_layout()

    graph_wrapper = tk.Frame(frame, width=340, height=320, bg="#ffeaf5")
    graph_wrapper.place(x=10, y=40)
    graph_wrapper.grid_propagate(False)
    graph_wrapper.pack_propagate(False)

    canvas = FigureCanvasTkAgg(fig, master=graph_wrapper)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=0, y=0, width=340, height=320)

    return frame
