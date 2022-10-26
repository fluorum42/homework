#Написать функцию перевода размеров женского белья из международного во все остальные. Внутри функции нужно просто
# обращаться к правильно составленному словарю.
# international= {'xxs', 'xs', 's', 'm', 'l', 'xl', 'xxl', 'xxxl'}
# russia = {'42', '44', '46', '48', '50', '52', '54', '56'}
# Germany = {'36', '38', '40', '42', '44', '46', '48', '50'}
# USA = {'8', '10', '12', '14', '16', '18', '20', '22'}
# France = {'38', '40', '42', '44', '46', '48', '50', '52'}
# GB = {'24', '26', '28', '30', '32', '34', '36', '38'}
sizes = {'international': {'xxs', 'xs', 's', 'm', 'l', 'xl', 'xxl', 'xxxl'}, #creation of a dict of women's lingerie sizes
         'russia': {'42', '44', '46', '48', '50', '52', '54', '56'},
         'Germany': {'36', '38', '40', '42', '44', '46', '48', '50'},
         'USA': {'8', '10', '12', '14', '16', '18', '20', '22'},
         'France': {'38', '40', '42', '44', '46', '48', '50', '52'},
         'GB': {'24', '26', '28', '30', '32', '34', '36', '38'}}

def convert_size(size, country):
      #assigning a value in the dict "international" to a given size
    result = ''
    for key, val in international.value():
        size = val
        size_key = filter(None, map(international.get, keys))
        for key, val in country.value():
            country = sizes(i)
            if country(val) == i(val):
                result = i(val)
    return result


print(convert_size('s', 'russia'))