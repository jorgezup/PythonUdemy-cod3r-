import matplotlib.pyplot as plt

x = [1, 2, 3, 5, 7]
y = [7, 8, 9, 2, 3]

# Título
titulo = "Scatterplot: gráfico de dispersão"
# Eixos
eixoX = "Eixo X"
eixoY = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

# plotar o gráfico
# dispersão
plt.scatter(x, y, label="Meus Pontos", color="r")
# linha
plt.plot(x, y)

# inserir legenda
plt.legend()

# mostrar o gráfico
plt.show()
