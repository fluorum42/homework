#Третий уровень ("Мистер Буль. Джордж Буль!"):
#Решить задачу:
#Задача fizz-buzz:
#У вас есть три числа, они вводятся из консоли. Первое число называется fizz, второе называется buzz.
# До третьего необходимо досчитать от единицы. Считая, надо выводить число. Если число кратно fizz - надо выводить F вместо числа.
# Если число кратно buzz - надо выводить B вместо числа. Если число кратно и fizz и buzz, надо выводить FB.
# И так - пока не будет достигнуто третье введенное число.
#Пример условия и результата:
#Введены числа 2, 5, 18
#Вывод должен быть таким:
#1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F

Fizz = int(input('Enter the number: '))
Buzz = int(input('Enter the number: '))
End_count = int(input('Enter the number: '))
number = 1
while number <= End_count:
    if number % Fizz == 0:
        print('F', end=' ')
    elif number % Buzz == 0:
        print('B', end=' ')
    elif (number % Fizz == 0) and (number % Buzz == 0):
            print('FB', end=' ')
    else:
        print(number, end=' ')
    number = number + 1
