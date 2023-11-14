import pygame
from entidades.detector_colisao import DetectorColisao
from entidades.plataforma import Plataforma


class Jogador:

    def __init__(self, constantes):
        self.__constantes = constantes
        self.__superficie = pygame.Surface((50, 50))
        self.__superficie.fill('Blue')

        self.__colidiu = False
    
        self.__velocidade = self.__constantes.jogador_veloc_base
        self.__tamanho_pulo = self.__constantes.jogador_pulo_base
        self.__velocidade_queda = 0

        self.__posicao = (self.__constantes.largura_tela / 2, 200)
        self.__rect = self.__superficie.get_rect(center=self.__posicao)

    def aplica_gravidade(self, detector_colisao) -> None:
        self.__velocidade_queda += self.__constantes.gravidade_jogo
        print (self.__velocidade_queda)

        if self.__velocidade_queda < 0:
            self.__rect.centery += self.__velocidade_queda
            return
        else:
            dy = 0
            while dy < self.__velocidade_queda:
                colidiu = detector_colisao.detectar_colisao(
                    self.__rect, 0, dy, Plataforma
                )
                if colidiu:
                    self.aterrissar()
                    return
                dy += 1
            
            print(self.__velocidade_queda)
            self.__rect.centery += dy - 1

    def pular(self):
        if self.__colidiu:
            self.__velocidade_queda -= self.__tamanho_pulo
            self.__colidiu = False
    
    def move_direita(self):
        y_atual = self.__rect.centery
        novo_x = self.__rect.centerx + self.__velocidade
        self.__rect.center = (novo_x, y_atual)

    def move_esquerda(self):
        y_atual = self.__rect.centery
        novo_x = self.__rect.centerx - self.__velocidade
        self.__rect.center = (novo_x, y_atual)

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

    @property
    def rect(self):
        return self.__rect
