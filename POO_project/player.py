from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self):
        self.kart = None

    @abstractmethod
    def move(self, string):
        pass
