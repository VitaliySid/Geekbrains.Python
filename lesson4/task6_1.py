# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
from itertools import count
from sys import argv

start, stop = argv[1:3]

if start.isnumeric() and stop.isnumeric() and int(start) < int(stop):
    for i in count(int(start)):
        print(i)
        if i >= int(stop):
            break
