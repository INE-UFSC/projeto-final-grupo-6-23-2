import pygame
from constantes import constantes


class Jogador:

    def __init__(self):
        self.__superficie = pygame.Surface((100, 100))
        self.__superficie.fill('Blue')
        self.__posicao = (constantes.LARGURA_TELA / 2, 200)
    
    def aplica_gravidade(self, gravidade: int) -> None:
        x_atual = self.__posicao[0]
        novo_y = self.__posicao[1] + gravidade
        self.__posicao = (x_atual, novo_y)

    @property
    def superficie(self) -> pygame.Surface:
        return self.__superficie
    
    @property
    def posicao(self) -> tuple:
        return self.__posicao
    
    
