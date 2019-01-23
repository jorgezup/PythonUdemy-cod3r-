produto = {'nome': 'Caneta Bic', 'preço': 3.25, 'importada': False,
           'estoque': 865}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)