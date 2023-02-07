class Pessoa:
    def __init__(self, nome=None, idade = None): #Atributos de instancia e objetos são criados através dessa função.
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa('Dudu', 29)
    print (p.cumprimentar())
    print (f'{p.cumprimentar()}, me chamo {p.nome} e tenho {p.idade} anos!')
