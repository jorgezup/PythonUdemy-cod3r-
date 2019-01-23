import random
import sys

lista_jogadores = []
timeB = []
timeA = []
with open("jogadores.txt") as f:
    for nome in f:
        nome_jogador = nome.strip()
        lista_jogadores.append(nome_jogador)
        timeB.append(nome_jogador)

cont = 0
while cont < len(lista_jogadores)//2:
    escolhido = random.choice(timeB)
    if cont < 5:
        timeA.append(escolhido)
        timeB.remove(escolhido)
    cont +=1

print(f"Time A: {timeA}")
print(f"Time B: {timeB[0:5]}")
if len(timeB) > 5:
    print(f"Time C: {timeB[5:]}")
