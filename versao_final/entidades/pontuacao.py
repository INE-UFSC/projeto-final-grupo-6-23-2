import pygame
import json

class Pontuacao:

    def __init__(self):
        self.__record = self.carregar_record()
        self.__pontuacao_atual = 0

    def aumenta_pontuacao(self):
        self.__pontuacao_atual += 0.015

    def verificar_pontuacao(self):
        if self.__pontuacao_atual > self.__record:
            self.__record = self.__pontuacao_atual
            self.persistencia()
    
    def pontuacao_bonus(self, bonus : int):
        self.__pontuacao_atual += bonus

    def persistencia(self):
        with open('record.json', 'w') as file:
            json.dump(self.__record, file)
    
    def carregar_record(self):
        try:
            with open('record.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return 0

    def mostrar_pontuacao(self, tela):
        font_path = "versao_final/styles/assets/fonte.ttf"
        font = pygame.font.Font(font_path, 50)
        self.__texto = str(int(self.__pontuacao_atual))
        self.__texto_surface = font.render(self.__texto, True, (255,255,255))
        self.__texto_rect = self.__texto_surface.get_rect()
        tela.blit(self.__texto_surface, self.__texto_rect)

    @property
    def record(self):
        return self.__record

    @record.setter 
    def record(self, novo_record):
        self.__record = novo_record
        self.persistencia()

    @property
    def pontuacao_atual(self):
        return self.__pontuacao_atual
