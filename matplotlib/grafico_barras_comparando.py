import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [7, 8, 9, 2, 3]

x2 = [2, 4, 6, 8, 10]
y2 = [3, 2, 5,  6, 8]

# Título
titulo = "Gráfico Barras Comparação"
# Eixos
eixoX = "Eixo X"
eixoY = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

# plotar o gráfico
plt.bar(x1, y1, label = "Grupo 1")
plt.bar(x2, y2, label = "Grupo 2")

# Inserir Legenda no gráfico
plt.legend()

# mostrar o gráfico
plt.show()