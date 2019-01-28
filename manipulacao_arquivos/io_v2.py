arquivo = open('pessoas.csv')
#streaming, consome os dados conforme o necessário.
#Não carrega todos o arquivo na memoria
for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.split(',')))
arquivo.close()