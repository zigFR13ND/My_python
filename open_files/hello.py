with open('hello.txt', 'w', encoding='utf-8') as file:
    file.write('Привет, это мой первый файл!\n')

with open('hello.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

with open('hello.txt', 'a', encoding='utf-8') as file:
    file.write("Добавляем еще текст.\n")  # ✅ Добавляем перенос строки

with open('hello.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()  # ✅ Теперь читаем ВСЕ строки
    print(content)  # Выведет список строк
