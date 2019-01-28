# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
def fibonnacci(quantidade):
    resultado = [0, 1]

    #Underline(_) variável não usada
    #for i in range(2, quantidade):
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    #Listar os 20 primeiros números da quantidade
    for fib in fibonnacci(20):
        print(fib, end=', ')
