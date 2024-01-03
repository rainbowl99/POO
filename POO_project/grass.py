import pygame


class Grass():  # Vous pouvez ajouter des classes parentes

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, [0,255,0], pygame.Rect(self.x, self.y, 50, 50))
