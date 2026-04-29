from code.background import Background
from code.constants import WINDOW_WIDTH, WINDOW_HEIGHT
from code.enemy import Enemy
from code.player import Player


class EntityFactory:
    @staticmethod
    def get_entity(name: str):
        match name:
            case 'Level1Bg':
                list_background: list[Background] = []
                for i in range(1, 4):
                    list_background.append(Background(f'{name}{i}', (0, 0)))
                    list_background.append(Background(f'{name}{i}', (WINDOW_WIDTH, 0)))
                return list_background
            case 'Level2Bg':
                list_background: list[Background] = []
                for i in range(1, 4):
                    list_background.append(Background(f'{name}{i}', (0, 0)))
                    list_background.append(Background(f'{name}{i}', (WINDOW_WIDTH, 0)))
                return list_background
            case 'Level3Bg':
                list_background: list[Background] = []
                for i in range(1, 5):
                    list_background.append(Background(f'{name}{i}', (0, 0)))
                    list_background.append(Background(f'{name}{i}', (WINDOW_WIDTH, 0)))
                return list_background
            case 'Level4Bg':
                list_background: list[Background] = []
                for i in range(1, 5):
                    list_background.append(Background(f'{name}{i}', (0, 0)))
                    list_background.append(Background(f'{name}{i}', (WINDOW_WIDTH, 0)))
                return list_background
            case 'Level5Bg':
                list_background: list[Background] = []
                for i in range(1, 5):
                    list_background.append(Background(f'{name}{i}', (0, 0)))
                    list_background.append(Background(f'{name}{i}', (WINDOW_WIDTH, 0)))
                return list_background
            case 'Player':
                return Player('Player', (WINDOW_WIDTH // 2, WINDOW_HEIGHT))
            case 'Enemies':
                list_enemies: list[Enemy] = []
                for i in range(1, 5):
                    list_enemies.append(Enemy(name='Enemy', position=((WINDOW_WIDTH // 4) * i, 0)))
                return list_enemies
        return None
