# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
from typing import Dict, List, Any

goods = []

while True:
    name = input('Введите наименование товара: ')
    cost = input('Введите цену: ')
    count = input('Введите количество: ')
    unit = input('Введите единицу измерения: ')

    goods.append((len(goods) + 1, {'название': name, 'цена': cost, 'количество': count, 'eд': unit}))

    if input('Продолжить ввод: ').lower() != 'y':
        break

print(goods)
statistics: Dict[str, List[Any]] = {'название': [], 'цена': [], 'количество': [], 'eд': []}

for item in goods:
    statistics['название'].append(item[1]['название'])
    statistics['цена'].append(item[1]['цена'])
    statistics['количество'].append(item[1]['количество'])
    statistics['eд'].append(item[1]['eд'])

statistics['eд'] = (list(set(statistics['eд'])))

print(statistics)
