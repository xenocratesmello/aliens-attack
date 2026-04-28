import pygame
from pygame import Surface, Rect

from code.constants import WINDOW_HEIGHT, WINDOW_WIDTH
from code.enemy_shot import EnemyShot
from code.entity import Entity
from code.settings import SHOT_DELAY, INITIAL_HEALTH, INITIAL_SPEED, SPRITE_SCALE_FACTOR, SPRITE_FILE


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.surface: Surface = pygame.transform.scale_by(surface=pygame.image.load(SPRITE_FILE[self.name]),
                                                          factor=SPRITE_SCALE_FACTOR).convert_alpha()
        self.rect: Rect = self.surface.get_rect(right=self.position[0], top=self.position[1])
        self.shot_delay: int = SHOT_DELAY[self.name]
        self.speed: int = INITIAL_SPEED[self.name]
        self.health: int = INITIAL_HEALTH[self.name]

    def move(self, direction: str):
        match direction:
            case 'left':
                self.rect.left = max(0, self.rect.left - self.speed)
            case 'right':
                self.rect.right = min(WINDOW_WIDTH, self.rect.right + self.speed)
            case 'down':
                self.rect.centery = min(WINDOW_HEIGHT, self.rect.centery + (WINDOW_HEIGHT // 5))

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        return None
