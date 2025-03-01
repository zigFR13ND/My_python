# main.py


import my_module
from theory_3 import is_odd

print('Введите Ваше имя')
print(my_module.say_hi(input()))
print()

print('Введите 2 числа')
print("Сумма:", my_module.add(int(input()), int(input())))
print()

print('Введите число')
print(is_odd(int(input())))
print()