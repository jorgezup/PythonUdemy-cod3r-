import matplotlib.pyplot as plt

x = [1, 2, 3, 5, 7]
y = [7, 8, 9, 2, 3]
z = [20, 100, 10, 33]

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
plt.scatter(x, y, label="Meus Pontos", color="#FF99AA", marker="h", s=z)
# linha
plt.plot(x, y, color="k", linestyle="-.")

# inserir legenda
plt.legend()

# mostrar o gráfico
plt.show()


# Documentação oficial do Matplotlib
# A seguir, alguns exemplos de argumentos que podem ser aplicados ao método plot( ).
#
#
#
# color:	cor (ver exemplos abaixo)
#
# label:	rótulo
#
# linestyle:	estilo de linha (ver exemplos abaixo)
#
# linewidth: largura da linha
#
# marker:	marcador (ver exemplos abaixo)
#
#
#
# CORES (color)
# 'b'	blue
#
# 'g'	green
#
# 'r'	red
#
# 'c'	cyan
#
# 'm'	magenta
#
# 'y'	yellow
#
# 'k'	black
#
# 'w'	white
#
#
#
# Marcadores (marker)
# '.'	point marker
#
# ','	pixel marker
#
# 'o'	circle marker
#
# 'v'	triangle_down marker
#
# '^'	triangle_up marker
#
# '<'	triangle_left marker
#
# '>'	triangle_right marker
#
# '1'	tri_down marker
#
# '2'	tri_up marker
#
# '3'	tri_left marker
#
# '4'	tri_right marker
#
# 's'	square marker
#
# 'p'	pentagon marker
#
# '*'	star marker
#
# 'h'	hexagon1 marker
#
# 'H'	hexagon2 marker
#
# '+'	plus marker
#
# 'x'	x marker
#
# 'D'	diamond marker
#
# 'd'	thin_diamond marker
#
# '|'	vline marker
#
# '_'	hline marker
#
#
#
#
#
# Tipos de linha (linestyle)
# '-'	solid line style
#
# '--'	dashed line style
#
# '-.'	dash-dot line style
#
# ':'	dotted line style
#
#
#
# Fonte: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html