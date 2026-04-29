import pygame
from pygame import Surface, Rect
from code.entity import Entity
from code.settings import INITIAL_SPEED, INITIAL_HEALTH, INITIAL_DAMAGE, SPRITE_FILE


class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple, player_shooter: Entity):
        super().__init__(name, position)

        self.surface: Surface = pygame.image.load(SPRITE_FILE[self.name]).convert_alpha()
        self.rect: Rect = self.surface.get_rect(left=self.position[0], top=self.position[1])
        self.player_shooter = player_shooter

        self.speed: int = INITIAL_SPEED[self.name]
        self.health: int = INITIAL_HEALTH[self.name]
        self.damage: int = INITIAL_DAMAGE[self.name]

    def move(self):
        self.rect.centery -= self.speed
