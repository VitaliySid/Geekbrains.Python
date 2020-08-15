# 4.Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
from enum import Enum


class CarState(Enum):
    STOPPED = 1
    GOING = 2
    TURNS = 3

    def __str__(self):
        value = self.value

        if value == 1:
            return 'Остановилась'
        elif value == 2:
            return 'Поехала'
        elif value == 3:
            return 'Повернула'
        else:
            raise Exception('Состояние не найдено')


class CarColor(Enum):
    WHITE = 0
    BLACK = 1
    RED = 2
    BLUE = 3


class Car:
    __state: CarState = CarState.STOPPED

    def __init__(self, color: CarColor, name: str, is_police: bool):
        self.is_police = is_police
        self.name = name
        self.color = color
        self.speed = 0

    def go(self, speed: int):
        self.__state = CarState.GOING

        if 0 < speed < 200:
            self.speed = speed

    def stop(self):
        self.__state = CarState.STOPPED
        self.speed = 0

    def turn(self):
        self.__state = CarState.TURNS
        self.speed = 20

    def show_speed(self):
        print('Машина ', self.name)
        print('Текущее состояние: ', self.__state)
        print('Текущая скорость: ', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()

        if self.speed > 60:
            print('Внимание! Превышение скорости!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()

        if self.speed > 60:
            print('Внимание! Превышение скорости!')


class PoliceCar(Car):
    pass


car1 = TownCar(CarColor.BLACK, '1', False)
car2 = SportCar(CarColor.WHITE, '2', False)
car3 = WorkCar(CarColor.BLUE, '3', False)
car4 = PoliceCar(CarColor.RED, '4', True)

car1.show_speed()
car1.go(120)
car1.show_speed()
car1.stop()
car1.show_speed()

car2.turn()
car2.show_speed()
car2.go(199)
car2.show_speed()

car3.go(60)
car3.show_speed()

car4.show_speed()
