PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')

textos = [
    'Maria adora falar sobre religião',
    'João gosta de futebol e política',
    'Fernando foi à praia com sua irmã'
]

for texto in textos:
    found = False

    for palavra in texto.lower().split():

        if palavra in PALAVRAS_PROIBIDAS:
            print("Texto censurado, contém uma palavra proibida. ", palavra)
            found = True
            break

    if not found:
        print("Texto autorizado!!\n",texto)