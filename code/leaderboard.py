import sys
from datetime import datetime
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.constants import MUSIC_VOL, WINDOW_HEIGHT, WINDOW_WIDTH, COLOR_BLUE, COLOR_GREEN, COLOR_WHITE, COLOR_RED, \
    COLOR_BROWN, COLOR_BLACK
from code.db_proxy import DbProxy
from code.settings import BACKGROUND_FILE, MUSIC_FILE, LEADERBOARD_TITLE, LEADERBOARD_POSITION, MAX_LEVEL


class Leaderboard:
    def __init__(self, window: Surface):
        self.window = window
        self.surface: Surface = pygame.transform.scale(surface=pygame.image.load(BACKGROUND_FILE['Leaderboard']),
                                                       size=(WINDOW_WIDTH, WINDOW_HEIGHT)).convert_alpha()
        self.rect: Rect = self.surface.get_rect(left=0, top=0)

    def save(self, last_level: str, player_score: int):
        pygame.mixer.music.load(MUSIC_FILE['Leaderboard'])
        pygame.mixer.music.set_volume(MUSIC_VOL)
        pygame.mixer.music.play(-1)

        db_proxy = DbProxy()
        player_name: str = ''
        leaderboard_title: str = LEADERBOARD_TITLE['Winner'] if last_level == 'Winner' else LEADERBOARD_TITLE[
            'Game Over']

        while True:
            self.window.blit(source=self.surface, dest=self.rect)
            self.leaderboard_text(48, leaderboard_title, COLOR_RED, LEADERBOARD_POSITION['Title'])
            text: str = 'Enter Player\'s Name'
            score: int = player_score

            self.leaderboard_text(20, text, COLOR_BROWN, LEADERBOARD_POSITION['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(player_name) == 4:
                        db_proxy.save_results({'player_name': player_name, 'score': score,
                                               'last_level': last_level if last_level != 'Winner' else f'Level{MAX_LEVEL}',
                                               'is_winner': last_level == 'Winner', 'date': self.get_formatted_date()})
                        db_proxy.close_connection()
                        self.show(winner=last_level == 'Winner')
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        if len(player_name) < 4:
                            player_name += event.unicode

            self.leaderboard_text(20, player_name, COLOR_BROWN, LEADERBOARD_POSITION['Name'])

            pygame.display.flip()

    def show(self, winner: bool = False):
        pygame.mixer.music.load(MUSIC_FILE['Leaderboard'])
        pygame.mixer.music.set_volume(MUSIC_VOL)
        pygame.mixer.music.play(-1)

        self.window.blit(source=self.surface, dest=self.rect)

        self.leaderboard_text(30, 'TOP TEN SCORE', COLOR_RED, LEADERBOARD_POSITION['Title'])
        self.leaderboard_text(20, 'NAME   SCORE    LEVEL    RESULT             DATE          ', COLOR_BLUE,
                              LEADERBOARD_POSITION['Label'])
        db_proxy = DbProxy()
        list_results = db_proxy.retrieve_winners_top10() if winner else db_proxy.retrieve_top10()
        db_proxy.close_connection()

        for player_score in list_results:
            player_name, score, last_level, is_winner, date = player_score
            self.leaderboard_text(20,
                                  f'{player_name}    {score: 05d}    {last_level}    {'Winner' if is_winner else 'Game Over'}    {date}',
                                  COLOR_BLACK, LEADERBOARD_POSITION[list_results.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            pygame.display.flip()

    def leaderboard_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name='Arial', size=text_size, bold=True, italic=False)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_position)
        self.window.blit(source=text_surface, dest=text_rect)

    @staticmethod
    def get_formatted_date():
        current_datetime: datetime = datetime.now()
        current_time = current_datetime.strftime("%H:%M")
        current_date = current_datetime.strftime("%d/%m/%Y")
        return f'{current_time} - {current_date}'
