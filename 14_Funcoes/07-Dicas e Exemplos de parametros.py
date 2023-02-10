def categoria(bebida, codigo):
    bebida = bebida.upper()
    if codigo in bebida:
        return True
    else:
        return False


# Texto para upper()
codigo_prod = 'beb90909'
print(codigo_prod.upper())

# ------------------------------\

# sort()
vendas_ano = [100, 200, 500, 390, 400]
vendas_ano.sort()
print(vendas_ano)

# -------------------------

vendas_novdez = [600, 290]

vendas_ano.extend(vendas_novdez)
print(vendas_ano)



if categoria(codigo_prod, 'BEB'):
    print('BEBIDA ALCOOLICA')

# ------------------------
