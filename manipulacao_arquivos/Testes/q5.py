def test_5():
    import csv
    from operator import itemgetter

    arquivo = open('data.csv', 'r')
    dados = csv.reader(arquivo)


    ordenado = sorted(dados, key=itemgetter(6), reverse=True)
    lista = []

    for nome in ordenado[1:11]:
       lista.append(nome[2])

    return lista

if __name__ == '__main__':
    a = test_5()
    print(a)