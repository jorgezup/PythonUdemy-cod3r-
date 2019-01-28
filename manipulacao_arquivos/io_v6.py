#FECHA automaticamente quando o arquivo termina
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome:{}, Idade:{}'.format(*pessoa), file=saida)


if arquivo.closed:
    print('Arquivo já foi fechado !!')

if saida.closed:
    print("Saída já foi fechado!")


