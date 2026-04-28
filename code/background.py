import decimal

import pygame
from pygame import Surface, Rect

from code.constants import WINDOW_WIDTH, WINDOW_HEIGHT
from code.entity import Entity
from code.settings import BACKGROUND_FILE


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.surface: Surface = pygame.image.load(BACKGROUND_FILE[name]).convert_alpha()
        self.rect: Rect = self.surface.get_rect(left=self.position[0], top=self.position[1])

    def move(self, speed: int):
        self.speed = speed
        self.rect.centerx -= self.speed
        if self.rect.right <= 0:
            self.rect.left = WINDOW_WIDTH
