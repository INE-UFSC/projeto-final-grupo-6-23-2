import pygame
from entidades.arquivos_jogador.estado_jogador import EstadoJogador


class EstadoPulo(EstadoJogador):
    def __init__(self, configuracoes):
        super().__init__()

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
        self._nome_estado = 'pulo'
