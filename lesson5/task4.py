# 4. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


int_list = []

str = input('Введите набор чисел через пробел " ": ')
int_list = [int(item) for item in str.split(' ') if item.isnumeric()]

try:
    with open('task4.txt', 'a', encoding='utf-8') as f_stream:
        print(f'Начальный список: {int_list}')
        print(f'Начальный список: {int_list}\n', file=f_stream)

        print(f'Сумма чисел: {sum(int_list)}')
        print(f'Сумма чисел: {sum(int_list)}\n', file=f_stream)

except IOError:
    print('Ошибка при записи файла')
