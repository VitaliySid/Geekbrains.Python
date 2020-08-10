# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

from lesson4.validators import validate_float


def calculate_salary(hours=0.0, rate=0.0, bonus=0.0):
    return hours * rate + bonus


(hours, rate, bonus) = argv[1:]

is_valid_hours, v_hours = validate_float(hours)
is_valid_rate, v_rate = validate_float(rate)
is_valid_bonus, v_bonus = validate_float(bonus)

if is_valid_hours and is_valid_rate and is_valid_bonus:
    print(calculate_salary(v_hours, v_rate, v_bonus))
