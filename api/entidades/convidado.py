class Convidado():
    def __init__(self, nome, telefone, casamento):
        self.__nome = nome
        self.__telefone = telefone
        self.__casamento = casamento

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def casamento(self):
        return self.__casamento
    
    @casamento.setter
    def casamento(self, casamento):
        self.__casamento = casamento