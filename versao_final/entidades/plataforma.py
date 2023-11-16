import pygame


class Plataforma:
    def __init__(self, posicao: tuple):
        self.__superficie = pygame.Surface((100, 25))
        self.__largura = self.__superficie.get_width()
        self.__superficie.fill("Gray")
        self.__posicao = posicao
        self.__rect = self.__superficie.get_rect(topleft=posicao)

    @property
    def superficie(self) -> pygame.Surface:
        return self.__superficie

    @property
    def posicao(self) -> tuple:
        return self.__posicao

    @property
    def rect(self):
        return self.__rect

    @property
    def largura(self):
        return self.__largura
