# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def print_user(name, surname, year, city, mail, phone):
    print(f'{surname} {name}, год рождения: {year}, город проживания: {city}, email: {mail}, телефон: {phone}')


def print_users(users):
    for user in users:
        print_user(surname=user['surname'],
                   name=user['name'],
                   mail=user['mail'],
                   year=user['year'],
                   phone=user['phone'],
                   city=user['city'])

users = [
    {'name': 'Иван', 'surname': 'Иванов', 'year': '1991',
     'city': 'Москва', 'mail': 'ivanov@mail.ru', 'phone': '999-123-12-11'},
    {'name': 'Сергей', 'surname': 'Иванов', 'year': '1971',
     'city': 'Воронеж', 'mail': 'ivanov.s@mail.ru', 'phone': '999-123-12-99'},
    {'name': 'Петр', 'surname': 'Сергеев', 'year': '1987',
     'city': 'Москва', 'mail': 'sergeev@mail.ru', 'phone': '991-123-12-11'}]

print_users(users)




