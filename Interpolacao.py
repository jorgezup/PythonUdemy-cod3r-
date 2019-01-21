nome, idade, salario = 'Jorge', 27, 1967.98

print('Nome: %s Idade: %d Salário: %.2f %r\n\n' %(nome, idade, salario, True))

print("Nome: {}\nIdade: {}\nSalario: {}".format(nome, idade, salario))

print(f"\n\nNome: {nome}\nIdade: {idade}\nSalário: {salario}")

from string import Template
print("\n\n")
s = Template('Nome: $nome_templ Idade: $idade_templ')
print(s.substitute(nome_templ=nome, idade_templ=idade))
