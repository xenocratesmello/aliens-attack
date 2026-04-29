import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.constants import MUSIC_VOL, COLOR_RED, WINDOW_WIDTH, WINDOW_HEIGHT, COLOR_GREEN, COLOR_WHITE
from code.settings import MUSIC_FILE, MENU_OPTION, BACKGROUND_FILE


class Menu:
    def __init__(self, window: Surface):
        self.window = window
        self.surface: Surface = pygame.transform.scale(surface=pygame.image.load(BACKGROUND_FILE['Menu']),
                                                       size=(WINDOW_WIDTH, WINDOW_HEIGHT)).convert_alpha()
        # self.surface: Surface = pygame.image.load(BACKGROUND_FILE['Menu']).convert_alpha()
        self.rect: Rect = self.surface.get_rect(left=0, top=0)
        self.menu_option: int = 0

    def run(self):
        pygame.mixer.music.load(MUSIC_FILE['Menu'])
        pygame.mixer.music.set_volume(MUSIC_VOL)
        pygame.mixer.music.play(-1)

        while True:
            # Draw images
            self.window.blit(source=self.surface, dest=self.rect)
            self.menu_text(50, "ALIENS ATTACK", COLOR_RED, ((WINDOW_WIDTH // 2), (
                    WINDOW_HEIGHT // (len(MENU_OPTION) + 3))))  # Header, Footer, Title and len(MENU_OPTION)

            for i in range(len(MENU_OPTION)):
                # The selected menu_option has another color
                self.menu_text(
                    text_size=20,
                    text=MENU_OPTION[i],
                    text_color=COLOR_GREEN if i == self.menu_option else COLOR_WHITE,
                    text_center_position=((WINDOW_WIDTH // 2),
                                          (WINDOW_HEIGHT // (len(MENU_OPTION) + 3)) * (2 + i)))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.menu_option = (self.menu_option + 1) % len(MENU_OPTION)
                    if event.key == pygame.K_UP:
                        self.menu_option = (self.menu_option - 1) % len(MENU_OPTION)
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[self.menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name='Arial', size=text_size, bold=True, italic=False)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_position)
        self.window.blit(source=text_surface, dest=text_rect)
