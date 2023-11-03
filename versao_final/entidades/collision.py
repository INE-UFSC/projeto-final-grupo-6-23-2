import pygame

from entidades.plataforma import Plataforma


class CollisionManager: # USANDO O DESIGN PATTERN OBSERVER
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_collisions(self, objeto):
        for observer in self.observers:
            if observer != objeto:
                if isinstance(objeto, pygame.sprite.Group):
                    for sprite in objeto:
                        if sprite.rect.colliderect(observer.rect):
                            return observer.handle_collision(sprite)
                else:
                    if objeto.rect.colliderect(observer.rect):
                        return observer.handle_collision(objeto)
                    
        return None
