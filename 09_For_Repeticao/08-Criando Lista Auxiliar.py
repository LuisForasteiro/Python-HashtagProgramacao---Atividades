estoque = [
    [1500, 1348, 143, 100, 4572],
    [200, 589, 1278, 90, 278],
    [199, 20, 29, 4820, 982],
    [900, 909, 826, 127, 90]
]
fabricas = ['Luis Manufacturing', 'Fabrica Hashtag',
            'Python Manufacturing', 'Luis e CIA']
estoque_min = 150

fabricas_estoque_min = []

for i, lista in enumerate(estoque):
    for qtde in lista:
        if qtde < estoque_min:
            # Se a fabrica ja estiver na lista, nao vai adicionar mais
            if fabricas[i] not in fabricas_estoque_min:
                fabricas_estoque_min.append(fabricas[i])

print(fabricas_estoque_min)
