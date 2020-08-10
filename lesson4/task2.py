# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
import random


my_list = [random.randint(1, 100) for i in range(25)]

new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]

print(f'Оригинальный {my_list}')
print(f'Конечный {new_list}')
