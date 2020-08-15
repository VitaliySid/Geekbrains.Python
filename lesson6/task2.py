# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def get_attributes(self):
        return self._length, self._width


class RoadCalculator:
    def __init__(self, weight, thickness):
        self._weight = weight
        self._thickness = thickness

    def calculate_asphalt_weight(self, road: Road):
        length, width = road.get_attributes()

        total_weight = length * width * self._weight * self._thickness
        print(f'Для построения дороги {width}м * {length}м необходимо {total_weight} тонн асфальта')

        return total_weight


calculator = RoadCalculator(25, 5)
road1 = Road(20, 5000)
road2 = Road(25, 10000)
road3 = Road(15, 100000)

calculator.calculate_asphalt_weight(road1)
calculator.calculate_asphalt_weight(road2)
calculator.calculate_asphalt_weight(road3)