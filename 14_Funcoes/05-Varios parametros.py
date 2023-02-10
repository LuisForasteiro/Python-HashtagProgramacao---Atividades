def bebida_categoria(bebida, categoria):
    bebida = bebida.upper()
    if categoria in bebida:
        return True
    else:
        return False


produtos = ['beb87989', 'TFA23962', 'TFA64715', 'TFA69555', 'TFA56743', 'BSA45510', 'TFA44968', 'CAR75448', 'CAR23596', 'CAR13490', 'BEB21365', 'BEB31623', 'BSA62419', 'BEB73344', 'TFA20079', 'BEB80694', 'BSA11769', 'BEB19495', 'TFA14792',
            'TFA78043', 'BSA33484', 'BEB97471', 'BEB62362', 'TFA27311', 'TFA17715', 'BEB85146', 'BEB48898', 'BEB79496', 'CAR38417', 'TFA19947', 'TFA58799', 'CAR94811', 'BSA59251', 'BEB15385', 'BEB24213', 'BEB56262', 'BSA96915', 'CAR53454', 'BEB75073']

for produto in produtos:
    if bebida_categoria(bebida=produto, categoria='BEB'):  # Pode passar dessa forma
        print(f'Enviar {produto.upper()} para setor de BEBIDAS ALCOOLICAS')
    elif bebida_categoria(produto, 'BSA'):  # Pode passar dessa forma
        print(
            f'Enviar {produto.upper()} para setor de BEBIDAS *NAO* ALCOOLICAS')


qtde_produtos = len(produtos)
print(f'Qtde Total: {qtde_produtos}', 'teste1',
      'teste2', 'teste3', sep='\n')
# Separador de palavras sep='\n', tem que ser utilizado no final do print(..., sep='\n')


# Existe 2 formas de passar um paramatro... pode ser em ordem (parametro1, parametro2, parametro3...)
# Ou voce pode declar ele na funcao (bebida=produto, categoria='BEB')... igual no exemplo
