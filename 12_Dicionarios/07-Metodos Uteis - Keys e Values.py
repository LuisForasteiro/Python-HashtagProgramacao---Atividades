# .keys() uma 'lista' com todas as chaves do dicionario
#  .values() uma 'lista' com todos os valores do dicionario


vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720,
                     'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}


chaves = vendas_tecnologia.keys()
valores = vendas_tecnologia.values()
print(chaves)  # dict_keys
print(valores)  # dict_keys
print(list(chaves))  # lista normal
print(list(valores))  # lista normal

for chave in vendas_tecnologia.keys():
    print(chave)

for valor in vendas_tecnologia.values():
    print(valor)


lista_chaves = list(chaves)
lista_chaves.sort()

for item in lista_chaves:
    # lista organizada com as unidades certas!
    print(f'{item} - {vendas_tecnologia[item]} unidades')
