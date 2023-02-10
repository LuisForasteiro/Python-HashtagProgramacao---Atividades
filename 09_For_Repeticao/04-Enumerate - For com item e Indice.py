# for item in lista:
#     resto do codigo


funcionarios = ['Luis', 'Maria', 'Lucas', 'Joao', 'Math']

for i, funcionario in enumerate(funcionarios):
    print(f'{i} - {funcionario}')


estoque = [1000, 120, 50, 100, 89]
produtos = ['Coca', 'fanta', 'dolly', 'bhrama', 'agua']
prod_minimo = 100

for i, qtde_estoque in enumerate(estoque):
    if qtde_estoque < prod_minimo:
        print(f'{produtos[i]} esta abaixo do estoque minimo. Apenas {qtde_estoque} estoque')

