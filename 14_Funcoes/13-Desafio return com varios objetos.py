precos_imoveis = [2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37, 2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37, 2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37, 2.17, 1.54, 1.45,
                  1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37, 2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37, 2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37, 2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37, 2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37]
tamanho_imoveis = [207, 148, 130, 203, 257, 228, 160, 194, 232, 147, 2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37, 2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37, 2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25,
                   1.37, 2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37, 2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37, 2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37, 2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37]

# Modelo de machine leraning onde eu determino o quanto ira para ele treinar e vai para teste

fator = 0.2
i = int((1 - fator) * len(precos_imoveis))

precos_treino = precos_imoveis[:i]
precos_teste = precos_imoveis[i:]


def separar_lista(precos, tamanhos, fator=0.1):
    if len(precos) == len(tamanhos):
        i = int((1 - fator) * len(precos))
        precos_imoveis_treino = precos[:i]
        precos_imoveis_teste = precos[i:]
        tamanho_imoveis_teste = tamanhos[i:]
        tamanho_imoveis_treino = tamanhos[:i]
        return (precos_imoveis_treino, precos_imoveis_teste, tamanho_imoveis_treino, tamanho_imoveis_teste)
    else:
        print(
            'AS LISTAS DE PRECOS E TAMANHOS DOS IMOVEIS NAO TEM A MESMA QUANTIDADE DE ITENS')
        return None


print(separar_lista(precos_imoveis, tamanho_imoveis))
