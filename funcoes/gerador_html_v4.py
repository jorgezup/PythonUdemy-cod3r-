def tag_bloco(conteudo, *args, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li> ' for item in itens)
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('ola'))
    print(tag_bloco('jorge', 'error'))
    print(tag_bloco('inline', inline=True))
    # parametros nomeados
    print(tag_bloco('falhou', classe='error', inline=True))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    print(tag_bloco(tag_lista('Sábado', 'Domingo'), classe='info', inline=True))
