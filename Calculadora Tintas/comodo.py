class Comodo:
    __largura: float
    __profundidade: float
    __altura: float

    def __init__(self, largura, profundidade):
        self.largura = largura
        self.profundidade = profundidade
        self.__altura = 2.9

    @property
    def largura(self):
        return self.__altura

    @property
    def profundidade(self):
        return self.__profundidade

    @property
    def altura(self):
        return self.__altura

    @largura.setter
    def largura(self,largura):
        self.__largura = largura

    @profundidade.setter
    def profundidade(self,profundidade):
        self.__profundidade = profundidade

    @altura.setter
    def altura(self,altura):
        self.__altura = altura