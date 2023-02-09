class Direcao:
    direcao = 'norte'
    def virar_a_direita(self):
        if self.direcao == 'norte':
            self.direcao = 'leste'
        elif self.direcao == 'leste':
            self.direcao = 'sul'
        elif self.direcao == 'sul':
            self.direcao = 'oste'
        elif self.direcao == 'oeste':
            self.direcao = 'norte'

    def virar_a_esquerda(self):
        if self.direcao == 'norte':
            self.direcao = 'oeste'
        elif self.direcao == 'oeste':
            self.direcao = 'sul'
        elif self.direcao == 'sul':
            self.direcao = 'leste'
        elif self.direcao == 'leste':
            self.direcao = 'norte'

if __name__ == '__main__':
    carro = Direcao()
    carro.virar_a_direita()
    carro.virar_a_direita()
    carro.virar_a_esquerda()
    carro.virar_a_esquerda()
    carro.virar_a_esquerda()

    print(carro.direcao)