# constants.py
import decimal
from typing import Final

import pygame

# C
COLOR_BLACK: Final[tuple[int]] = (0, 0, 0)
COLOR_WHITE: Final[tuple[int]] = (255, 255, 255)
COLOR_RED: Final[tuple[int]] = (255, 0, 0)
COLOR_GREEN: Final[tuple[int]] = (0, 255, 0)
COLOR_YELLOW: Final[tuple[int]] = (255, 255, 0)
COLOR_BLUE: Final[tuple[int]] = (0, 0, 255)
COLOR_MAGENTA: Final[tuple[int]] = (255, 0, 255)
COLOR_CYAN: Final[tuple[int]] = (0, 255, 255)
COLOR_GRAY: Final[tuple[int]] = (128, 128, 128)
COLOR_ORANGE: Final[tuple[int]] = (255, 165, 0)
COLOR_PURPLE: Final[tuple[int]] = (128, 0, 128)
COLOR_PINK: Final[tuple[int]] = (255, 192, 203)
COLOR_VIOLET: Final[tuple[int]] = (128, 128, 0)
COLOR_BROWN: Final[tuple[int]] = (128, 128, 0)

# F
FPS: Final[int] = 30

# M
MUSIC_VOL: Final[decimal] = 0.3

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# S
SPAWN_TIME: Final[int] = 3000

# T
TIMEOUT_STEP: Final[int] = 100 # 100ms
TIMEOUT_LEVEL: Final[int] = 60000 # 60s

# W
WINDOW_WIDTH: Final[int] = 576
WINDOW_HEIGHT: Final[int] = 324
