import pygame


class Checkpoint():  # Vous pouvez ajouter des classes parentes
    
    def __init__(self, x, y, checkpoint_id):
        self.x = x
        self.y = y
        self.checkpoint_id = checkpoint_id

    def draw(self, screen):
        pygame.draw.rect(screen, [128, 128, 128], pygame.Rect(self.x, self.y, 50, 50))