import pygame
from configuracoes.configuracoes import Configuracoes
from jogo.estado_jogando import EstadoJogando
from jogo.estado_menu import EstadoMenu
from jogo.estado_tutorial import EstadoTutorial


class Jogo:
    def __init__(self):
        # Inicia a biblioteca pygame
        pygame.init()

        #  Instancia singleton das Configuracoes
        self.__configuracoes = Configuracoes()

        # Inicia display
        self.__tela = pygame.display.set_mode(
            (
                self.__configuracoes.largura_tela,
                min(800, pygame.display.Info().current_h - 50),
            )
        )
        pygame.display.set_caption("Volcano Jumper")

        # Inicia o mixer do pygame
        pygame.mixer.init()

        self.__estados = {
            "jogando": EstadoJogando,
            "menu": EstadoMenu,
            "tutorial": EstadoTutorial,
            "game over": ...,
        }
        self.__estado_atual = self.__estados["menu"](
            refer_jogo=self, configuracoes=self.__configuracoes
        )
        self.__estado_atual.entrar_estado()

    # Roda o jogo (loop principal)
    def iniciar(self) -> None:
        clock = pygame.time.Clock()

        while True:
            eventos = pygame.event.get()
            self.atualizar_estado(eventos)
            clock.tick(self.__configuracoes.fps)

    def atualizar_estado(self, eventos):
        self.__estado_atual.atualizar_estado(eventos=eventos, tela=self.__tela)

        prox_estado = self.__estado_atual.prox_estado
        if self.__estado_atual.nome_estado != prox_estado:
            del self.__estado_atual
            self.__estado_atual = self.__estados[prox_estado](
                refer_jogo=self, configuracoes=self.__configuracoes
            )
            self.__estado_atual.entrar_estado()
