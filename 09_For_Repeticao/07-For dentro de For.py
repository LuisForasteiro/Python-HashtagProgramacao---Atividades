# for item in lista:
#     for item2 in lista2:
#         codigo...

estoque = [
    [1500, 1348, 143, 100, 4572],
    [200, 589, 1278, 90, 278],
    [199, 20, 29, 4820, 982],
    [900, 909, 826, 127, 90]
]
fabricas = ['Luis Manufacturing', 'Fabrica Hashtag',
            'Python Manufacturing', 'Luis e CIA']
estoque_min = 150

for i, lista in enumerate(estoque):
    for qtde in lista:
        if qtde < estoque_min:
            print(f'Fabrica : {fabricas[i]}')
