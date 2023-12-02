import pygame
from jogo.estado import Estado
from entidades.entidades_tela.button import Button


class EstadoGameOver(Estado):

    def __init__(self, refer_jogo, configuracoes):
        super().__init__(
            jogo=refer_jogo, configuracoes=configuracoes, estado_atual="gameover"
        )
        self._configuracoes = configuracoes

        font_path = "versao_final/styles/assets/fonte-textos.ttf"
        self.__font = pygame.font.Font(font_path, 50)

        record = f"Novo record" if int(self._configuracoes.pontuacao.record) == int(self._configuracoes.pontuacao.pontuacao_atual) else f"Record: {int(self._configuracoes.pontuacao.record)}"
        self.__textos = {
            (80, 200): f"Pontuação: {int(self._configuracoes.pontuacao.pontuacao_atual)}",
            (100, 300): record
        }

        self.__replay_button = Button((150, 550), self.replay, img_hover="button-restart-hover.png", img_static="button-restart-static.png")
        self.__home_button = Button((231, 550), self.home, img_hover="button-home-hover.png", img_static="button-home-static.png")
        self.__background = pygame.image.load('versao_final/styles/assets/telas/backgrounds/bg-inicial.png').convert()
        self.__background = pygame.transform.scale(self.__background, (450, 800))
        self.__background_rect = self.__background.get_rect()
        self.__background_rect.x = 0
        self.__background_rect.y = 0

        self.__panel = pygame.image.load('versao_final/styles/assets/telas/backgrounds/panel.png').convert_alpha()
        self.__panel_rect = self.__panel.get_rect()
        self.__panel_rect.x = 25
        self.__panel_rect.y = 90

        self.__title = pygame.image.load(f'versao_final/styles/assets/telas/title/gameover-title.png').convert_alpha()
        self.__title = pygame.transform.scale_by(self.__title, 0.8)
        self.__title_rect = self.__title.get_rect()
        self.__title_rect.x = 0
        self.__title_rect.y = 30


    def entrar_estado(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load('versao_final/styles/assets/musica/gameover.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

    def atualizar_estado(self, eventos, tela):
        tela.blit(self.__background, self.__background_rect)
        tela.blit(self.__panel, self.__panel_rect)
        tela.blit(self.__title, self.__title_rect)

        for pos, texto in self.__textos.items():
            t = self.__font.render(texto, True, (32, 28, 28))
            t_rect = t.get_rect()
            t_rect.x = pos[0] 
            t_rect.y = pos[1]
            tela.blit(t, t_rect)

        self.__home_button.desenhar_tela(tela)
        self.__replay_button.desenhar_tela(tela)

        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            self.__home_button.update(evento)
            self.__replay_button.update(evento)

        pygame.display.flip()
            
    def replay(self):
        self._prox_estado = "jogando"

    def home(self):
        self._prox_estado = "menu"