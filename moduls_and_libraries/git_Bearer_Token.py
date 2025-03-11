import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

token = os.getenv("GITHUB_TOKEN")  # Получаем токен
url = "https://api.github.com/user"
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)
print(response.json())
