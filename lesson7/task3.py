# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и целочисленное (с округлением до целого) деление клеток, соответственно.


class OrganicCell:

    @property
    def cores(self):
        return self.__cores

    def __init__(self, cores: int):
        self.__cores = cores if cores > 0 else 0

    def __add__(self, other: 'OrganicCell'):
        return OrganicCell(self.__cores + other.cores)

    def __sub__(self, other: 'OrganicCell'):
        if self.__cores < other.cores:
            return 'Результат разности клеток должен быть положительный'

        return OrganicCell(self.__cores - other.cores)

    def __mul__(self, other):
        return OrganicCell(self.__cores * other.cores)

    def __truediv__(self, other):
        return OrganicCell(self.__cores // other.cores)

    def __str__(self):
        return f'Количество ядер клетки {self.__cores}'

    def make_order(self, count: int):
        v_str = ''

        if self.__cores // count > 0:
            v_str += r'\n'.join(['*' * count for i in range(self.__cores // count)])

        if self.__cores % count > 0:
            v_str += r'\n' + '*' * (self.__cores % count)

        return v_str


cell1 = OrganicCell(2)
cell2 = OrganicCell(12)
cell3 = OrganicCell(8)
cell4 = OrganicCell(5)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell2 - cell3)
print(cell1 * cell4)
print(cell2 / cell1)
print(cell1 / cell2)

print(cell2.make_order(5))
