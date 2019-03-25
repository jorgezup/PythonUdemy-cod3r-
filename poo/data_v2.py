class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self): # método especial, imprime string
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(9, 9, 2018)
print(d1)

d2 = Data(ano=2017)
d2.dia = 9
print(d2)
