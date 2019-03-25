def mapear(funcao, lista):
    for elemento in lista:
        yield funcao(elemento) # avaliação tardia


if __name__ == '__main__':
    print(list(mapear(lambda x: x ** 2, [2, 3, 4])))
