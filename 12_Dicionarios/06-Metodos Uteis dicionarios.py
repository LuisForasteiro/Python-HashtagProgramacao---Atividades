# metodo .items()
# itens_dicionario = dicionario.items()

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720,
                     'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# Tranformando um dicionario em uma lista de Tuplas!
# itens_dicionario = vendas_tecnologia.items()
# print(itens_dicionario)  # Tupla

# for produto, qtde in vendas_tecnologia.items():  # unpacking dos items
#     print(f'{produto}: {qtde} unidades')  # Tuplas


# 01 exercicio
# for produto, qtde in vendas_tecnologia.items()...
print('FORMA 1')
for produto, qtde in vendas_tecnologia.items():
    if qtde >= 5000:
        print(f'{produto}: {qtde} unidades')

# 02 exercicio
print('\nFORMA 2')
for item in vendas_tecnologia:
    if vendas_tecnologia[item] > 5000:
        print(f'{item}: {vendas_tecnologia[item]} unidades')
