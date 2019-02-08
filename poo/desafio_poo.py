class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        pass

    def e_dulto(self):
        pass

class Vendedor():
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


class Cliente():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def registrar_compra(self, compra):
        self.compra = compra

    def get_data_ultima_compra(self):
        pass

    def total_compras(self):
        pass

class Compra():
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor


def main():
    pass

if __name__ == '__main__':
    main()