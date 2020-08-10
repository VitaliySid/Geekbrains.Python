# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.


while True:
    input_str = input('Введите число:')

    if input_str.isnumeric():
        max_num = 0

        for num in input_str:
            if int(num) > max_num:
                max_num = int(num)

        print('Наибольшая цифра в строке: ', max_num)
        break
