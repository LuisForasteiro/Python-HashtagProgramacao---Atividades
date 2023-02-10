# Utilizando Range!s

produtos = ['iphone', 'ipad', 'macbook', 'iMac']
estoque = [100, 400, 50, 90]

for i in range(4):
    print(f'{produtos[i]}: {estoque[i]} estoque')

# range com inicio e fim
print(range(1, 10))

for i in range(1, 10):
    print(i)


# passo do range

print(range(0, 100, 10))
for i in range(0, 1000, 10):
    print(i)
