# Crescimento da População Brasileita
# DataSus

import matplotlib.pyplot as plt

dados = open('populacao-brasileira.csv').readlines()

x = []
y = []

for i in range(len(dados)): #pega a quantidade de linhas do arquivo
    if i != 0: #ignora a primeira linha
        linha = dados[i].split(";") #recebe o dado na posicao i, faz o split por ;
        x.append(int(linha[0])) #posicao 0 da linha é o ano
        y.append(int(linha[1])) #posicao 1 da linha é a população

# Título, Eixos
plt.title("Crescimento da População Brasileira")
plt.xlabel("Ano")
plt.ylabel("População")

# Gráfico de Linha
plt.plot(x, y, color="k")

# Gráfico de Barras
plt.bar(x, y, color="#e4e4e4")

# Mostrar Gráfico
plt.show()