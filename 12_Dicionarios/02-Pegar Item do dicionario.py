mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu',
                 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720,
                     'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# Duas formas de pegar o valor de um item...
# 1
print(f'Livro mais vendido: {mais_vendidos["livros"]}')
print(f'Lazer mais vendido: {mais_vendidos["lazer"]}')

# 2
notebook_asus = vendas_tecnologia.get('notebook asus')
print(notebook_asus)

# as aspas duplas fazem diferenca na hora de passar a chave utilizando o .get("")
print(f'Vendas iPad (unidades): {vendas_tecnologia.get("ipad")}')  # Correto
# print(f'Vendas iPad (unidades): {vendas_tecnologia.get('ipad')}')  # Errado

# Formas de tratar um erro caso um item estaja fora da lista
# 1
if 'copo' in vendas_tecnologia:
    print(vendas_tecnologia['copo'])
else:
    print('Copo nao esta na lista de tecnologia!')

# 2
if vendas_tecnologia.get('copo') == None:
    print('Copo nao esta na lista de tecnologia!')
else:
    print(vendas_tecnologia['copo'])
