pessoas = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 21},
    {'nome': 'José', 'idade': 16},
    {'nome': 'Jorge', 'idade': 48},
    {'nome': 'Joaquim', 'idade': 68},
    {'nome': 'Felisberto', 'idade': 8}
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

nome_grande = filter(lambda n: len(n['nome']) > 6, pessoas)
print(list(nome_grande))