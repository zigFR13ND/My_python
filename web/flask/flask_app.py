# flask_app.py
#   Раздел 5. Веб-разработка с Python (Flask)


# Импортируем класс Flask и необходимые функции из модуля flask.
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy


# Создаем экземпляр приложения. Аргумент __name__ помогает Flask определить, где искать ресурсы.
app = Flask(__name__)

# Конфигурация подключения к базе данных: база данных SQLite будет храниться в файле app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Отключаем уведомления об изменениях (не обязательный параметр)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация ORM
db = SQLAlchemy(app)

class User(db.Model):
    """
    Модель User представляет таблицу пользователей.
    Поля:
      - id: уникальный идентификатор (целое число, первичный ключ)
      - name: имя пользователя (строка)
      - age: возраст пользователя (целое число)
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"<User {self.name}>"
    

@app.route("/add_user/<name>/<int:age>")
def add_user(name, age):
    """
    Добавляет нового пользователя в базу данных.
    
    URL: /add_user/<name>/<age>
    :param name: Имя пользователя.
    :param age: Возраст пользователя.
    :return: Строка с сообщением об успешном добавлении.
    """
    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()
    return f"User {name} added successfully!"


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
if __name__ == "__main__":
    # Создание всех таблиц (если они ещё не созданы)
    with app.app_context():
        db.create_all()
    # Запуск приложения в режиме отладки (для разработки)
    app.run(debug=True)