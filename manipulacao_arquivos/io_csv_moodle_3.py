import csv

arquivo = open('moodle.csv')

linhas = csv.reader(arquivo)
tutores=[]
for linha in linhas:
     # print(linha)
     tutores.append(linha[1])

tutores = set(tutores)
for nome in tutores:
     print(nome)

arquivo2 = open('moodle.csv')
colunas = csv.reader(arquivo2)
for col in colunas:
     if nome == col
     print(col[0])
#
# dict_1={}
# nome_tutor = []
# for linha in csv.reader(arquivo):
#      print("Nome Breve: ", linha[0], "Tutor: ", linha[1])
#      if linha[1] not in nome_tutor:
#           nome_tutor.append(linha[1])
#
#      print(nome_tutor)



