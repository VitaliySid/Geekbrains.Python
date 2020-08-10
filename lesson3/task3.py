# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(x=0, y=0, z=0):
    if x > y:
        return x + (y if y > z else z)

    return y + (x if x > z else z)


while True:
    a = input('Введите число a: ')
    b = input('Введите число b: ')
    c = input('Введите число c: ')

    if a.isnumeric() and b.isnumeric() and c.isnumeric():
        print('Результат: ', my_func(int(a), int(b), int(c)))
        break
