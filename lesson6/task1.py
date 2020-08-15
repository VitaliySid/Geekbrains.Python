# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
import time


class TrafficLight:
    __color: str
    counter: int = 0
    red_time: int
    yellow_time: int
    green_time: int

    def __init__(self, red_time=7, yellow_time=2, green_time=15):
        self.red_time = red_time
        self.yellow_time = red_time + yellow_time
        self.green_time = self.yellow_time + green_time

    def running(self):
        self.counter = 0
        color_time = 0

        while True:
            if self.counter <= self.red_time:
                self.__color = 'Красный'
                color_time = self.red_time-self.counter

            elif self.counter <= self.yellow_time:
                self.__color = 'Желтый'
                color_time = self.yellow_time - self.counter
            else:
                self.__color = 'Зеленый'
                color_time = self.green_time - self.counter

                if self.counter >= self.green_time:
                    self.counter = 0

            print(f'\r{self.__color} {color_time}', end='')
            self.counter += 1
            time.sleep(1)


trafficLight = TrafficLight()
trafficLight.running()
