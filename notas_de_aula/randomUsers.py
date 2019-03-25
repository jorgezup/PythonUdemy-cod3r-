import random
import sys

qntdUsers = int(input("Quantos usuários a cadastrar: "))

listaUsers = []
lst = []
cont = 0

while cont < qntdUsers:
    nome = str(input("Digite um nome: "))
    listaUsers.append(nome)
    lst.append(nome)
    cont +=1

for user in listaUsers:
    sorteado = random.choice(lst)
    if sorteado == user:
        while sorteado == user:
            sorteado = random.choice(lst)
    print(f"O {user} tirou o {sorteado}")
    lst.remove(sorteado)