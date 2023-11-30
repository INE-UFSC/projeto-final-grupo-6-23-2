import pygame
from jogo.estado import Estado
from entidades.entidades_cenario.cenario import Cenario
from entidades.arquivos_jogador.jogador import Jogador
from entidades.detector_colisao import DetectorColisao
from entidades.entidades_cenario.itens.moeda import Moeda


class EstadoJogando(Estado):
    def __init__(self, refer_jogo, configuracoes):
        super().__init__(
            jogo=refer_jogo, configuracoes=configuracoes, estado_atual="jogando"
        )

        # Instancia jogador
        self.__jogador = Jogador(self._configuracoes)

        # Instancia detector de colisão
        self.__detector_colisao = DetectorColisao()
        self.__detector_colisao.adicionar_objeto(self.__jogador)
    

        # Inicia cenário
        self.__cenario = Cenario(self._configuracoes, self.__detector_colisao)

        # Instancia pontuacao
        self.__pontuacao = self._configuracoes.pontuacao

        self.__detector_colisao.adicionar_objeto(self.__cenario.lava)
        for plataforma in self.__cenario.plataformas:
            self.__detector_colisao.adicionar_objeto(plataforma)

    def entrar_estado(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load('versao_final/styles/assets/musica/jeremy_blake_powerup.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

    def atualizar_estado(self, eventos, tela):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    if self.__jogador.jump_finished:
                        self.__jogador.jump_finished =  False
                        self.__jogador.pular(self.__detector_colisao)

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_UP:
                    self.__jogador.jump_finished = True 

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
        self.__cenario.movimentar_cenario()
        self.__cenario.atualizar_inimigos()
        self.__cenario.atualizar_itens()

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
        for item in self.__cenario.itens:
            tela.blit(item.imagem, item.rect)
            item.update()
        self.__pontuacao.mostrar_pontuacao(tela)

        tela.blit(self.__cenario.lava.superficie, self.__cenario.lava.rect)
        pygame.display.flip()
