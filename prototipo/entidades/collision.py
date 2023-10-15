import pygame


class CollisionManager: # USANDO O DESIGN PATTERN OBSERVER (FAZ PARTE DO CONTEÚDO)
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_collisions(self, objeto):
        for observer in self.observers:
            if observer != objeto:
                # if objeto.rect.colliderect(observer.rect):
                    # observer.handle_collision(objeto)
                print(observer.rect.y)
                print(objeto.rect.y)
