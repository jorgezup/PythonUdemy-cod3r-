#import math
from math import pi

raio = input('Informe o raio: ')

#formula = math.pi*(raio**2)
formula = pi*(float(raio)**2)

print(f'A area da circunferência é: {formula}')

print('Nome do módulo: ', __name__)
