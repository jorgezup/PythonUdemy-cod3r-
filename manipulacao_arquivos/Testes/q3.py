def test_3():

    import csv
    lista = []
    with open('data.csv') as arquivo:
        for linha  in csv.reader(arquivo.readlines()[1:21]):
            lista.append(linha[2])
        return(lista)

if __name__ == '__main__':
    a = test_3()
    print(a)