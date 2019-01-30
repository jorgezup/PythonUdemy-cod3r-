def tag_bloco(texto, classe='sucess'):
    return f'<div class="{classe}">{texto}</div>'

if __name__ == '__main__':
    print(tag_bloco('ola'))
    print(tag_bloco('jorge','error'))
