with open('hello.txt', 'a', encoding='utf-8') as file:
    print('Введите ваш текст или "стоп" для завершения')

    txt = ""  # ✅ Инициализируем txt перед циклом
    while txt.lower() != 'стоп':  # ✅ Проверяем с учётом регистра
        txt = input()
        if txt.lower() != 'стоп':  # ✅ Не записываем "стоп" в файл
            file.write(f'{txt}\n')

    print('Ввод завершен')
