# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
from itertools import cycle
from sys import argv

count = argv[1]
my_list = argv[2:]

if count.isnumeric():
    i = 0
    for el in cycle(my_list):
        print(el)
        i += 1
        if i >= int(count):
            break
