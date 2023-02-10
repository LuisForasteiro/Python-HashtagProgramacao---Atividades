def cadastrar_produto():
    produto = input('Digite o nome do produto: ')
    produto = produto.casefold()
    print(f'{produto} cadastrado com sucesso! ')

for i in range(2):
    cadastrar_produto()
