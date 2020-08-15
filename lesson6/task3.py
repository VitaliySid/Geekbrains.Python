# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage:int, bonus:int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus'], self._income['bonus']


def print_position(position:Position):
    print('Сотрудник: ', position.get_full_name())

    salary, bonus = position.get_total_income()
    print(f'Зарплата(бонус): {salary}({bonus})')


position1 = Position('Иван', 'Иванов', 'Менеджер', 35000, 12000)
position2 = Position('Петр', 'Петров', 'Старший менеджер', 45000, 15000)
position3 = Position('Семен', 'Смирнов', 'Кассир', 30000, 9000)

print_position(position1)
print_position(position2)
print_position(position3)
