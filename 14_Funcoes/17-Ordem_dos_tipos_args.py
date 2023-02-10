'''
regra padrao - Sempre os positional vem antes e depois os kwords arguments
            - Sempre os argumentos individuais vem antes e depois os multiplos!

'''

# correto
def minha_funcao(num1, num2, *args, **kwargs):
    pass

#nao funciona
def minha_funcao_2(*args, num1, **kwargs):
    pass
