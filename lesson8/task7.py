# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = f'{a} + {b} * i'

    def __add__(self, other: 'ComplexNumber'):
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other: 'ComplexNumber'):
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z1 = ComplexNumber(2, -5)
z2 = ComplexNumber(1, 3)
print(z1)
print(z2)
print('Сумма чисел: ', z1 + z2)
print('Произведение чисел: ', z1 * z2)
