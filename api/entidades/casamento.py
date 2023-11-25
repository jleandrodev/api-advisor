class Casamento():
    def __init__(self, name, data_casamento, assistentes):
        self.__name = name
        self.__data_casamento = data_casamento
        self.__assistentes = assistentes

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def data_casamento(self):
        return self.__data_casamento
    
    @data_casamento.setter
    def data_casamento(self, data_casamento):
        self.__data_casamento = data_casamento

    @property
    def assistentes(self):
        return self.__assistentes
    
    @assistentes.setter
    def assistentes(self, assistentes):
        self.__assistentes = assistentes
