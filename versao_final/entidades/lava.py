import pygame
from constantes.constantes import Constantes


class Lava(pygame.sprite.Sprite):
    """Classe responsável pela lava"""

    def __init__(self):
        super().__init__()
        self.__constantes = Constantes()
        self.__image = pygame.image.load("versao_final/styles/assets/sprite_lava_2.png")
        self.__image = pygame.transform.scale(self.__image, (500, 150))
        self.__mask_image = pygame.mask.from_surface(self.__image)
        self.__rect = self.__mask_image.get_rect()

        self.rect.x = 0
        self.rect.y = self.__constantes.altura_tela * 0.85

    def uptade(self):
        pass

    @property
    def superficie(self) -> pygame.sprite.Sprite:
        return self.__image
    
    @property
    def posicao(self) -> tuple:
        return (self.__rect.x, self.__rect.y)
    
    @property
    def rect(self):
        return self.__rect