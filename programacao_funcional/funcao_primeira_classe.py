def dobro(x):
    return x * 2

def quadrado(x):
    return x ** 2

if __name__ == '__main__':
    # retorna alteranadamente a função dobro e quadrado no números de 1 a 10
    funcs = [dobro, quadrado] * 5
    for funcs, numero in zip(funcs, range(1, 11)):
        print(f'O {funcs.__name__} de {numero} é {funcs(numero)}')
