import pygame
import json
import random
from os import path


class Inimigo(pygame.surface.Surface):
    def __init__(self):
        self.__styles = path.join(
            path.dirname(__file__), "../styles/assets/inimigos/inimigos.json"
        )
        self.__style = self.set_style()

        self.__image = pygame.image.load(f"{self.__style['sprite']}tile000.png").convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (48, 48))
        self.__mask_image = pygame.mask.from_surface(self.__image)
        self.__rect = self.__mask_image.get_rect()

        self.__rect.x = 100
        self.__rect.y = 100

        self.__id_tile = 0
        self.__ctrl_tick = 0

    def update(self):
        self.__ctrl_tick += 1
        if self.__ctrl_tick == 8:
            self.__ctrl_tick = 0
            self._animar()

    def set_style(self):
        with open(self.__styles, "r") as file:
            data = json.load(file)
            keys = list(data.keys())
            key_random = random.choice(keys)
            style = data[key_random]

        return style

    def _animar(self):
        self.__id_tile = 0 if self.__id_tile == 3 else self.__id_tile + 1
        self.__image = pygame.image.load(f"{self.__style['sprite']}/tile00{self.__id_tile}.png").convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (48, 48))

    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect