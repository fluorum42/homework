#Разбираемся, что делает функция zip, и пробуем написать свой собственный zip.
def my_zip(lst, tpl):
    return list(map(lambda x,y: (x,y), lst,tpl))

a = [89, -1 ,0]
b = ['f', 'jo', 'a']
print(my_zip(a, b))