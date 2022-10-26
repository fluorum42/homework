# Заканчиваем прошлые задачи, украшаем работу физбазов работой со строками, списками, пробуем генераторы списков и
# прочие новые красоты, которые выучили. Доводим код до идеала!

import sys
final_list = []
number = 1
f = 'Lesson03_Homework02_Fizz_Buzz_Add_file.txt'
new_f = 'Lesson04_Homework02_New_Fizz_Buzz_Add_file_w.txt'
with open(f, "r") as f:
    for line in f:
        my_list = []
        line = line.split()
        num_line = list(map(int, line))
        Fizz, Buzz, End_count = num_line[:]
        for number in range(1, End_count):
            if (number % Fizz == 0) and (number % Buzz == 0):
                my_list.append('FB')
            elif number % Buzz == 0:
                my_list.append("B")
            elif number % Fizz == 0:
                my_list.append('F')
            else:
                my_list.append(str(number))
        final_list.append(' '.join(my_list))
print(final_list)
with open(new_f, 'w') as new_f:
    for elem in final_list:
        new_f.write(elem + '\n')