class Constantes:
    """Classe relativa às constantes do jogo"""

    def __new__(cls):
        if not hasattr(cls, 'isinstance'):
            cls.instance = super(Constantes, cls).__new__(cls)
            cls.instance.__init_constantes()
        return cls.instance

    def __init_constantes(self):
        self.__largura_tela = 450
        self.__altura_tela = 800
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
