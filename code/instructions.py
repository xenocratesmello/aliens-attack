import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.constants import WINDOW_WIDTH, WINDOW_HEIGHT, MUSIC_VOL, COLOR_RED, COLOR_WHITE
from code.settings import BACKGROUND_FILE, MUSIC_FILE, LEADERBOARD_POSITION


class Instruction:
    def __init__(self, window: Surface):
        self.window = window
        self.surface: Surface = pygame.transform.scale(surface=pygame.image.load(BACKGROUND_FILE['Instruction']),
                                                       size=(WINDOW_WIDTH, WINDOW_HEIGHT)).convert_alpha()
        self.rect: Rect = self.surface.get_rect(left=0, top=0)

    def show(self):
        pygame.mixer.music.load(MUSIC_FILE['Instruction'])
        pygame.mixer.music.set_volume(MUSIC_VOL)
        pygame.mixer.music.play(-1)

        self.window.blit(source=self.surface, dest=self.rect)

        self.instruction_text(30, 'INSTRUCTIONS', COLOR_RED, LEADERBOARD_POSITION['Title'])
        self.instruction_text(20, '- The player uses K_LEFT and K_RIGHT to move', COLOR_WHITE,
                              LEADERBOARD_POSITION[0])
        self.instruction_text(20, '  to left or right.', COLOR_WHITE,
                              LEADERBOARD_POSITION[1])
        self.instruction_text(20, '- The player shoot by K_UP.', COLOR_WHITE,
                              LEADERBOARD_POSITION[2])
        self.instruction_text(20, '- Each level will end when all enemies are', COLOR_WHITE,
                              LEADERBOARD_POSITION[3])
        self.instruction_text(20, '  dead or the timeout be achieved.', COLOR_WHITE,
                              LEADERBOARD_POSITION[4])
        self.instruction_text(20, '- The game over occurs when the player', COLOR_WHITE,
                              LEADERBOARD_POSITION[5])
        self.instruction_text(20, '  receives an enemies\' shot.', COLOR_WHITE,
                              LEADERBOARD_POSITION[6])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            pygame.display.flip()

    def instruction_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name='Arial', size=text_size, bold=True, italic=False)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        # text_rect: Rect = text_surface.get_rect(left=10,top=text_center_position[1])
        text_rect: Rect = text_surface.get_rect(center=text_center_position)
        self.window.blit(source=text_surface, dest=text_rect)