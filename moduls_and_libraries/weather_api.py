import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

API_KEY = os.getenv("WEATHER_API_KEY")  # Получаем токен


# 🔍 Определяем IP и местоположение
geo_response = requests.get("http://ip-api.com/json/")
geo_data = geo_response.json()
city = geo_data["city"]  # Получаем город

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"

response = requests.get(url)

if response.status_code == 200:
    weather = response.json()  # ✅ Преобразуем в JSON (dict)
    print(weather)  # 🔍 Выведем полный JSON, чтобы проверить его структуру
    
    if isinstance(weather, list):  # ✅ Если API вернул список, берём первый элемент
        weather = weather[0]

    print(f"📍 Город: {weather['name']}")  
    print(f"🌡 Температура: {weather['main']['temp']}°C")
    print(f"🌤 Описание: {weather['weather'][0]['description']}")
else:
    print(f"❌ Ошибка {response.status_code}! Проверь API-ключ или название города.")

