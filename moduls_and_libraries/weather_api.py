import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

API_KEY = os.getenv("WEATHER_API_KEY")  # Получаем токен


# 🔍 Определяем IP и местоположение
geo_url = "http://ip-api.com/json/?lang=ru"
geo_response = requests.get(geo_url)
geo_data = geo_response.json()

if geo_response.status_code == 200 and geo_data["status"] == "success":
    city = geo_data["city"]  # Получаем город
    country = geo_data["country"]  # Получаем страну
    print(f"🌍 Определено местоположение: {city}, {country}")
else:
    print("❌ Ошибка! Не удалось определить местоположение.")
    exit()  # Завершаем программу, если город не определён

weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
weather_response = requests.get(weather_url)

if weather_response.status_code == 200:
    weather = weather_response.json()
    print(f"📍 Город: {weather['name']}")
    print(f"🌡 Температура: {weather['main']['temp']}°C")
    print(f"💨 Ветер: {weather['wind']['speed']} м/с")
    print(f"🌤 Описание: {weather['weather'][0]['description']}")
else:
    print(f"❌ Ошибка {weather_response.status_code}! Проверь API-ключ или название города.")

