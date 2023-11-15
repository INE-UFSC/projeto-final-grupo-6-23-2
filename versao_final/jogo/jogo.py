import pygame
from constantes.constantes import Constantes
from entidades.cenario import Cenario
from entidades.jogador import Jogador
from entidades.detector_colisao import DetectorColisao


class Jogo:

    def __init__(self):
        # Inicia biblioteca
        pygame.init()

        #  Instancia singleton das constantes
        self.__constantes = Constantes()

        # Inicia display
        self.__tela = pygame.display.set_mode(
            (self.__constantes.largura_tela, self.__constantes.altura_tela)
        )
        pygame.display.set_caption('Volcano Jumper')

        # Inicia cenário
        self.__cenario = Cenario(self.__tela, self.__constantes)

        # Instancia jogador
        self.__jogador = Jogador(self.__constantes)

        # Instancia detector de colisão
        self.__detector_colisao = DetectorColisao()
        self.__detector_colisao.adicionar_objeto(self.__jogador)
        for plataforma in self.__cenario.plataformas:
            self.__detector_colisao.adicionar_objeto(plataforma)

    # Roda o jogo (loop principal)
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

            self.__jogador.aplica_gravidade(self.__detector_colisao)
            self.__desenhar_objetos()

            clock.tick(self.__constantes.fps)
            pygame.display.flip()

    def __desenhar_objetos(self):
        self.__tela.fill('Black')
        self.__tela.blit(self.__jogador.superficie,
                         self.__jogador.rect)
        self.__tela.blit(self.__cenario.lava.superficie,
                         self.__cenario.lava.rect)

        for plataforma in self.__cenario.plataformas:
            self.__tela.blit(plataforma.superficie, plataforma.rect)
