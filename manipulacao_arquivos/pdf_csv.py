import csv

with open("resultado.csv") as arquivo:
    cont=0
    for linha in csv.reader(arquivo):
        if linha[1] == 'ANDS':
            cont +=1
            print(linha)

print(cont)
