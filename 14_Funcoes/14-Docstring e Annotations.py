# Docstring - O que a fuincao faz, quais valores ela tem como argumento e o que significa cada valor

def minha_soma(num1, num2):
    '''Faz a soma de dois numeros e devolve como resposta um numero inteiro
    Parameters:
        num1 (int): primeiro numero a ser somado
        num2 (int): segundo numero a ser somado
    
    Returns:
        soma (int)
    '''
    soma = num1 + num2 
    return soma 

minha_soma(5, 6)


# Annotation - Eh focado no parametro o que ele deve "ser"

def subtracao(num1: int, num2: int):
    resp = num1 - num2
    return resp

subtracao(10, 5)
