from entidades.lava import Lava
from entidades.jogador import Jogador
from entidades.plataforma import Plataforma
from constantes import constantes
from pygame import Surface


class Cenario:

    def __init__(self, tela: Surface):
        self.__jogador = Jogador()
        self.__lava = Lava()
        plataforma_inicial = Plataforma((constantes.LARGURA_TELA / 2, 400))
        self.__plataformas = [plataforma_inicial]
        self.__gravidade = 0.25

        tela.blit(self.__lava.superficie, self.__lava.posicao)
        tela.blit(self.__jogador.superficie, self.__jogador.posicao)
        tela.blit(plataforma_inicial.superficie, plataforma_inicial.posicao)

    # Desenha os componentes do jogo na tela
    def gerar_cenario(self, tela: Surface) -> None:
        tela.fill('Brown')
        self.__jogador.aplica_gravidade(self.__gravidade)

        tela.blit(self.__lava.superficie, self.__lava.posicao)
        tela.blit(self.__jogador.superficie, self.__jogador.posicao)

        for plataforma in self.__plataformas:
            tela.blit(plataforma.superficie, plataforma.posicao)
