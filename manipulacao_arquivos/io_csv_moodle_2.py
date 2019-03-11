import csv

arquivo = open('moodle.csv')

linhas = csv.reader(arquivo)
#
# for linha in linhas:
#     print(linha)


lista_tutores=[]
tutor=[]
nome_breve=[]
dicionario={}
for linha in csv.reader(arquivo):
     if linha[1] not in lista_tutores:
          lista_tutores.append(linha[1])
     tutor.append(linha[1])
     #print(lista_tutores)
     nome_breve.append(linha[0])
     # print(f'{linha[0]}: {linha[1]}')
     dicionario = dict(zip(nome_breve, tutor))
for nome in lista_tutores:
     if nome in dicionario.values():
          print(dicionario.keys())
#print(dicionario.keys()) -> nome breve
#print(dicionario.values()) -> nome tutor


