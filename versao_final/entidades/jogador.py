import pygame
import sys
from entidades.detector_colisao import DetectorColisao
from entidades.entidades_cenario.plataforma import Plataforma
from entidades.entidades_cenario.lava import Lava
from entidades.arquivos_jogador.estado_parado import EstadoParado
from entidades.arquivos_jogador.estado_andando import EstadoAndando
from entidades.arquivos_jogador.estado_pulo import EstadoPulo

from configuracoes.configuracoes import Configuracoes


class Jogador:
    """O jogador vai ser ser o objeto que se movimenta na tela, e
    que será controlado pelas teclas, de modo a evitar que caia na lava."""

    def __init__(self, configuracoes: Configuracoes):
        self.__configuracoes = configuracoes
        self.__largura = configuracoes.tamanho_jogador[0]
        self.__altura = configuracoes.tamanho_jogador[1]
        superficie = pygame.Surface(configuracoes.tamanho_jogador)
        self.__rect = superficie.get_rect(center=configuracoes.jogador_pos_inicial)

        self.__estados = {
            'parado': EstadoParado(configuracoes),
            'andando': EstadoAndando(configuracoes),
            'pulo': EstadoPulo(configuracoes),
        }
        self.__virado_direita = True
        self.trocar_estado('parado')

        self.__veloc_corrida = configuracoes.jogador_veloc_base
        self.__tamanho_pulo = configuracoes.jogador_pulo_base
        self.__veloc_queda = 0


    def aplica_gravidade(self, detector_colisao: DetectorColisao, veloc_cenario: float):
        """Esse método cuida da movimentação horizontal do jogador. Caso ele esteja subindo
        (self.__veloc_queda < 0), basta deslocá-lo. Caso contrário, é preciso fazer uma
        verificação, a fim de saber se ele colidiu com a lava (fim de jogo) ou com uma
        plataforma (aterrissar)."""

        colidiu_lava = detector_colisao.detectar_colisao(
            rect=self.__rect, mascara=self.__estado_atual.mascara, desloc_x=0, desloc_y=1, tipo=Lava
        )
        if colidiu_lava:
            pygame.quit()
            sys.exit()

        self.__veloc_queda_min = veloc_cenario
        self.__veloc_queda += self.__configuracoes.gravidade_jogo

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
                mascara=self.__estado_atual.mascara,
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
            mascara=self.__estado_atual.mascara,
            desloc_x=0,
            desloc_y=1,
            tipo=Plataforma,
        )
        if colidiu:
            self.trocar_estado('pulo')
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
        self.trocar_estado('parado')
        self.__veloc_queda = self.__veloc_queda_min

    def trocar_estado(self, estado):
        self.__estado_atual = self.__estados[estado]
        self.__estado_atual.entrar_estado(self.__virado_direita)

    def animar(self) -> None:
        self.__estado_atual.animar(self.__virado_direita)

    @property
    def imagem(self) -> pygame.Surface:
        return self.__estado_atual.imagem

    @property
    def posicao_centro(self) -> tuple:
        return self.__posicao

    @property
    def rect(self) -> pygame.Rect:
        return self.__rect

    @property
    def posicao_centro(self) -> tuple:
        return self.__rect.center

    @posicao_centro.setter
    def posicao_centro(self, nova_posicao: tuple) -> None:
        """O setter da posição verifica duas coisas: se o jogador está
        tentando ultrapassar as laterais, ou se ele está tentando atravessar
        o topo. Ambos os casos são impedidos."""

        if (nova_posicao[0] >= self.__largura / 2) and (
            nova_posicao[0] <= (
                self.__configuracoes.largura_tela - self.__largura / 2)
        ):
            if nova_posicao[1] >= self.__altura / 2:
                self.__rect.center = nova_posicao
            else:
                self.__veloc_queda = 0
