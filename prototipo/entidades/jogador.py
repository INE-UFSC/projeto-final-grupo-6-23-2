import pygame
from constantes.constantes import constantes
from entidades.lava import Lava
from entidades.plataforma import Plataforma


class Jogador:
    """Classe responsável pelo jogador"""

    def __init__(self):

        self.__tamanho_jogador = (50,50)
        self.__superficie = pygame.Surface(self.__tamanho_jogador)
        self.__superficie.fill('Blue')

        self.__posicao = (constantes.largura_tela / 2, 0)
        self.__colidiu = False

        self.__velocidade = 2
        self.__velocidade_queda = 0
        self.__tamanho_pulo = 3

    def aplica_gravidade(self, gravidade: int) -> None:
        """Caso o jogador não esteja sob uma plataforma, essa função
        irá faze-lo cair com uma certa aceleração"""

        if not self.__colidiu:
            self.__velocidade_queda += gravidade
            x_atual = self.posicao[0]
            novo_y = self.posicao[1] + self.__velocidade_queda

            self.posicao = (x_atual, novo_y)

    def pular(self):
        if self.__colidiu:
            self.__velocidade_queda -= self.__tamanho_pulo
    
    def move_direita(self):
        y_atual = self.posicao[1]
        novo_x = self.posicao[0] + self.__velocidade
        self.posicao = (novo_x, y_atual)

    def move_esquerda(self):
        y_atual = self.posicao[1]
        novo_x = self.posicao[0] - self.__velocidade
        self.posicao = (novo_x, y_atual)


    def aterrissar(self):
        self.__velocidade_queda = 0
        self.__colidiu = True

    def cair(self):
        self.__colidiu = False

    def handle_collision(self, objeto):
        if isinstance(objeto, Lava):
            print("Colidiu com a lava")
        if isinstance(objeto, Plataforma):
            self.aterrissar()

    @property
    def superficie(self) -> pygame.Surface:
        return self.__superficie
    
    @property
    def posicao(self) -> tuple:
        return self.__posicao
    
    @property
    def rect(self):
        return self.superficie.get_rect()
    
    @posicao.setter
    def posicao(self, nova_posicao):
        if (nova_posicao[0] >= 0) and (nova_posicao[0] <= (constantes.largura_tela - self.__tamanho_jogador[0])):
            if (nova_posicao[1] >= 0) and (nova_posicao[1] <= constantes.altura_tela):
                self.__posicao = nova_posicao
                self.rect.x = nova_posicao[0]
                self.rect.y = nova_posicao[1]
            else:
                self.__velocidade_queda = 0

