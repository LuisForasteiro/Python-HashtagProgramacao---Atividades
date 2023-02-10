produtos = ['iphone', 'ipad', 'iMac', 'Apple Watch']
vendas = [1500, 2000, 489, 559]


dicionario = dict.fromkeys(produtos, 0)
print(dicionario)


lista_tuplas = zip(produtos, vendas)
dicionario_vendas = dict(lista_tuplas)
print(dicionario_vendas)


# fazendo com lista
indice = produtos.index('ipad')
print(vendas[indice])


# fazendo com dicionario
print(f'vendemos {dicionario_vendas["ipad"]}')


# QUANDO SE TEM UM DICIONARIO FICA MUITO MAIS FACIL DE TRABALHAR COM O CODIGO
