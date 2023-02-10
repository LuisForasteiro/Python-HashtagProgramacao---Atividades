'''
Trabalhando com GRAFICO dentro do python!
- Melhor visualizacao dos dados
'''

import matplotlib.pyplot as plt

vendas_meses = [1829, 2949, 3867, 2483, 2847, 4590]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun']

plt.plot(meses, vendas_meses)
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0, 6, 0, max(vendas_meses) + 500])
plt.show()