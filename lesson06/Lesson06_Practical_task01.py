# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.
import itertools

marks = {
    'White': [7, 4, 9, 8],
    'Orange': [10, 9, 11, 7],
    'Pink': [9, 7, 8, 8],
    'Blue': [6, 7, 5, 5],
    'Brown': [8, 7, 9, 7]
}
list_total = []
for key, val in marks.items():
    sumv = 0
    marks_av = []
    for v in val:
        sumv += v
        average = int(sumv / len(val))
        marks[key] = marks_av
    marks_av.append(average)
    for item in marks_av:
        list_val = range(item)
        list_total.append(item)
max_average = max(list_total)
min_average = min(list_total)
for key, val in marks.items():
    marks['Orange'] = max_average
    marks['Blue'] = min_average
    if val == max_average or val == min_average:
        print(key, val)