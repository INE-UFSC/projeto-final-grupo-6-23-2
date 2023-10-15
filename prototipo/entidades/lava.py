import pygame
from constantes.constantes import constantes


class Lava:
    """Classe responsável pela lava"""

    def __init__(self):
        self.__superficie = pygame.Surface((constantes.largura_tela, constantes.altura_tela * 0.2))
        self.__superficie.fill('Orange')
        self.__posicao = (0, 800)

    @property
    def superficie(self) -> pygame.Surface:
        return self.__superficie
    
    @property
    def posicao(self):
        return self.__posicao
