import pygame
from constantes.constantes import Constantes


class Lava(pygame.sprite.Sprite):
    """Classe responsável pela lava"""

    def __init__(self):
        super().__init__()
        self.__constantes = Constantes()
        self.__image = pygame.image.load("versao_final/styles/assets/sprite_lava.png").convert_alpha()
        self.__mask_image = pygame.mask.from_surface(self.__image)
        self.__rect = self.__mask_image.get_rect()

        self.__rect.x = 0
        self.__rect.y = min(self.__constantes.altura_tela, pygame.display.Info().current_h - 50) * 0.9

        self.__rect_collide = pygame.Rect(self.__rect.x, self.__rect.y + 30, self.__rect.width, self.__rect.height - 30) #30 para que a colisão seja registrada apenas quando o jogador estiver imerso 30px na lava

    def animacao(self):
        posicao = self.__rect.x 
        if posicao >= -449:
            self.__rect.x -= 1
        else:
            self.__rect.x = -65.5

        


    @property
    def superficie(self) -> pygame.sprite.Sprite:
        return self.__image
    
    @property
    def posicao(self) -> tuple:
        return (self.__rect.x, self.__rect.y)
    
    @property
    def rect(self):
        return self.__rect_collide