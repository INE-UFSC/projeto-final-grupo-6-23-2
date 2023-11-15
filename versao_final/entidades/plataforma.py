import pygame


class Plataforma:

    def __init__(self, posicao: tuple):
        self.__superficie = pygame.Surface((300, 50))
        self.__superficie.fill('Gray')
        self.__posicao = posicao
        self.__rect = self.__superficie.get_rect(center=posicao)

    @property
    def superficie(self) -> pygame.Surface:
        return self.__superficie

    @property
    def posicao(self) -> tuple:
        return self.__posicao

    @property
    def rect(self):
        return self.__rect
