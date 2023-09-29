import pygame
from constantes import constantes
from entidades.cenario import Cenario


class  Jogo:

    def __init__(self):
        # Inicia biblioteca
        pygame.init()

        # Inicia display
        self.__tela = pygame.display.set_mode(
            (constantes.LARGURA_TELA, constantes.ALTURA_TELA)
        )
        pygame.display.set_caption('Volcano Jumper')

        # Inicia cenário
        self.__cenario = Cenario(self.__tela)

    # Roda o jogo (loop principal)
    def iniciar(self) -> None:
        clock = pygame.time.Clock()

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.__cenario.gerar_cenario(self.__tela)
            clock.tick(constantes.FPS)
            pygame.display.flip()
