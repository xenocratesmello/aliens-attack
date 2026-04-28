# settings.py
from typing import Final

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
    'Level5Bg4': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_5/4.png'}

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
INITIAL_HEALTH: Final[dict[str, int]] = {
    'Entity': 999}

INITIAL_SCORE: Final[dict[str, int]] = {
    'Entity': 0,
    'Player': 0,
    'Enemy': 0}

# M
MAX_LEVEL: Final[int] = 5

MENU_OPTION: Final[tuple[str]] = (
    'NEW GAME',
    'SCORE',
    'INSTRUCTIONS',
    'SETTINGS',
    'EXIT')

MUSIC_FILE: Final[dict[str, str]] = {
    'Menu': 'asset/craftpix/music/Dark_winter_theme.mp3',
    'Level1': 'asset/craftpix/music/Battle_theme_snow_city_loopable.mp3',
    'Level2': 'asset/craftpix/music/Dark_winter_theme.mp3',
    'Level3': 'asset/craftpix/music/Main_theme_snow_city_alternative_loopable.mp3',
    'Level4': 'asset/craftpix/music/Main_theme_snow_city_loopable.mp3',
    'Level5': 'asset/craftpix/music/Winter_ambient_loopable.mp3'}

# R
RELATIVE_PATH = {
    'Level1BG': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_1',
    'Level2BG': 'asset/craftpix/background/craftpix-net-724983-ocean-and-clouds-free-pixel-art-backgrounds/Ocean_2'}
