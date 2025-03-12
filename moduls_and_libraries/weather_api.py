import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

API_KEY = os.getenv('WEATHER_API_KEY')  # Получаем токен


# 🔍 Определяем IP и местоположение (широта и долгота)
geo_url = 'http://ip-api.com/json/?lang=ru'
geo_response = requests.get(geo_url)
geo_data = geo_response.json()

if geo_response.status_code == 200 and geo_data['status'] == 'success':
    city = geo_data['city']  # Получаем город
    country = geo_data['country']  # Получаем страну
    lat, lon = geo_data['lat'], geo_data['lon'] # ✅ Широта и долгота
    print(f'🌍 Определено местоположение: {city}, {country}, (Ш: {lat}, Д: {lon})')
else:
    print("❌ Ошибка! Не удалось определить местоположение.")
    exit()  # Завершаем программу, если город не определён

weather_today_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru'
weather_today_response = requests.get(weather_today_url)

if weather_today_response.status_code == 200:
    weather_today = weather_today_response.json()
    print(f"\n 📍 Город: {weather_today['name']}")
    print(f" 🌡  Температура: {weather_today['main']['temp']}°C")
    print(f" 💨 Ветер: {weather_today['wind']['speed']} м/с")
    print(f" 🌤  Описание: {weather_today['weather'][0]['description']}")
else:
    print(f'❌ Ошибка {weather_today_response.status_code}! Проверь API-ключ или название города.')


weather_5days_url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ru'
weather_5days_response = requests.get(weather_5days_url)

if weather_5days_response.status_code == 200:
    weather_5days = weather_5days_response.json()
    print(f"\nПрогноз погоды на 5 дней в {city}:")
    for i in range(0, len(weather_5days['list']), 8):
        day = weather_5days['list'][i]
        date = day["dt_txt"].split()[0]  # 📅 Дата
        temp = day['main']['temp'] # 🌡 Температура
        wind = day['wind']['speed'] # 💨 Ветер
        description = day["weather"][0]["description"]  # 🌤 Описание
        humidity = day["main"]["humidity"]  # 💧 Влажность
        pressure = day["main"]["pressure"]  # 📊 Давление

        print(f"📅 {date}  🌡 {temp} °C  💨 {wind} м/с  🌤 {description}  💧 {humidity} %  📊 {pressure} гПа")

else:
    print(f"❌ Ошибка {weather_5days_response.status_code}! Проверь API-ключ.")