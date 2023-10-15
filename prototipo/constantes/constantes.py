class Constantes:
    """Classe relativa às constantes do jogo"""

    def __init__(self):
        self.__largura_tela = 1000
        self.__altura_tela = 1000
        self.__fps = 60
        self.__gravidade = 0.25
    
    @property
    def largura_tela(self):
        return self.__largura_tela
    
    @property
    def altura_tela(self):
        return self.__altura_tela

    @property
    def fps(self):
        return self.__fps

    @property
    def gravidade(self):
        return self.__gravidade

constantes = Constantes()