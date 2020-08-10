# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


def calculate(n):
    return n + 11 * n + 111 * n


def calculate_with_parse(n):
    return n + int('{0}{0}'.format(n)) + int('{0}{0}{0}'.format(n))


while True:
    input_str = input('Введите число:')

    if input_str.isnumeric():
        total_seconds = int(input_str)

        print('Результат: ', calculate(total_seconds))
        print('Результат: ', calculate_with_parse(total_seconds))
        break
