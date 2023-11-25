import pygame
from entidades.arquivos_jogador.estado_jogador import EstadoJogador
from entidades.detector_colisao import DetectorColisao
from configuracoes.configuracoes import Configuracoes


class EstadoPulo(EstadoJogador):
    def __init__(self, jogador, configuracoes: Configuracoes):
        super().__init__(jogador)

        imagem_parado = pygame.image.load(
            "versao_final/styles/assets/sprites_jogador/parado0.png"
        ).convert_alpha()
        self._imagem = pygame.image.load(
            "versao_final/styles/assets/sprites_jogador/pulo0.png"
        ).convert_alpha()

        self._imagem = pygame.transform.scale_by(self._imagem, factor=3)
        imagem_parado = pygame.transform.scale_by(imagem_parado, factor=3)
        self._mascara = pygame.mask.from_surface(imagem_parado)
        self._largura = self._imagem.get_width()
        self._altura = self._imagem.get_height()

        self._total_imagens = configuracoes.jogador_num_imagens_pulo
        self._nome_estado = "pulo"
        self._prox_estado = "pulo"

    def entrar_estado(self):
        super().entrar_estado(estado_atual="pulo")

    def pular(self, detector_colisao: DetectorColisao) -> None:
        return

    def aterrissar(self):
        self._jogador.veloc_queda = self._jogador.veloc_queda_min
        self._prox_estado = "parado"
