# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
def fibonnacci(quantidade):
    resultado = [0, 1]

    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    #Listar os 20 primeiros números da quantidade
    for fib in fibonnacci(20):
        print(fib, end=', ')
