from random import randint

def sortear_dado():
    dado = randint(1,6)
    return dado

for numero in range(1, 7):
    if numero % 2 == 1:
        continue

    if numero == sortear_dado():
        print("Acertou ", numero)
        break
else:
    print("Não acertou")