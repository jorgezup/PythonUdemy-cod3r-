lista = []

#print(type(lista))
#print(dir(lista))
#print(help(lista))

print(len(lista))

lista.append(5)
lista.append(76)
lista.append(99)
lista.insert(1, 2)
lista.append(9)
print(lista)
lista.remove(5)
print(lista)
lista.reverse()
print(lista)

print('\n')
print("# "*30)
print('\n')

lista2 = [1, 5, 'Rebeca', 'Maria', 'Joana', 3.1415]
print(lista2.index('Rebeca'))
print(1 in lista2)
print('Maria' in lista2)
print(lista2[-1])
print(lista2[2:])
del lista2[3]
print(lista2)
