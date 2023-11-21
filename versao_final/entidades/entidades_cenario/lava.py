import pygame
from configuracoes.configuracoes import Configuracoes


class Lava(pygame.sprite.Sprite):
    """Classe responsável pela lava"""

    def __init__(self):
        super().__init__()
        self.__configuracoes = Configuracoes()
        self.__image = pygame.image.load(
            "versao_final/styles/assets/sprite_lava_resized.png").convert_alpha()
        self.__mascara = pygame.mask.from_surface(self.__image)
        self.__rect = self.__image.get_rect()

        self.rect.x = 0
        self.__rect.y = min(self.__configuracoes.altura_tela,
                            pygame.display.Info().current_h - 50) * 0.9

    def animacao(self):
        posicao = self.rect.x
        if posicao >= -449:
            self.rect.x -= 1
        else:
            self.rect.x = -65.5

    @property
    def mascara(self):
        return self.__mascara

    @property
    def superficie(self) -> pygame.sprite.Sprite:
        return self.__image

    @property
    def posicao(self) -> tuple:
        return (self.__rect.x, self.__rect.y)

    @property
    def rect(self):
        return self.__rect
