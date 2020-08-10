# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].


try:
    statistics = {}
    average = {}

    with open('task7.txt', 'r', encoding='utf-8') as f_stream:
        for str in f_stream:
            row = str.rstrip('\n').split(' ')
            profit = 0

            statistics[row[0]] = int(row[2])-int(row[3])

        firm_with_profit = [item for item in statistics.values() if item >= 0]
        average['average_profit'] = sum(firm_with_profit) / len(firm_with_profit)
        my_list = [statistics, average]

        print(my_list)
except IOError:
    print('Ошибка чтения файла')


