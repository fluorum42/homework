"""
Створити клас, який буде описувати властивості хімічного елементу.
Для класу має бути описаний метод __init__(...), який приймає два параметри:
температура плавлення та температура кипіння.
В класі має бути описаний метод, який в якості аргумента отримує температуру (в градусах цельсія) та повертає строку,
яка відповідає агрегатному стану речовини при цій температурі.
* Додати в клас метод, який приймає в якості аргументів температуру (число) та назву шкали виміру (“C” / “F” / “K”) та
конвертує її в градуси цельсія.
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

    def convert_t(self, temp, name_t='C'):
        to_k = 273  # t по Кельвину == 0 °C
        to_f = 32  # t по Фаренгейту == 0 °C
        if name_t == 'K':
            return temp - to_k
        elif name_t == 'F':
            return (temp - to_f) * (5 / 9)
        return temp


water = ChemElem(melting_point=0,
                 boiling_point=100)
print(water.get_state(-5))
print(water.get_state(1))
print(water.get_state(115))
print(water.convert_t(212, 'F'))
print(water.convert_t(373, 'K'))
print(water.convert_t(100, 'C'))
