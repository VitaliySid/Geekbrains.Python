# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.


def get_input_int(message):
    while True:
        input_str = input(message if message is not None else 'Введите число: ')

        if input_str.isnumeric():
            return int(input_str)


distance = get_input_int('Введите результат пробежки в первый день: ')
final_distance = get_input_int('Введите желаемый результат пробежки: ')
day = 1

while True:
    print('{}-й день: {:.2f} км.'.format(day, distance))

    if distance >= final_distance:
        break

    day += 1
    distance += distance * 0.1

print('Ответ: на {}-й день спортсмен достиг результата — не менее {} км'.format(day, final_distance))
