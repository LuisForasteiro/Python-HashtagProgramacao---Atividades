import time

segundos_hoje = time.time()
print(segundos_hoje)

data_hoje = time.ctime()
print(data_hoje)

tempo_inicial = time.time()
for i in range(100000000):
    pass

tempo_final = time.time()
duracao = tempo_final - tempo_inicial
print(f'levou {duracao} segundos')


# Fazer o cogio esperar alguns segundos antes de rodar
time.sleep(5)
