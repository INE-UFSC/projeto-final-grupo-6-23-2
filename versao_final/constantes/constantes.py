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
        self.__gravidade = 0.4
        self.__jogador_veloc_base = 5
        self.__jogador_pulo_base = 10
        self.__cenario_veloc_base = 1
        self.__gravidade_jogo = 0.4
        self.__jogador_pos_inicial = (self.__largura_tela / 2, 50)

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

    @property
    def jogador_veloc_base(self):
        return self.__jogador_veloc_base

    @property
    def jogador_pulo_base(self):
        return self.__jogador_pulo_base

    @property
    def gravidade_jogo(self):
        return self.__gravidade_jogo

    @property
    def jogador_pos_inicial(self):
        return self.__jogador_pos_inicial
    
    @property
    def cenario_veloc_base(self):
        return self.__cenario_veloc_base
