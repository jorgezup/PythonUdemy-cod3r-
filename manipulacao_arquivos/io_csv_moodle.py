import csv

lista_tutores = []
lista = {}
with open('moodle.csv') as entrada:
    # coluna 0 -> nome_breve
    # coluna 1 -> lista_tutores
    for coluna in csv.reader(entrada):
        if coluna[1] not in lista_tutores:
            lista_tutores.append(coluna[1])
        for k, nome_tutor in enumerate(lista_tutores):

            if coluna[1] == nome_tutor:
                lista{[k]:coluna[0]}
            print(lista)




    #
    #
    #
    #     for nome_breve in lista_tutores:
    #         nome_breve = coluna[0]
    #         if lista_tutores == coluna[1]:
    #             print(nome_breve)
    #


