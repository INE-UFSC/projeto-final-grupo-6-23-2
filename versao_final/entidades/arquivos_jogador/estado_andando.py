import pygame
from entidades.arquivos_jogador.estado_jogador import EstadoJogador


class EstadoAndando(EstadoJogador):
    def __init__(self, configuracoes):
        super().__init__()

        imagem = pygame.image.load(
            "versao_final/styles/assets/sprites_jogador/andando1.png"
        ).convert_alpha()
        self._imagem = pygame.transform.scale_by(imagem, factor=3)
        self._mascara = pygame.mask.from_surface(self._imagem)
        self._largura = self._imagem.get_width()
        self._altura = self._imagem.get_height()    

        self._total_imagens = configuracoes.jogador_num_imagens_andando
        self._nome_estado = 'andando'