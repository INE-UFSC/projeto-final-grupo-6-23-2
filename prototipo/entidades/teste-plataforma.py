import pygame
import constantes
from tiles_package import *
from cenario import Cenario


# Inicia biblioteca
pygame.init()

# Inicia display
tela = pygame.display.set_mode(
    (constantes.LARGURA_TELA, constantes.ALTURA_TELA)
)
pygame.display.set_caption('Volcano Jumper')

scene = Cenario(tiles_horizontal=10, tiles_vertical=10, largura_tela=constantes.LARGURA_TELA, altura_tela=constantes.ALTURA_TELA, dist_x_max=2, dist_y_max=2)
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    tela.fill((0, 0, 0))

    scene.grid.draw(tela)
    scene.update_cenario(1)
    clock.tick(constantes.FPS)

    pygame.display.flip()

