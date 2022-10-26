# Написать fizzbuzz для 20 троек чисел, которые записаны в файл. Читаете из файла первую строку, берете из нее числа,
# считаете для них fizzbuzz, выводите, повторяете со всеми остальными строками.

import sys

f = open('Lesson03_Homework02_Fizz_Buzz_Add_file.txt', 'r')
for line in f:
    # line = f.readline()
    line_split = line.split()
    num_line = list(map(int, line_split))

    Fizz, Buzz, End_count = num_line[:]
    print()
    number = 1
    while number <= End_count:
        if (number % Fizz == 0) and (number % Buzz == 0):
            print('FB', end=' ')
        elif number % Buzz == 0:
            print('B', end=' ')
        elif number % Fizz == 0:
            print('F', end=' ')
        else:
            print(number, end=' ')
        number = number + 1

f.close()
