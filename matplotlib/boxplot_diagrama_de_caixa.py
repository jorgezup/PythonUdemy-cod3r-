import matplotlib.pyplot as plt
import random

vetor = []

for i in range(18):
    num_aleatorio = random.randint(0, 5000)
    vetor.append(num_aleatorio)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()
