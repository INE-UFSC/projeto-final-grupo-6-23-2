import pygame
from entidades.arquivos_jogador.estado_jogador import EstadoJogador
from entidades.entidades_cenario.plataforma import Plataforma
from entidades.detector_colisao import DetectorColisao
from configuracoes.configuracoes import Configuracoes


class EstadoMachucado(EstadoJogador):
    def __init__(self, jogador, configuracoes: Configuracoes):
        super().__init__(jogador, configuracoes)

        imagem = pygame.image.load(
            "versao_final/styles/assets/sprites_jogador/machucado0.png"
        ).convert_alpha()
        self._imagem = pygame.transform.scale_by(imagem, factor=3)
        self._mascara = pygame.mask.from_surface(self._imagem)
        self._largura = self._imagem.get_width()
        self._altura = self._imagem.get_height()

        self._total_imagens = configuracoes.jogador_num_imagens_machucado
        self._nome_estado = "machucado"

    def entrar_estado(self):
        super().entrar_estado()

    def andar_jogador(self, keys) -> None:
        """No estado 'machucado', é permitido ao jogador
        movimentar-se lateralmente."""

        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
            return
        if keys[pygame.K_RIGHT]:
            self.move_direita()
        if keys[pygame.K_LEFT]:
            self.move_esquerda()

    def colide_inimigos(self, detector_colisao: DetectorColisao):
        """Durante o estado 'machucado', o jogador ganha imunidade
        temporária a colisões com outros inimigos."""

        return

    def animar(self) -> None:
        """O estado 'machucado' dura até que a sua animação acabe, e
        então o jogador retorna para o estado 'parado'."""

        super().animar()
        if int(self._indice_imagem) == (self._total_imagens - 1):
            self._jogador.trocar_estado("parado")

    def pular(self, detector_colisao: DetectorColisao) -> None:
        """Não é permitido pular no estado 'machucado'."""

        return
