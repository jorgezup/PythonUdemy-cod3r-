from math import pi
import sys

def circulo(raio):
       return pi*(float(raio)**2)

def help():
    print("""\
           É necessário informar o raio do círculo.
           Sintaxe: area_circulo <raio>""")


if __name__ == '__main__':
    if len(sys.argv) < 2:
       help()
       sys.exit(1)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print(f'Área do círculo: {area}')




