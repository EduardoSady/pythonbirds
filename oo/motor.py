class Motor:
    velocidade = 0
    def acelerar(self):
        self.velocidade += 1
        print(f'Você esta acelerou. Sua velocidade é: {self.velocidade}KM')
    def frear(self):
        if self.velocidade >= 2:
            self.velocidade -= 2
        else:
            self.velocidade = 0
            print('Você parou.')

    def freio_alternativo(self): #Utilizando a função max, determinando que caso seja menor que 0 atribui 0
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
        print(f'Você freiou. Sua velocidade é: {self.velocidade}KM')
        if self.velocidade == 0:
            print(f'Você parou.{self.velocidade}KM')

if __name__ == '__main__':
    carro = Motor()
    carro.acelerar()
    carro.acelerar()
    carro.acelerar()
    carro.acelerar()
    carro.freio_alternativo()
    carro.freio_alternativo()
    carro.freio_alternativo()

