# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
def fibonnacci(quantidade, sequencia=(0,1 )):
    #Importe: Condição de parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibonnacci(quantidade, sequencia + (sum(sequencia[-2:]),))

if __name__ == '__main__':
    #Listar os 20 primeiros números
    for fib in fibonnacci(20):
        print(fib, end=', ')
