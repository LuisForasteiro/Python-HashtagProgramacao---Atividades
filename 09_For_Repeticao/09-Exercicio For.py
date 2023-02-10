meta = 10000
vendas = [
    ['Joao', 15945],
    ['Luis', 12047],
    ['Lucas', 9748],
    ['Maria', 800099],
    ['Duda', 9999],
    ['Luis Felipe', 10000]
]

# Primeira maneira
acima_meta = []

for venda in vendas:
    print(venda)
    # venda[0] = Nome pessoa
    # venda[1] = Vendas da pessoa
    if venda[1] >= meta:
        acima_meta.append(venda)
print(f'BATEU A META: {acima_meta}')

print(f'{len(acima_meta) / len(vendas):.1%} dos vendedores bateram a meta')


# Segunda maneira
contador_acima_meta = 0

for venda in vendas:
    if venda[1] >= meta:
        contador_acima_meta += 1

print(f'{contador_acima_meta / len(vendas):.1%} dos vendedores bateram a meta')


# Vendedor que mais vendeu?

melhor_vendedor = ''
maior_vendas = 0

for venda in vendas:
    if venda[1] > maior_vendas:
        maior_vendas = venda[1]
        melhor_vendedor = venda[0]

print(f'Melehor vendedor: {melhor_vendedor}\nVendas: R${maior_vendas:,.2f}')
