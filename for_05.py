PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')

textos = [
    'Maria adora falar sobre religião',
    'João gosta de futebol e política',
    'Fernando foi à praia com sua irmã'
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print("Texto censurado, contém uma palavra proibida. ", palavra)
            break
    else:
        print("Texto autorizado!!\n",texto)