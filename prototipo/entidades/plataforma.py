import pygame
from abc import ABC
from tiles_package import *
import json


class Plataforma:
    def __init__(self, style_source: str):
        self.__tilegrid = None
        self.load_style(style_source)

    @property
    def tilegrid(self):
        return self.__tilegrid
    
    def load_style(self, style_source: str):
        with open(f'prototipo/styles/styles-plataformas.json', 'r') as file:
            style = json.load(file)[style_source]
        
        tileset_data = style["tileset"]
        tileset = Tileset(tileset_data["tileset_image"], int(tileset_data["tile_width"]), int(tileset_data["tile_height"]))
        self.__tilegrid = TileGrid(int(tileset_data["tile_width"]), int(tileset_data["tile_height"]), tiles_vertical=int(style["width"]), tiles_horizontal=int(style["height"]))

        i = 0
        for linha in style["structure"]:
            j = 0
            for tile in linha:
                self.tilegrid.add_tile(tileset.get_tile(int(tile["linha_tileset"]), int(tile["coluna_tileset"])), i, j)
                j += 1
            i += 1
    
