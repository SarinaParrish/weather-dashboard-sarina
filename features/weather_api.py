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

        from collections import defaultdict
        from datetime import datetime

        daily = defaultdict(list)
        for entry in forecasts:
            dt = datetime.fromtimestamp(entry["dt"])
            day_str = dt.strftime("%a")  # "Mon", "Tue", etc.
            main = entry["weather"][0]["main"]
            desc = entry["weather"][0]["description"]
            temp = entry["main"]["temp"]
            daily[day_str].append((main, desc, temp))

        result = []
        for i, (day, entries) in enumerate(daily.items()):
            conditions, descriptions, temps = zip(*entries)
            main_condition = max(set(conditions), key=conditions.count)
            desc_summary = max(set(descriptions), key=descriptions.count)
            result.append({
                "day": day,
                "main": main_condition,
                "desc": desc_summary,
                "high": round(max(temps)),
                "low": round(min(temps))
            })
            if len(result) == 5:
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
    
def get_weather(city, units="imperial"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ API error: {e}")
        return None
