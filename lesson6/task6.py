# 6. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    __title: str

    def __init__(self, title):
        self.__title = title

    def draw(self):
        print('Запуск отрисовки.')

    def print_title(self):
        print('Title: ', self.__title)


class Pen(Stationery):
    def draw(self):
        self.print_title()
        print('Запуск отрисовки ручкой. ')


class Pencil(Stationery):
    def draw(self):
        self.print_title()
        print('Запуск отрисовки карандашом. ')


class Handle(Stationery):
    def draw(self):
        self.print_title()
        print('Запуск отрисовки маркером. ')


stationery1 = Pen('Синяя ручка')
stationery2 = Pencil('Серый карандаш')
stationery3 = Handle('Черный маркер')

stationery1.draw()
stationery2.draw()
stationery3.draw()
