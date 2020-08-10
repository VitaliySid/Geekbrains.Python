# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


def get_input_int(message):
    while True:
        input_str = input(message if message is not None else 'Введите число: ')

        if input_str.isnumeric():
            return int(input_str)


revenue = get_input_int('Введите значение выручки: ')
costs = get_input_int('Введите значение издержек: ')
profit = revenue - costs


print('Фирма отработала с ', 'прибылью' if profit > 0 else 'убытком')

if profit > 0:
    print('Рентабельность выручки: {:.2f}%'.format(profit / revenue * 100))

    number_of_employees = get_input_int('Введите количество сотрудников: ')

    profit_per_employer = profit / number_of_employees
    print('Прибыль фирмы в расчете на одного сотрудника: ', profit_per_employer)

