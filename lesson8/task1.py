# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, dateStr: str):
        self.dateString = dateStr

    @classmethod
    def parse_str(cls, date: 'Date'):
        arr = date.dateString.strip().split('-')
        return int(arr[0]), int(arr[1]), int(arr[2])

    @staticmethod
    def validate_str(day: int, month: int, year: int):
        if 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 2999:
            return True
        else:
            raise Exception('Некорректные данные')

    def __str__(self):
        return self.dateString


date = Date('12-12-2012')
if Date.validate_str(*Date.parse_str(date)):
    print('Введена корректная дата: ', date)

date1 = Date('13-13-2013')
if Date.validate_str(*Date.parse_str(date1)):
    print('Введена корректная дата: ', date1)

