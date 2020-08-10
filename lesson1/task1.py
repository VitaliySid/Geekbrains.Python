# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.


lesson = 'Задание'
lesson_number = 1
print('{} {}'.format(lesson, lesson_number))

name = input('Введите свое имя:')

while True:
    age = input('Введите свой возраст:')

    if age.isnumeric():
        break

print('Вас зовут: ', name)
print('Возраст: ', age)
