import pygame
from jogo.estado import Estado
from entidades.entidades_cenario.cenario import Cenario
from entidades.arquivos_jogador.jogador import Jogador
from entidades.detector_colisao import DetectorColisao
from entidades.entidades_tela.button import Button


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
        self.__pontuacao.zerar_pontuacao()

        self.__pausado = False
        self.__pause_button = Button((400, 5), self.pausa, img_hover="button-pause-hover.png", img_static="button-pause-static.png")

        self.__detector_colisao.adicionar_objeto(self.__cenario.lava)
        for plataforma in self.__cenario.plataformas:
            self.__detector_colisao.adicionar_objeto(plataforma)

    def entrar_estado(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load('versao_final/styles/assets/musica/jeremy_blake_powerup.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

    def atualizar_estado(self, eventos, tela):
        if self.__pausado:
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                self.__home_button.update(evento)
                self.__replay_button.update(evento)
                self.__play_button.update(evento)
            
            tela.blit(self.__popup, self.__popup_rect)
            tela.blit(self.__title, self.__title_rect)
            tela.blit(self.__texto_pontuacao, self.__texto_pontuacao_rect)
            self.__home_button.desenhar_tela(tela)
            self.__replay_button.desenhar_tela(tela)
            self.__play_button.desenhar_tela(tela)

            pygame.display.flip()

        else:
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

                if evento.type == self._configuracoes.GAMEOVER:
                    self._prox_estado = "gameover"

                self.__pause_button.update(evento)

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

        self.__pause_button.desenhar_tela(tela)

        tela.blit(self.__cenario.lava.superficie, self.__cenario.lava.rect)
        pygame.display.flip()

    def configura_popup_pausa(self):
        font_path = "versao_final/styles/assets/fonte-textos.ttf"
        self.__font = pygame.font.Font(font_path, 50)

        self.__popup = pygame.image.load('versao_final/styles/assets/telas/backgrounds/bg-menu-pause.png').convert_alpha()
        self.__popup_rect = self.__popup.get_rect()
        self.__popup_rect.x = 25
        self.__popup_rect.y = 90

        self.__title = pygame.image.load(f'versao_final/styles/assets/telas/title/pausado-title.png').convert_alpha()
        self.__title = pygame.transform.scale_by(self.__title, 0.8)
        self.__title_rect = self.__title.get_rect()
        self.__title_rect.x = 60
        self.__title_rect.y = 30

        self.__texto_pontuacao = self.__font.render(f"Pontuação: {int(self._configuracoes.pontuacao.pontuacao_atual)}", True, (32, 28, 28))
        self.__texto_pontuacao_rect = self.__texto_pontuacao.get_rect()
        self.__texto_pontuacao_rect.x = 80
        self.__texto_pontuacao_rect.y = 200

        self.__replay_button = Button((120, 375), self.replay, img_hover="button-restart-hover.png", img_static="button-restart-static.png")
        self.__home_button = Button((201, 375), self.home, img_hover="button-home-hover.png", img_static="button-home-static.png")
        self.__play_button = Button((281, 375), self.play, img_hover="button-play-hover.png", img_static="button-play-static.png")



    def pausa(self):
        self.configura_popup_pausa()
        pygame.mixer.music.pause()
        self.__pausado = True

    def replay(self):
        # Instancia jogador
        self.__jogador = Jogador(self._configuracoes)

        # Instancia detector de colisão
        self.__detector_colisao = DetectorColisao()
        self.__detector_colisao.adicionar_objeto(self.__jogador)
    

        # Inicia cenário
        self.__cenario = Cenario(self._configuracoes, self.__detector_colisao)

        # Instancia pontuacao
        self.__pontuacao = self._configuracoes.pontuacao
        self.__pontuacao.zerar_pontuacao()

        self.__pausado = False
        self.__pause_button = Button((400, 5), self.pausa, img_hover="button-pause-hover.png", img_static="button-pause-static.png")

        self.__detector_colisao.adicionar_objeto(self.__cenario.lava)
        for plataforma in self.__cenario.plataformas:
            self.__detector_colisao.adicionar_objeto(plataforma)
        
        pygame.mixer.music.play(-1)

    def home(self):
        self._prox_estado = "menu"

    def play(self):
        self.__pausado = False
        pygame.mixer.music.play(-1)


