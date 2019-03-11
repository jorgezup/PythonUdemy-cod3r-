import csv
entrada = open('teste.csv').readlines()[1:]
saida = open('saida.txt', 'w')

cont = {}
lista_cursos = []
lista_nomes = []

for i in csv.reader(entrada):
    lista_cursos.append(i[0])

for j in csv.reader(entrada):
    lista_nomes.append(j[1])

for k in range(len(lista_cursos)):
    print('curso{} role{}' .format(k, k), end=' ')

for nome in set(lista_nomes):
    cont[nome] = []
    funcao = input(f'Informe o nome da funçao deseja para {nome}: ')
    for c in csv.reader(entrada):

        if nome in c:
            cont[nome].append(c[0])
            cont[nome].append(funcao)
    print(nome,cont[nome], file=saida)
