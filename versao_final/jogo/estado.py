from abc import ABC, abstractmethod


class Estado(ABC):
    """O estado gerencia os componentes e a lógica da tela atual do
    jogo (são três: a do menu, a do jogo em si e a de game over)."""

    def __init__(self, jogo, configuracoes, estado_atual):
        self._refer_jogo = jogo
        self._configuracoes = configuracoes
        self._nome_estado = estado_atual
        self._prox_estado = estado_atual

    @abstractmethod
    def entrar_estado(self):
        pass

    @abstractmethod
    def atualizar_estado(self, eventos, tela):
        pass

    @property
    def nome_estado(self):
        return self._nome_estado

    @property
    def prox_estado(self):
        return self._prox_estado
