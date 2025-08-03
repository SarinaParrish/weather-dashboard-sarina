# 🌦️ WeatherStarr ✨

**WeatherStarr** is a nostalgic, kawaii-inspired weather dashboard built in Python using Tkinter. It fetches real-time weather data, displays forecasts, and includes animated visuals, custom slides, and a Tamagotchi-style flying pig mascot.

---

## 📦 Features

- 📍 **Searchable Location Input**  
  Users can enter any city to fetch real-time weather data.

- 🌤️ **Current Conditions Slide**  
  Displays temperature, humidity, and other key metrics.

- 🔮 **Forecast Slide**  
  Shows multi-day weather predictions from the API.

- 📈 **Graph Slide**  
  Displays model-predicted trends using matplotlib.

- 🌙 **Almanac Slide**  
  Shows a year’s worth of Clearwater weather data as a graph.

- 🐷 **Custom Feature #1 — User Settings**  
  Users can select their **preferred units** (°F/°C) and set a **home city**. These preferences are saved and automatically loaded on app startup. This feature includes a themed UI with a flying pig mascot.

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/SarinaParrish/weather-dashboard-sarina.git
   cd weather-dashboard-sarina
   ```

2. Set up your virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # or use source for Mac/Linux
   pip install -r requirements.txt
   ```

3. Add your OpenWeatherMap API key to `config.py`:
   ```python
   API_KEY = "your_api_key_here"
   ```

4. Run the app:
   ```bash
   python main.py
   ```

---

## 🐛 Known Bugs / Next Steps

- Unit conversion (°F ↔ °C) is not yet reflected across all slides.
- Animations for the pig mascot may occasionally desync.
- Some slides require API re-fetching when switching locations.

---

## 🎥 Demo

> [Loom video link :
 https://www.loom.com/share/5e8df493116743e086ad54fe7f681cfc?sid=1863be92-c9f6-4855-8973-e37a9f29a568 ] 


---

## 🔖 Tag for Submission

```bash
git tag feature1-complete
git push origin feature1-complete
```

---

## 🛠️ Built With

- Python 3.11
- Tkinter
- PIL (Pillow)
- Matplotlib
- OpenWeatherMap API
