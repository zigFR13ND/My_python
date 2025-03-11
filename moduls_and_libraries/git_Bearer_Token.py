import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

token = os.getenv("GITHUB_TOKEN")  # Получаем токен


headers = {"Authorization": f"Bearer {token}"}  # ✅ Передаём токен



# ===========================
# Проверка токена
# ===========================
if not token:  # Если нет локального .env, пробуем GitHub Secret
    token = os.getenv("GITHUB_ACTIONS_SECRET")

if not token:
    raise ValueError("❌ Токен не найден! Проверь .env или GitHub Secrets.")

print("✅ Токен загружен!")


# ===========================
# Получение информации о пользователе GitHub
# ===========================
username = input('Введите пользователя Github:\n')
url_git = f"https://api.github.com/users/{username}"  # 📌 GitHub API URL
response_url = requests.get(url_git)

if response_url.status_code == 200:
    user_data = response_url.json()
    print('Получение информации о пользователе GitHub:')
    print(f"👤 Пользователь: {user_data['login']}")
    print(f"📦 Публичные репозитории: {user_data['public_repos']}")
    print(f"📅 Дата создания аккаунта: {user_data['created_at']}")
else:
    print("❌ Ошибка! Пользователь не найден.")


# ===========================
# Запрос с Bearer Token (для личных данных)
# ===========================
url_token = "https://api.github.com/user"  # 📌 Запрос к ЛИЧНЫМ данным
response_token = requests.get(url_token, headers=headers)

if response_token.status_code == 200:
    user_data = response_token.json()
    print('\nЗапрос с Bearer Token (для личных данных) GitHub:')
    print(f"👤 Авторизованный пользователь: {user_data['login']}")
    print(f"📩 Email: {user_data.get('email', 'Скрыт')}")
else:
    print("❌ Ошибка! Проверьте токен.")