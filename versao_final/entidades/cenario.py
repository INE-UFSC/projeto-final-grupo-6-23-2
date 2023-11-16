import random
from entidades.lava import Lava
from entidades.plataforma import Plataforma
from pygame import Surface


class Cenario:
    def __init__(self, constantes):
        self.__constantes = constantes
        self.__lava = Lava()

        self.__plataforma_refenc = Plataforma(
            (self.__constantes.largura_tela / 2, 500))
        self.__plataformas = [self.__plataforma_refenc]
        for _ in range(20):
            self.gerar_plataforma()

        self.__veloc_cenario = self.__constantes.cenario_veloc_base
        self.__aceleracao = self.__constantes.aceleracao_cenario

    def gerar_plataforma(self):
        plataforma_y = self.__plataforma_refenc.rect.y - 100
        intervalo_x = range(
            max(0, self.__plataforma_refenc.rect.centerx - 300),
            min(self.__constantes.largura_tela - self.__plataforma_refenc.largura,
                self.__plataforma_refenc.rect.x + 300),
        )
        plataforma_x = random.choice(intervalo_x)
        self.__plataforma_refenc = Plataforma((plataforma_x, plataforma_y))
        self.__plataformas.append(self.__plataforma_refenc)
    
    def movimentar_cenario(self, detector_colisao):
        for indice in range(len(self.__plataformas)):
            if self.__plataformas[indice].rect.y >= self.__constantes.altura_tela:
                self.eliminar_plataforma(indice, detector_colisao)
                break
            self.__plataformas[indice].rect.y += self.__veloc_cenario

        self.__veloc_cenario += self.__aceleracao

    def eliminar_plataforma(self, indice, detector_colisao):
        self.__plataformas.pop(indice)
        detector_colisao.remover_objeto(self.__plataformas[indice])
        self.gerar_plataforma()
        detector_colisao.adicionar_objeto(self.__plataforma_refenc)

    @property
    def lava(self):
        return self.__lava

    @property
    def plataformas(self):
        return self.__plataformas
    
    @property
    def veloc_cenario(self):
        return self.__veloc_cenario
