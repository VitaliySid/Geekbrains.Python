# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
from enum import Enum


class AppliancesTypes(Enum):
    Printer = 1
    Scanner = 2
    Xerox = 3


class StoreOverflowError(Exception):
    pass


class ShortageGoodsError(Exception):
    pass


class OfficeAppliancesStore:
    __count: int = 0
    __max_count: int = 0
    __appliances: {AppliancesTypes, list} = {}

    def __init__(self, max_count: int):
        self.__max_count = max_count

    def take(self, appliances: list):
        if len(appliances) + self.__count > self.__max_count:
            raise StoreOverflowError('Склад переполнен')

        for item in appliances:
            if isinstance(item, OfficeAppliances):
                if not item.type in self.__appliances:
                    self.__appliances[item.type] = []

                self.__appliances[item.type].append(item)
                self.__count += 1
                print(f'Товар {item.type} успешно освоен')

    def send_appliances(self, type: AppliancesTypes, count: int):
        goods = self.__appliances[type]

        if len(goods) < count:
            raise ShortageGoodsError('Недостаточно товара на складе')

        del self.__appliances[type][:count]
        print(f'Отправлено со склада {count} единиц техники {type}')

    def __str__(self):
        return str.join('\n', [f'{key}:{len(self.__appliances[key])}' for key in self.__appliances])


class OfficeAppliances:
    __type: AppliancesTypes
    __price: int

    def __init__(self, type: AppliancesTypes, price: int):
        self.__type = type
        self.__price = price

    @property
    def type(self):
        return self.__type


class Printer(OfficeAppliances):
    __color: bool

    def __init__(self, type: AppliancesTypes, price: int, color: bool):
        super().__init__(type, price)
        self.__color = color


class Scanner(OfficeAppliances):
    __speed: int

    def __init__(self, type: AppliancesTypes, price: int, speed: int):
        super().__init__(type, price)
        self.__speed = speed


class Xerox(OfficeAppliances):
    __color: int
    __speed: int

    def __init__(self, type: AppliancesTypes, price: int, speed: int, color: bool):
        super().__init__(type, price)
        self.__speed = speed
        self.__color = color


store = OfficeAppliancesStore(10)
printer = Printer(AppliancesTypes.Printer, 12000, True)
scanner = Scanner(AppliancesTypes.Scanner, 10000, 14000)
xerox = Xerox(AppliancesTypes.Xerox, 25000, 12000, False)

try:
    print(store)
    store.take([xerox, printer, printer, scanner, scanner, xerox, xerox, xerox])
    store.take([xerox, xerox, xerox])

except StoreOverflowError as ex:
    print(ex)
    print(store)

try:
    store.send_appliances(AppliancesTypes.Xerox, 2)
    store.send_appliances(AppliancesTypes.Printer, 2)
    store.send_appliances(AppliancesTypes.Scanner, 5)
except ShortageGoodsError as ex:
    print(ex)
    print(store)
