#Придумать свои собственные примеры на альтернативные варианты if и активное использование булевой алгебры.

price = int(input('Enter the price: '))
if price <= 100:
    print("I'll buy it!")
elif price > 100 and price < 300:
    print('Ok, thanks :(')
else:
    print('Oh maaan!')
