# Analise de vendas
meta = 10000
vendas = [
    ('Joao', 15000),
    ('Julia', 27000),
    ('Luis', 20999),
    ('Marcus', 9000),
    ('Ana', 10300),
    ('Alon', 7890)
]
print(f'***META: {meta}***')
for venda in vendas:
    nome, metas = venda
    if metas >= meta:
        print(f'Vendedor {nome} bateu a meta, com {metas} vendas')


# Comparacao com ano anterior

vendas_produtos = [
    ('iphone', 558147, 951642),
    ('galaxy', 712350, 244295),
    ('ipad', 573823, 26964),
    ('tv', 405252, 787604),
    ('máquina de café', 718654, 867660),
    ('kindle', 531580, 78830),
    ('geladeira', 973139, 710331),
    ('adega', 892292, 646016),
    ('notebook dell', 422760, 694913),
    ('notebook hp', 154753, 539704),
    ('notebook asus', 887061, 324831),
    ('microsoft surface', 438508, 667179),
    ('webcam', 237467, 295633),
    ('caixa de som', 489705, 725316),
    ('microfone', 328311, 644622),
    ('câmera canon', 591120, 994303)
]

for produto in vendas_produtos:
    nome_produto, venda_2019, venda_2020 = produto
    if venda_2020 > venda_2019:
        print(
            f'Produto: {nome_produto}\nVenda 2019: {venda_2019}\nVenda 2020: {venda_2020}\nCrescimento: {venda_2020/venda_2019 - 1:.2%}')
