def cadastrar_produto():
    produto = input('Digite o nome do produto: ')
    produto = produto.casefold()
    produto = produto.strip()
    print(f'Produto cadastrado: **{produto}**')
    return produto

# ou

if __name__ == "__main__":
    cadastrar_produto()
