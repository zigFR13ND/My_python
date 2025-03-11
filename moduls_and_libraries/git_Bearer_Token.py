import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

token = os.getenv("GITHUB_TOKEN")  # Получаем токен

if not token:  # Если нет локального .env, пробуем GitHub Secret
    token = os.getenv("GITHUB_ACTIONS_SECRET")

if not token:
    raise ValueError("❌ Токен не найден! Проверь .env или GitHub Secrets.")

print("✅ Токен загружен!")
