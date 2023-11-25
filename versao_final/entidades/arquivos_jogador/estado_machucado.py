import pygame
from entidades.arquivos_jogador.estado_jogador import EstadoJogador
from entidades.entidades_cenario.plataforma import Plataforma
from entidades.detector_colisao import DetectorColisao
from configuracoes.configuracoes import Configuracoes


class EstadoMachucado(EstadoJogador):
    def __init__(self, jogador, configuracoes: Configuracoes):
        super().__init__(jogador)

        imagem = pygame.image.load(
            "versao_final/styles/assets/sprites_jogador/machucado0.png"
        ).convert_alpha()
        self._imagem = pygame.transform.scale_by(imagem, factor=3)
        self._mascara = pygame.mask.from_surface(self._imagem)
        self._largura = self._imagem.get_width()
        self._altura = self._imagem.get_height()

        self._total_imagens = configuracoes.jogador_num_imagens_machucado
        self._nome_estado = "machucado"
        self._prox_estado = "machucado"

    def entrar_estado(self):
        super().entrar_estado(estado_atual="machucado")

    def colide_inimigos(self, detector_colisao: DetectorColisao):
        return

    def animar(self) -> None:
        super().animar()
        if int(self._indice_imagem) == (self._total_imagens - 1):
            self._prox_estado = "parado"

    def pular(self, detector_colisao: DetectorColisao) -> None:
        return

    def aterrissar(self) -> None:
        self._jogador.veloc_queda = self._jogador.veloc_queda_min
