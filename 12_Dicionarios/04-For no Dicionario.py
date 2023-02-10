# for chave in dicionario:
#     do something...

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720,
                     'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

total_notebooks = 0

for chave in vendas_tecnologia:
    print(f'{chave}: {vendas_tecnologia[chave]} unidades')
    if 'notebook' in chave:
        total_notebooks += vendas_tecnologia[chave]

print(f'Total de notebooks: {total_notebooks}')
