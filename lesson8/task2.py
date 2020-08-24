# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.


class ZeroDivisionException(Exception):
    pass


class ArgumentException(Exception):
    pass


while True:
    number1_str = input('Введите первое число:')
    number2_str = input('Введите второе число:')

    try:
        if number1_str.isnumeric() and number2_str.isnumeric():
            number1 = int(number1_str)
            number2 = int(number2_str)

            if number2 == 0:
                raise ZeroDivisionException('Ошибка деления на ноль')
            else:
                print('Результат: ', number1/number2)
                break
        else:
            raise ArgumentException('Введены некорректные данные')

    except ZeroDivisionException as ex:
        print(ex)
    except ArgumentException as ex:
        print(ex)
