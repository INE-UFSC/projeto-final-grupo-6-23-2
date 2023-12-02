import pygame
from jogo.estado import Estado
from entidades.entidades_tela.button import Button



class EstadoTutorial(Estado):

    def __init__(self, refer_jogo, configuracoes):
        super().__init__(
            jogo=refer_jogo, configuracoes=configuracoes, estado_atual="tutorial"
        )
        self._configuracoes = configuracoes

        font_path = "versao_final/styles/assets/fonte-textos.ttf"
        self.__font = pygame.font.Font(font_path, 20)

        self.__home_button = Button((75, 580), self.home, text="Voltar")
        self.__background = pygame.image.load('versao_final/styles/assets/telas/backgrounds/bg-inicial.png').convert()
        self.__background = pygame.transform.scale(self.__background, (450, 800))
        self.__background_rect = self.__background.get_rect()
        self.__background_rect.x = 0
        self.__background_rect.y = 0

        self.__panel = pygame.image.load('versao_final/styles/assets/telas/backgrounds/panel.png').convert_alpha()
        self.__panel_rect = self.__panel.get_rect()
        self.__panel_rect.x = 25
        self.__panel_rect.y = 90

        self.__title = pygame.image.load(f'versao_final/styles/assets/telas/title/tutorial-title.png').convert_alpha()
        self.__title_rect = self.__title.get_rect()
        self.__title_rect.x = 0
        self.__title_rect.y = 30

        self.__keys = pygame.image.load(f'versao_final/styles/assets/telas/buttons/keys.png').convert_alpha()
        self.__keys_rect = self.__keys.get_rect()
        self.__keys_rect.x = 240
        self.__keys_rect.y = 150

        self.__coins = pygame.image.load(f'versao_final/styles/assets/telas/buttons/coins.png').convert_alpha()
        self.__coins = pygame.transform.scale_by(self.__coins, 2.5)
        self.__coins_rect = self.__coins.get_rect()
        self.__coins_rect.x = 315
        self.__coins_rect.y = 290

        self.__duplopulo = pygame.image.load(f'versao_final/styles/assets/telas/buttons/duplopulo.png').convert_alpha()
        self.__duplopulo = pygame.transform.scale_by(self.__duplopulo, 2.5)
        self.__duplopulo_rect = self.__duplopulo.get_rect()
        self.__duplopulo_rect.x = 315
        self.__duplopulo_rect.y = 390

        self.__imortal = pygame.image.load(f'versao_final/styles/assets/telas/buttons/imortal.png').convert_alpha()
        self.__imortal = pygame.transform.scale_by(self.__imortal, 2.5)
        self.__imortal_rect = self.__imortal.get_rect()
        self.__imortal_rect.x = 315
        self.__imortal_rect.y = 490

        self.__textos = {(30, 170): "Para mover-se utilize\nas teclas de seta.",
                        (30, 300): "Colete moedas para\naumentar sua pontuação.",
                        (30, 400): "Esse powerup lhe permite\n1 pulo no ar por 10 segundos.", 
                        (30, 500): "Esse powerup lhe protege\ncontra os inimigos"
                        }

    def entrar_estado(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load('versao_final/styles/assets/musica/musica-inicial.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

    def atualizar_estado(self, eventos, tela):
        tela.blit(self.__background, self.__background_rect)
        self.desenhar_tutorial(tela)
        self.__home_button.desenhar_tela(tela)
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            self.__home_button.update(evento)

        
        pygame.display.flip()

    def desenhar_tutorial(self, tela):
        tela.blit(self.__panel, self.__panel_rect)
        tela.blit(self.__title, self.__title_rect)

        for pos, texto in self.__textos.items():
            textlines = texto.splitlines()
            for i, line in enumerate(textlines):
                t = self.__font.render(line, True, (32, 28, 28))
                t_rect = t.get_rect()
                t_rect.x = pos[0] 
                t_rect.y = pos[1]+22*i # 22 é o espaçamento entre linhas
                tela.blit(t, t_rect)

        tela.blit(self.__keys, self.__keys_rect)
        tela.blit(self.__coins, self.__coins_rect)
        tela.blit(self.__duplopulo, self.__duplopulo_rect)
        tela.blit(self.__imortal, self.__imortal_rect)
        

    def home(self):
        self._prox_estado = "menu"