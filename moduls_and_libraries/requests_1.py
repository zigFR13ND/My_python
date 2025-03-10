import requests

##  GET — это запрос на получение данных с сервера (например, загрузка веб-страницы).
#
#
#   Простой GET-запрос
response = requests.get("https://httpbin.org/get")  # Отправляем GET-запрос
print(response.text)  # Выводим ответ сервера

#   Разбор ответа сервера (JSON)
data = response.json()  # Преобразуем ответ в словарь
print("\n📌 Выводим JSON:")
print(data)  # Выводим JSON
print("\n📌 Получаем заголовки запроса:")
print(data["headers"])  # Получаем заголовки запроса

# Можно передавать параметры запроса (например, name=Ильнур)
params = {"name": "Ильнур", "age": 33}
response_2 = requests.get("https://httpbin.org/get", params=params)
print("\n📌 Response 2 (URL с параметрами):")
print(response_2.url)  # URL с параметрами
# Сервер получит https://httpbin.org/get?name=Ильнур&age=25.

data_2 = response_2.json() 
print(f"\nИмя: {data_2['args']['name']}\nВозраст: {data_2['args']['age']}")

#🔹 requests.get(URL) — отправляет GET-запрос.
#🔹 response.text — получает ответ в виде строки.
#🔹 response.json() — превращает JSON-ответ в словарь.
#🔹 params={} — передаёт параметры запроса.


##  POST-запрос используется для отправки данных (например, формы на сайте или запроса к API).
#
# GET передаёт параметры в URL (?key=value), а POST передаёт данные в теле запроса.

# POST-запрос с requests.post()
data_3 = {"username": "Ilnur", "password": "12345"}  # Данные для отправки
response_3 = requests.post("https://httpbin.org/post", data=data_3)
print("\n📌 Response 3 (data={}):")
print(response_3.json())  # Вывод ответа сервера


#  Отправка JSON-данных (json={})
data_4 = {"username": "Ilnur", "password": "12345"}  # JSON-данные
response_4 = requests.post("https://httpbin.org/post", json=data_4)
print("\n📌 Response 4 (json={}):")
print(response_4.json())  # Вывод JSON-ответа


# data={} → отправляет как обычные формы (x-www-form-urlencoded). Используется, если сервер ожидает обычные HTML-формы (как на сайтах).  Данные отправляются в теле запроса в виде key=value&key=value.
#  Когда использовать? Если API или сайт принимает обычные формы (Content-Type: application/x-www-form-urlencoded). Например, если нужно авторизоваться на сайте через requests.

# json={} → отправляет как JSON (application/json). Используется, если сервер ожидает JSON-формат (Content-Type: application/json). Данные отправляются как {"key": "value"} в теле запроса.
#  Когда использовать? Если API требует JSON (Content-Type: application/json). Например, если работаешь с Telegram API, VK API, GitHub API.

#💡 Главное правило:

# Если сервер ждёт HTML-форму → используй data={}.   "form"	Обычные формы (например, авторизация на сайте)
# Если сервер ждёт JSON → используй json={}.          API, которые принимают JSON (например, Telegram API)


