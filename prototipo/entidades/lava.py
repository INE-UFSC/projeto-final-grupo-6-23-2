import pygame
from constantes import constantes


class Lava:

    def __init__(self):
        self.__superficie = pygame.Surface((constantes.LARGURA_TELA, constantes.ALTURA_TELA * 0.2))
        self.__superficie.fill('Orange')
        self.__velocidade = 1
        self.__posicao = (0, 800)

    def sobe_lava(self) -> None:
        novo_y = self.__posicao[1] + self.__velocidade
        self.__posicao = (0, novo_y)

    @property
    def velocidade(self) -> int:
        return self.__velocidade

    @property
    def posicao(self) -> tuple:
        return self.__posicao

    @property
    def superficie(self) -> pygame.Surface:
        return self.__superficie