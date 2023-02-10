vendas = ('Luis Felipe', '25/09/2020', '12/09/2000', 2200, 'Auxiliar TI')

nome = vendas[0]
data_contratante = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]

print(f'Nome 1: {nome}')

# Sao a mesma coisa, porem de um jeito melhor de Unpacking - Muito importante em tuplas

vendas = nome, data_contratante, data_nascimento, salario, cargo

print(f'Data Nascimento 2: {data_contratante}')

# Enumerate eh de certa forma uma Tupla

vendas = [1000, 2000, 300, 200, 100]
funcionarios = ['Luis', 'Lucas', 'joao', 'Maria', 'Duda']

for i, venda in enumerate(vendas):
    print(f'{funcionarios[i]} vendeu {vendas[i]} unidades!')
