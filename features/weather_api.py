# features/weather_api.py

import requests
from config import API_KEY

import requests
from datetime import datetime
from collections import defaultdict

def get_forecast(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=imperial"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        forecasts = data.get("list", [])

        # Group forecasts by day
        daily = defaultdict(list)
        for entry in forecasts:
            dt = datetime.fromtimestamp(entry["dt"])
            day_str = dt.strftime("%a")  # e.g., 'Mon'
            main = entry["weather"][0]["main"]
            daily[day_str].append(main)

        # Reduce to top 3 days
        result = []
        for i, (day, conditions) in enumerate(daily.items()):
            # Get most common weather condition for the day
            main_condition = max(set(conditions), key=conditions.count)
            result.append({"day": day, "main": main_condition})
            if len(result) == 3:
                break

        return result

    except Exception as e:
        print(f"❌ Forecast API error: {e}")
        return None

def get_user_city():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        return data.get("city", "New York")  # default fallback
    except Exception as e:
        print("🌐 Could not get location from IP:", e)
        return "New York"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ API error: {e}")
        return None
