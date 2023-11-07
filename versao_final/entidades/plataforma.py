import pygame
from entidades.tiles_package import *
import json
import random
from os import path


class Plataforma:
    """A classe plataforma ambém possui um tilegrid interno, onde são definidas as posições
    de cada tile desta plataforma. Além disso, também possui um estilo; estes estão definidos
    em styles/styles-plataformas.json"""

    def __init__(self, style_source: str = "default", random=False):
        self.__largura = 0
        self.__tilegrid = None
        self.__json_path = path.join(
            path.dirname(__file__), "../styles/styles-plataformas.json"
        )

        self.__image_path = path.join(
            path.dirname(__file__), "../styles/assets/plataforma-tileset.png"
        )

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
        """Esse método carrega um style de acordo com o nome dele no json, montando a grade de tiles
        definidas em structure no json. Assim, além do sprite de cada tile da plataforma, também é definido
        a posição dele na própria plataforma"""

        with open(self.__json_path, "r") as file:
            style = json.load(file)[style_source]

        self.__largura = style["width"]
        tileset_data = style["tileset"]
        tileset = Tileset(
            self.__image_path,
            int(tileset_data["tile_width"]),
            int(tileset_data["tile_height"]),
        )
        self.__tilegrid = TileGrid(
            int(tileset_data["tile_width"]),
            int(tileset_data["tile_height"]),
            tiles_vertical=int(style["height"]),
            tiles_horizontal=int(style["width"]),
        )
    
        linha_tilegrid = 0
        for linha in style["structure"]:
            coluna_tilegrid = 0
            for tile in linha:
                self.tilegrid.add_tile(
                    tileset.get_tile(
                        int(tile["linha_tileset"]), int(tile["coluna_tileset"])
                    ),
                    linha_tilegrid,
                    coluna_tilegrid,
                )
                coluna_tilegrid += 1
            linha_tilegrid += 1

    def random_style(self) -> str:
        """Pega todos os estilos definidos no json e sorteia um aleatóriamente retornando o seu nome."""
        with open(self.__json_path, "r") as file:
            style = list(json.load(file).keys())
            return random.choice(style)


class Plataformas(pygame.sprite.Group):
    """Essa classe também é um grupo de tiles e apenas foi definida para melhor compreensão do código
    visto que é um grupo (do pygame Group) de objetos tilegrid (de cada uma das plataformas), assim,
    na verificação da colisão com o jogador é possível apenas verificar se este colide com o grupo Plataformas."""

    def __init__(self) -> None:
        super().__init__()
