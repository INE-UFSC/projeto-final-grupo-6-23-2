from entidades.entidades_cenario.plataforma import Plataforma
import pygame


class DetectorColisao:
    """O detector de colisão servirá para testar se um retângulo
    colidiu com algum outro retângulo dentro de uma lista (self.__objetos)."""

    def __init__(self):
        self.__objetos = []

    def adicionar_objeto(self, objeto):
        self.__objetos.append(objeto)

    def remover_objeto(self, objeto):
        self.__objetos.remove(objeto)

    def detectar_colisao(
        self,
        rect: pygame.Rect,
        mascara: pygame.Mask,
        desloc_x: float,
        desloc_y: float,
        tipo: type,
    ):
        """Esse método recebe um retângulo, um deslocamento (x e y) e
        um tipo. Então, ele movimenta esse retângulo com base nos parâmetros
        desloc_x e desloc_y, e verifica se houve colisão com um objeto do tipo
        'tipo', retornando True em caso afirmativo. Se não, retorna False."""

        colidiu = False
        rect.centerx += desloc_x
        rect.centery += desloc_y

        objeto_colidido = None
        for objeto in self.__objetos:
            if isinstance(objeto, tipo) and mascara.overlap(
                objeto.mascara, (objeto.rect.x - rect.x,
                                 objeto.rect.y - rect.y)
            ):
                if tipo == Plataforma:
                    if int(rect.bottom) <= int(objeto.rect.top) + 1:
                        colidiu = True
                        objeto_colidido = objeto

                else:
                    colidiu = True
                    objeto_colidido = objeto

        rect.centerx -= desloc_x
        rect.centery -= desloc_y
        return colidiu, objeto_colidido
