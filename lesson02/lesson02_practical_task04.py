#Ввести число, вывести его разряды и их множители.

number = input('Enter the number: ')
index = 0
while index < len(number):
    radix = 10 ** (len(number) - index - 1)
    print(f'{number[index]}*{radix} ' , end = '')
    index = index + 1

