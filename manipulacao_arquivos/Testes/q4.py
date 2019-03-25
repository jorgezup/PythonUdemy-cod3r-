def test_4():
    import csv
    from operator import itemgetter

    lista = []

    arquivo = open('data.csv', 'r')
    dados = csv.reader(arquivo.readlines()[1:])

    # ordenado = sorted(dados, key=itemgetter(17), reverse=True)
    ordenado = sorted(dados, key=lambda row: float(row[17]), reverse=True)

    for nome in ordenado[0:10]:
       lista.append(nome[2])

    return lista

if __name__ == '__main__':
    a = test_4()
    print(a)
