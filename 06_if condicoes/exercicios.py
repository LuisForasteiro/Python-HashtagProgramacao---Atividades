meta = 1000
funcio01 = 1000
funcio02 = 770
funcio03 = 2500

if funcio01 >= meta:
    bonus = funcio01 * 0.1
    print(f'Bonus funcionaria 01 {bonus}')
else:
    bonus = 0
    print(f'Bonus funcionaria 01 {bonus}')


# Exercicio 02
meta = 1000
meta_funcionario = float(input("Digite a Quantidade de vendas: "))

if meta_funcionario >= meta:
    print('ATINGIU A META!')
    if meta_funcionario >= 2000:
        bonus = meta_funcionario * 0.15
        print(f'SEU BONUS FOI DE R$ {bonus} - 15%')
    else:
        bonus = meta_funcionario * 0.1
        print(f'SEU BONUS FOI DE R$ {bonus} - 10%')
else:
    print(f'NAO ATINGIU A META DE {meta} - 0%')


# Ecercicios 03
produto = input('Qual o produto: ').upper()
categoria = input('Qual a categoria: ').upper()
qtde = int(input('Qual a quantidade do produto: '))

if produto and categoria and qtde:  # Verificando se todas as informacoes estao preenchidas!
    if categoria in ('BEBIDAS', 'BEBIDA'):
        if qtde < 75:
            print(
                f'Solicitar {produto} a equipe de compras, temos apenas {qtde} unidades em estoque')
        else:
            print('Produto com estoque OK')

    elif categoria == 'LIMPEZA':
        if qtde < 30:
            print(
                f'Solicitar {produto} a equipe de compras, temos apenas {qtde} unidades em estoque')
        else:
            print('Produto com estoque OK')

    elif categoria in ('ALIMENTOS', 'ALIMENTO'):
        if qtde < 50:
            print(
                f'Solicitar {produto} a equipe de compras, temos apenas {qtde} unidades em estoque')
        else:
            print('Produto com estoque OK')
    else:
        print(
            'DIGITE APENAS UMA DAS TRES OPCOES [ALIMENTOS, BEBIDAS, LIMPEZA]')
else:
    print('Preencha todas a informacoes!')