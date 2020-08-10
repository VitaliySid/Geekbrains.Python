# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


str_list = []
while True:
    str = input('Введите строку: ')

    if str.strip() == '':
        print('Ввод окончен')
        break

    str_list.append(str+'\n')

try:
    with open('task1.txt', 'a') as f_stream:
        f_stream.writelines(str_list)
except IOError:
    print('Ошибка при записи файла')

try:
    with open('task1.txt', 'r') as f_stream:
        for line in f_stream:
            print(line)
except IOError:
    print('Ошибка при чтении ')
