import pygame
from abc import ABC


class EstadoJogador(ABC):
    def animar(self, virado_direita) -> None:
        self._indice_imagem = (self._indice_imagem +
                                0.01) % (self._total_imagens)
        imagem = pygame.image.load(
            f"versao_final/styles/assets/sprites_jogador/{self._nome_estado}{int(self._indice_imagem)}.png"
        ).convert_alpha()
        self._imagem = pygame.transform.scale_by(imagem, factor=3)
        if not virado_direita:
            self._imagem = pygame.transform.flip(
                self._imagem, flip_x=True, flip_y=False)
    
    @property
    def imagem(self):
        return self._imagem
    
    @property
    def mascara(self):
        return self._mascara
