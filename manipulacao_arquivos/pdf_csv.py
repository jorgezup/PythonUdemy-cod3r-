import csv

with open("resultado.csv") as arquivo:
    cont=0
    for linha in csv.reader(arquivo):
        if linha[3] == 'ATENDEU' and linha [4] == '7':
            cont +=1
            print(linha)

print(cont)
