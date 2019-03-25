generator = (i ** 2 for i in range(1000) if i % 2 == 0)
print(next(generator))  # Saída 0
print(next(generator))  # Saída 4
print(next(generator))  # Saída 16
print(next(generator))  # Saída 32
print(next(generator))  # Saída 64
# print(next(generator))  # Erro

dobro_pares = [i * 2 for i in range(1000) if i % 2 == 0]

import sys
print('Size of Generator: ', sys.getsizeof(generator))
print('Size of List: ', sys.getsizeof(dobro_pares))

#List Comprehension carrega todos os valores na memória
#Generator carrega apenas o valor próximo, quando solicitado.
