import pygame
from entidades.arquivos_jogador.estado_jogador import EstadoJogador
from entidades.entidades_cenario.plataforma import Plataforma
from entidades.detector_colisao import DetectorColisao
from configuracoes.configuracoes import Configuracoes


class EstadoAndando(EstadoJogador):
    def __init__(self, jogador, configuracoes: Configuracoes):
        super().__init__(jogador, configuracoes)

        imagem = pygame.image.load(
            "versao_final/styles/assets/sprites_jogador/andando1.png"
        ).convert_alpha()
        self._imagem = pygame.transform.scale_by(imagem, factor=3)
        self._mascara = pygame.mask.from_surface(self._imagem)
        self._largura = self._imagem.get_width()
        self._altura = self._imagem.get_height()

        self._total_imagens = configuracoes.jogador_num_imagens_andando
        self._nome_estado = "andando"
        self._prox_estado = "andando"
        self.__pulou = False

    def entrar_estado(self):
        super().entrar_estado(estado_atual="andando")

    def andar_jogador(self, keys):
        """No estado 'andando', caso tanto seta para esquerda quanto
        seta para direita sejam pressionadas ao mesmo tempo, o próximo estado
        será 'parado'. Para que o próximo estado seja 'andando', é necessário
        que somente uma delas esteja sendo pressionada, ou então o jogador irá
        para o estado 'parado'."""

        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
            self._prox_estado = "parado"
            return
        if keys[pygame.K_RIGHT]:
            self.move_direita()
            if not self.__pulou:
                self._prox_estado = "andando"
            return
        if keys[pygame.K_LEFT]:
            self.move_esquerda()
            if not self.__pulou:
                self._prox_estado = "andando"
            return
        self._prox_estado = "parado"

    def pular(self, detector_colisao: DetectorColisao) -> None:
        """Se o jogador estiver imediatamente acima (1 pixel acima)
        de uma plataforma, ele pula e vai para o estado 'pulo'."""

        colidiu = detector_colisao.detectar_colisao(
            rect=self._jogador.rect,
            mascara=self._mascara,
            desloc_x=0,
            desloc_y=1,
            tipo=Plataforma,
        )
        if colidiu:
            self._jogador.veloc_queda = -self._jogador.tamanho_pulo
            self.__pulou = True
            self._prox_estado = "pulo"
