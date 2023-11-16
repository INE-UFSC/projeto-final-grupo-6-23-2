import pygame
from constantes.constantes import Constantes


class Lava:
    def __init__(self):
        self.__constantes = Constantes()

        self.__superficie = pygame.Surface(
            (self.__constantes.largura_tela, self.__constantes.altura_tela * 0.2)
        )
        self.__superficie.fill("Orange")
        self.__posicao = (0, self.__constantes.altura_tela * 0.8)

        self.__rect = self.__superficie.get_rect(topleft=self.__posicao)

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

    @property
    def rect(self):
        return self.__rect
