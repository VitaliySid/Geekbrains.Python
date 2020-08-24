# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.


class ArgumentException(Exception):
    pass


arr = []
while True:
    input_str = input('Введите значение:')

    try:
        if input_str.isnumeric():
            arr.append(int(input_str))
        elif input_str.strip() == 'stop':
            break
        else:
            raise ArgumentException('Введены некорректные данные')

    except ArgumentException as ex:
        print(ex)

print('Результат: ', arr)
