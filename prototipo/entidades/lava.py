import pygame
from constantes import constantes


class Lava:

    def __init__(self):
        self.__superficie = pygame.Surface((constantes.LARGURA_TELA, constantes.ALTURA_TELA * 0.2))
        self.__superficie.fill('Orange')
        self.__posicao = (0, 800)

    @property
    def superficie(self) -> pygame.Surface:
        return self.__superficie
    
    @property
    def posicao(self):
        return self.__posicao
