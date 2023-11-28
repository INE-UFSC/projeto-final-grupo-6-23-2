import pygame
import sys
from entidades.detector_colisao import DetectorColisao
from entidades.arquivos_jogador.estado_parado import EstadoParado
from entidades.arquivos_jogador.estado_andando import EstadoAndando
from entidades.arquivos_jogador.estado_pulo import EstadoPulo
from entidades.arquivos_jogador.estado_machucado import EstadoMachucado
from configuracoes.configuracoes import Configuracoes


class Jogador:
    """O jogador vai ser ser o objeto (dinossauro) que se movimenta na tela, e
    que será controlado pelas teclas, de modo a evitar que caia na lava. O jogador
    também possui estados (parado, andando, pulando e machucado), que determinam a lógica de
    funcionamento do jogador (movimentação, animação, etc) e o próximo estado."""

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
            "machucado": EstadoMachucado(self, configuracoes),
        }
        self.__virado_direita = True
        self.__estado_atual = self.__estados["parado"]
        self.__estado_atual.entrar_estado()

        self.__veloc_corrida = configuracoes.jogador_veloc_base
        self.__tamanho_pulo = configuracoes.jogador_pulo_base
        self.__veloc_queda = 0
        self.__veloc_queda_min = configuracoes.cenario_veloc_base

    def atualizar_jogador(
        self, detector_colisao: DetectorColisao, veloc_cenario: float
    ):
        """A cada ciclo do loop principal, é preciso atualizar o jogador, aplicando a
        gravidade do jogo, verificando a colisão com inimigos, animando a sua sprite
        e atualizando o estado atual."""

        self.__estado_atual.aplicar_gravidade(
            detector_colisao=detector_colisao, veloc_cenario=veloc_cenario
        )
        self.__estado_atual.colide_inimigos(detector_colisao=detector_colisao)
        self.__estado_atual.animar()

    def andar_jogador(self, keys):
        self.__estado_atual.andar_jogador(keys)

    def pular(self, detector_colisao: DetectorColisao) -> None:
        self.__estado_atual.pular(detector_colisao=detector_colisao)

    def trocar_estado(self, estado):
        """Método chamado por cada estado para alterar o
        estado atual do jogador."""

        self.__estado_atual = self.__estados[estado]
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

    @veloc_queda_min.setter
    def veloc_queda_min(self, veloc_queda_min) -> None:
        self.__veloc_queda_min = veloc_queda_min

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
