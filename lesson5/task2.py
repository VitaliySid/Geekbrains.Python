# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

row_count = 0
words_count = {}

try:
    with open('task2.txt', 'r') as f_stream:
        for str in f_stream:
            row_count += 1
            words_count[row_count] = len(str.split(' '))

except IOError:
    print('Ошибка чтения файла')

for key in words_count.keys():
    print(f'Строка номер {key}, количество слов - {words_count[key]}')

print('Сумма строк:', row_count)
