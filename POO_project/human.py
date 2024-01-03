import time
import pygame
from player import Player


class Human(Player):

    def __init__(self):
        super().__init__()

    def move(self, string):
        time.sleep(0.02)
        return pygame.key.get_pressed()
