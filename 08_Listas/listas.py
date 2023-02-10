# Listas estruturas
nome = 'computador'
produtos = ['tv', nome, 'celular', 'mouse', 'teclado']
vendas = [1500, 900, 800, 200, 300]
print(produtos)
print(produtos[1])
print(f'Vendas do produto {produtos[4]} foram de {vendas[4]} unidades')

# Substituir valor
vendas[4] = 500
print(f'Vendas do produto {produtos[4]} foram de {vendas[4]} unidades')

# Nao pode substituir string, apenas com .replace
texto = 'luis@gmail.com'
texto = texto.replace('i', 'a')
print(texto)


# Descobrir o indice de um item na lista! .index
produtos = ['Geladeira', 'celulcar', 'teclado', 'mouse']
estoque = [1500, 600, 700, 100]

i = produtos.index('teclado')
print(f'Produto: {produtos[i].upper()}\nEstoque: {estoque[i]} unidades')

# Adicionar e remover item de uma lista
# lista.append(item)
# lista.pop(indice)
# lista.remove(item)

produtos = ['apple watch', 'iphone 13',
            'iphone X', 'MacBook air', 'iPhone 7', 'iMac']

print(produtos)
produtos.append('iphone 14')
print(produtos)

produtos.pop(4)
print(produtos)

produtos.remove('iMac')
print(produtos)

# Try e Except
try:
    produtos.remove('apple watch')
    print('Produto removido!')
    print(produtos)

except Exception:
    print('Produto nao foi removido ou nao contem na lista')

# Funcoes basicas da lista
produtos = ['apple watch', 'iphone 13',
            'iphone X', 'MacBook air', 'iPhone 7', 'iMac']
vendas = [100, 500, 200, 50, 800, 90]

# Tamanho da lista
tamanho = len(produtos)
print(f'Tamanho da lista: {tamanho}')

# Max e Min
maior = max(vendas)
print(f'O produto mais vendido (valor): {maior}')
menor = min(vendas)
print(f'O produto menos vendido (valor): {menor}')

i = vendas.index(maior)
print(f'Produto: {produtos[i]}\nUnidades: {vendas[i]}')

i = vendas.index(menor)
print(f'Produto: {produtos[i]}\nUnidades: {vendas[i]}')

# JUNTAR LISTAS

produtos = ['apple tv', 'macbook', 'iphone x', 'iphone 11']
novos_produtos = ['iphone 12', 'iphone 13', 'iphone 14']
print(produtos)
print(novos_produtos)

# extend
print('\nJUNTANDO AS LISTAS! #1')
produtos.extend(novos_produtos)
print(produtos)

# +
print('\nJUNTANDO AS LISTAS! #2')
nova_lista = produtos + novos_produtos
print(nova_lista)

# ordenar
produtos.sort(reverse=False)
print(produtos)

# Metodo Join
print('\n'.join(produtos))


# Alteracoes 'Incrementais' de variaveis
lista = ['mac', 'iphone']
vendas = [100, 500]

lista = lista + ['ipad']
lista += ['iphone 15']
print(lista)

contador = 0
contador += 5
print(contador)


# Copiar e "Igualdade de Listas"
lista = ['Luis', 'Lucas', 'Carol']
lista2 = lista.copy()

lista[1] = 'iphone 11'
print(lista)
print(lista2)


# Lista de Lista ou Nasted List
vendedores = ['Luis', 'Lucas', 'carol']
produtos = ['Iphone 11', 'Iphone 12']
vendas = [
    [100, 200],
    [300, 400],
    [160, 700],
]

# Qunto que Carol vendeu de iPad?

vendas_iphone12_carol = vendas[2][1]
print(vendas_iphone12_carol)

# Luis vendas iphone?
vendas_iphone11_luis = vendas[0][0]
print(vendas_iphone11_luis)

# Total de vendas iphone 11
total_vendas_iphone11 = vendas[0][0] + vendas[1][0] + vendas[2][0]
print(f'Total vendas: {total_vendas_iphone11}')

# Modificando o valor do Luis iphone11
vendas[0][0] = 50
print(vendas)

# Adicionando um novo produto para cada vendedor
vendas_mac = [100, 500, 200]

vendas[0].append(vendas_mac[0])
vendas[1].append(vendas_mac[1])
vendas[2].append(vendas_mac[2])
print(vendas)

