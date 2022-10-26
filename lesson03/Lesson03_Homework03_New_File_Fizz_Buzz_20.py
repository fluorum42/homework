# Написать fizzbuzz для 20 троек чисел, которые записаны в файл. Читаете из файла первую строку, берете из нее числа,
# считаете для них fizzbuzz, выводите, повторяете со всеми остальными строками. Переделать задачу так, чтобы результат
# писался в другой файл.

import sys
final_list = []
f = 'Lesson03_Homework02_Fizz_Buzz_Add_file.txt'
new_f = 'Lesson03_Homework03_New_Fizz_Buzz_Add_file_w.txt'
with open(f, "r") as f:
    for line in f:
        my_list = []
        line = line.split()
        num_line = list(map(int, line))
        Fizz, Buzz, End_count = num_line[:]
        number = 1
        while number <= End_count:
            if (number % Fizz == 0) and (number % Buzz == 0):
                my_list.append('FB')
            elif number % Buzz == 0:
                my_list.append("B")
            elif number % Fizz == 0:
                my_list.append('F')
            else:
                my_list.append(str(number))
            number = number + 1
        final_list.append(' '.join(my_list))
print(final_list)
with open(new_f, 'w') as new_f:
    for elem in final_list:
        new_f.write(elem + "\n")