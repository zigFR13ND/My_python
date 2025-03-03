import unittest
from flask_app import app, db, User

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Настраиваем тестовый клиент и базу данных
        self.app = app.test_client()
        # Перед каждым тестом создаем новую базу данных в памяти
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Очистка базы данных после каждого теста
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home(self):
        # Тест главной страницы
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Добро пожаловать в Flask Demo!', response.data)

    def test_add_user(self):
        # Тест добавления пользователя
        response = self.app.get('/add_user/TestUser/25')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Пользователь TestUser успешно создан!', response.data)

        # Проверка, что пользователь появился в базе
        with app.app_context():
            user = User.query.filter_by(name="TestUser").first()
            self.assertIsNotNone(user)
            self.assertEqual(user.age, 25)

    def test_get_users(self):
        # Сначала добавим пару пользователей
        self.app.get('/add_user/Alice/30')
        self.app.get('/add_user/Bob/40')
        # Затем получим список пользователей
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        # Проверяем, что в ответе содержатся имена Alice и Bob
        self.assertIn(b'Alice', response.data)
        self.assertIn(b'Bob', response.data)

if __name__ == '__main__':
    unittest.main()
