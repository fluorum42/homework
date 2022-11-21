"""
Створити клас, який буде описувати властивості хімічного елементу.
Для класу має бути описаний метод __init__(...), який приймає два параметри:
температура плавлення та температура кипіння.
В класі має бути описаний метод, який в якості аргумента отримує температуру (в градусах цельсія) та повертає строку,
яка відповідає агрегатному стану речовини при цій температурі.
"""


class ChemElem:
    def __init__(self, melting_point, boiling_point):
        self.melting_point = melting_point  # t °C
        self.boiling_point = boiling_point  # t °C

    def get_state(self, temp):
        if temp < self.melting_point:
            return 'Element is solid'
        elif temp > self.boiling_point:
            return 'Element is gas'
        return 'Element is liquid'


water = ChemElem(melting_point=0,
                 boiling_point=100)
print(water.get_state(-5))
print(water.get_state(1))
print(water.get_state(115))
