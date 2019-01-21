from math import pi
import sys
import errno


def circulo(raio):
       return pi*(float(raio)**2)

def help():
    print("""\
           É necessário informar o raio do círculo.
           Sintaxe: area_circulo <raio>""")


if __name__ == '__main__':
    if len(sys.argv) < 2:
       help()
       sys.exit(errno.EPERM)
    #   sys.exit(1)

    #elif not sys.argv[1].isnumeric():
    #    help()
    #    print("O raio deve um valor numérico")
    if not sys.argv[1].isnumeric():
        help()
        print("O raio deve ser um valor numérico")
        sys.exit(errno.EINVAL)
    #else:
    raio = sys.argv[1]
    area = circulo(raio)
    print(f'Área do círculo: {area}')




