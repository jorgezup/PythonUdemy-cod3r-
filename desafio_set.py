PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}

textos = [
    'Maria adora falar sobre religião',
    'João gosta de futebol e política',
    'Fernando foi à praia com sua irmã'
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))

    if intersecao:
        print('Texto possui palavras proibidas: ', intersecao)
    else:
        print('Texto autorizado: ', texto)