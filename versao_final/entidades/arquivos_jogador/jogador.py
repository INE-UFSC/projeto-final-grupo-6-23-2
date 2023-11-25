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
    """O jogador vai ser ser o objeto (dinossauro) que se movimenta na tela, e
    que será controlado pelas teclas, de modo a evitar que caia na lava. O jogador
    também possui estados, que transicionam com base nos botões de movimento e na
    colisão com as plataformas. Esses estados também determinam a sua animação."""

    def __init__(self, configuracoes: Configuracoes):
        self.__configuracoes = configuracoes
        self.__largura = configuracoes.tamanho_jogador[0]
        self.__altura = configuracoes.tamanho_jogador[1]
        superficie_rect = pygame.Surface(configuracoes.tamanho_jogador)
        self.__rect = superficie_rect.get_rect(
            center=configuracoes.jogador_pos_inicial)

        self.__estados = {
            "parado": EstadoParado(self, configuracoes),
            "andando": EstadoAndando(self, configuracoes),
            "pulo": EstadoPulo(self, configuracoes),
        }
        self.__virado_direita = True
        self.__estado_atual = self.__estados["parado"]
        self.__estado_atual.entrar_estado()

        self.__veloc_corrida = configuracoes.jogador_veloc_base
        self.__tamanho_pulo = configuracoes.jogador_pulo_base
        self.__veloc_queda = 0

    def atualizar_jogador(
        self, detector_colisao: DetectorColisao, veloc_cenario: float
    ):
        self.__aplica_gravidade(detector_colisao, veloc_cenario)
        self.__atualizar_estado()

    def andar_jogador(self, keys):
        self.__estado_atual.andar_jogador(keys)

    def pular(self, detector_colisao: DetectorColisao) -> None:
        """O método só deixa o jogador pular se ele estiver imediatamente
        acima de uma plataforma, o que é verificado pelo detector_colisao."""

        self.__estado_atual.pular(detector_colisao)

    def __aterrissar(self) -> None:
        self.__estado_atual.aterrissar()

    def __aplica_gravidade(
        self, detector_colisao: DetectorColisao, veloc_cenario: float
    ):
        """Esse método cuida da movimentação horizontal do jogador. Caso ele esteja subindo
        (self.__veloc_queda < 0), basta deslocá-lo. Caso contrário, é preciso fazer uma
        verificação, a fim de saber se ele colidiu com a lava (fim de jogo) ou com uma
        plataforma (aterrissar)."""

        colidiu_lava = detector_colisao.detectar_colisao(
            rect=self.__rect,
            mascara=self.__estado_atual.mascara,
            desloc_x=0,
            desloc_y=1,
            tipo=Lava,
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
                self.__aterrissar()
                return dy - 1
        return dy

    def __atualizar_estado(self):
        """Esse método atualiza o estado atual, transicionando caso seja
        necessário."""

        self.__estado_atual.animar()
        if self.__estado_atual != self.__estados[self.__estado_atual.prox_estado]:
            self.__estado_atual = self.__estados[self.__estado_atual.prox_estado]
            self.__estado_atual.entrar_estado()

    @property
    def imagem(self) -> pygame.Surface:
        return self.__estado_atual.imagem

    @property
    def virado_direita(self) -> bool:
        return self.__virado_direita

    @virado_direita.setter
    def virado_direita(self, virado_direita: bool) -> None:
        self.__virado_direita = virado_direita

    @property
    def rect(self) -> pygame.Rect:
        return self.__rect

    @property
    def tamanho_pulo(self) -> float:
        return self.__tamanho_pulo

    @property
    def veloc_corrida(self) -> float:
        return self.__veloc_corrida

    @property
    def veloc_queda(self) -> float:
        return self.__veloc_queda

    @property
    def veloc_queda_min(self) -> float:
        return self.__veloc_queda_min

    @veloc_queda.setter
    def veloc_queda(self, veloc_queda: float) -> None:
        self.__veloc_queda = veloc_queda

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
