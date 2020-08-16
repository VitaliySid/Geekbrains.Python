# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.


class Matrix:
    __rank: int
    __matrix: list

    def __init__(self, *args: list):
        self.__rank = 0
        self.__matrix = []

        for i, lst in enumerate(args):
            if self.__rank == 0 or self.__rank == len(lst):
                self.__matrix.append(lst)

    def get_matrix_list(self):
        return self.__matrix

    def __str__(self):
        string = ''

        for lst in self.__matrix:
            string += str(lst) + '\n'

        return string

    def __repr__(self):
        self.__str__(self)

    def __add__(self, other):
        matrix_zip = [list(zarr) for zarr in zip(self.__matrix, other.get_matrix_list())]
        sum_lst = []
        for row in matrix_zip:
            sum_lst.append([sum(a) for a in map(list, zip(row[0], row[1]))])
        return Matrix(*sum_lst)


matrix1 = Matrix([1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3])
print(matrix1)

print('\n####################################')

matrix2 = Matrix([9, 8, 7, 6], [5, 4, 3, 2], [1, 9, 8, 7])
print(matrix2)

print('Сумма матриц: ')

matrix3 = matrix1 + matrix2
print(matrix3)
