# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


dic = {'12': 'зима', '1': 'зима', '2': 'зима',
       '3': 'весна', '4': 'весна', '5': 'весна',
       '6': 'лето', '7': 'лето', '8': 'лето',
       '9': 'осень', '10': 'осень', '11': 'осень'}
array = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']

while True:
    month = input('Введите номер месяца: ')

    if month.isnumeric() and 0 < int(month) <= 12:
        print('Месяц из словаря: ', dic[month])
        print('Месяц из списка: ', array[int(month) - 1])

        break