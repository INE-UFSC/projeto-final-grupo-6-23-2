import pygame
import random
from configuracoes.configuracoes import Configuracoes


class Plataforma:
    def __init__(self, posicao: tuple, centralizar: bool = False):
        numero = random.randint(1, 8)
        self.__imagem = pygame.image.load(
            f"versao_final/styles/assets/plataformas/style{numero}.png"
        ).convert_alpha()
        self.__mascara = pygame.mask.from_surface(self.__imagem)
        self.__largura = self.__imagem.get_width()
        self.__posicao = posicao
        self.__rect = self.__imagem.get_rect(topleft=posicao)

        config = Configuracoes()
        if centralizar:
            self.__rect.x = (config.largura_tela/2) - (self.__largura/2)

    @property
    def imagem(self) -> pygame.Surface:
        return self.__imagem

    @property
    def posicao(self) -> tuple:
        return self.__posicao

    @property
    def rect(self):
        return self.__rect

    @property
    def largura(self):
        return self.__largura

    @property
    def mascara(self):
        return self.__mascara
