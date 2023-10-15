from entidades.lava import Lava
from entidades.jogador import Jogador
from entidades.plataforma import Plataforma
from constantes.constantes import constantes
from pygame import Surface
from plataforma import Plataforma
from tiles_package import TileGrid
import random


class Cenario:

    def __init__(self, tiles_horizontal: int, tiles_vertical: int, largura_tela: int, altura_tela: int,
                 dist_y_max: int, dist_x_max: int):
        self.__lava = Lava()
        self.__grid = TileGrid(16, 16, tiles_horizontal=tiles_horizontal, tiles_vertical=tiles_vertical, largura_tela=largura_tela, altura_tela= altura_tela)
        self.__reference_platform = ((10, 3), 3)
        self.__dist_x_max = dist_x_max
        self.__dist_y_max = dist_y_max
        self.gerar_cenario()

    @property
    def grid(self):
        return self.__grid

    def gerar_cenario(self) -> None:
        plataforma_gerada = self.__reference_platform
        while True:
            plataforma_gerada = self.gerar_plataforma(*plataforma_gerada)
            if plataforma_gerada[0][0] in range(-self.grid.tiles_vertical, -self.grid.tiles_vertical+self.__dist_y_max):
                self.__reference_platform = ((0, plataforma_gerada[0][1]), plataforma_gerada[1])
                break

    def gerar_plataforma(self, initial_position: tuple, initial_width: int,):
        random.seed(None)

        plataforma = Plataforma(random=True)

        Imin = initial_position[0] - self.__dist_y_max
        Imax = initial_position[0]-2
        linha = random.randint(Imin, Imax)  

        col = 0
        Ia = initial_position[1]+initial_width
        Ib = min(self.grid.tiles_horizontal-1, initial_position[1]+initial_width+self.__dist_x_max)
        right = random.randint(min(Ia, Ib), max(Ia, Ib))

        Ia= initial_position[1]-plataforma.largura
        Ib = max(1-plataforma.largura, initial_position[1]-self.__dist_x_max-plataforma.largura)
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
        return ((linha,col), plataforma.largura)

    def update_cenario(self, move_down: float):
        if self.grid.move_down(move_down):
            self.gerar_cenario()
        

        
