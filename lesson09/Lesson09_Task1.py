# Задача 1. Курьер
# Вам известен номер квартиры, этажность дома и количество квартир на этаже. Задача: написать функцию, которая по
# заданным параметрам напишет вам, в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.
def courier(flat, floors, ft_floor):
    res_floor = 0
    res_entr = 0
    floor_entr = floors * ft_floor  # количество квартир в подъезде
    res_entr = flat // floor_entr + 1  # определяем нужный подъезд
    res_floor = int(str(res_entr).split('.')[1])  # определяем нужный этаж
    return f'Entrance: {res_entr}, floor: {res_floor}'

print(courier(88, 9, 4))