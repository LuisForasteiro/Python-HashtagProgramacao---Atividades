'''*args posso passar quantos arguemntos eu quiser! 
Ele junta todos os argumentos em uma TUPLA (numero, numero, numero)
'''

def minha_soma(*args):
    print(args)
    soma = 0
    for numero in args:
        soma += numero
    return soma

print(minha_soma(10, 20, 40, 60))


'''**kwargs -> argumentos vem em formato de dicionario
Argumento q tem palavras chaves. Pode passar quantos argumentos de palavras chaves precisar
'''

def preco_final(preco, **kwargs):
    print(kwargs)
    if 'desconto' in kwargs:
        preco *= (1 - kwargs['desconto'])
    if 'garantia_extra' in kwargs:
        preco += kwargs['garantia_extra']
    if 'imposto' in kwargs:
        preco *= (1 + kwargs['imposto'])
    return preco

print(preco_final(1000, desconto=0.1, imposto= 0.3, garantia_extra=500))