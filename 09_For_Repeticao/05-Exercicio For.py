# Exercicio 1
qtd_hospede = int(input('Digite a qut de pessoas: '))
quarto = []

for i in range(qtd_hospede):
    nome = input('Digite o NOME: ')
    cpf = input('Digite o CPF: ')
    hospede = [f'Nome: {nome}', f'CPF: {cpf}']
    quarto.append(hospede)
    print('Cadastro Concluido!')

print(quarto)

print('--------------------------------------------')
# Exercicio 2
meta = 10000
vendas = [
    ['Joao', 15000],
    ['Luis', 10000],
    ['Lucas', 9000],
    ['Luiza', 9999],
    ['Math', 83965]
]

for i in vendas:
    if i[1] >= meta:
        print(f'Vendedor {i[0]} bateu a meta. Fez {i[1]} vendas')
