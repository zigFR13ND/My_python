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


if __name__ == '__main__':
    # Создаем объект прямоугольника с заданными размерами
    rect = Rectangle(5, 3)
    
    # Выводим информацию о прямоугольнике: ширину и высоту
    print(f"Прямоугольник: ширина {rect.width}, высота {rect.height}")
    
    # Вычисляем и выводим площадь прямоугольника
    area = rect.area()
    print("Площадь:", area)
    
    # Вычисляем и выводим периметр прямоугольника
    perimeter = rect.perimeter()
    print("Периметр:", perimeter)
