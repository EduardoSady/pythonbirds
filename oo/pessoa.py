class Pessoa:
    def __init__(self, *filhos, nome=None, idade = 29): #Atributos de instancia e objetos são criados através dessa função.
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':
    mila = Pessoa(nome='Mila')
    dudu = Pessoa(mila, nome='Dudu')
    print (dudu.cumprimentar())

    for filho in dudu.filhos:
        print(filho.nome)

    dudu.sobrenome = 'Sady' # Criando atributo dinâmico, fora do escopo do __init__
    print(f'{dudu.sobrenome}')
    print(dudu.__dict__) ##Usado para analisar todos os atributos do objeto
    del dudu.sobrenome #Para remover qualquer atributo, não somente os dinâmicos

    #print (f'{dudu.cumprimentar()}, me chamo {dudu.nome} e tenho {dudu.idade} anos!')
