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

[print(txt, info[txt]) for txt in info]
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

[print(i) for i in range(1, 11)]