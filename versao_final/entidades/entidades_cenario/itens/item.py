from abc import ABC, abstractclassmethod
import pygame

class Item(ABC):

    def __init__(self):
        super().__init__()

    @abstractclassmethod
    def efeito(self):
        pass

    @abstractclassmethod
    def get_powerup(self):
        pass

    @abstractclassmethod
    def update(self):
        pass

    @abstractclassmethod
    def animar(self):
        pass

 

