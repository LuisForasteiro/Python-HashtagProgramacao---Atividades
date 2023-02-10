def calcular_tributo(preco, custo, lucro):
    imposto = preco - custo - lucro
    carga = imposto/preco
    return carga


p_preco = float(input('Digite o preco do produto: '))
p_custo = float(input('Digite o custo: '))
p_lucro = float(input('Digite o Lucro: '))


print(f'{calcular_tributo(preco=p_preco, custo=p_custo, lucro=p_lucro):.1%}')
