#Ввести число, вывести все его делители.

number = int(input('Enter the number: '))
index = 1
while index <= number/2:
    if number % index == 0:
        print(index)
    index = index + 1
