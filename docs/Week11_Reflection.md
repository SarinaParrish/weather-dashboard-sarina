# Week11_Reflection.md

## 📌 Section 0: Fellow Details

| Field                | Your Entry                 |
|----------------------|----------------------------|
| Name                 | Sarina Parrish             |
| GitHub Username      | SarinaParrish              |
| Preferred Feature Track | Visual / Interactive       |
| Team Interest        | Yes — Project Owner        |

---

## ✍️ Section 1: Week 11 Reflection

### Key Takeaways
- The capstone project is a chance to bring together everything we’ve learned.
- We are expected to create at least 3 features and 1 enhancement.
- Clean, modular code and a good user experience are essential.
- Weekly planning is important for pacing and managing scope.
- Creativity and polish will make my app stand out on Demo Day.

### Concept Connections
- Strong in: Tkinter GUI design, API usage, matplotlib graphing.
- Need more practice with: testing, packaging apps, error handling.
- Confident with `ttk`, `PIL`, and using `.env` for API keys.
- Learning how to organize large apps across multiple files and features.

### Early Challenges
- Managing multiple Tkinter frames and slide transitions.
- Getting the animated “moon friend” to appear only on the Almanac.
- Finding good moon phase data (solved with emoji chart workaround).
- Avoiding errors when the weather API returns incomplete data.

### Support Strategies
- Office hours for bug fixes and architecture help.
- Slack for live debugging and design feedback.
- Code reviews from peers and instructors if time allows.

---

## 🧠 Section 2: Feature Selection Rationale

| #  | Feature Name           | Difficulty (1–3) | Why You Chose It / Learning Goal                         |
|----|------------------------|------------------|----------------------------------------------------------|
| 1  | Current Weather Slide  | 2                | Display real-time weather from OpenWeatherMap API        |
| 2  | Forecast Slide         | 2                | Practice looping through forecast data & UI integration  |
| 3  | Graph Slide (Line)     | 3                | Use matplotlib with Tkinter to visualize temperature     |
| –  | Almanac Enhancement    | –                | Add moon phase emojis, sparkles, and retro visual charm  |

---

## 🗂️ Section 3: High-Level Architecture Sketch

### App Structure
- `main.py`: runs the app, handles navigation and layout
- `/features/`
  - `current_conditions.py`
  - `forecast.py`
  - `graph_view.py`
  - `almanac.py`
- `config.py`: loads environment variables
- `/data/`: text or JSON files (e.g. saved weather logs)
- `/assets/`: pixel art, gifs, fonts

### Data Flow
1. User enters a location → `main.py` → `get_weather(city)`
2. API returns data → passed to each frame
3. Slides update their widgets based on that data

---

## 📊 Section 4: Data Model Plan

| File/Table Name       | Format | Example Row                                 |
|-----------------------|--------|---------------------------------------------|
| weather_history.txt   | txt    | 2025-07-21,New Brunswick,82,Clear           |
| favorite_locations.json | json | ["New Brunswick", "Tokyo", "Miami"]         |

---

## 📆 Section 5: Personal Project Timeline (Weeks 12–17)

| Week | Monday       | Tuesday         | Wednesday       | Thursday        | Key Milestone         |
|------|--------------|------------------|------------------|------------------|------------------------|
| 12   | API setup    | Error handling   | Tkinter shell    | Buffer day       | Basic working app      |
| 13   | Feature 1    |                  |                  | Integrate        | Feature 1 complete     |
| 14   | Feature 2    |                  | Review & test    | Finish           | Feature 2 complete     |
| 15   | Feature 3    | Polish UI        | Error passing    | Refactor         | All features complete  |
| 16   | Enhancement  | Docs             | Tests            | Packaging        | Ready-to-ship app      |
| 17   | Rehearse     | Buffer           | Showcase         | –                | Demo Day               |

---

## ⚠️ Section 6: Risk Assessment

| Risk              | Likelihood | Impact | Mitigation Plan                                 |
|-------------------|------------|--------|--------------------------------------------------|
| API Rate Limit    | Medium     | Medium | Add simple cache and throttle updates           |
| Tkinter Crashes   | High       | Medium | Isolate slides, test each in isolation          |
| Font/Asset Issues | Medium     | High   | Use fallback fonts; test across systems         |

---

## 🤝 Section 7: Support Requests

- Help troubleshooting visibility issues with moon friend animation
- Font rendering and pixel-style text compatibility
- Testing weather location search on multiple machines
- Advice on packaging app for Windows showcase

---

## ✅ Section 8: Before Monday (Start of Week 12)

- [x] `main.py`, `config.py`, and `/data/` pushed to GitHub
- [x] `.env` file created (not committed) with `OPENWEATHERMAP_API_KEY`
- [x] Feature files created: `current_conditions.py`, `forecast.py`, `graph_view.py`, `almanac.py`
- [x] README.md includes description, install steps, and planned features
- [x] Office hour booked for moon friend glitch and `.env` errors

---
