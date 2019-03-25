import csv

lista_club = []
lista_unica = []
with open('data.csv') as arquivo:
    for linha in csv.reader(arquivo.readlines()[1:]):
        lista_club.append(linha[3])

    lista_unica = list(set(lista_club))
    print(len(lista_unica))