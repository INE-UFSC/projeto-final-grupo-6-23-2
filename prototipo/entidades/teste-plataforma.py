import random
import pygame
from plataforma import Plataforma
import constantes
from tiles_package import *
from plataforma import Plataforma
from cenario import Cenario


# Inicia biblioteca
pygame.init()

# Inicia display
tela = pygame.display.set_mode(
    (constantes.LARGURA_TELA, constantes.ALTURA_TELA)
)
pygame.display.set_caption('Volcano Jumper')

scene = Cenario(tiles_horizontal=15, tiles_vertical=15, largura_tela=constantes.LARGURA_TELA, altura_tela=constantes.ALTURA_TELA)
scene.grid.add_tilegrid(Plataforma().tilegrid, 14, 3)
scene.gerar_cenario(3, 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    tela.fill((0, 0, 0))  # Limpe a tela

    # Renderize todos os tiles no TileGroup
    scene.grid.draw(tela)

    pygame.display.flip()  # Atualize a tela

