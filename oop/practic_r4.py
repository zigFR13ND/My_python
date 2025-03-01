# practic_r4.py

#   Раздел 4. Объектно-ориентированное программирование (ООП)
# Тема 1: Классы и объекты


class Rectangle:
    """
    Класс Rectangle представляет прямоугольник с атрибутами width (ширина) и height (высота).
    """
    def __init__(self, width, height):
        """
        Инициализирует новый экземпляр прямоугольника.
        
        :param width: Ширина прямоугольника
        :param height: Высота прямоугольника
        """
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами")
        self.width = width
        self.height = height

    

    def area(self):
        """
        Вычисляет площадь прямоугольника.
        
        :return: Площадь (width * height)
        """
        return self.width * self.height


    def perimetr(self):
        """
        Вычисляет периметр прямоугольника.
        
        :return: Периметр (2 * (width + height))
        """
        return 2 * (self.width + self.height)



class Employee:
    """
    Класс Employee представляет базового сотрудника.
    
    Attributes:
        name (str): Имя сотрудника.
        salary (int): Зарплата сотрудника.
    """
    def __init__(self, name, salary):
        """
        Инициализирует новый экземпляр сотрудника.
        
        :param name: Имя сотрудника
        :param salary: Зарплата сотрудника
        """
        self.name = name
        self.salary = salary

    def work(self):
        """
        Возвращает строку, описывающую работу сотрудника.
        
        :return: Строка с описанием работы.
        """
        return 'Сотрудник работает'


class Developer(Employee):
    """
    Класс Developer наследует Employee и добавляет атрибут programming_language.
    """
    def __init__(self, name, salary, programming_language):
        """
        Инициализирует нового разработчика.

        :param name: Имя разработчика
        :param salary: Зарплата разработчика
        :param programming_language: Язык программирования
        """
        super().__init__(name, salary)
        self.programming_language = programming_language

    
    def work(self):
        """
        Переопределяет метод work для разработчика.
        """
        return f'Разрабатывает программное обеспечение на {self.programming_language}'
        

class Designer(Employee):
    """
    Класс Designer наследует Employee и добавляет атрибут tool.
    """
    def __init__(self, name, salary, tool):
        """
        Инициализирует нового дизайнера.

        :param name: Имя дизайнера
        :param salary: Зарплата дизайнера
        :param tool: Инструмент дизайнера
        """
        super().__init__(name, salary)
        self.tool = tool


    def work(self):
        """
        Переопределяет метод work для дизайнера.
        """
        return f'Создаёт дизайн с помощью {self.tool}'

    

if __name__ == '__main__':
    # Создаем объект прямоугольника с заданными размерами
    rect = Rectangle(5, 3)
    
    # Выводим информацию о прямоугольнике: ширину и высоту
    print(f"Прямоугольник: ширина {rect.width}, высота {rect.height}")
    
    # Вычисляем и выводим площадь прямоугольника
    area = rect.area()
    print("Площадь:", area)
    
    # Вычисляем и выводим периметр прямоугольника
    perimeter = rect.perimetr()
    print("Периметр:", perimeter)

    # Создаем объект сотрудника с Именем и зарплатой.
    developer = Developer("Алексей", 80000, "Python")
    print(f'{developer.name} ({developer.__class__.__name__}): {developer.work()}')

    designer = Designer('Мария', 100000, 'Photoshop')
    print(f'{designer.name} ({designer.__class__.__name__}): {designer.work()}')
