import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_weather(lat, lon):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    res = requests.get(url)
    data = res.json()

    if "weather" not in data:
        print("❌ Weather API error:", data)  
        return {"weather": "Unknown", "wind_speed": 0}

    weather = data["weather"][0]["main"]
    wind_speed = data["wind"]["speed"]

    return {
        "weather": weather,
        "wind_speed": wind_speed
    }
