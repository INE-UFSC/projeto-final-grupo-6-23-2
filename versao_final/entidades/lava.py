# import pygame
# from constantes.constantes import Constantes


# class Lava:
#     def __init__(self):
#         self.__constantes = Constantes()

#         self.__superficie = pygame.Surface(
#             (self.__constantes.largura_tela, self.__constantes.altura_tela * 0.2)
#         )
#         self.__superficie.fill("Orange")
#         self.__posicao = (0, self.__constantes.altura_tela * 0.8)

#         self.__rect = self.__superficie.get_rect(topleft=self.__posicao)

#     def sobe_lava(self) -> None:
#         novo_y = self.__posicao[1] + self.__velocidade
#         self.__posicao = (0, novo_y)

#     @property
#     def velocidade(self) -> int:
#         return self.__velocidade

#     @property
#     def posicao(self) -> tuple:
#         return self.__posicao

#     @property
#     def superficie(self) -> pygame.Surface:
#         return self.__superficie

#     @property
#     def rect(self):
#         return self.__rect
import pygame
from constantes.constantes import Constantes


class Lava(pygame.sprite.Sprite):
    """Classe responsável pela lava"""

    def __init__(self):
        super().__init__()
        self.__constantes = Constantes()
        self.__image = pygame.image.load("versao_final/styles/assets/sprite_lava_5.png").convert_alpha()
        self.__mask_image = pygame.mask.from_surface(self.__image)
        self.__rect = self.__mask_image.get_rect()

        self.rect.x = 0
        self.rect.y = self.__constantes.altura_tela * 0.9

    def animacao(self):
        posicao = self.rect.x 
        if posicao >= -449:
            self.rect.x -= 1
        else:
            self.rect.x = -65.5

        


    @property
    def superficie(self) -> pygame.sprite.Sprite:
        return self.__image
    
    @property
    def posicao(self) -> tuple:
        return (self.__rect.x, self.__rect.y)
    
    @property
    def rect(self):
        return self.__rect