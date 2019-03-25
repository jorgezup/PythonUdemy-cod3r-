import csv

lista_nacionalidades = []
lista_unica = []
with open('data.csv') as arquivo:
    for linha in csv.reader(arquivo.readlines()[1:]):
        lista_nacionalidades.append(linha[14])

for elemento in lista_nacionalidades:
    if elemento not in lista_unica:
        lista_unica.append(elemento)

print(len(lista_unica))