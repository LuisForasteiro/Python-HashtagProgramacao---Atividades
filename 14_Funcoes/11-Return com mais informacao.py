from audioop import mul


def operacoes(n1, n2):
    soma = n1 + n2
    multi = n1 * n2
    divisao = n1 / n2
    subtra = n1 - n2
    return (soma, multi, divisao, subtra)


# sempre retorna uma TUPLA por padrao...
print(operacoes(20, 5))

