import pygame
from entidades.entidades_cenario.itens.item import Item
from configuracoes.configuracoes import Configuracoes

class Moeda(Item):
    def __init__(self, x, y):
        super().__init__()

        self.__configuracoes = Configuracoes()

        self.__image = pygame.image.load("versao_final/styles/assets/itens/moedas/tile000.png").convert_alpha()
        self.__image = pygame.transform.scale_by(self.__image, 1.5)
        self.__rect = self.__image.get_rect()
        self.__mascara = pygame.mask.from_surface(self.__image)
        self.__id_tile = 0
        self.__ctrl_tick = 0

        self.__sound = pygame.mixer.Sound('versao_final/styles/assets/sound_effects/moeda.wav')
        self.__sound.set_volume(0.2)

        self.__rect.x = x
        self.__rect.y = y

    def efeito(self):
        self.__configuracoes.pontuacao.pontuacao_bonus(5)
        self.__sound.play()

    def update(self):
        self.__ctrl_tick += 1
        if self.__ctrl_tick == 8:
            self.__ctrl_tick = 0
            self.animar()

    def animar(self):
        self.__id_tile = 0 if self.__id_tile == 7 else self.__id_tile + 1
        self.__image = pygame.image.load(f"versao_final/styles/assets/itens/moedas/tile00{self.__id_tile}.png").convert_alpha()
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