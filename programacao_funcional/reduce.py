from functools import reduce

pessoas = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 21},
    {'nome': 'José', 'idade': 16},
    {'nome': 'Jorge', 'idade': 48},
    {'nome': 'Joaquim', 'idade': 68},
    {'nome': 'Felisberto', 'idade': 8}
]

soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
print(soma_idades)