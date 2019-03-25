# List Comprehension
dobro_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobro_pares)

# Versão "Normal"
dobro_pares = []
for i in range(10):
    if i % 2 == 0:
        dobro_pares.append(i*2)
print(dobro_pares)