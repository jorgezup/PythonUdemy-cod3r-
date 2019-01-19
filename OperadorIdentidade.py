x = 3
y = x
z = 3

a = x is y
print(a)

b = y is z
print(b)

c = x is not z
print(c)


#########LISTA##############

lista_A = [1, 2, 3]
lista_B = lista_A
lista_C = [1,2,3]

x = lista_A is lista_B
print(x)
### Apesar de os valores serem os mesmos.
### É falso, pois apontam para espaços distintos da memória
y = lista_B is lista_C
print(y)
