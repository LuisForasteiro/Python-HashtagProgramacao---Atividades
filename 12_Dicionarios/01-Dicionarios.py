# Estrutura
# dicionario = {chave: valor, chave:valor, chave:valor...}
# Pode ter varios tipo no dicionario como: nome, texto, numero etc

mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu',
                 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720,
                     'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}


livro = mais_vendidos['livros']
lazer = mais_vendidos['lazer']
print(f'Livro mais vendido: {livro}')
print(f'Lazer mais vendido: {lazer}')

notebook_asus = vendas_tecnologia['notebook asus']
print(f'Quantidade de vendas notebook Asus: {notebook_asus} unidades')
