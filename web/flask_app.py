# flask_app.py
#   Раздел 5. Веб-разработка с Python (Flask)


# Импортируем класс Flask и необходимые функции из модуля flask.
from flask import Flask, render_template, jsonify


# Создаем экземпляр приложения. Аргумент __name__ помогает Flask определить, где искать ресурсы.
app = Flask(__name__)


# Декоратор @app.route("/") указывает, что функция ниже должна обрабатывать запросы к URL "/".
@app.route("/")
def home():
    # Функция home возвращает HTML-строку. Здесь мы просто выводим заголовок и параграф.
    return "<h1>Добро пожаловать в Flask Demo!</h1><p>Это учебное приложение на Flask.</p>"


# Маршрут для API, который возвращает данные в формате JSON.
@app.route("/api/info")
def api_info():
    # Функция jsonify превращает словарь в корректный JSON-ответ.
    return jsonify({"app": "Flask Demo", "version": "1.0"})


# Еще один маршрут, который принимает параметр из URL.
@app.route("/greet/<name>")
def greet(name):
    # Здесь функция greet принимает переменную name из URL и вставляет её в строку приветствия.
    return f'<h1>Hello, {name}!</h1>'


# Этот блок гарантирует, что приложение запустится только если файл запускается напрямую.
if __name__ == '__main__':
    app.run(debug=True)