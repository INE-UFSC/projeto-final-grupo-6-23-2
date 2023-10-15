import pygame
from constantes.constantes import constantes
from entidades.cenario import Cenario

class  Jogo:
    """Classe principal que dará início ao jogo"""

    def __init__(self):
        # Inicia biblioteca
        pygame.init()

        # Inicia display
        self.__tela = pygame.display.set_mode(
            (constantes.largura_tela, constantes.altura_tela)
        )
        pygame.display.set_caption('Volcano Jumper')

        # Inicia cenário
        self.__cenario = Cenario(self.__tela)

    """Função responsável pelo loop principal do jogo e por gerar o cenário"""
    def iniciar(self) -> None:
        clock = pygame.time.Clock()

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.__cenario.gerar_cenario(self.__tela)
            clock.tick(constantes.fps)
            pygame.display.flip()
