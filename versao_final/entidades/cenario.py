from entidades.lava import Lava
from entidades.jogador import Jogador
from entidades.plataforma import Plataforma
from pygame import Surface


class Cenario:

    def __init__(self, tela: Surface, constantes):
        self.__constantes = constantes
        self.__lava = Lava()
        plataforma_inicial = Plataforma((self.__constantes.largura_tela / 2, 400))
        a = Plataforma((self.__constantes.largura_tela / 2, 500))
        self.__plataformas = [plataforma_inicial, a]
        self.__gravidade = 0.25

        tela.blit(self.__lava.superficie, self.__lava.posicao)
        tela.blit(plataforma_inicial.superficie, plataforma_inicial.posicao)

    # Desenha os componentes do jogo na tela
    def gerar_cenario(self, tela: Surface) -> None:
        tela.fill('Black')
        tela.blit(self.__lava.superficie, self.__lava.rect)

        for plataforma in self.__plataformas:
            tela.blit(plataforma.superficie, plataforma.posicao)

    @property
    def lava(self):
        return self.__lava
    
    @property
    def plataformas(self):
        return self.__plataformas
