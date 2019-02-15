entrada = open("16s_bacteria.fasta").readlines()
saida = open("bacteria.html", "w")

# Cria um dicionário
contador = {}

# Percorre os valores, fazendo a combinação em PAR
for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        # inicia contador para cada par de letra
        contador[i+j] = 0

# Retira a quebra de linha, trocando o \n por nada
entrada = entrada.replace("\n", "")

# Percorre o tamanho do arquivo -1, faz o somatório para cada PAR
for k in range(len(entrada)-1):
    # Realiza a soma no par de letra
    contador[entrada[k]+entrada[k+1]] =+ 1

# HTML
saida.write("<div>")

i = 1
for k in contador:
    # Transparencia recebe o par de valor dividido
    # pelo valor máximo armazenado em contador
    transparencia = contador[k]/max(contador.values())
    saida.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; "
                "float:left; background-color:rgba(0, 0, 0, "+str(transparencia)+"')>"+k+"</div>")

    if i%4 == 0:
        saida.write("<div style='clear:both'></div>")

    i+=1

saida.close()
