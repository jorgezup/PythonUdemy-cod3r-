arquivo = open('pessoas.csv')


try:
    for registro in arquivo:
        print('Nome:{}, Idade:{}'.format(*registro.strip().split(',')))
finally:
    #SEMPRE será executado
    #MESMO COM ERRO
    arquivo.close()
    print('Finally')

if arquivo.closed:
    print('Arquivo já foi fechado !!')


