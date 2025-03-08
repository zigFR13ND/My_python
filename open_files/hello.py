try:
    with open('hello.txt', 'a', encoding='utf-8') as file: 
        print('Введите ваш текст или "стоп" для завершения') 

        while True: 
            txt = input().strip()  # ✅ Убираем лишние пробелы 

            if txt.lower() == 'стоп':  # ✅ Проверяем "стоп" (регистр неважен) 
                print('Ввод завершен') 
                break  # ✅ Выходим из цикла 

            if txt:  # ✅ Если строка НЕ пустая, записываем 
                file.write(f'{txt}\n')

    # ✅ Если всё прошло успешно, читаем файл
    with open('hello.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print("\nСодержимое файла:")
        print(content)

except KeyboardInterrupt:  # ✅ Теперь Ctrl+C правильно обрабатывается
    print("\nВы прервали ввод. Программа завершена.")

except Exception as e:  # ✅ Ловим все другие ошибки
    print(f"Ошибка: {e}")  
