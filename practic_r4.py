# practic_r4.py

#   Раздел 4. Объектно-ориентированное программирование (ООП)
# Тема 1: Классы и объекты


class Rectangle:
    """
    Класс Rectangle представляет прямоугольник с атрибутами width (ширина) и height (высота).
    """
    def __init__(self, width, height):
        # Метод __init__ вызывается при создании нового объекта.
        self.width = width
        self.height = height

    

    def area(self):
        """
        Метод для расчета площади прямоугольника.
        """
        return self.width * self.height


    def perimetr(self):
        """
        Метод для расчета периметра прямоугольника
        """
        return 2 * (self.width + self.height)


# Создание объекта (экземпляра класса Rectangle)
rec = Rectangle(5, 3)
print(f'Прямоугольник: ширина {rec.width}, высота {rec.height}')

# Использование методов класса
area1 = rec.area()
perim1 = rec.perimetr()
print(f'Площадь: {area1}')
print(f'Периметр: {perim1}')