nota = float(input("Digite a nota: "))

if nota >= 9:
    print("Quadro de Honra")

elif nota >= 7:
    print("Aprovado")

elif nota >= 5:
    print("Recuperação")

elif nota >= 3:
    print("Recuperação + Trabalho")

else:
    print("Reprovado!!")