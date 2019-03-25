import csv

lista_tutores = []
lista = {}
with open('moodle.csv') as entrada:
    # coluna 0 -> nome_breve
    # coluna 1 -> lista_tutores
    for coluna in csv.reader(entrada):
        if coluna[1] not in lista_tutores:
            lista_tutores.append(coluna[1])
    #print(lista_tutores)
        for nome in lista_tutores:
            if nome == coluna[1]:
                lista.update("nome", nome, "curso", coluna[0])
                print(lista)
