class Data:
    # def to_str(self):
    def __str__(self): # método especial, imprime string
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2018
# print(d1.to_str())
print(d1)

d2 = Data()
d2.dia = 9
d2.mes = 8
d2.ano = 1991
# print(d2.to_str())
print(d2)
