from abc import ABC, abstractclassmethod
import pygame

class Item(ABC):

    def __init__(self):
        super().__init__()
        self.__is_visible = True

    @abstractclassmethod
    def efeito(self):
        pass

    @abstractclassmethod
    def update(self):
        pass

    @abstractclassmethod
    def animar(self):
        pass
    
    def handle_collide(self):
        self.__is_visible = False

    @property
    def is_visible(self) -> bool:
        return self.__is_visible
        
 

