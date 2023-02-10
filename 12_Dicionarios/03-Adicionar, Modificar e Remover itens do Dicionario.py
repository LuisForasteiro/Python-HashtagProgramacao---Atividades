# Adicionar um item em um dicionario!
# 1
dicionario = {}
dicionario['Apple'] = 'iPhone 10'
dicionario['Notebook'] = 'Notebook Aspire'
dicionario['Vendas'] = 1500
print(dicionario)

# 2
dicionario.update({'Celular': 'Galaxy', 'Cozinha': 'Micro-ondas'})
print(dicionario)

# Exercicio
lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'marco': 90000}
lucro_2tri = {'abril': 88000, 'maio': 130000, 'junho': 78000}

# Adicionando 1 item
print(lucro_1tri)
lucro_1tri['abril'] = 88000
print(lucro_1tri)

# Add varios itens
lucro_1tri.update(lucro_2tri)
print(lucro_1tri)

# Add um item ja existente
# A chave nao pode ser repetida se nao ela modifica o item
lucro_1tri.update({'janeiro': 90000})
print(lucro_1tri)

# Modificando o valor de Fevereiro
lucro_fevereiro = 99999
lucro_1tri['fevereiro'] = lucro_fevereiro
print(lucro_1tri)


# Remover um item do dicionario
# 1 Removendo por completo
del lucro_1tri['janeiro']
print(lucro_1tri)

# 2 armazena o valor em uma variavel... porem o valor eh retirado do dicionario
lucro_janeiro = lucro_1tri.pop('marco')
print(lucro_1tri)
print(lucro_janeiro)

del lucro_1tri  # delete o dicionario todo... por que nao foi definido um valor
