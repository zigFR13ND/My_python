# practic_r4.py

def count_lines_and_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = 0
        words = 0
        for line in file:
            lines += 1
            words += len(line.split())
            
        with open('result.txt', 'w', encoding='utf-8') as result:
            result.write(f'Количество строк: {lines}\n')
            result.write(f'Количество слов: {words}\n')
    


count_lines_and_words('data.txt')