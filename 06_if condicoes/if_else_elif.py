# Como funciona!
meta = 5000
qtde_vendas = 4000

if qtde_vendas >= meta:
    print('Bateu a meta! ')
else:
    print(f'Nao bateu a meta! A meta era de: {meta}')

print('FIM PROGRAMA!')


# EXEMPLO IPHONE
meta = 50000.0
qtde_vendida = 65300.0

if qtde_vendida >= meta:
    print(
        f'Batemos a meta de vendas de iPhone. Vendemos {qtde_vendida} unidades')
else:
    print(
        f'Nao batemos a meta! Vendemos apenas {qtde_vendida} e a meta era de {meta}')


# if dentro de if
meta = 0.05
taxa = 0
rendimento = 0.02

if rendimento > meta:
    if rendimento > 0.20:
        taxa = 0.04
        print(f'A taxa foi de {taxa:.1%}')
    else:
        taxa = 0.02
        print(f'TAXA DE {taxa:.1%}')
else:
    taxa = 0
    print(f'Taxa de {taxa}')

# elif
meta = 20000
vendas = 25000

if vendas < meta:
    print('SEM BONUS')
elif vendas > (meta * 2):
    bonus = 0.07 * vendas
    print(f'Bonus 7%: {bonus}')
else:
    bonus = 0.03 * vendas
    print(f'GANHOU 3%: {bonus}')


# Comparadores
faturamento01 = 1000
faturamento02 = 2000
email = 'luis@gmail.com'

print('PROGRAMA 01')
if faturamento01 == faturamento02:
    print('FATURAMENTO IGUAIS')
else:
    print('FATURAMENTO DIFERENTES')

print('PROGRAMA 02')
if email != 'luis@gmail.com':
    print('EMAIL DIFERENTE!')
else:
    print('EMAIL CORRETO!')

print('PROGRAMA 03')
email_usuario = input('DIGITE SEU EMAIL: ')
if not '@' in email_usuario:
    print('EMAIL INCORRETO!')
else:
    pass


# CONDICOES E COMPARACOES (AND ou OR)
meta_loja = 5000
meta_funcionario = 2000
vendas_loja = 200000
vendas_funcionario = 1000

if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_funcionario
    print(f'BONUS FUNCIONARIO FOI DE {bonus}')
else:
    print('NAO GANHOU BONUS!')
