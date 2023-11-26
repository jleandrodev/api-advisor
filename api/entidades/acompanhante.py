class Acompanhante():
    def __init__(self, nome, idade, convidado):
        self.__nome = nome
        self.__idade = idade
        self.__convidado = convidado

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def convidado(self):
        return self.__convidado
    
    @convidado.setter
    def convidado(self, convidado):
        self.__convidado = convidado