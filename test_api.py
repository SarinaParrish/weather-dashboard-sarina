from features.weather_api import get_weather

print("Testing API call...")

data = get_weather("Denver")

if data:
    print("✅ Success! Here's a snippet of the data:")
    print("City:", data.get("name"))
    print("Temperature:", data["main"].get("temp"), "°F")
    print("Weather:", data["weather"][0].get("description"))
else:
    print("❌ Failed to get data from API.")
