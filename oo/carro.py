from oo.direcao import Direcao
from oo.motor import Motor
class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao
    def calcular_velocidade(self):
        return self.motor.velocidade
    def acelerar(self):
        return self.motor.frear()
    def virar_direita(self):
        return self.direcao.virar_a_direita()
    def virar_esquerda(self):
        return self.direcao.virar_a_esquerda()




