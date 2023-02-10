vendas = []

while True:
    produto = input('Digite o produto: ')
    if not produto:
        break
    qtde_produto = int(input('Qual a quantidade: '))
    vendas.append([produto, qtde_produto])

print(vendas)
