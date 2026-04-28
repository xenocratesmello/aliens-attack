import sys

import pygame.time
from pygame import Surface, Rect
from pygame.font import Font

from code.background import Background
from code.constants import EVENT_ENEMY, SPAWN_TIME, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL, MUSIC_VOL, FPS, \
    COLOR_MAGENTA, WINDOW_WIDTH
from code.enemy import Enemy
from code.enemy_shot import EnemyShot
from code.entity_factory import EntityFactory
from code.player import Player
from code.player_shot import PlayerShot
from code.settings import MUSIC_FILE, BACKGROUND_SPEED, INITIAL_SPEED


class Level:
    def __init__(self, window: Surface, name: str, player_score: int):
        self.window = window
        self.name = name
        self.player_score = player_score
        self.timeout: int = TIMEOUT_LEVEL
        self.background_list: list[Background] = []
        self.background_list.extend(EntityFactory.get_entity(f'{self.name}Bg'))
        self.enemy_list: list[Enemy] = []
        self.enemy_list.extend(EntityFactory.get_entity('Enemies'))
        self.enemy_direction: str = 'left'

        self.player_list: list[Player] = []
        self.player_list.append(EntityFactory.get_entity('Player'))
        self.player_list[0].score = self.player_score

        self.player_shot_list: list[PlayerShot] = []
        self.enemy_shot_list: list[EnemyShot] = []

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: int):
        pygame.mixer_music.load(MUSIC_FILE[self.name])
        pygame.mixer.music.set_volume(MUSIC_VOL)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(FPS)

            # Background control
            for i in range(len(self.background_list)):
                self.window.blit(source=self.background_list[i].surface, dest=self.background_list[i].rect)
                self.background_list[i].move(BACKGROUND_SPEED[self.background_list[i].name])

            # Player control
            for player in self.player_list:
                self.window.blit(source=player.surface, dest=player.rect)
                player.speed = INITIAL_SPEED[player.name] + int(''.join(char for char in self.name if char.isdigit()))
                player.move()
                shoot = player.shoot()
                if shoot is not None:
                    self.player_shot_list.append(shoot)
                self.level_text(14, f'{player.name} - Health: {player.health:.0f} | Score: {player.score}',
                                COLOR_MAGENTA, (10, 25))

            # Enemy control
            for enemy in self.enemy_list:
                self.window.blit(source=enemy.surface, dest=enemy.rect)
                enemy.speed = INITIAL_SPEED[enemy.name] + int(''.join(char for char in self.name if char.isdigit()))
                enemy.move(self.enemy_direction)
                if enemy.rect.left <= 0:
                    self.enemy_direction = 'right'
                elif enemy.rect.right >= WINDOW_WIDTH:
                    self.enemy_direction = 'down'
                    for ent in self.enemy_list:
                        ent.move(self.enemy_direction)
                    self.enemy_list.extend(EntityFactory.get_entity('Enemies'))
                    self.enemy_direction = 'left'

                shoot = enemy.shoot()
                if shoot is not None:
                    self.enemy_shot_list.append(shoot)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        for player in self.player_list:
                            self.player_score = max(player.score, self.player_score)

                        return True

                if len(self.player_list) == 0:
                    return False

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Arial', size=text_size, bold=False, italic=True)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surface, dest=text_rect)
