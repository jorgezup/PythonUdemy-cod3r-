compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 40}
)


def calc_preco_total(compras):
    return compras['quantidade'] * compras['preco']


totais = tuple(map(calc_preco_total, compras))

print('Preços totais: ', totais)
print('Total geral: ', sum(totais))
