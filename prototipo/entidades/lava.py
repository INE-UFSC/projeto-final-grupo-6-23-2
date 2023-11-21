import pygame
from constantes.constantes import Constantes


class Lava:
    """Classe responsável pela lava"""

    def __init__(self):
        self.__constantes = Constantes()
        self.__superficie = pygame.Surface(
            (self.__constantes.largura_tela, self.__constantes.altura_tela * 0.2))
        self.__superficie.fill('Orange')
        self.__posicao = (0, self.__constantes.altura_tela * 0.8)
        self.__rect = pygame.Rect(
            *self.__posicao, self.__constantes.largura_tela, self.__constantes.altura_tela * 0.2)

    @property
    def superficie(self) -> pygame.Surface:
        return self.__superficie

    @property
    def posicao(self) -> tuple:
        return self.__posicao

    @property
    def rect(self):
        return self.__rect
