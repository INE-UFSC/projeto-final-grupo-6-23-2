import pygame
from entidades.arquivos_jogador.estado_jogador import EstadoJogador
from entidades.detector_colisao import DetectorColisao
from configuracoes.configuracoes import Configuracoes


class EstadoPulo(EstadoJogador):
    def __init__(self, jogador, configuracoes: Configuracoes):
        super().__init__(jogador, configuracoes)

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

    def andar_jogador(self, keys) -> None:
        """No estado 'pulo', é permitido ao jogador
        movimentar-se lateralmente."""

        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
            return
        if keys[pygame.K_RIGHT]:
            self.move_direita()
        if keys[pygame.K_LEFT]:
            self.move_esquerda()

    def pular(self, detector_colisao: DetectorColisao) -> None:
        """Não é permitido pular dentro do estado 'pulo'."""

        return

    def aterrissar(self):
        """Ao aterrissar, o jogador no estado 'pulo'
         vai para o estado 'parado'."""

        super().aterrissar()
        self._prox_estado = "parado"
