import pygame
import json
import random
from os import path
import math
from constantes.constantes import Constantes


class Inimigo(pygame.surface.Surface):
    def __init__(self):
        self.__styles = path.join(
            path.dirname(__file__), "../styles/assets/inimigos/inimigos.json"
        )
        self.__style = self.set_style()

        self.__constantes = Constantes()

        self.__image = pygame.image.load(f"{self.__style['sprite']}tile000.png").convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (48, 48))
        self.__mask_image = pygame.mask.from_surface(self.__image)
        self.__rect = self.__mask_image.get_rect()

        self.__rect.x = self.__style['posicaoInicial']['x']
        self.__rect.y = self.__style['posicaoInicial']['y']

        self.__id_tile = 0
        self.__ctrl_tick = 0

        self.__velocidade_base_y = self.__constantes.cenario_veloc_base
        self.__direcao = 1

    def update(self):
        self.__ctrl_tick += 1
        if self.__ctrl_tick == 8:
            self.__ctrl_tick = 0
            self._animar()
        self._movimentar()

    def set_style(self):
        random.seed()
        with open(self.__styles, "r") as file:
            data = json.load(file)
            keys = list(data.keys())
            key_random = random.choice(keys)
            style = data[key_random]

        return style

    def _movimentar(self):
        if self.__style['gravidade']:
            # Antes do loop principal (for example)

            limite_esquerda = 0
            limite_direita = 402

            # Verificar a direção e mover o inimigo
            if self.__direcao == 1:  # Movimento para a direita
                self.rect.x += 2
                if self.rect.x >= limite_direita:
                    self.__direcao = -1  # Altera a direção para mover para a esquerda
            
            if self.__direcao == -1:  # Movimento para a esquerda
                self.rect.x -= 2
                if self.rect.x <= limite_esquerda:
                    self.__direcao = 1  # Altera a direção para mover para a direita

            self.rect.y += self.__velocidade_base_y
            self.__velocidade_base_y += self.__constantes.aceleracao_cenario
        else:
            self.rect.x += 0.5
             # A*sen(B*x) + C
            A = self.__style['movimento']['A']
            B = self.__style['movimento']['B']
            C = self.__style['movimento']['C']
            self.rect.y = A*math.sin((B*self.rect.x)) + C

    def _animar(self):
        self.__id_tile = 0 if self.__id_tile == 3 else self.__id_tile + 1
        self.__image = pygame.image.load(f"{self.__style['sprite']}/tile00{self.__id_tile}.png").convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (48, 48))
        if self.__direcao == -1:
            self.__image = pygame.transform.flip(self.__image, True, False)

    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
