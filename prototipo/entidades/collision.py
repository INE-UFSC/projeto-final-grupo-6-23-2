import pygame


class CollisionManager: # USANDO O DESIGN PATTERN OBSERVER
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_collisions(self, *objetos):
        for observer in self.observers:
            for objeto in objetos:
                if observer != objeto:
                    if objeto.rect.colliderect(observer.rect):
                        return observer.handle_collision(objeto)
                    
        return None
