class Configuracoes:
    """Classe relativa às Configuracoes do jogo"""

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Configuracoes, cls).__new__(cls)
            cls.instance.__init_configuracoes()
        return cls.instance

    def __init_configuracoes(self):
        self.__largura_tela = 450
        self.__altura_tela = 800
        self.__fps = 60

        self.__jogador_veloc_base = 5
        self.__jogador_pulo_base = 10
        self.__jogador_num_imagens_parado = 4
        self.__jogador_num_imagens_pulo = 2
        self.__jogador_pos_inicial = (self.__largura_tela / 2, 50)
        self.__gravidade_jogo = 0.4

        self.__cenario_veloc_base = 1
        self.__aceleracao_cenario = 0.0005

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

    @property
    def aceleracao_cenario(self):
        return self.__aceleracao_cenario

    @property
    def jogador_num_imagens_parado(self):
        return self.__jogador_num_imagens_parado

    @property
    def jogador_num_imagens_pulo(self):
        return self.__jogador_num_imagens_pulo
