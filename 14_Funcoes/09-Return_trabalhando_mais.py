# retornar um numero

def soma(num1, num2, num3):
    return num1 + num2 + num3


# retornar texto
def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  ", " ")
    texto = texto.strip()
    return texto


# Retornanr Boolean
def boleano(vendas, meta):
    if vendas > meta:
        return True
    else:
        return False


# retornar lista, tupla ou dicionario
def filtrar_lista_texto(lista, pedaco_texto):
    lista_filtrada = []
    for item in lista:
        if pedaco_texto in item:
            lista_filtrada.append(item)
    return lista_filtrada


lista_texto = ['luis@gmail.com', 'Lucas@hotmail.com',
               'joao@gmail.com', 'alon@gmail.com']

print(filtrar_lista_texto(lista_texto, '@hotmail'))
