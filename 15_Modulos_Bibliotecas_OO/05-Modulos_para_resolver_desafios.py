'''
Pegandos o top 3 produtos mais vendidos utilizando modulos

'''

from collections import Counter

vendas_tecnologia = {'notebook asus': 2500, 'iphone x': 1000, 'samsumg galaxy': 1809, 'iphone 11': 1389, 'iphone 12': 890}

count = Counter(vendas_tecnologia)
print(count.most_common(2))

