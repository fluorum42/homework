#Банкомат выдает сумму максимально возможными купюрами

number = int(input('Enter the withdraw amount: '))
i = i1 = i2 = i3 = i4 = i5 = i6 = i7 = i8 = i9 = 0

if number >= 1000:
    while number >= 1000:
        number = number - 1000
        i += 1
    print(f'{i} bill(s) * 1000 UAH')
if number >= 500:
      while number >= 500:
          number = number - 500
          i1 += 1
      print(f'{i1} bill(s) * 500 UAH')
if number >= 200:
      while number >= 200:
          number -= 200
          i2 += 1
      print(f'{i2} bill(s) * 200 UAH')
if number >= 100:
      while number >= 100:
          number -= 100
          i3 += 1
      print(f'{i3} bill(s) * 100 UAH')
if number >= 50:
      while number >= 50:
          number -= 50
          i4 += 1
      print(f'{i4} bill(s) * 50 UAH')
if number >= 20:
      while number >= 20:
          number -= 20
          i5 += 1
      print(f'{i5} bill(s) * 20 UAH')
if number >= 10:
      while number >= 10:
          number -= 10
          i6 += 1
      print(f'{i6} bill(s) * 10 UAH')
if number >= 5:
      while number >= 5:
          number -= 5
          i7 += 1
      print(f'{i7} bill(s) * 5 UAH')
if number >= 2:
      while number >= 2:
          number -= 2
          i8 += 1
      print(f'{i8} bill(s) * 2 UAH')
if number >= 1:
      while number >= 1:
          number -= 1
          i9 += 1
      print(f'{i9} bill(s) * 1 UAH')