# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


#region functions
def validate_x(x):
    try:
        val = float(x)

        return val if val > 0 else None

    except Exception:
        return None


def validate_y(y):
    try:
        val = int(y)

        return val if val < 0 else None

    except Exception:
        return None


def f_pow(x, y):
    res = 1

    for i in range(abs(y)):
        res *= x

    return res if y >= 0 else 1 / res
#endregion


while True:
    inp_x = input('Введите действительное положительное число x: ')
    inp_y = input('Введите целое отрицательное число y: ')

    x = validate_x(inp_x)
    y = validate_y(inp_y)

    if x is not None and y is not None:
        print('Результат: ', x ** y)
        print('Результат функции f_pow: ', f_pow(x, y))
        break
