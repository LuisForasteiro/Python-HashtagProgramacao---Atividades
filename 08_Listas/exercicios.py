# produtos = ['teclado', 'geladeira', 'mouse', 'celular']
# produto = str(input('Digite o nome do produto: '))

# if produto in produtos:
#     i = produtos.index(produto)
#     print(f'Item: {produto.capitalize()}')
# else:
#     print(f'{produto} nao existe no estoque!')


# PEGAR O MELHOR E PIOR MES DO ANO
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun']
vendas_1_tri = [1500, 200, 600]
vendas_2_tri = [800, 2000, 900]

vendas_1_tri.extend(vendas_2_tri)
print(f'Juntando as listas: {vendas_1_tri}')

maior_valor = max(vendas_1_tri)
print(f'O maior valor: {maior_valor}')

menor_valor = min(vendas_1_tri)
print(f'Menor valor: {menor_valor}')

i_maior_valor = vendas_1_tri.index(maior_valor)
print(f'O melhor mes foi: {meses[i_maior_valor]} com {maior_valor} vendas!')

i_menor_valor = vendas_1_tri.index(menor_valor)
print(f'O pior mes do ano foi: {meses[i_menor_valor]} com {menor_valor}')

faturamento_total = sum(vendas_1_tri)
print(f'Faturamento Total: R${faturamento_total:.2f}')

percent = maior_valor / faturamento_total
print(f'A representacao: {percent:.1%}')


# EXERCICIO DE MUDANCA DE CARGA TRIBUTARIA
produtos = ['Computador', 'livro', 'tablet', 'celular', 'tv', 'alexa']
produto_ecomerce = [  # Quantidade vendida e Valor do Produto
    [10000, 5000],
    [50000, 40],
    [1000, 50],
    [900, 80],
    [5000, 100],
    [4000, 49],
]

if 'livro' in produtos:
    i = produtos.index('livro')
    total_antigo = produto_ecomerce[i][0] * produto_ecomerce[i][1]
    print(f'Index do livro: {i}')
    print(f'Preco do livro: R${produto_ecomerce[i][1]:.2f}')
    produto_ecomerce[i][1] *= 1.1
    print(f'Preco do livro (com 10%): R${produto_ecomerce[i][1]:.2f}')
    novo_total = produto_ecomerce[i][0] * produto_ecomerce[i][1]
    print(f'Imposto a mais: R${novo_total-total_antigo:,.2f}') 
    
    
