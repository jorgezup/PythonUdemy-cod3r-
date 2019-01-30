def tag_bloco(texto, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'

if __name__ == '__main__':
    print(tag_bloco('ola'))
    print(tag_bloco('jorge','error'))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error', inline=True))
