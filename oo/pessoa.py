class Pessoa:

    olhos = 2 #Atributo de classe criado diretamente fora do __init__. Usado quando você tem uma "caracteristica padrão."
    def __init__(self, *filhos, nome=None, idade = 29): #Atributos de instancia e objetos são criados através dessa função.
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'

    @staticmethod ##Usado para criar metodos estaticos, que não usam obejtos como parâmetros
    def metodo_estatico():
        return 12

    @classmethod #Usado para criar o metodo da Classe, podendo atribuir atributos como parâmetros.
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa): #Criando a Classe herdando todos atributos da Classe passada como parâmetro
    pass

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
    dudu.olhos = 1 #É possível alterar o valor padrão.
    print(Pessoa.olhos, dudu.olhos)
    #print (f'{dudu.cumprimentar()}, me chamo {dudu.nome} e tenho {dudu.idade} anos!')
    print(Pessoa.metodo_estatico(), dudu.metodo_estatico()) #Possivel chamar metodos estaticos tanto pela classe quando pelo objeto.
    print(Pessoa.nome_e_atributos_de_classe(), dudu.nome_e_atributos_de_classe()) #Possivel chamar metodos estaticos tanto pela classe quando pelo objeto.