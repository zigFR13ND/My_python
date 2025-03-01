# my-first-project.py


print("Как тебя зовут?") 
name = input()

print("Сколько тебе лет?")
age = int(input())
print()

print(f'Привет, {name}! Тебе {age} лет.')
print()

av_point = 4.1
is_student = False


#print(f'Привет, Мир и {name}!')

#   1 Особенности типов данных
# Задание 1
print(f'''Имя: {name},
Возраст: {age},
Средний балл: {av_point},
{"Студент" if is_student else "Не студент"}''')

print()

books = ['1984', 'Над пропастью во ржи', 'Марсианин']

info = {'name': name, 'age': age, 'hobby': 'games'}

for key, value in info.items():
    print(key, value)

print()


#   2 Условные конструкции
# Задание 2
if age >= 18:
    index = 0
elif 13 <= age <= 17:
    index = 1
elif age <= 12:
    index = 2

print(f"Привет, {name}! Ты {('взрослый.', 'подросток', 'еще ребенок.')[index]}")
print()

#   3 Циклы
# Задание 3

total = 0
for i in range(1, 11):
    print("Итерация", i)
    total += i
print()
print("Итоговая сумма", total, end='\n')

print('Введите цифру, которая напоминает О')
n = int(input())
print()

while n != 0:
    print('Вы введли цифру:', n)
    print('Ты особенный, но попробуй еще раз.')
    n = int(input())
    print()
print('Вы введли цифру:', n)
print('Можешь собой гордиться! Цикл завершен.')
print()


#   4 Функции
# Задание 4


print('Введите 2 числа')
n1, n2 = int(input()), int(input())
def multiply(a, b):
    """
    Вычисляет произведение двух чисел.
    
    :param a: первое число
    :param b: второе число
    :return: строка с результатом произведения
    """
    return f'Произведение {a} и {b} = {a * b}'

print(multiply(n1, n2))
print()

print('Введите число, я сообщу: четное оно или нет')
n3 = int(input())
def is_even(a):
    """
    Определяет, является число четным или нечетным
    :param a: число на проверку
    """
    return f'Число {("нечетное", "четное")[a % 2 == 0]}'

print(is_even(n3))
print()

print('Введите 3 числа, а я найду самое большое среди них')
n4, n5, n6 = int(input()), int(input()), int(input())
print()
def get_max(a, b, c):
    '''
    Определяет максимальное число среди трех введенных
    :param a: первое число
    :param b: второе число
    :param c: третье число
    '''
    return f'Максимальное число: {max(a, b, c)}'
    
print(get_max(n4, n5, n6 ))
print()




