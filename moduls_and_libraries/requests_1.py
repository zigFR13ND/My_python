import requests
import json  # Для красивого вывода JSON

# ===========================
# 1. ПРОСТОЙ GET-ЗАПРОС
# ===========================
response_get = requests.get("https://httpbin.org/get")  # Отправляем GET-запрос
print("\n📌 1. Простой GET-запрос")
print(json.dumps(response_get.json(), indent=4, ensure_ascii=False))  # Выводим JSON-ответ

# ===========================
# 2. GET-ЗАПРОС С ПАРАМЕТРАМИ
# ===========================
params = {"name": "Ильнур", "age": 33}  # Передаём параметры запроса
response_params = requests.get("https://httpbin.org/get", params=params)  # Отправляем GET-запрос с параметрами
print("\n📌 2. GET-запрос с параметрами")
print("URL запроса:", response_params.url)  # Выводим URL с параметрами
print(json.dumps(response_params.json(), indent=4, ensure_ascii=False))  # Выводим JSON-ответ

# ===========================
# 3. POST-ЗАПРОС (data={})
# ===========================
data_post = {"username": "Ilnur", "password": "12345"}  # Данные для отправки
response_post = requests.post("https://httpbin.org/post", data=data_post)  # Отправляем POST-запрос с data={}
print("\n📌 3. POST-запрос (data={})")
print(json.dumps(response_post.json(), indent=4, ensure_ascii=False))  # Выводим JSON-ответ

# ===========================
# 4. POST-ЗАПРОС (json={})
# ===========================
response_post_json = requests.post("https://httpbin.org/post", json=data_post)  # Отправляем POST-запрос с json={}
print("\n📌 4. POST-запрос (json={})")
print(json.dumps(response_post_json.json(), indent=4, ensure_ascii=False))  # Выводим JSON-ответ

# ===========================
# 5. PUT-ЗАПРОС (Обновление данных)
# ===========================
data_put = {"username": "Ilnur", "password": "newpassword"}  # Обновляемые данные
response_put = requests.put("https://httpbin.org/put", json=data_put)  # Отправляем PUT-запрос с json={}
print("\n📌 5. PUT-запрос (Обновление данных)")
print(json.dumps(response_put.json(), indent=4, ensure_ascii=False))  # Выводим JSON-ответ

# ===========================
# 6. DELETE-ЗАПРОС (Удаление данных)
# ===========================
data_delete = {"username": "Ilnur"}  # Данные для удаления
response_delete = requests.delete("https://httpbin.org/delete", json=data_delete)  # Отправляем DELETE-запрос
print("\n📌 6. DELETE-запрос (Удаление данных)")
print(json.dumps(response_delete.json(), indent=4, ensure_ascii=False))  # Выводим JSON-ответ

# ===========================
# 7. ПРОВЕРКА УДАЛЕНИЯ ПОСТА
# ===========================
post_id = 1  # ID удаляемого поста
delete_response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')  # Отправляем DELETE-запрос
print("\n📌 7. Удаление поста (JSONPlaceholder)")
print("Статус-код:", delete_response.status_code)  # Выводим статус-код удаления

get_response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')  # Проверяем, удалён ли пост
print("Статус-код после удаления:", get_response.status_code)  # Выводим статус-код повторного GET-запроса
if get_response.status_code == 404:
    print("✅ Пост успешно удалён!")  # Если 404, значит пост удалён
else:
    print("❌ Пост всё ещё существует! (JSONPlaceholder не удаляет данные)")

# ===========================
# 8. ЗАПРОС С Bearer Token
# ===========================
url = 'https://httpbin.org/bearer'
headers_bearer = {"Authorization": "Bearer your_api_token_123"}  

print("\n📌 8. Запрос с Bearer Token:")

try:
    response_bearer = requests.get(url, headers=headers_bearer)

    if response_bearer.status_code == 401:
        print("❌ Неверный токен! Доступ запрещён.")
    else:
        print("✅ Токен верный! Доступ разрешён.")
        print(response_bearer.json())  # Выводим ответ
except requests.exceptions.RequestException as e:
    print(f"⚠ Ошибка соединения: {e}")