import pygame
from abc import ABC
from entidades.tiles_package import *
import json
import random


class Plataforma:
    def __init__(self, style_source: str = 'default', random=False):
        self.__largura = 0
        self.__tilegrid = None
        if random:
            self.load_style(self.random_style())
        else:
            self.load_style(style_source)

    @property
    def tilegrid(self):
        return self.__tilegrid
    
    @property
    def largura(self):
        return self.__largura

    def load_style(self, style_source: str) -> None:
        with open(f'prototipo/styles/styles-plataformas.json', 'r') as file:
            style = json.load(file)[style_source]
        
        self.__largura = style["width"]
        tileset_data = style["tileset"]
        tileset = Tileset(tileset_data["tileset_image"], int(tileset_data["tile_width"]), int(tileset_data["tile_height"]))
        self.__tilegrid = TileGrid(int(tileset_data["tile_width"]), int(tileset_data["tile_height"]), tiles_vertical=int(style["height"]), tiles_horizontal=int(style["width"]))

        i = 0
        for linha in style["structure"]:
            j = 0
            for tile in linha:
                self.tilegrid.add_tile(tileset.get_tile(int(tile["linha_tileset"]), int(tile["coluna_tileset"])), i, j)
                j += 1
            i += 1

    def random_style(self) -> str:
        with open(f'prototipo/styles/styles-plataformas.json', 'r') as file:
            style = list(json.load(file).keys())
            return random.choice(style)
    
