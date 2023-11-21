import pygame
import sys
from entidades.detector_colisao import DetectorColisao
from entidades.plataforma import Plataforma
from entidades.lava import Lava


class Jogador:
    """O jogador vai ser ser o objeto que se movimenta na tela, e
    que será controlado pelas teclas, de modo a evitar que caia na lava."""

    def __init__(self, constantes):
        self.__constantes = constantes

        self.__imagem_base = pygame.image.load(
            "versao_final/styles/assets/sprites_jogador/parado0.png"
        ).convert_alpha()
        self.__imagem_base = pygame.transform.scale_by(self.__imagem_base, 3)
        self.__imagem = self.__imagem_base
        self.__indice_imagem = 0
        self.__virado_direita = True
        self.__mascara = pygame.mask.from_surface(self.__imagem)
        self.__largura = self.__imagem.get_width()
        self.__altura = self.__imagem.get_height()

        self.__veloc_corrida = self.__constantes.jogador_veloc_base
        self.__tamanho_pulo = self.__constantes.jogador_pulo_base
        self.__veloc_queda = 0

        self.__posicao = self.__constantes.jogador_pos_inicial
        self.__rect = self.__imagem.get_rect(center=self.__posicao)

    def aplica_gravidade(self, detector_colisao: DetectorColisao, veloc_cenario: float):
        """Esse método cuida da movimentação horizontal do jogador. Caso ele esteja subindo
        (self.__veloc_queda < 0), basta deslocá-lo. Caso contrário, é preciso fazer uma
        verificação, a fim de saber se ele colidiu com a lava (fim de jogo) ou com uma
        plataforma (aterrissar)."""

        colidiu_lava = detector_colisao.detectar_colisao(
            rect=self.__rect, mascara=self.__mascara, desloc_x=0, desloc_y=1, tipo=Lava
        )
        if colidiu_lava:
            pygame.quit()
            sys.exit()

        self.__veloc_queda_min = veloc_cenario
        self.__veloc_queda += self.__constantes.gravidade_jogo

        if self.__veloc_queda < 0:
            self.posicao_centro = (
                self.posicao_centro[0],
                self.posicao_centro[1] + self.__veloc_queda,
            )
            return
        else:
            deslocamento = self.__calcula_queda(detector_colisao)
            self.posicao_centro = (
                self.posicao_centro[0],
                self.posicao_centro[1] + deslocamento,
            )

    def __calcula_queda(self, detector_colisao: DetectorColisao) -> int:
        """Esse método determina a quantidade que o jogador vai descer (dy). Quando
        houver uma plataforma no caminho do jogador, ele não irá realizar todo o
        deslocamento previsto para aquele instante, e sim somente o necessário para
        que ele fique exatamente no topo da plataforma."""

        dy = 0
        while dy < self.__veloc_queda:
            dy += 1
            colidiu = detector_colisao.detectar_colisao(
                rect=self.__rect,
                mascara=self.__mascara,
                desloc_x=0,
                desloc_y=dy,
                tipo=Plataforma,
            )
            if colidiu:
                self.aterrissar()
                return dy - 1
        return dy

    def pular(self, detector_colisao: DetectorColisao) -> None:
        """O método só deixa o jogador pular se ele estiver imediatamente
        acima de uma plataforma, o que é verificado pelo detector_colisao."""

        colidiu = detector_colisao.detectar_colisao(
            rect=self.__rect,
            mascara=self.__mascara,
            desloc_x=0,
            desloc_y=1,
            tipo=Plataforma,
        )
        if colidiu:
            self.__veloc_queda = -self.__tamanho_pulo

    def move_direita(self) -> None:
        y_atual = self.__rect.centery
        novo_x = self.__rect.centerx + self.__veloc_corrida
        self.posicao_centro = (novo_x, y_atual)
        self.__virado_direita = True

    def move_esquerda(self) -> None:
        y_atual = self.__rect.centery
        novo_x = self.__rect.centerx - self.__veloc_corrida
        self.posicao_centro = (novo_x, y_atual)
        self.__virado_direita = False

    def aterrissar(self) -> None:
        self.__veloc_queda = self.__veloc_queda_min
    
    def animar(self) -> None:
        self.__indice_imagem = (self.__indice_imagem + 0.1) % 4
        self.__imagem = pygame.image.load(
            f"versao_final/styles/assets/sprites_jogador/parado{int(self.__indice_imagem)}.png"
        ).convert_alpha()
        if not self.__virado_direita:
            self.__imagem = pygame.transform.flip(self.__imagem, flip_x=True, flip_y=False)

        self.__imagem = pygame.transform.scale_by(self.__imagem, 3)
        self.__mascara = pygame.mask.from_surface(self.__imagem)

    @property
    def imagem(self) -> pygame.Surface:
        return self.__imagem

    @property
    def posicao_centro(self) -> tuple:
        return self.__posicao

    @property
    def rect(self) -> pygame.Rect:
        return self.__rect

    @property
    def posicao_centro(self) -> tuple:
        return self.__posicao

    @posicao_centro.setter
    def posicao_centro(self, nova_posicao: tuple) -> None:
        """O setter da posição verifica duas coisas: se o jogador está
        tentando ultrapassar as laterais, ou se ele está tentando atravessar
        o topo. Ambos os casos são impedidos."""

        if (nova_posicao[0] >= self.__largura / 2) and (
            nova_posicao[0] <= (self.__constantes.largura_tela - self.__largura / 2)
        ):
            if nova_posicao[1] >= self.__altura / 2:
                self.__posicao = nova_posicao
                self.__rect.center = nova_posicao

            else:
                self.__veloc_queda = 0
