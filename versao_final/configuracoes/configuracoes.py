import pygame
from entidades.pontuacao import Pontuacao

class Configuracoes:
    """Classe relativa às configurações gerais do jogo. Ela
    utiliza o padrão singleton para garantir que haja, no máximo,
    uma instância sua."""

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Configuracoes, cls).__new__(cls)
            cls.instance.__init_configuracoes()
        return cls.instance

    def __init_configuracoes(self):
        self.__largura_tela = 450
        self.__altura_tela = 800
        self.__fps = 60

        self.__tamanho_jogador = (24 * 3, 21 * 3)
        self.__jogador_veloc_base = 5
        self.__jogador_pulo_base = 10
        self.__jogador_num_imagens_parado = 4
        self.__jogador_num_imagens_andando = 7
        self.__jogador_num_imagens_pulo = 1
        self.__jogador_num_imagens_machucado = 3
        self.__num_ciclos_machucado = 18
        self.__jogador_pos_inicial = (self.__largura_tela / 2, 50)
        self.__gravidade_jogo = 0.4

        self.__plataforma_inicial_pos = (self.__largura_tela / 2 - 50, 120)
        self.__cenario_veloc_base = 1
        self.__cenario_veloc_max = 2.5
        self.__aceleracao_cenario = 0.0005

        self.GAMEOVER = pygame.USEREVENT + 1

        # Instancia pontuacao
        self.__pontuacao = Pontuacao()

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
    def cenario_veloc_max(self):
        return self.__cenario_veloc_max

    @property
    def aceleracao_cenario(self):
        return self.__aceleracao_cenario

    @property
    def tamanho_jogador(self):
        return self.__tamanho_jogador

    @property
    def jogador_num_imagens_parado(self):
        return self.__jogador_num_imagens_parado

    @property
    def jogador_num_imagens_andando(self):
        return self.__jogador_num_imagens_andando
    
    @property
    def jogador_num_imagens_machucado(self):
        return self.__jogador_num_imagens_machucado

    @property
    def num_ciclos_machucado(self):
        return self.__num_ciclos_machucado

    @property
    def jogador_num_imagens_pulo(self):
        return self.__jogador_num_imagens_pulo

    @property
    def plataforma_inicial_pos(self):
        return self.__plataforma_inicial_pos
    
    @property
    def pontuacao(self):
        return self.__pontuacao
