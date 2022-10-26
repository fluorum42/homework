# Продолжаем идеализировать fizzbuzz, теперь применяем функции и map везде, где можно и нельзя!

result_tot = []
f = 'Lesson03_Homework02_Fizz_Buzz_Add_file.txt'
new_f = 'Homework05_New_Fizz_Buzz.txt'
with open(f, "r") as f:
    for line in f:
        result = []
        line = line.split()
        num_line = list(map(int, line))
        rng = range(1, num_line[2]+1)

        def fizz_buzz(num_line):
            fizz = num_line[0]
            buzz = num_line[1]
            if (number % fizz == 0) and (number % buzz == 0):
                result.append("FB")
            elif number % buzz == 0:
                result.append("B")
            elif number % fizz == 0:
                result.append('F')
            else:
                result.append(str(number))
            # number = number + 1
            return result
        result_tot.append(result)
result_tot = list(map(fizz_buzz, rng))
print(result_tot)

with open(new_f, 'w') as new_f:
    for elem in result_tot:
        new_f.write(str(elem) + '\n')
