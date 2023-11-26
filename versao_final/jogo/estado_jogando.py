import pygame
from jogo.estado import Estado
from entidades.entidades_cenario.cenario import Cenario
from entidades.arquivos_jogador.jogador import Jogador
from entidades.detector_colisao import DetectorColisao
from entidades.pontuacao import Pontuacao


class EstadoJogando(Estado):
    def __init__(self, refer_jogo, configuracoes):
        super().__init__(
            jogo=refer_jogo, configuracoes=configuracoes, estado_atual="jogando"
        )

        # Inicia cenário
        self.__cenario = Cenario(self._configuracoes)

        # Instancia pontuacao
        self.__pontuacao = Pontuacao()

        # Instancia jogador
        self.__jogador = Jogador(self._configuracoes)

        # Instancia detector de colisão
        self.__detector_colisao = DetectorColisao()
        self.__detector_colisao.adicionar_objeto(self.__jogador)
        self.__detector_colisao.adicionar_objeto(self.__cenario.lava)
        for plataforma in self.__cenario.plataformas:
            self.__detector_colisao.adicionar_objeto(plataforma)

    def entrar_estado(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load('versao_final/styles/assets/musica/jeremy_blake_powerup.mp3')
        pygame.mixer.music.play(-1)

    def atualizar_estado(self, eventos, tela):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    self.__jogador.pular(self.__detector_colisao)

        self.lidar_cenario()
        self.lidar_jogador()
        self.lidar_pontuacao()
        self.desenhar_objetos(tela=tela)

    def lidar_jogador(self):
        self.__jogador.andar_jogador(pygame.key.get_pressed())
        self.__jogador.atualizar_jogador(
            self.__detector_colisao, self.__cenario.veloc_cenario
        )

    def lidar_cenario(self):
        self.__cenario.movimentar_cenario(self.__detector_colisao)
        self.__cenario.atualizar_inimigos(self.__detector_colisao)

    def lidar_pontuacao(self):
        self.__pontuacao.aumenta_pontuacao()
        self.__pontuacao.verificar_pontuacao()

    def desenhar_objetos(self, tela):
        tela.fill("Black")
        self.__cenario.paisagem.draw(tela)
        for plataforma in self.__cenario.plataformas:
            tela.blit(plataforma.imagem, plataforma.rect)
        for inimigo in self.__cenario.inimigos:
            tela.blit(inimigo.image, inimigo.rect)
            inimigo.update()
        tela.blit(self.__jogador.imagem, self.__jogador.rect)
        tela.blit(self.__cenario.lava.superficie, self.__cenario.lava.rect)
        self.__pontuacao.mostrar_pontuacao(tela)

        pygame.display.flip()
