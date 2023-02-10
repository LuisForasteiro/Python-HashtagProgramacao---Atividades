# nao pode ter valores duplicados
set_estoque = {1123, 1534, 2234, 5442, 1897}
set_produtos = {'arroz', 'feijao', 'macarrao', 'atum'}

print(set_produtos)  # aleatorio

cpf_clientes = ['788.563.158-31', '788.563.158-31',
                '601.051.626-98', '616.289.328-64', '773.204.458-40', '765.474.480-37', '765.474.480-37']

print(len(cpf_clientes))  # contem cpf repetidos

set_cpf_clientes = set(cpf_clientes)  # cpf nao esta repetido
print(f'Qauntidade de cpf: {len(set_cpf_clientes)}')
print(list(set_cpf_clientes))
