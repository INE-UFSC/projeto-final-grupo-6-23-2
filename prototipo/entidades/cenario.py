from plataforma import Plataforma
from tiles_package import TileGrid
import random


class Cenario:

    def __init__(self, tiles_horizontal: int, tiles_vertical: int, largura_tela: int, altura_tela: int):
        self.__grid = TileGrid(16, 16, tiles_horizontal=tiles_horizontal, tiles_vertical=tiles_vertical, largura_tela=largura_tela, altura_tela= altura_tela)
        self.__plataformas = dict()

    @property
    def grid(self):
        return self.__grid

    def gerar_cenario(self, a_max, l_max) -> None:
        plataforma_gerada = self.gerar_plataforma((0, 3), 3, a_max, l_max)
        while True:
            plataforma_gerada = self.gerar_plataforma(*plataforma_gerada)
            if plataforma_gerada[0][0] in range(0, a_max):
                break

    def gerar_plataforma(self, initial_position: tuple, initial_width: int, a_max: int, l_max: int):
        random.seed(None)
        if initial_position[0] <= 0:
            initial_position = (self.grid.tiles_vertical+ initial_position[0], initial_position[1])

        plataforma = Plataforma(random=True)

        Imin = max(0, initial_position[0] - a_max)
        Imax = max(0, initial_position[0]-2)
        linha = random.randint(Imin, Imax)
        

        col = 0
        Ia = initial_position[1]+initial_width
        Ib = min(self.grid.tiles_horizontal-1, initial_position[1]+initial_width+l_max)
        right = random.randint(min(Ia, Ib), max(Ia, Ib))

        Ia= initial_position[1]-plataforma.largura
        Ib = max(1-plataforma.largura, initial_position[1]-l_max-plataforma.largura)
        print(f"{initial_position} - {plataforma.largura}")
        left = random.randint(min(Ia, Ib), max(Ia, Ib))

        if initial_position[1] <= 0:
            col = right
        elif initial_position[1]+initial_width >= self.grid.tiles_horizontal:
            col = left
        else:
            if random.randint(0, 1): # para posicionar a plataforma a direita
                col = right
            else: # plataforma a esquerda
                col = left

        self.grid.add_tilegrid(plataforma.tilegrid, linha, col)
        return ((linha,col), plataforma.largura, a_max, l_max)

        
