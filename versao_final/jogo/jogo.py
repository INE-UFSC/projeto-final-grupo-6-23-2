import pygame
from constantes.constantes import Constantes
from entidades.cenario import Cenario
from entidades.jogador import Jogador
from entidades.detector_colisao import DetectorColisao
from entidades.pontuacao import Pontuacao
from entidades.inimigo import Inimigo


class Jogo:
    def __init__(self):
        # Inicia biblioteca
        pygame.init()

        #  Instancia singleton das constantes
        self.__constantes = Constantes()

        # Inicia display
        self.__tela = pygame.display.set_mode(
            (self.__constantes.largura_tela, min(800, pygame.display.Info().current_h - 50))
        )
        pygame.display.set_caption("Volcano Jumper")

        # Inicia cenário
        self.__cenario = Cenario(self.__constantes)

        # Instancia pontuacao
        self.__pontuacao = Pontuacao()

        # Instancia jogador
        self.__jogador = Jogador(self.__constantes)

        # Instancia detector de colisão
        self.__detector_colisao = DetectorColisao()
        self.__detector_colisao.adicionar_objeto(self.__jogador)
        self.__detector_colisao.adicionar_objeto(self.__cenario.lava)
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
                        self.__jogador.pular(self.__detector_colisao)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.__jogador.move_esquerda()
            if keys[pygame.K_RIGHT]:
                self.__jogador.move_direita()

            self.__cenario.movimentar_cenario(self.__detector_colisao)
            self.__jogador.aplica_gravidade(
                self.__detector_colisao, self.__cenario.veloc_cenario
            )
            self.__desenhar_objetos()
            self.__pontuacao.aumenta_pontuacao()
            self.__pontuacao.verificar_pontuacao()


            clock.tick(self.__constantes.fps)
        

    def __desenhar_objetos(self):
        self.__tela.fill("Black")
        self.__cenario.paisagem.draw(self.__tela)
        for plataforma in self.__cenario.plataformas:
            self.__tela.blit(plataforma.imagem, plataforma.rect)
        for inimigo in self.__cenario.inimigos:
            self.__tela.blit(inimigo.image, inimigo.rect)
            inimigo.update()
        self.__cenario.gerar_inimigo()
        self.__cenario.remover_inimigos()
        print(len(self.__cenario.inimigos))
        self.__tela.blit(self.__jogador.superficie, self.__jogador.rect)

        self.__tela.blit(self.__cenario.lava.superficie,
                         self.__cenario.lava.rect)
        self.__pontuacao.mostrar_pontuacao(self.__tela)

        pygame.display.flip()
