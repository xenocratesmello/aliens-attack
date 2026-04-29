import sys

import pygame
from pygame import Surface

from code.constants import WINDOW_WIDTH, WINDOW_HEIGHT
from code.entity_factory import EntityFactory
from code.instructions import Instruction
from code.leaderboard import Leaderboard
from code.player import Player
from code.settings import MENU_OPTION, MAX_LEVEL
from code.menu import Menu
from code.level import Level


class Game:
    def __init__(self):
        pygame.init()
        # Create the game's window
        self.window: Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


    def run(self):
        # To use the package it must be initialized.
        while True:
            leaderboard = Leaderboard(self.window)
            instruction = Instruction(self.window)
            menu = Menu(self.window)
            menu_option: str = menu.run()
            # Create the player
            player: Player = EntityFactory.get_entity('Player')

            if menu_option == MENU_OPTION[0]:

                i: int = 1
                level_return: bool = True
                while i <= MAX_LEVEL and level_return:
                    level = Level(window=self.window, name=f'Level{i}', player=player)
                    level_return = level.run()
                    i += 1

                leaderboard.save(last_level='Winner' if level_return else f'Level{i - 1}', player_score=player.score)

            elif menu_option == MENU_OPTION[1]:
                leaderboard.show()
            elif menu_option == MENU_OPTION[2]:
                instruction.show()
            elif menu_option == MENU_OPTION[3]:
                pygame.quit()
                sys.exit()
            else:
                pygame.quit()
                sys.exit()
