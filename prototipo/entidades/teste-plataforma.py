import pygame
from plataforma import Plataforma
import constantes
from tiles_package import *
from plataforma import Plataforma


# Inicia biblioteca
pygame.init()

# Inicia display
tela = pygame.display.set_mode(
    (constantes.LARGURA_TELA, constantes.ALTURA_TELA)
)
pygame.display.set_caption('Volcano Jumper')

grade = TileGrid(16, 16, tiles_horizontal=10, tiles_vertical=10, largura_tela=constantes.LARGURA_TELA, altura_tela=constantes.ALTURA_TELA)
plataforma_default = Plataforma("dark-side-brick-3_1")
#grade.add_tile(Tileset("prototipo/styles/assets/plataforma-tile-test.png", 16, 16).get_tile(0, 0), 0, 0)
#grade.add_tile(Tileset("prototipo/styles/assets/plataforma-tile-test.png", 16, 16).get_tile(0, 2), 0, 1)
grade.add_tilegrid(plataforma_default.tilegrid, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    tela.fill((0, 0, 0))  # Limpe a tela

    # Renderize todos os tiles no TileGroup
    grade.draw(tela)

    pygame.display.flip()  # Atualize a tela

