import pygame
from entidades.entidades_cenario.itens.item import Item

class DuploPulo(Item):
    def __init__(self, x, y):
        super().__init__()

        self.__image = pygame.image.load("versao_final/styles/assets/itens/duplo_pulo/tile000.png")
        self.__image = pygame.transform.scale_by(self.__image, 1.5)
        self.__rect = self.__image.get_rect()
        self.__mascara = pygame.mask.from_surface(self.__image)

        self.__rect.x = x
        self.__rect.y = y

        self.__id_tile = 0
        self.__ctrl_tick = 0

    def efeito(self):
        pass

    def update(self):
        self.__ctrl_tick += 1
        if self.__ctrl_tick == 8:
            self.__ctrl_tick = 0
            self.animar()

    def animar(self):
        self.__id_tile = 0 if self.__id_tile == 7 else self.__id_tile + 1
        self.__image = pygame.image.load(f"versao_final/styles/assets/itens/duplo_pulo/tile00{self.__id_tile}.png").convert_alpha()
        self.__image = pygame.transform.scale_by(self.__image, 1.5)

    @property
    def rect(self):
        return self.__rect
    
    @property
    def imagem(self):
        return self.__image
    
    @property
    def mascara(self):
        return self.__mascara