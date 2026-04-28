import sys

import pygame.time
from pygame import Surface

from code.background import Background
from code.constants import EVENT_ENEMY, SPAWN_TIME, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL, MUSIC_VOL, FPS, \
    WINDOW_WIDTH, WINDOW_HEIGHT
from code.entity_factory import EntityFactory
from code.player import Player
from code.settings import MUSIC_FILE, BACKGROUND_SPEED


class Level:
    def __init__(self, window: Surface, name: str, player_score: int):
        self.window = window
        self.name = name
        self.player_score = player_score
        self.timeout: int = TIMEOUT_LEVEL
        self.background_list: list[Background] = []
        self.background_list.extend(EntityFactory.get_entity(f'{self.name}Bg'))
        # self.enemy_list: list[Enemy] = []

        self.player: Player = EntityFactory.get_entity('Player')
        self.player.score = self.player_score

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: int):
        pygame.mixer_music.load(MUSIC_FILE[self.name])
        pygame.mixer.music.set_volume(MUSIC_VOL)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(FPS)

            for i in range(len(self.background_list)):
                self.window.blit(source=self.background_list[i].surface, dest=self.background_list[i].rect)
                self.background_list[i].move(BACKGROUND_SPEED[self.background_list[i].name])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        return True

            pygame.display.flip()