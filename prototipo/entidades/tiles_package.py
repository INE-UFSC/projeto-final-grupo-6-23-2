import math
from typing import Iterable, Union
import pygame
from pygame.sprite import AbstractGroup
import json


class Tileset:
    def __init__(self, imagem: str, largura_tile: int, altura_tile: int):
        self.tileset = pygame.image.load(imagem).convert()
        self.largura_tile = largura_tile
        self.altura_tile = altura_tile

    def get_tile(self, linha: int, coluna: int):
        # Calcula a posição do retângulo do tile na imagem
        x = coluna * self.largura_tile
        y = linha * self.altura_tile

        # Corta o tile da imagem e retorna uma sub-superfície
        tile_subsurface = self.tileset.subsurface(pygame.Rect(x, y, self.largura_tile, self.altura_tile))

        # Crie um objeto Tile diretamente com a sub-superfície e retorne-o
        tile = Tile(tile_subsurface, self.largura_tile, self.altura_tile)

        return tile

class Tile(pygame.sprite.Sprite):
    def __init__(self, imagem, largura_tile: int, altura_tile: int, solido=True):
        super().__init__()

        # Use a sub-superfície diretamente como imagem
        self.image = imagem

        # Redimensione a imagem, se necessário
        self.image = pygame.transform.scale(self.image, (largura_tile, altura_tile))
        self.rect = self.image.get_rect()

        # Define se o tile é sólido ou não
        self.solido = solido

class TileGrid(pygame.sprite.Group):
    def __init__(self, largura_tile: int, altura_tile: int, tiles_horizontal:int = 1, tiles_vertical:int = 1, largura_tela: int = None, altura_tela: int = None):
        super().__init__()
        self.__tiles_horizontal = tiles_horizontal
        self.__tiles_vertical = tiles_vertical
        if largura_tela is not None and altura_tela is not None:
            self.__largura_tile = round(largura_tile*(largura_tela/(largura_tile*tiles_horizontal)))
            self.__altura_tile = round(altura_tile*(altura_tela/(altura_tile*tiles_vertical)))
        else:
            self.__largura_tile = largura_tile
            self.__altura_tile = altura_tile
        self.__tiles = {}
        self.__desloc = 0
    
    @property
    def tiles(self):
        return self.__tiles
    
    @property
    def tiles_horizontal(self):
        return self.__tiles_horizontal
    
    @property
    def tiles_vertical(self):
        return self.__tiles_vertical
    
    @property
    def largura_tile(self):
        return self.__largura_tile
    
    @property
    def altura_tile(self):
        return self.__altura_tile

    def add_tilegrid(self, tilegrid, linha, coluna):
        if isinstance(tilegrid, TileGrid):
            for pos, tile in tilegrid.tiles.items():
                i = pos[0]
                j = pos[1]
                if coluna+j in range(0, self.tiles_horizontal):
                    self.add_tile(tile, linha+i, coluna+j)
        else:
            raise TypeError("add_tilegrid deve receber um objeto do tipo TileGrid")
        
    def add_tile(self, tile, linha, coluna):
        if isinstance(tile, Tile):
            tile.image = pygame.transform.scale(tile.image, (self.largura_tile, self.altura_tile))
            tile.rect.y = linha*self.largura_tile
            tile.rect.x = coluna*self.altura_tile
            if tile.image.get_size() == (self.largura_tile, self.altura_tile):
                try:
                    if coluna in range(0, self.tiles_horizontal):
                        self.tiles[(linha, coluna)] = tile
                        super().add(tile)
                    else:
                        raise KeyError()
                except KeyError:
                    raise KeyError(f"({linha}, {coluna}) inválidos para esta grade")
            else:
                raise ValueError("O tile deve ter as mesma dimensões do que as definidas pelo TileGrid")
        else:
            raise TypeError("add_tile deve receber um objeto do tipo Tile")
        
    def remove_tile(self, linha, coluna):
        try:
            super().remove(self.tiles[(linha, coluna)])
            if (linha, coluna) in self.tiles:
                self.tiles.pop((linha, coluna))
        except KeyError:
            if coluna > self.tiles_horizontal:
                raise KeyError(f"({linha}, {coluna}) inválidos para esta grade")
        
    def get_tile(self, linha, coluna):
        try:
            return self.tiles[(linha, coluna)]
        except KeyError:
            if coluna > self.tiles_horizontal:
                raise KeyError(f"({linha}, {coluna}) inválidos para esta grade")
            else:
                return None
            
    def move_down(self, velocity: float):
        gerar = False
        self.__desloc += velocity
        if self.__desloc >= self.altura_tile*self.tiles_vertical:
            self.__desloc = 0
            gerar = True
        tiles_copy = self.tiles.copy()
        for position, tile in tiles_copy.items():
            linha = position[0]
            coluna = position[1]
            tile = self.get_tile(linha, coluna)
            

            if self.__desloc % self.altura_tile == 0:
                self.remove_tile(linha, coluna)
                self.add_tile(tile, linha+1, coluna)
            else:
                tile.rect.y += velocity

            if tile.rect.y > self.altura_tile*self.tiles_vertical:
                self.remove_tile(linha, coluna)
        del tiles_copy
        return gerar
            
        
        


        
    
