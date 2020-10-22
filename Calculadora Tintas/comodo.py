class Comodo:
    __largura: float
    __profundidade: float
    __altura: float

    def __init__(self, largura, profundidade):
        self.largura = largura
        self.profundidade = profundidade
        self.__altura = 2.9
# propriedades do objeto comodo
    @property
    def largura(self):
        return self.__altura

    @property
    def profundidade(self):
        return self.__profundidade

    @property
    def altura(self):
        return self.__altura
# Metodo setter para passar valores e validar
    @largura.setter
    def largura(self,largura):
        try:
            self.__largura = float(largura)
        except Exception:
            print("O valor de largura inserido é inválido ")
            exit()

    @profundidade.setter
    def profundidade(self,profundidade):
        try:
            self.__profundidade = float(profundidade)
        except Exception:
            print("O valor profunidade inserido é inválido ")
            exit()

    @altura.setter
    def altura(self,altura):
        try:
            self.__altura = altura
        except Exception:
            print("O valor de altura inserido é inválido ")
            exit()
