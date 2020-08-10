# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.


while True:
    input_str = input('Введите время в секундах:')

    if input_str.isnumeric():
        total_seconds = int(input_str)
        hours = total_seconds // 3600
        minutes = total_seconds % 3600 // 60
        seconds = total_seconds % 3600 % 60

        print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))
        break
