from datetime import datetime

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Possível IndexError
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s)'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.cricao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluída)' if self.feito else '')


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passa Roupa')
    casa.add('Lavar Prato')
    print(casa)

    casa.procurar('Lavar Prato').concluir()
    for tarefa in casa.tarefas:
        print(f'- {tarefa}')

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Frango')
    print('\n',mercado)

    compra_carne = mercado.procurar('Carne')
    compra_carne.concluir()
    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()
