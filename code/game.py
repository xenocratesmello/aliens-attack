import sys

import pygame

from code.constants import WINDOW_WIDTH, WINDOW_HEIGHT
from code.settings import MENU_OPTION, MAX_LEVEL
from code.menu import Menu
from code.level import Level


class Game:
    def __init__(self):
        pygame.init()
        # Create the game's window
        self.window: Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.player_score: int = 0

    def run(self):
        # To use the package it must be initialized.
        while True:
            menu = Menu(self.window)
            menu_option: str = menu.run()

            if menu_option == MENU_OPTION[0]:
                i: int = 1
                level_return: bool = True
                while i <= MAX_LEVEL and level_return:
                    level = Level(self.window, f'Level{i}', self.player_score)
                    level_return = level.run(self.player_score)
                    i += 1

            elif menu_option == MENU_OPTION[1]:
                pass
            elif menu_option == MENU_OPTION[2]:
                pass
            elif menu_option == MENU_OPTION[3]:
                pass
            elif menu_option == MENU_OPTION[4]:
                pygame.quit()
                sys.exit()
            else:
                pygame.quit()
                sys.exit()
