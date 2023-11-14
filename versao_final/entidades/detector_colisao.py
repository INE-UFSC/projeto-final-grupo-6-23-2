from entidades.plataforma import Plataforma


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
                    print(f'Jogador: {rect.midbottom[1]}, plataforma: {objeto.rect.midtop[1]}')
                    if int(rect.midbottom[1] - 1) <= int(objeto.rect.midtop[1]):
                        colidiu = True
                else:
                    colidiu = True
        
        rect.centerx -= desloc_x
        rect.centery -= desloc_y
        return colidiu
