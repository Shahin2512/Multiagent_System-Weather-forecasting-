import tkinter as tk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather_by_city(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        return None
    return data

def get_weather_by_coords(lat, lon):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        return None
    return data

def show_weather():
    city = city_entry.get().strip()
    lat = lat_entry.get().strip()
    lon = lon_entry.get().strip()

    if city:
        data = get_weather_by_city(city)
    elif lat and lon:
        try:
            float(lat), float(lon)
        except ValueError:
            messagebox.showerror("Invalid Input", "Latitude and Longitude must be numbers.")
            return
        data = get_weather_by_coords(lat, lon)
    else:
        messagebox.showerror("Input Required", "Please enter either a City or Latitude & Longitude.")
        return

    if data:
        weather = data['weather'][0]['main']
        wind_speed = data['wind']['speed']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        result_label.config(
        text=f"🌤️ Weather: {weather}\n"
             f"🌡️ Temperature: {temperature} °C\n"
             f"💨 Wind Speed: {wind_speed} m/s\n"
             f"💧 Humidity: {humidity}%"
        )
    else:
        result_label.config(text="❌ Could not fetch weather data.")

# UI setup
root = tk.Tk()
root.title("Weather Checker")

tk.Label(root, text="Enter City Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
city_entry = tk.Entry(root, width=30)
city_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Or Latitude:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
lat_entry = tk.Entry(root, width=30)
lat_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Longitude:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
lon_entry = tk.Entry(root, width=30)
lon_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="Get Weather", command=show_weather).grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.grid(row=4, columnspan=2, pady=10)

root.mainloop()
