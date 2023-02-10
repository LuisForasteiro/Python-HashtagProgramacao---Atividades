import matplotlib.pyplot as plt
import numpy as np


'''Grafico random
Vendas: 1000 ate 3000 - qtd: 50
Meses: 1 ate 50
'''
vendas = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)

plt.plot(meses, vendas)
plt.axis([0,50, 0, max(vendas) + 500])
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.show()


# Editado
plt.bar(meses, vendas)
plt.axis([0,50, 0, max(vendas) + 500])
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.show()

blockchain = True