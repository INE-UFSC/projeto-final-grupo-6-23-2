import pygame
from abc import ABC, abstractmethod
from entidades.detector_colisao import DetectorColisao
from entidades.entidades_cenario.plataforma import Plataforma
from entidades.entidades_cenario.lava import Lava
from entidades.entidades_cenario.inimigo import Inimigo
from entidades.entidades_cenario.itens.item import Item
from entidades.entidades_cenario.itens.powerup import PowerUp



class EstadoJogador(ABC):
    """Esta classe é a classe abstrata que será herdada pelos
    estados do jogador. Ela possui métodos para gerenciar a
    lógica do jogador."""

    def __init__(self, jogador, configuracoes):
        self._jogador = jogador
        self._configuracoes = configuracoes
        self._indice_imagem = 0

    def entrar_estado(self, estado_atual: str):
        self.animar()
        self._prox_estado = estado_atual

    def animar(self) -> None:
        """Esse método acessa a próxima imagem da sequência de imagens
        correspondentes à animação do estado, levando em conta, é claro, se
        o jogador está virado para a direita ou para a esquerda."""

        self._indice_imagem = (self._indice_imagem +
                               0.1) % (self._total_imagens)
        imagem = pygame.image.load(
            f"versao_final/styles/assets/sprites_jogador/{self._nome_estado}{int(self._indice_imagem)}.png"
        ).convert_alpha()
        self._imagem = pygame.transform.scale_by(imagem, factor=3)
        if not self._jogador.virado_direita:
            self._imagem = pygame.transform.flip(
                self._imagem, flip_x=True, flip_y=False
            )

    def move_direita(self) -> None:
        y_atual = self._jogador.posicao_centro[1]
        novo_x = self._jogador.posicao_centro[0] + self._jogador.veloc_corrida
        self._jogador.posicao_centro = (novo_x, y_atual)
        self._jogador.virado_direita = True

    def move_esquerda(self) -> None:
        y_atual = self._jogador.posicao_centro[1]
        novo_x = self._jogador.posicao_centro[0] - self._jogador.veloc_corrida
        self._jogador.posicao_centro = (novo_x, y_atual)
        self._jogador.virado_direita = False

    def aplicar_gravidade(
        self, detector_colisao: DetectorColisao, veloc_cenario: float
    ):
        """Esse método cuida da movimentação horizontal do jogador. Caso ele tenha colidido
        com a lava, o jogo acaba. Depois, verificamos se ele está subindo, isto é,
        se self._jogador.veloc_queda < 0, bastando apenas subi-lo nessa situação. Por fim,
        se estiver descendo, precisamos saber se colidiu com alguma plataforma no caminho."""

        colidiu_lava, _ = detector_colisao.detectar_colisao(
            rect=self._jogador.rect,
            mascara=self._mascara,
            desloc_x=0,
            desloc_y=1,
            tipo=Lava,
        )
        if colidiu_lava:
            pygame.quit()
            exit()

        self._jogador.veloc_queda_min = veloc_cenario
        self._jogador.veloc_queda += self._configuracoes.gravidade_jogo

        if self._jogador.veloc_queda < 0:
            self._jogador.posicao_centro = (
                self._jogador.posicao_centro[0],
                self._jogador.posicao_centro[1] + self._jogador.veloc_queda,
            )
            return
        else:
            deslocamento = self.__calcula_queda(detector_colisao)
            self._jogador.posicao_centro = (
                self._jogador.posicao_centro[0],
                self._jogador.posicao_centro[1] + deslocamento,
            )

    def __calcula_queda(self, detector_colisao: DetectorColisao) -> int:
        """Esse método determina a quantidade que o jogador vai descer (dy). Quando
        houver uma plataforma no caminho do jogador, ele não irá realizar todo o
        deslocamento previsto para aquele instante, e sim somente o necessário para
        que ele fique exatamente no topo da plataforma (1 pixel acima)."""

        dy = 0
        while dy < self._jogador.veloc_queda:
            dy += 1
            colidiu, _ = detector_colisao.detectar_colisao(
                rect=self._jogador.rect,
                mascara=self._mascara,
                desloc_x=0,
                desloc_y=dy,
                tipo=Plataforma,
            )
            if colidiu:
                self.aterrissar()
                return dy - 1
        return dy

    def colide_inimigos(self, detector_colisao: DetectorColisao):
        """Se, na posição atual do jogador (por isso desloc_x=0 e
        desloc_y=0), houver um inimigo, ele forçosamente irá para o
        estado 'machucado'."""

        colidiu, _ = detector_colisao.detectar_colisao(
            rect=self._jogador.rect,
            mascara=self._mascara,
            desloc_x=0,
            desloc_y=0,
            tipo=Inimigo,
        )
        if colidiu:
            self._prox_estado = "machucado"
    
    def colide_item(self, detector_colisao: DetectorColisao):
        
        colidiu, objeto = detector_colisao.detectar_colisao(
            rect=self._jogador.rect,
            mascara=self._mascara,
            desloc_x=0,
            desloc_y=0,
            tipo=Item,
        )

        if colidiu:
            if isinstance(objeto, PowerUp):
                self._jogador.add_powerup(objeto.__class__.__name__)
            objeto.efeito()
            objeto.handle_collide()

    def aterrissar(self):
        """Ao aterrissar, a velocidade do jogador é igualada
        à velocidade de queda mínima (velocidade com que as plataformas
        estão descendo)."""

        self._jogador.veloc_queda = self._jogador.veloc_queda_min

    @abstractmethod
    def andar_jogador(self, keys) -> None:
        pass

    @abstractmethod
    def pular(self, detector_colisao: DetectorColisao) -> None:
        pass

    @property
    def imagem(self):
        return self._imagem

    @property
    def mascara(self):
        return self._mascara

    @property
    def nome_estado(self):
        return self._nome_estado

    @property
    def prox_estado(self):
        return self._prox_estado
