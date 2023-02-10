qtde_vendas_coca = 150
qtde_vendas_pepsi = 130
preco_coca = 1.50
preco_pepsi = 1.50
custo_loja = 2500.00

faturamento_pepsi = qtde_vendas_pepsi * preco_pepsi
print(f'Faturamento Pepsi: {faturamento_pepsi}')

faturamento_coca = qtde_vendas_coca * preco_coca
print(f'Faturamento coca: {faturamento_coca}')

lucro_loja = faturamento_coca + faturamento_pepsi
lucro_real = lucro_loja - custo_loja
print(f'Lucro Loja: {lucro_real}')

margem = (lucro_real / lucro_loja)
print(f'Margem: {margem:.2%}')

# Bebidas alcoolicas
consulta = input('Digite o nome da bebida: ')

if 'BAC' in consulta:
    print('BEBIDA ALCOOLICA!')
elif 'BEB' in consulta:
    print('BEBIDA NAO ALCOOLICA')
else:
    print('CODIGO INCORRETO / NAO EXISTE!')
