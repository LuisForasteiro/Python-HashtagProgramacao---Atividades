# break -> Interrompe e finaliza o for
# continue -> Interrompe e vai para o proximo item do for

vendas = [100, 200, 890, 50, 90, 124]
meta = 110

for venda in vendas:
    if venda < meta:
        print('Loja nao ganha bonus')
        break
    print(venda)


vendedores = ['Joao', 'Maria', 'Lucas', 'Math', 'Luis']
meta = 130

for venda in vendas:
    if venda < meta:
        continue
    print(venda)

