from entidades.lava import Lava
from entidades.jogador import Jogador
from entidades.plataforma import Plataforma
from pygame import Surface


class Cenario:

    def __init__(self, tela: Surface, constantes):
        self.__constantes = constantes
        self.__lava = Lava()
        self.__plataforma_refenc = Plataforma(
            (self.__constantes.largura_tela / 2, 400))
        self.__gravidade = 0.25
        self.__plataformas = [self.__plataforma_refenc]

    def gerar_plataforma(self):
        plataforma_y = self.__plataforma_refenc.rect.bottom

    @property
    def lava(self):
        return self.__lava

    @property
    def plataformas(self):
        return self.__plataformas
