produtos = ['iphone 10', 'ipad', 'ipod', 'kingle', 'adega']
vendas_2021 = [1000, 9867, 9482, 2174, 1038]
vendas_2022 = [3472, 9489, 986, 1030, 2367]

for i, produto in enumerate(produtos):
    if vendas_2022[i] > vendas_2021[i]:
        print(
            f'Produto: {produto} - 2021: {vendas_2021[i]} unidades - 2022: {vendas_2022[i]} unidades - Crescimento: {vendas_2022[i]/ vendas_2021[i]:.2%}')
