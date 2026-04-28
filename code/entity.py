from abc import ABC, abstractmethod

from pygame import Surface, Rect

from code.settings import INITIAL_HEALTH, INITIAL_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.position = position

        self.surface: Surface | None = None
        self.rect: Rect | None = None
        self.speed: int = 0
        self.health: int = INITIAL_HEALTH['Entity']
        self.damage: int = 0
        self.score: int = INITIAL_SCORE['Entity']

        @abstractmethod
        def move():
            pass
