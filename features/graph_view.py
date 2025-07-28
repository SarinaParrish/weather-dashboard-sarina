import tkinter as tk
import matplotlib
matplotlib.use("Agg")  # ⛔ Block Tkinter backend interference

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd

# Load CSV for Starr Trends
csv_path = "data/final_cleaned_weather_data_clearwater.csv"
df = pd.read_csv(csv_path, parse_dates=["date"])
df["month"] = df["date"].dt.strftime("%b")

# Monthly summary
monthly_summary = df.groupby("month").agg({
    "max_temp": "mean",
    "min_temp": "mean",
    "precip": "sum"
}).reset_index()

# Order months
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthly_summary["month"] = pd.Categorical(monthly_summary["month"], categories=month_order, ordered=True)
monthly_summary = monthly_summary.sort_values("month")

def create_graph_frame(parent):
    # 🔒 Fully controlled frame
    frame = tk.Frame(parent, width=360, height=450, bg="#ffeaf5")
    frame.grid_propagate(False)
    frame.pack_propagate(False)
    frame.place(x=0, y=0)

    # Title
    tk.Label(frame, text="★ Starr Trends ★", font=("Press Start 2P", 9), bg="#ffeaf5", fg="#ff69b4").place(x=40, y=10)

    # Create matplotlib figure
    fig, ax1 = plt.subplots(figsize=(4.8, 2.5), dpi=100)

    ax1.bar(monthly_summary["month"], monthly_summary["precip"], color="#a2e4f8", label="Precipitation (in)")
    ax1.set_ylabel("Precip (in)", color="#0093b5")
    ax1.tick_params(axis='y', labelcolor="#0093b5")

    # Show only 4 month labels evenly spaced (Jan, Apr, Jul, Oct)
    ax1.set_xticks([0, 3, 7, 11])
    ax1.set_xticklabels(["Jan", "Apr", "Aug", "Dec"])

    ax2 = ax1.twinx()
    ax2.plot(monthly_summary["month"], monthly_summary["max_temp"], marker="o", color="#ff69b4", label="Max Temp")
    ax2.plot(monthly_summary["month"], monthly_summary["min_temp"], marker="o", color="#bb7af3", label="Min Temp")
    ax2.set_ylabel("Temp (°F)", color="#a70094")
    ax2.tick_params(axis='y', labelcolor="#a70094")

    fig.tight_layout()

    # Fixed-size wrapper to prevent shrinking
    graph_wrapper = tk.Frame(frame, width=340, height=320, bg="#ffeaf5")
    graph_wrapper.place(x=10, y=40)
    graph_wrapper.grid_propagate(False)
    graph_wrapper.pack_propagate(False)

    canvas = FigureCanvasTkAgg(fig, master=graph_wrapper)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=0, y=0, width=340, height=320)

    return frame
