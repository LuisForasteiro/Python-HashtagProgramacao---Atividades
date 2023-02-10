meta = 10000
vendas = {'joao': 15000,
          'julia': 27000,
          'marcus': 9900,
          'maria': 3750,
          'ana': 10300
          }


def calculo_meta(meta, lista_vendas):
    bateram_meta = []
    for vendedor in lista_vendas:
        if vendas[vendedor] > meta:
            bateram_meta.append(vendedor)
    perc_bateu_meta = len(bateram_meta) / len(lista_vendas)
    return (bateram_meta, perc_bateu_meta)


print(calculo_meta(meta=meta, lista_vendas=vendas))


# Ou Fazer o unpacking

vendedores_bateu_meta, percentual_meta = calculo_meta(meta, vendas)
print(f'Os vendedores que bateram a meta: {vendedores_bateu_meta}'
      f'\nPorcentagem meta: {percentual_meta:.2%}')
