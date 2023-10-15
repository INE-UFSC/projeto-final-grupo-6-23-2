import pygame
from constantes.constantes import constantes


class Jogador:
    """Classe responsável pelo jogador"""

    def __init__(self):

        self.__superficie = pygame.Surface((100, 100))
        self.__superficie.fill('Blue')

        self.__posicao = (constantes.largura_tela / 2, 200)
        self.__colidiu = False

        self.__velocidade = 1
        self.__velocidade_queda = 0
        self.__tamanho_pulo = 3

    def aplica_gravidade(self, gravidade: int) -> None:
        """Caso o jogador não esteja sob uma plataforma, essa função
        irá faze-lo cair com uma certa aceleração"""

        if not self.__colidiu:
            self.__velocidade_queda += gravidade
            x_atual = self.__posicao[0]
            novo_y = self.__posicao[1] + self.__velocidade_queda

            self.__posicao = (x_atual, novo_y)

    def pular(self):
        if self.__colidiu:
            self.__velocidade_queda -= self.__tamanho_pulo
    
    def move_direita(self):
        y_atual = self.__posicao[1]
        novo_x = self.__posicao[0] + self.__velocidade

    def move_esquerda(self):
        y_atual = self.__posicao[1]
        novo_x = self.__posicao[0] - self.__velocidade

    def aterrissar(self):
        self.__velocidade_queda = 0
        self.__colidiu = True

    def cair(self):
        self.__colidiu = False

    @property
    def superficie(self) -> pygame.Surface:
        return self.__superficie
    
    @property
    def posicao(self) -> tuple:
        return self.__posicao
