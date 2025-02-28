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
{("Не студент", "Студент")[is_student]}''')
print()

books = ['1984', 'Над пропастью во ржи', 'Марсианин']

info = {'name': name, 'age': age, 'hobby': 'games'}

for key in info:
    print(key, info[key])

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
c, d = int(input()), int(input())
def multiply(a, b):
    return f'Произведение {a} и {b} = {a * b}'

print(multiply(c, d))
print()

print('Введите число, я сообщу: четное оно или нет')
e = int(input())
def is_even(a):
    return f'Число {("нечетное", "четное")[a % 2 == 0]}'

print(is_even(e))
print()

print('Введите 3 числа, а я найду самое большое среди них')
g, f, r = int(input()), int(input()), int(input())
print()
def get_max(a, b, c):
    return f'Максимальное число: {max(a, b, c)}'
    
print(get_max(g, f, r))
print()




