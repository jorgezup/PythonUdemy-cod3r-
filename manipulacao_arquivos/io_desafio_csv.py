import csv

with open('desafio-ibge.csv', encoding='latin1') as arquivo:
    for linha in csv.reader(arquivo):
        print(f'{linha[8]}: {linha[3]}')