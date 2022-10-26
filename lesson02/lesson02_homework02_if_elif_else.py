#Придумать свои собственные примеры на альтернативные варианты if и активное использование булевой алгебры.
#what would the Doctor Who say to you

name = (input('Enter your name: '))
if name == 'River' or name == 'River Song':
    print("Hello, Sweettie!")
elif name == 'Davros' or name == 'Master':
    print("I'm sorry, "+name)
else:
    print('Trust me, ' + name +"! \nI'm the Doctor!")
