from math import factorial

import pygame
from pygame import Surface, Rect

from code.constants import WINDOW_WIDTH
from code.entity import Entity
from code.player_shot import PlayerShot
from code.settings import INITIAL_SPEED, SHOT_DELAY, INITIAL_HEALTH, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, \
    PLAYER_KEY_SHOOT, SPRITE_FILE, SPRITE_SCALE_FACTOR


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.surface: Surface = pygame.transform.scale_by(surface=pygame.image.load(SPRITE_FILE[self.name]), factor=SPRITE_SCALE_FACTOR).convert_alpha()
        self.rect: Rect = self.surface.get_rect(left=self.position[0], bottom=self.position[1])
        self.shot_delay: int = SHOT_DELAY[self.name]
        self.speed: int = INITIAL_SPEED[self.name]
        self.health: int = INITIAL_HEALTH[self.name]

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= self.speed
        if pressed_keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WINDOW_WIDTH:
            self.rect.centerx += self.speed

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = SHOT_DELAY[self.name]
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        return None

