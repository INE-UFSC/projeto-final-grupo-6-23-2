import sys
import pygame
from constantes.constantes import Constantes
from entidades.cenario import Cenario
from entidades.jogador import Jogador
from entidades.collision import CollisionManager


class  Jogo:
    """Classe principal que dará início ao jogo"""

    def __init__(self):
        # Inicia biblioteca
        pygame.init()
        self.__constantes = Constantes()

        self.__velocidade_descida = 1

        # Instancia jogador e gerenciador de colisões (padrão observador)
        self.__adm_colisao = CollisionManager()
        self.__jogador = Jogador(self.__velocidade_descida)
        self.__adm_colisao.add_observer(self.__jogador)

        # Inicia display
        self.__tela = pygame.display.set_mode(
            (self.__constantes.largura_tela, self.__constantes.altura_tela)
        )
        pygame.display.set_caption('Volcano Jumper')


        # Inicia cenário
        self.__cenario = Cenario(9, 16, self.__constantes.largura_tela, self.__constantes.altura_tela, 2, 2)

    def iniciar(self) -> None:
        """Função responsável pelo loop principal do jogo e por gerar o cenário"""

        # O clock regula a taxa de frames do jogo
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
            self.__cenario.update_cenario(self.__velocidade_descida)
            self.__tela.blit(self.__cenario.lava.superficie, self.__cenario.lava.posicao)
            self.__tela.blit(self.__jogador.superficie, self.__jogador.posicao)
            self.__jogador.aplica_gravidade(0.2)

            if self.__adm_colisao.notify_collisions(self.__cenario.lava) == 'kill':
                pygame.quit()
                sys.exit()
            
            self.__adm_colisao.notify_collisions(self.__cenario.plataformas, group=True)

            clock.tick(self.__constantes.fps)
            pygame.display.flip()
