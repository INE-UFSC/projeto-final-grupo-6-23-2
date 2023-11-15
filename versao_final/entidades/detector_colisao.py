from entidades.plataforma import Plataforma
import pygame


class DetectorColisao:
    def __init__(self):
        self.__objetos = []

    def adicionar_objeto(self, objeto):
        self.__objetos.append(objeto)

    def detectar_colisao(self, rect, desloc_x, desloc_y, tipo):
        colidiu = False
        rect.centerx += desloc_x
        rect.centery += desloc_y

        for objeto in self.__objetos:
            if isinstance(objeto, tipo) and rect.colliderect(objeto.rect):
                if (tipo == Plataforma):
                    if int(rect.bottom) <= int(objeto.rect.top) + 1:
                        colidiu = True
                else:
                    colidiu = True
        
        rect.centerx -= desloc_x
        rect.centery -= desloc_y
        return colidiu
