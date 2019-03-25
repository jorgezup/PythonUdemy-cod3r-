class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self


if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn').das_cavernas() # por causa do return self


    print(f'Humano.especies: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especies: {grokn.especie}')
