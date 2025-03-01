# theory_3.py

#   Раздел 3. Функции, модули и работа с файлами

#   1. Функции
# Практическое задание 1

def subtract(a, b):
    # принимает два числа и возвращает их разность
    return f'{a} - {b} = {a - b}'


def power(base, exp):
    # вычисляет значение base^exp (целая степень)
    return f'{base} ^ {exp} = {base ** exp}'

def is_odd(n):
    # возвращает строку "Нечетное", если число нечетное, и "Четное", если число четное.
    return f'Введенное число {("нечетное", "четное")[n % 2 == 0]}'

#print('Введите два числа')
#n1, n2 = int(input()), int(input())
#print(subtract(n1, n2))
#print()

#print('Введите два числа')
#n3, n4 = int(input()), int(input())
#print(power(n3, n4))
#print()


#print('Введите число')
#n5 = int(input())
#print(is_odd(n5))
#print()