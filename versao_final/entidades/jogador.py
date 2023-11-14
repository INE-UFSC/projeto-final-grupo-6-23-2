import pygame
from constantes.constantes import Constantes
from entidades.lava import Lava
from entidades.tiles_package import Tile


class Jogador(pygame.sprite.Sprite):
    """Classe responsável pelo jogador"""

    def __init__(self, velocidade_descida):
        super().__init__()

        self.__constantes = Constantes()
        self.__imagem_parado = pygame.image.load("versao_final/styles/assets/parado.png").convert_alpha()
        self.__imagem_correndo = pygame.image.load("versao_final/styles/assets/correndo.png").convert_alpha()
        self.__image = self.__imagem_parado
        self.__rect = self.__image.get_rect()

        self.__virado_direita = False
        self.__moving = False

        self.__posicao = (self.__constantes.largura_tela / 2, 0)
        self.__colidiu = False

        self.__velocidade = 3 # Para deslocamento horizontal
        self.__velocidade_queda = 0 # Velocidade de queda atual
        self.__velocidade_descida = velocidade_descida # Velocidade de queda mínima
        self.__tamanho_pulo = 10
    
    def atualizar(self):
        if self.__moving:
            if not self.__virado_direita:
                self.__image = pygame.transform.flip(surface=self.__imagem_correndo, flip_x=True, flip_y=False)
                
            else:
                self.__image = self.__imagem_correndo
            self.__moving = False
            return

        if not self.__virado_direita:
            self.__image = pygame.transform.flip(surface=self.__imagem_parado, flip_x=True, flip_y=False)
            return
        else:
            self.__image = self.__imagem_parado
            return

    def aplica_gravidade(self, gravidade, velocidade_descida) -> None:
        """Caso o jogador não esteja sob uma plataforma, essa função
        irá faze-lo cair com uma certa aceleração"""

        self.__velocidade_descida = velocidade_descida

        if not self.__colidiu:
            self.__velocidade_queda += gravidade
            x_atual = self.posicao[0]
            novo_y = self.posicao[1] + self.__velocidade_queda
            self.posicao = (x_atual, novo_y)
        
        else:
            x_atual = self.posicao[0]
            novo_y = self.posicao[1] + self.__velocidade_queda
            self.posicao = (x_atual, novo_y)
            self.__colidiu = False

    def pular(self):
        if self.__colidiu:
            self.__velocidade_queda -= self.__tamanho_pulo
            self.__colidiu = False
    
    def move_direita(self):
        self.__virado_direita = True
        self.__moving = True
        y_atual = self.posicao[1]
        novo_x = self.posicao[0] + self.__velocidade
        self.posicao = (novo_x, y_atual)

    def move_esquerda(self):
        self.__virado_direita = False
        self.__moving = True
        y_atual = self.posicao[1]
        novo_x = self.posicao[0] - self.__velocidade
        self.posicao = (novo_x, y_atual)

    def aterrissar(self):
        self.__velocidade_queda = self.__velocidade_descida
        self.__colidiu = True

    def cair(self):
        self.__colidiu = False

    def handle_collision(self, objeto):
        if isinstance(objeto, Lava):
            return 'kill'
        if isinstance(objeto, Tile) and self.__velocidade_queda > 0:
            """Verifica se a parte de baixo do jogador colide com o topo do tile (a não ser por um desvio máximo)"""
            DESVIO = 20 
            if abs(objeto.rect.top - self.rect.bottom) in range(DESVIO): 
                if objeto.solido:
                    self.aterrissar()

    @property
    def superficie(self) -> pygame.Surface:
        return self.__image
    
    @property
    def posicao(self) -> tuple:
        return self.__posicao
    
    @property
    def rect(self):
        return self.__rect
    
    @posicao.setter
    def posicao(self, nova_posicao):
        if (nova_posicao[0] >= 0) and (nova_posicao[0] <= (self.__constantes.largura_tela - 50)):
            if (nova_posicao[1] >= 0) and (nova_posicao[1] <= self.__constantes.altura_tela):
                self.__posicao = nova_posicao
                self.__rect.x = nova_posicao[0]
                self.__rect.y = nova_posicao[1]
            else:
                self.__velocidade_queda = 0

