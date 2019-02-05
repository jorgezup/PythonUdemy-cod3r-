class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0
        self.velocidade_minima = 0

    def acelerar(self, delta=5):
        self.velocidade_atual += delta
        if self.velocidade_atual <= self.velocidade_maxima:
            return self.velocidade_atual
        else:
            return self.velocidade_maxima

    def frear(self, delta=5):
        self.velocidade_atual -= delta
        if self.velocidade_atual <= self




if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(10))



