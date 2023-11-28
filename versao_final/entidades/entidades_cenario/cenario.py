import random
from entidades.entidades_cenario.lava import Lava
from entidades.entidades_cenario.plataforma import Plataforma
from entidades.entidades_cenario.paisagem import Paisagem
from entidades.entidades_cenario.inimigo import Inimigo
from entidades.detector_colisao import DetectorColisao
from entidades.entidades_cenario.itens.moeda import Moeda
from entidades.entidades_cenario.itens.duplo_pulo import DuploPulo


class Cenario:
    def __init__(self, constantes, detector_colisao: DetectorColisao):
        """Essa classe será responsável pelos objetos que serão desenhados
        na tela do jogo (plataformas, lava, inimigos). Ao iniciar o jogo, um
        número pré-determinado de plataformas é gerado na tela. Note queesses
        objetos movem-se de forma descendente e acelerada."""

        self.__deslocamento = 1
        self.__constantes = constantes
        self.__lava = Lava()
        self.__paisagem = Paisagem()

        self.__inimigos = []
        self.__itens = []

        self.__detector_colisao = detector_colisao

        self.__plataforma_refenc = Plataforma(
            (self.__constantes.largura_tela / 2, 500))
        self.__plataformas = [self.__plataforma_refenc]
        for _ in range(20):
            self.gerar_plataforma()

        self.__veloc_cenario = self.__constantes.cenario_veloc_base
        self.__aceleracao = self.__constantes.aceleracao_cenario


    def gerar_plataforma(self):
        """Essa função gera uma plataforma aleatória, tendo como base uma plataforma
        de referência, que é sempre a última paltaforma a ser gerada. Sua distância
        vertical, bem como a horizontal em relação à plataforma de referência é aleatória
        (função random.choice()). No entanto, precisamos levar em consideração a largura
        da tela, para que não seja gerada uma plataforma fora das bordas do display.
        Posteriormente, essa plataforma é acrescida à lista de plataformas."""

        intervalo_y = range(
            self.__plataforma_refenc.rect.y - 125, self.__plataforma_refenc.rect.y - 100
        )
        plataforma_y = random.choice(intervalo_y)
        intervalo_x = range(
            max(0, self.__plataforma_refenc.rect.centerx - 300),
            min(
                self.__constantes.largura_tela - self.__plataforma_refenc.largura,
                self.__plataforma_refenc.rect.x + 300,
            ),
        )
        plataforma_x = random.choice(intervalo_x)
        self.__plataforma_refenc = Plataforma((plataforma_x, plataforma_y))
        self.__plataformas.append(self.__plataforma_refenc)
        self.__deslocamento += 1

        
        self.gerar_moeda(plataforma_x + int(self.__plataforma_refenc.rect.width/2), plataforma_y - 55)

    def movimentar_cenario(self):
        """Com esse método, é possível movimentar todas as plataformas de
        uma só vez. No entanto, se a plataforma atinge o fundo da tela, ela é
        eliminada (método eliminar_plataforma()). Ademais, ele também serve para
        acelerar o cenário."""

        for indice in range(len(self.__plataformas)):
            if self.__plataformas[indice].rect.y >= self.__constantes.altura_tela:
                self.eliminar_plataforma(indice)
            self.__plataformas[indice].rect.y += self.__veloc_cenario 

        for indice in range(len(self.__itens)):
            self.__itens[indice].rect.y += self.__veloc_cenario

        self.__veloc_cenario += self.__aceleracao
        self.lava.animacao()
        self.__paisagem.move(self.__veloc_cenario)




    def eliminar_plataforma(self, indice):
        """Esse método elimina uma plataforma que atingiu o fundo
        da tela, e também remove-a da lista do detector_colisao. Ele
        também chama o gerar_plataforma para repor a plataforma que
        foi eliminada."""

        self.__plataformas.pop(indice)
        self.__detector_colisao.remover_objeto(self.__plataformas[indice])
        self.gerar_plataforma()
        self.__detector_colisao.adicionar_objeto(self.__plataforma_refenc)

    def atualizar_inimigos(self):
        self.gerar_inimigo()
        self.remover_inimigos()

    def gerar_inimigo(self):
        if len(self.__inimigos) <= 3:
            if self.__deslocamento % 6 == 0:
                if random.randint(1, 3) == 1:
                    self.__deslocamento += 1
                    inimigo = Inimigo()
                    self.__inimigos.append(inimigo)
                    self.__detector_colisao.adicionar_objeto(inimigo)

    def remover_inimigos(self):
        copy_inimigos = self.__inimigos.copy()
        for index in range(len(copy_inimigos)):
            inimigo = self.__inimigos[index]
            if (
                inimigo.rect.x >= 508 + 100
                or inimigo.rect.x <= -10 - 100
                or inimigo.rect.y <= -10
                or inimigo.rect.y >= 858
            ):
                self.__detector_colisao.remover_objeto(self.__inimigos[index])
                copy_inimigos.pop(index)

        self.__inimigos = copy_inimigos

    def gerar_moeda(self, x , y):
        if random.randint(1,3) == 1:
            moeda = Moeda(x, y)
            moeda.rect.x -= int(moeda.rect.width/2)
            self.__itens.append(moeda)
            self.__detector_colisao.adicionar_objeto(moeda)


    def gerar_powerups(self):
        if random.randint(1,2) == 1:
            x = random.randint(0,402)
            y = random.randint(0, 500)
            duplopulo = DuploPulo(x, y)
            duplopulo
            self.__itens.append(duplopulo)
            self.__detector_colisao.adicionar_objeto(duplopulo)


    def remover_itens(self):
        copy_itens = self.__itens.copy()
        for index in range(len(copy_itens)):
            moeda = self.__itens[index]
            if not moeda.is_visible:
                copy_itens.pop(index)
                self.__detector_colisao.remover_objeto(self.__itens[index])
                continue
            if moeda.rect.y >= self.__constantes.altura_tela:
                self.__detector_colisao.remover_objeto(self.__itens[index])
                copy_itens.pop(index)

        self.__itens = copy_itens

    def atualizar_itens(self):
        self.remover_itens()

    @property
    def lava(self):
        return self.__lava

    @property
    def plataformas(self):
        return self.__plataformas

    @property
    def veloc_cenario(self):
        return self.__veloc_cenario

    @property
    def paisagem(self):
        return self.__paisagem

    @property
    def inimigos(self):
        return self.__inimigos
    
    @property
    def itens(self):
        return self.__itens