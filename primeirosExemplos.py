salario = 3678.78
despesas = 2589.25
saldo = 1000

percentual_gastos = (despesas*100)/salario

print("{}".format(percentual_gastos))


meta = saldo > 0 and salario - despesas >= 0.2 * salario

print(meta)