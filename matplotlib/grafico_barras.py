import matplotlib.pyplot as plt

x = [1, 2, 3, 5, 7]
y = [7, 8, 9, 2, 3]

# Título
titulo = "Gráfico Barras"
# Eixos
eixoX = "Eixo X"
eixoY = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

# plotar o gráfico
plt.bar(x, y)
# mostrar o gráfico
plt.show()