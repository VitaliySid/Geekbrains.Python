# 5. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб)
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
from functools import reduce


def parse_hour(str=''):
    number = str.split('(')[0]

    return int(number) if number.isnumeric() else 0


try:
    disciplines = {}

    with open('task5.txt', 'r', encoding='utf-8') as f_stream:
        for str in f_stream:
            row = str.rstrip('\n').split(':')
            sum=0
            
            for item in row[1].strip().split(' '):
                sum+=parse_hour(item)

            disciplines[row[0]] = sum

        for key in disciplines.keys():
            print(f'{key} - {disciplines[key]} часов')

except IOError:
    print('Ошибка чтения файла')
