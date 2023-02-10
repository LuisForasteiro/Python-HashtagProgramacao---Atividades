# CUIDADO COM O WHILE CASO ENTRE EM LOOP INFINITO

vendas = [12938, 9048, 8889, 52847, 728]  # Ordem Decrecente
vendedores = ['Luis', 'Maria', 'Joao', 'Marcos', 'Luan']
meta = 3000

i = 0

while vendas[i] > meta:
    print(f'{vendedores[i]} bateu a meta. Vendas: {vendas[i]}')
    i += 1


for i, venda in enumerate(vendas):
    if venda > meta:
        print(f'Vendedor: {vendedores[i]} Venda: {venda}')
