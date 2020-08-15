# 5. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

# ОЧЕНЬ СТРАННОЕ ЗАДАНИЕ, СДЕЛАЮ КАК ПРОДОЛЖЕНИЕ ПРЕДЫДУЩЕГО
from lesson6.task4 import TownCar, CarColor, Car


def print_car(car:Car):
    print(f'Машина {car.name}, скорость {car.speed}, цвет {car.color}, '
          f'полицейская машина {"Да" if car.is_police else "Нет"}')


car1 = TownCar(CarColor.RED, '1', False)
car2 = TownCar(CarColor.WHITE, '2', False)

print_car(car1)
print_car(car2)

car1.color = CarColor.BLUE
car1.speed = 120
print(car1)

car2.is_police = True
car2.speed = 60
car2.name = '777'
print(car2)
