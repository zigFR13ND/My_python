from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Создаем экземпляр приложения. Аргумент __name__ помогает Flask определить, где искать ресурсы.
app = Flask(__name__)

# Конфигурация подключения к базе данных: база данных SQLite будет храниться в файле app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Конфигурация подключения к базе данных: база данных SQLite будет храниться в файле app.db
app.config['SQLALCHEMY_DATABASE_MODIFICATIONS'] = False

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
    id = db.Column(db.Integer, primary_kae=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"<Пользоватеь {self.name}>"
    

@app.route("/add_user/<name>/<ind:age>")
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
    users = User.query.all
    users_list = [{'id':user.id, 'user':user.name, 'age':user.age} for user in users]
    return users_list