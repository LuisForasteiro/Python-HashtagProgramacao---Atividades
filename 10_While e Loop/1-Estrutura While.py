# while condicao: 
#     repete tal codigo

produto = input('Digite o nome do produto: ')
print('Para sair TECLE ENTER')
vendas = []

while produto != '' or produto == 'SAIR':
    vendas.append(produto)
    produto = input('Digite o nome do produto: ')

print(f'Registro finalizado os produtos cadastrados foram {vendas}')