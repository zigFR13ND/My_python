import requests


#   Простой GET-запрос
response = requests.get("https://httpbin.org/get")  # Отправляем GET-запрос
print(response.text)  # Выводим ответ сервера


#   Разбор ответа сервера (JSON)
response = requests.get("https://httpbin.org/get")
data = response.json()  # Преобразуем ответ в словарь

print(data)  # Выводим JSON
print(data["headers"])  # Получаем заголовки запроса
