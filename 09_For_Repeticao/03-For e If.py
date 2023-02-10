# for item in lista:
#     if condicao:
#         do something
#     else:
#         otherwise

# len() verificar o tamanho da lista!
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 80, 100, 387]
meta = 1000
bateu_meta = 0
n_bateu_meta = 0

for venda in vendas:
    if venda >= meta:
        bateu_meta += 1
    else:
        n_bateu_meta += 1

total_pessoas = len(vendas)
percentual = bateu_meta / total_pessoas

print(f'Total pessoas: {len(vendas)}')
print(f'Total que bateu meta: {percentual:.2%}')
print(f'Total que nao bateu meta: {n_bateu_meta}')
