# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


try:
    persons = []
    salaries = []

    with open('task3.txt', 'r', encoding='utf-8') as f_stream:
        for str in f_stream:
            row = str.rstrip('\n').split(' ')
            salary = int(row[1])

            if salary < 20000:
                persons.append((row[0], row[1]))

            salaries.append(salary)

    if len(persons):
        print('Сотрудники с зарплатой менее 20тыс.:\n')

        for person in persons:
            print(f'{person[0]}-{person[1]} тыс.')

    print('Средняя зарплата сотрудников: ', sum(salaries) / len(salaries))

except IOError:
    print('Ошибка чтения файла')
