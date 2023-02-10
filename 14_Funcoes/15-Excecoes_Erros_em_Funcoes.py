# Como testar erros e tratar excecoes!


def descobrir_servidor(email):
    try:
        posicao_a = email.index('@')
        servidor = email[posicao_a:]
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        else:
            return 'Nao determinado'
    except:
        raise Exception(f'Email digiteado sem @, digite novamente!')
        # Criando uma mensagem de erro!
        
    
email = input(f'Digite seu email: ')
print(descobrir_servidor(email))


# Tratamento completo de um erro

try:
    # Isolando um erro, caso o TRY passe, ele pula para o else e continua o codigo!
    pass
except:
    # caso o try nao de certo ele cai aqui no except
    pass
else:
    # continua o codigo do try!
    pass
finally:
    # roda independente se der erro ou nao!
    pass

# Mais comum utilizar try, except e else


