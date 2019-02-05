pessoa = {'nome': 'Prof(a). Eiva', 'idade':28, 'cursos': ['inglês', 'química', 'legislação']}
print(pessoa)

print(len(pessoa))

print(pessoa['nome'])
print(pessoa['cursos'][1])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

print('\n')
print(" # "*10)
print('\n')

pessoa = {'nome':'Prof. ALberto', 'idade':45, 'curso':['Redes de Computadores', 'Programação I']}
print(pessoa['idade'])
print(pessoa)
pessoa.update({'idade':49})
print(pessoa['idade'])
pessoa.update({'sexo':'masculino'})
pessoa.pop('nome')
print(pessoa)
del pessoa['curso']
print(pessoa)
pessoa.clear()
print(pessoa)
