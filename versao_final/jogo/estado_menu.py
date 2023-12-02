import pygame
from jogo.estado import Estado
from entidades.entidades_tela.button import Button


class EstadoMenu(Estado):
    def __init__(self, refer_jogo, configuracoes):
        super().__init__(
            jogo=refer_jogo, configuracoes=configuracoes, estado_atual="menu"
        )
        self._configuracoes = configuracoes

        self.__play_button = Button((75, 450), self.play, text="Jogar")
        self.__tutorial_button = Button(
            (75, 550), self.tutorial, text="Tutorial")
        self.__background = pygame.image.load(
            "versao_final/styles/assets/telas/backgrounds/bg-inicial.png"
        ).convert()
        self.__background = pygame.transform.scale(
            self.__background, (450, 800))
        self.__background_rect = self.__background.get_rect()
        self.__background_rect.x = 0
        self.__background_rect.y = 0

        self.__index_title = 0
        self.__title = pygame.image.load(
            f"versao_final/styles/assets/telas/title/title{self.__index_title}.png"
        ).convert_alpha()
        self.__title_rect = self.__title.get_rect()
        self.__title_rect.x = 0
        self.__title_rect.y = 200
        self.__ctrl_tick = 0
        self.__anima_title_counter = 0

    def entrar_estado(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(
            "versao_final/styles/assets/musica/musica-inicial.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

    def atualizar_estado(self, eventos, tela):
        tela.blit(self.__background, self.__background_rect)
        tela.blit(self.__title, self.__title_rect)
        self.__play_button.desenhar_tela(tela)
        self.__tutorial_button.desenhar_tela(tela)
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            self.__tutorial_button.update(evento)
            self.__play_button.update(evento)

        self.__ctrl_tick += 1
        if self.__anima_title_counter != 0:
            self.anima_title()
        else:
            if self.__ctrl_tick == 1 or self.__ctrl_tick % 100 == 0:
                self.anima_title()

        pygame.display.flip()

    def anima_title(self):
        self.__anima_title_counter += 1
        if self.__anima_title_counter % 5 == 0:
            self.__index_title += 1
            if self.__index_title > 5:
                self.__index_title = 0
                self.__anima_title_counter = 0
            self.__title = pygame.image.load(
                f"versao_final/styles/assets/telas/title/title{self.__index_title}.png"
            ).convert_alpha()

    def play(self):
        self._prox_estado = "jogando"

    def tutorial(self):
        self._prox_estado = "tutorial"
