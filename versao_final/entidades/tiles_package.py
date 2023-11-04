import pygame
import math


class Tileset:
    """O objetivo desta classe é cortar os tiles de uma imagem, por exemplo, a imagem dos tiles que estão
    em styles/assets/plataformas-tiles-test.png. Assim, é possível passar a imagem inteira, de modo que o
    próprio pygame já corta e retorna o bloco que queremos."""

    def __init__(self, imagem: str, largura_tile: int, altura_tile: int):
        self.tileset = pygame.image.load(imagem).convert_alpha()
        self.largura_tile = largura_tile
        self.altura_tile = altura_tile

    def get_tile(self, linha: int, coluna: int):
        """Retorna um objeto de Tile referente ao bloco posicionado na linha e coluna do tileset."""

        # Calcula a posição do retângulo do tile na imagem
        x = coluna * self.largura_tile
        y = linha * self.altura_tile

        # Corta o tile da imagem e retorna uma sub-superfície
        tile_subsurface = self.tileset.subsurface(
            pygame.Rect(x, y, self.largura_tile, self.altura_tile)
        )

        # Crie um objeto Tile diretamente com a sub-superfície e retorne-o
        tile = Tile(tile_subsurface, self.largura_tile, self.altura_tile)

        return tile


class Tile(pygame.sprite.Sprite):
    """Essa classe em si é responsável por modelar o objeto de Tile (extraído do Tileset). Como é
    algo gráfico, ela herda de Sprite do pygame. O que ela faz é basicamente ter uma imagem, altura e largura
    associada ao tile. Além disso, há uma implementação que provavelmente será útil mais adiante: dizer
    se este tile é sólido ou não."""

    def __init__(self, imagem, largura_tile: int, altura_tile: int, solido=True):
        super().__init__()

        # Usa a sub-superfície diretamente como imagem
        self.image = pygame.transform.scale(imagem, (largura_tile, altura_tile))
        self.rect = self.image.get_rect()

        # Define se o tile é sólido ou não
        self.solido = solido


class TileGrid(pygame.sprite.Group):
    """Essa classe TileGrid é basicamente uma grade de Tiles. De maneira gráfica, é uma grade
    onde poderemos posicionar os nossos 'blocos gráficos'. Ela herda de Group, pois como cada Tile é um
    sprite, e o TileGrid nada mais é do que uma grade de Tiles, faz sentido esta classe herdar de Group.

    De forma genérica, o TileGrid também é utilizado em cada plataforma, pois uma plataforma também possui
    uma grade de tiles. Exemplo: plataforma 1x3 é uma grade de 1 tile na vertical e 3 na horizontal.

    Os cálculos aqui feito se baseiam nas dimensões do tile em si e nas dimensões da tela (quando
    a grade for a grade principal da tela do jogo). Então a imagem de cada tile é adequada para que
    a tela realmente possua os tiles informados (tiles_horizontal e tiles_vertical).

    Caso não seja definido as dimensões da tela, então considera-se que esta grade é uma grade interna.
    No caso das plataformas, cada plataforma é uma grade interna de tiles, como comentado."""

    def __init__(
        self,
        largura_tile: int,
        altura_tile: int,
        tiles_horizontal: int = 1,
        tiles_vertical: int = 1,
        largura_tela: int = None,
        altura_tela: int = None,
    ):
        super().__init__()
        self.__tiles_horizontal = tiles_horizontal
        self.__tiles_vertical = tiles_vertical
        if largura_tela is not None and altura_tela is not None:
            self.__largura_tile = math.floor(
                (largura_tela / (tiles_horizontal))
            )
            self.__altura_tile = math.floor(
                (altura_tela / tiles_vertical)
            )
        else:
            self.__largura_tile = largura_tile
            self.__altura_tile = altura_tile
        self.__tiles = {}
        self.__desloc = 0

    @property
    def tiles(self):
        return self.__tiles

    @property
    def plataforma_rects(self):
        return self.__plataforma_rects

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
        """Este método permite adicionar uma grade de tiles dentro de outra grade, como no caso das plataformas.
        Então, ele basicamente pega a grade a ser adicionada, e adiciona tile por tile na grade em questão"""

        if isinstance(tilegrid, TileGrid):
            for pos, tile in tilegrid.tiles.items():
                num_linhas = pos[0]
                num_colunas = pos[1]
                if coluna + num_colunas in range(0, self.tiles_horizontal):
                    self.add_tile(tile, linha + num_linhas, coluna + num_colunas)
        else:
            raise TypeError("add_tilegrid deve receber um objeto do tipo TileGrid")

    def add_tile(self, tile, linha, coluna):
        """Este método adiciona um tile específico na (linha, coluna) da grade, previamente é feito
        o redimensionamento do tile de acordo com as dimensões calculadas no construtor. Um ponto importante
        aqui é que para adicionar o tile não é feito a verificação se a linha realmente existe, apenas a coluna.
        Isso nos foi útil, já que o cenário é gerado antes (acima da tela) para que possa ir descendo de acordo
        com o jogo, e, consequentemente gerando mais cenário (isso é feito na classe Cenario)"""

        if isinstance(tile, Tile):
            tile.image = pygame.transform.scale(
                tile.image, (self.largura_tile, self.altura_tile)
            )
            tile.rect = tile.image.get_rect()
            tile.rect.y = linha * self.largura_tile
            tile.rect.x = coluna * self.altura_tile
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
                raise ValueError(
                    "O tile deve ter as mesma dimensões do que as definidas pelo TileGrid"
                )
        else:
            raise TypeError("add_tile deve receber um objeto do tipo Tile")

    def remove_tile(self, linha, coluna):
        """Remove um tile da grade em questão"""

        try:
            super().remove(self.tiles[(linha, coluna)])
            if (linha, coluna) in self.tiles:
                self.tiles.pop((linha, coluna))
        except KeyError:
            if coluna > self.tiles_horizontal:
                raise KeyError(f"({linha}, {coluna}) inválidos para esta grade")

    def get_tile(self, linha, coluna):
        """Retorna o tile da respectiva posição"""

        try:
            return self.tiles[(linha, coluna)]
        except KeyError:
            if coluna > self.tiles_horizontal:
                raise KeyError(f"({linha}, {coluna}) inválidos para esta grade")
            else:
                return None

    def move_down(self, velocity: float):
        """Esse método é responsável por mover a grade para baixo de acordo com uma certa velocidade definida
        pelo jogo. Então, é considerado se o tile já se moveu o suficiente para ir para a próxima linha da
        grade, ou se ele saiu da tela, mudando o tile de linha e removendo-o quando sai da tela."""

        gerar = False
        self.__desloc += velocity

        if self.__desloc >= self.altura_tile * self.tiles_vertical:
            self.__desloc = 0
            gerar = True
        tiles_copy = self.tiles.copy()

        for position, tile in tiles_copy.items():
            linha = position[0]
            coluna = position[1]
            tile = self.get_tile(linha, coluna)

            if self.__desloc % self.altura_tile == 0:
                self.remove_tile(linha, coluna)
                self.add_tile(tile, linha + 1, coluna)
            else:
                tile.rect.y += velocity

            if tile.rect.y > self.altura_tile * self.tiles_vertical:
                self.remove_tile(linha, coluna)
        del tiles_copy
        return gerar
