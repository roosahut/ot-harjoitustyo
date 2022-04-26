import sys
import pygame
from gameloop import GameLoop


class Start:
    def __init__(self, screen, display):
        self.screen = screen
        self.display = display

    def start(self):
        while True:
            self.draw_screen()
            self.get_events()

    def draw_screen(self):
        self.display.fill(0)
        pygame.draw.rect(
            self.display, (0, 0, 255), pygame.Rect(325, 300, 100, 100))
        start_text, xy_start = self.center_text(
            "Press the blue button to start the game!", 250)
        self.display.blit(start_text, xy_start)
        pygame.display.flip()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # pylint: disable=invalid-name
                if 325 <= x <= 425 and 300 <= y <= 400:
                    play = GameLoop(self.screen, self.display)
                    play.loop()

    def center_text(self, text, y_position):
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render(text, True, (255, 255, 255))
        rect = txt.get_rect(center=(750/2, y_position))
        return txt, rect
