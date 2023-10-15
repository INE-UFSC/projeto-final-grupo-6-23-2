import pygame
from constantes.constantes import constantes
from entidades.cenario import Cenario
from entidades.jogador import Jogador


class  Jogo:
    """Classe principal que dará início ao jogo"""

    def __init__(self):
        # Inicia biblioteca
        pygame.init()

        self.__jogador = Jogador()

        # Inicia display
        self.__tela = pygame.display.set_mode(
            (constantes.largura_tela, constantes.altura_tela)
        )
        pygame.display.set_caption('Volcano Jumper')

        # Inicia cenário
        self.__cenario = Cenario(9, 16, constantes.largura_tela, constantes.altura_tela, 2, 2)

    """Função responsável pelo loop principal do jogo e por gerar o cenário"""
    def iniciar(self) -> None:
        clock = pygame.time.Clock()

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.__jogador.pular()
                        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.__jogador.move_esquerda()
            if keys[pygame.K_RIGHT]:
                self.__jogador.move_direita()
            
            self.__tela.fill('Black')
            self.__cenario.grid.draw(self.__tela)
            self.__cenario.update_cenario(1)
            self.__tela.blit(self.__cenario.lava.superficie, self.__cenario.lava.posicao)
            self.__tela.blit(self.__jogador.superficie, self.__jogador.posicao)
            self.__jogador.aplica_gravidade(0.02)

            clock.tick(constantes.fps)
            pygame.display.flip()
