# Задача 3. Файл-тест
def task3(file_test):
    with open(file_test, 'r') as file:
        result = list()
        for line in file:
            line = line.split(";")
            line_prt1 = line[0].split()
            sum_elem = 0
            for i in line_prt1:
                sum_elem += int(i)
            average = int(sum_elem // len(line_prt1))
            line_prt2 = line[1].split()
            if average == int(line_prt2[0]) and (sum_elem % len(line_prt1) == int(line_prt2[1])):
                result.append('True')
            else:
                result.append('False')
    return (result)


print(task3('test.txt'))