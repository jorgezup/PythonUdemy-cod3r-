def executar (funcao):
    if callable(funcao):
        funcao()

def bom_dia():
    print('Bom dia !')

def boa_tarde():
    print('Boa tarde !')

if __name__ == '__main__':
    executar(boa_tarde())
    executar(bom_dia())
    executar(1)
