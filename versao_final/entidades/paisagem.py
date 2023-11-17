import math
import pygame
from pygame.sprite import Sprite, Group
import os

class Paisagem(Group):
    def __init__(self):
        super().__init__()
        self.images = {}
        self.add_layer(Layer("bg.png"), 6)

    def add_layer(self, layer, speed):
        super().add(layer)
        self.images[speed] = layer
        
    def move(self, velocidade_descida):
        for speed, sprite in self.images.items():
            if sprite.rect.y >= 0:
                sprite.rect.y = -1600
            else:
                sprite.rect.y += (velocidade_descida*(speed/10))

class Layer(Sprite):
    def __init__(self, file: str, alpha=False):
        super().__init__()
        if alpha:
            self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "../styles/assets/"+file)).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "../styles/assets/"+file)).convert()
        self.rect = self.image.get_rect()
        self.rect.y = -2400