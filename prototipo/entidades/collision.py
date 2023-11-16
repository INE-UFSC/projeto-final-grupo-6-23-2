import pygame


class CollisionManager: # USANDO O DESIGN PATTERN OBSERVER
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_collisions(self, objeto, group=False):
        for observer in self.observers:
            if observer != objeto:
                if group:
                    if pygame.sprite.groupcollide(objeto, [observer], False, False):
                        return observer.handle_collision(objeto)
                else:
                    if objeto.rect.colliderect(observer.rect):
                        return observer.handle_collision(objeto)
                    
        return None
