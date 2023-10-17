from entidades.lava import Lava
from entidades.plataforma import Plataforma
from constantes.constantes import constantes
from entidades.plataforma import Plataformas
from entidades.plataforma import Plataforma
from entidades.tiles_package import TileGrid
import random


"""A classe Cenario é responsável por juntar tudo que terá no cenário, e particularmente gerá-lo aleatoriamente.
Ele é composto em si por um objeto de TileGrid, ou seja, ele tem uma grade onde é possível posicionar tiles.
dist_x_max e dist_y_max se referem a distância máxima na horizontal e na vertical entre duas plataformas
a serem geradas, estas distâncias tem relação direta com o pulo do jogador. Além disso, o atributo
reference_platform define uma plataforma referência onde a partir desta será gerado novas plataformas
acessíveis ao jogador, então a plataforma de referência é constantemente atualizada de acordo com a 
geração do cenário."""
class Cenario:

    def __init__(self, tiles_horizontal: int, tiles_vertical: int, largura_tela: int, altura_tela: int,
                 dist_y_max: int, dist_x_max: int):
        self.__lava = Lava()
        self.__grid = TileGrid(16, 16, tiles_horizontal=tiles_horizontal, tiles_vertical=tiles_vertical, largura_tela=largura_tela, altura_tela= altura_tela)
        self.__reference_platform = ((10, 3), 3)
        self.__dist_x_max = dist_x_max
        self.__dist_y_max = dist_y_max
        self.__plataformas = Plataformas()
        self.gerar_cenario()

    @property
    def grid(self):
        return self.__grid
    
    @property
    def plataformas(self):
        return self.__plataformas

    """Neste método o cenário é gerado, inicialmente o cenário gera plataformas na tela visível, e 
    posteriormente na parte sobre não visível da tela para que o cenário vá descendo. O intervalo considerado
    no range permite que o cenário só gere plataformas na tela visível e apenas uma tela invisível sobre esta (para
    não gerar uso excessivo de memória), a cada geração de plataforma a última destas é considerada
    a plataforma de referência para gerar mais posteriormente"""
    def gerar_cenario(self) -> None:
        plataforma_gerada = self.__reference_platform
        
        while True:
            plataforma_gerada = self.gerar_plataforma(*plataforma_gerada)
            if plataforma_gerada[0][0] in range(-self.grid.tiles_vertical, -self.grid.tiles_vertical+self.__dist_y_max):
                self.__reference_platform = ((0, plataforma_gerada[0][1]), plataforma_gerada[1])
                break

    """Esse método gera aleatoriamente cada plataforma, para isso ele leva em consideração a posição, e 
    a largura da plataforma de referência. Ao iniciar, ele gera propriamente uma plataforma aleatória e 
    após isso é realizado randomicamente de acordo com os intervalos máximos e mínimos definidos pelas distâncias
    o valor da linha e da coluna a ser posicionada a plataforma. Note que na geração da coluna, é feito a
    verificação se a plataforma deve ser gerada a esquerda, a direita ou tanto faz, para garantir que
    todas as plataformas estejam no limite da tela e são acesíveis pelo jogador."""
    def gerar_plataforma(self, initial_position: tuple, initial_width: int,):
        random.seed(None)

        plataforma = Plataforma(random=True)

        self.__plataformas.add(plataforma.tilegrid)

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

    """Esse método atualiza o cenário, movendo-o para baixo de acordo com um valor passado pelo Jogo por parâmetro
    para isso ele chama o move_down de sua grade, se o move_down retornar True, é necessário gerar mais plataformas
    sobre a tela."""
    def update_cenario(self, move_down: float):
        if self.grid.move_down(move_down):
            self.gerar_cenario()
    
    @property
    def lava(self):
        return self.__lava

        
