from typing import Final
import pygame
from code.constants import WINDOW_WIDTH

# D
DB_NAME: Final[str] = 'db_aliens_attack'

# F
BACKGROUND_FILE: Final[dict[str, str]] = {
    'Menu': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_8/6.png',
    'Level1Bg1': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_1/1.png',
    'Level1Bg2': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_1/2.png',
    'Level1Bg3': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_1/3.png',
    'Level2Bg1': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_2/2.png',
    'Level2Bg2': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_2/3.png',
    'Level2Bg3': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_2/4.png',
    'Level3Bg1': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_3/1.png',
    'Level3Bg2': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_3/2.png',
    'Level3Bg3': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_3/3.png',
    'Level3Bg4': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_3/4.png',
    'Level4Bg1': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_4/1.png',
    'Level4Bg2': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_4/2.png',
    'Level4Bg3': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_4/3.png',
    'Level4Bg4': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_4/4.png',
    'Level5Bg1': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_5/1.png',
    'Level5Bg2': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_5/2.png',
    'Level5Bg3': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_5/3.png',
    'Level5Bg4': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_5/4.png',
    'Leaderboard': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_7/6.png',
    'Instruction': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_6/5.png'}

BACKGROUND_SPEED: Final[dict[str, int]] = {
    'Level1Bg1': 0,
    'Level1Bg2': 1,
    'Level1Bg3': 1,
    'Level2Bg1': 0,
    'Level2Bg2': 1,
    'Level2Bg3': 1,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 1,
    'Level3Bg4': 2,
    'Level4Bg1': 0,
    'Level4Bg2': 1,
    'Level4Bg3': 2,
    'Level4Bg4': 3,
    'Level5Bg1': 0,
    'Level5Bg2': 1,
    'Level5Bg3': 2,
    'Level5Bg4': 3}

# I
INITIAL_DAMAGE: Final[dict[str, int]] = {
    'Player': 1,
    'Enemy': 1,
    'PlayerShot': 30,
    'EnemyShot': 50
}

INITIAL_HEALTH: Final[dict[str, int]] = {
    'Entity': 999,
    'Player': 300,
    'PlayerShot': 1,
    'Enemy': 100,
    'EnemyShot': 1}

INITIAL_SCORE: Final[dict[str, int]] = {
    'Entity': 0,
    'Player': 0,
    'Enemy': 0}

INITIAL_SPEED: Final[dict[str, int]] = {
    # The level number will be added to the speed to increase the level difficulty.
    'Player': 2,
    'PlayerShot': 5,
    'Enemy': 0,
    'EnemyShot': 2}

# L
LEADERBOARD_TITLE: Final[dict[str, str]] = {
    'Winner': 'YOU WIN',
    'Game Over': 'GAME OVER'}

LEADERBOARD_POSITION: Final[dict[str | int, tuple]] = {
    'Title': (WINDOW_WIDTH // 2, 50),
    'EnterName': (WINDOW_WIDTH // 2, 80),
    'Label': (WINDOW_WIDTH // 2, 90),
    'Name': (WINDOW_WIDTH // 2, 110),
    0: (WINDOW_WIDTH // 2, 110),
    1: (WINDOW_WIDTH // 2, 130),
    2: (WINDOW_WIDTH // 2, 150),
    3: (WINDOW_WIDTH // 2, 170),
    4: (WINDOW_WIDTH // 2, 190),
    5: (WINDOW_WIDTH // 2, 210),
    6: (WINDOW_WIDTH // 2, 230),
    7: (WINDOW_WIDTH // 2, 250),
    8: (WINDOW_WIDTH // 2, 270),
    9: (WINDOW_WIDTH // 2, 290)}

# M
MAX_LEVEL: Final[int] = 5

MENU_OPTION: Final[tuple[str]] = (
    'NEW GAME',
    'LEADERBOARD',
    'INSTRUCTIONS',
    'EXIT')

MUSIC_FILE: Final[dict[str, str]] = {
    'Menu': 'asset/craftpix/music/Dark_winter_theme.mp3',
    'Level1': 'asset/craftpix/music/Battle_theme_snow_city_loopable.mp3',
    'Level2': 'asset/craftpix/music/Dark_winter_theme.mp3',
    'Level3': 'asset/craftpix/music/Main_theme_snow_city_alternative_loopable.mp3',
    'Level4': 'asset/craftpix/music/Main_theme_snow_city_loopable.mp3',
    'Level5': 'asset/craftpix/music/Winter_ambient_loopable.mp3',
    'Leaderboard': 'asset/pixabay/music/arthurhale-8bit-video-game-music-289970.mp3',
    'Instruction': 'asset/pixabay/music/tudo_free-16-bits-music-294095.mp3'}

# P
PLAYER_KEY_SHOOT: Final[dict[str, int]] = {
    'Player': pygame.K_UP}
PLAYER_KEY_LEFT: Final[dict[str, int]] = {
    'Player': pygame.K_LEFT
}
PLAYER_KEY_RIGHT: Final[dict[str, int]] = {
    'Player': pygame.K_RIGHT
}

# S
SHOT_DELAY: Final[dict[str, int]] = {
    'Player': 15,
    'Enemy': 100}

SPRITE_FILE: Final[dict[str, str]] = {
    'Player': 'asset/craftpix/sprites/craftpix-net-757069-free-spaceship-pixel-art-sprite-sheets/Fighter/Idle.png',
    'Enemy': 'asset/craftpix/sprites/craftpix-net-757069-free-spaceship-pixel-art-sprite-sheets/Bomber/Idle.png',
    'PlayerShot': 'asset/craftpix/sprites/craftpix-net-757069-free-spaceship-pixel-art-sprite-sheets/Fighter/Charge_1.png',
    'EnemyShot': 'asset/craftpix/sprites/craftpix-net-757069-free-spaceship-pixel-art-sprite-sheets/Bomber/Charge_2.png'}

SPRITE_SCALE_FACTOR: Final[float] = 0.5
