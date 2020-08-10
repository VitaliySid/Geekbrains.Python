# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def f_division(val_1, val_2):
    try:
        return round(val_1 / val_2, 2)
    except ZeroDivisionError:
        print("Ошибка деления на ноль")


while True:
    number_1 = input('Введите первое число: ')
    number_2 = input('Введите второе число: ')

    if number_1.isnumeric() and number_2.isnumeric():
        print('Результат: ', f_division(int(number_1), int(number_2)))

        break
