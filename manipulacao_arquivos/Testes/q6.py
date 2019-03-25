def test_6():
    import csv

    arquivo = open('data.csv').readlines()[1:]

    dicionario_idades = {}

    for linha in csv.reader(arquivo):

        idade = int(linha[6])

        if idade not in dicionario_idades:
            dicionario_idades[idade] = 0


    for i in csv.reader(arquivo):
        idade = int(i[6])
        # int(idade)
        dicionario_idades[idade] +=1

    return dicionario_idades


if __name__ == '__main__':
    a = test_6()
    print(a)
