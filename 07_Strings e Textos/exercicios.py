# Cadastro CPF
cpf = input('DIGITE SEU CPF: ')
cpf = cpf.replace('.', '').replace('-', '').strip()


while cpf:
    if len(cpf) == 11 and cpf.isnumeric():
        print(f'CPF: {cpf}')
    else:
        print('DIGITE CORRETAMENTE O CPF!')
        break

# Cadastro email
nome = input('Digite seu nome: ')
email = input('Digite seu email: ')

if nome and email:
    arroba = email.find('@')
    servidor = email[arroba:]

    if arroba != -1 and '.' in servidor:
        print('Cadastro concluido!')
    else:
        print('Digite seu email invalido')

else:
    print('Email ou nome nao preenchidos')
