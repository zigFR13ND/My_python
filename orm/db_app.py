from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Создаем экземпляр приложения. Аргумент __name__ помогает Flask определить, где искать ресурсы.
app = Flask(__name__)

# Конфигурация подключения к базе данных: база данных SQLite будет храниться в файле app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
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
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"<Пользователь {self.name}>"
    

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
    return f'Пользователь {name} успешно создан!'


@app.route("/users")
def get_users():
    """
    Возвращает список всех пользователей в формате JSON.
    
    URL: /users
    :return: JSON-ответ со списком пользователей.
    """
    users = User.query.all()
    users_list = [{'id':user.id, 'user':user.name, 'age':user.age} for user in users]
    return jsonify(users_list)

@app.route("/")
def home():
    return "Добро пожаловать в Flask Demo!"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/api/info")
def api_info():
    return jsonify({"app": "Flask Demo", "version": "1.0"})


# Этот блок гарантирует, что приложение запустится только если файл запускается напрямую.
if __name__ == "__main__":
    # Создание всех таблиц (если они ещё не созданы)
    with app.app_context():
        db.create_all()
    # Запуск приложения в режиме отладки (для разработки)
    app.run(debug=True)