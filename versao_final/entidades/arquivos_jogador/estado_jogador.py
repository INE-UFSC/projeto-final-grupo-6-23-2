import pygame
from abc import ABC, abstractmethod
from entidades.detector_colisao import DetectorColisao


class EstadoJogador(ABC):
    """Esta classe é a classe abstrata que será herdada pelos
    estados do jogador. Ela cuida dos métodos e atributos próprios
    do estado (entrar_estado(), animar(), imagem, etc) e também da lógica
    dos métodos do jogador que possivelmente mudarão o estado atual (pular(),
    andar_jogador(), etc)."""

    def __init__(self, jogador):
        self._jogador = jogador
        self._indice_imagem = 0

    def entrar_estado(self, nome_estado):
        self.animar()
        self._prox_estado = nome_estado

    def animar(self) -> None:
        """Esse método acessa a próxima imagem da sequência de imagens
        correspondentes à animação do estado, levando em conta, é claro, se
        o jogador está virado para a direita ou para a esquerda."""

        self._indice_imagem = (self._indice_imagem +
                               0.05) % (self._total_imagens)
        imagem = pygame.image.load(
            f"versao_final/styles/assets/sprites_jogador/{self._nome_estado}{int(self._indice_imagem)}.png"
        ).convert_alpha()
        self._imagem = pygame.transform.scale_by(imagem, factor=3)
        if not self._jogador.virado_direita:
            self._imagem = pygame.transform.flip(
                self._imagem, flip_x=True, flip_y=False
            )

    def andar_jogador(self, keys: list) -> None:
        if keys[pygame.K_RIGHT]:
            self.move_direita()
        if keys[pygame.K_LEFT]:
            self.move_esquerda()

    def move_direita(self) -> None:
        y_atual = self._jogador.posicao_centro[1]
        novo_x = self._jogador.posicao_centro[0] + self._jogador.veloc_corrida
        self._jogador.posicao_centro = (novo_x, y_atual)
        self._jogador.virado_direita = True

    def move_esquerda(self) -> None:
        y_atual = self._jogador.posicao_centro[1]
        novo_x = self._jogador.posicao_centro[0] - self._jogador.veloc_corrida
        self._jogador.posicao_centro = (novo_x, y_atual)
        self._jogador.virado_direita = False

    @abstractmethod
    def pular(self, detector_colisao: DetectorColisao) -> None:
        pass

    @abstractmethod
    def aterrissar(self):
        pass

    @property
    def imagem(self):
        return self._imagem

    @property
    def mascara(self):
        return self._mascara

    @property
    def prox_estado(self):
        return self._prox_estado
