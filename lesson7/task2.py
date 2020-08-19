# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
from abc import ABC, abstractmethod


class ClothingCalculator(ABC):

    @abstractmethod
    def calculate_cloth_size(self) -> float:
        pass


class Costume(ClothingCalculator):

    def __init__(self, growth: int):
        self.__growth = growth

    @property
    def growth(self):
        return self.__growth

    @growth.setter
    def growth(self, growth):
        self.__growth = growth

    def calculate_cloth_size(self):
        return 2 * self.__growth + 0.3


class Coat(ClothingCalculator):

    def __init__(self, size: int):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def calculate_cloth_size(self):
        return self.__size / 6.5 + 0.5


class Calculator:

    def __init__(self, *args: ClothingCalculator):
        self.__calculators = args

    def calculate(self):
        for calc in self.__calculators:
            print('Размер ткани для одежды: ', calc.calculate_cloth_size())


costume1 = Costume(45)
costume2 = Costume(50)
costume3 = Costume(52)
coat1 = Coat(45)
coat2 = Coat(50)
coat3 = Coat(52)

calculator = Calculator(costume1, costume2, costume3, coat1, coat2, coat3)
calculator.calculate()