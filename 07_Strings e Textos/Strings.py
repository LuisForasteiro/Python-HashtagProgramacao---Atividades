email = 'luis@gmail.com'
nome = 'Luis Felipe'

# Tamanho do texto / caracteres
print(len(email))
print(len(nome))

# Pegar o indice
print(email[0])
print(nome[8])

# Pega o indice pra frente ou para tras :
print(email[6:])
print(nome[3:])
print(email[:-1])
print(nome[2:8])


# fixacao
print(f'Tamanho email: {len(email)} caracteres')
print(f'Primeira letra: {email[0]}')
print(f'Ultimo caractere: {email[-1]}')
print(f'Servidor email: {email[4:]}')


# Operacoes em Strings
print('@' in email)


# Formulas de Texto
texto = 'luis FELIPE silva bezerra'
print(texto.upper())  # todas a letras em maiusculo
print(texto.capitalize())  # primeira letra maiusculo
print(texto.casefold())  # todas as letras em minusculo
print(texto.title())  # primeira letra em maiusculo das palavras
print(texto.strip())  # junta os espacos do comeco do texto
print(texto.endswith('gmail.com'))
print(texto.find('F'))
print(texto.replace('u', 'P'))
print(texto.split('s'))

# Format tipos

