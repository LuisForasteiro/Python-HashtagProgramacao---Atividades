# Lista que contem Tuplas
vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone 11', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone 13', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

# Qual o faturamento de iPhone no dia 20/08/2020

faturamento = 0
for item in vendas:
    data, produto, cor, capacidade, unidades, valor_unitario = item
    print(produto)
    if 'iphone' in produto and data == '20/08/2020':
        faturamento += unidades * valor_unitario

print(f'Faturmento iPhone 20/08/2020: R${faturamento:,.2f}')

# Qual o produto mais vendido no dia 21/08/2020

produto_mais_vendido = ''
quantidade_mais_vendida = 0

for item in vendas:
    data, produto, cor, capacidade, unidades, valor_unitario = item
    if '21/08/2020' in data:  # if data == '21/08/2020'
        if unidades > quantidade_mais_vendida:
            produto_mais_vendido = produto
            quantidade_mais_vendida = unidades

print(
    f'Produto + Vendido: {produto_mais_vendido}\nUnidades: {quantidade_mais_vendida} - 21/08/2020')


# Como seria feito sem percorrer a lista

# data, produto, cor, capacidade, unidades, valor_unitario = vendas[0]
# faturamento = unidades * valor_unitario
# print(f'R${faturamento:,.2f}')
