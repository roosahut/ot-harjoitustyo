import sys
import pygame
from gameloop import GameLoop
from speedtyping import SpeedTyping


class Start:
    def __init__(self, display):
        self.display = display
        self.mode = 0
        self.mode_selected = False

    def start(self):
        while True:
            self.draw_screen()
            self.get_events()

    def draw_screen(self):
        self.display.fill(0)
        if not self.mode_selected:
            self.draw_mode_selection()
        elif self.mode_selected:
            self.draw_start_event()
        pygame.display.flip()

    def draw_mode_selection(self):
        pygame.draw.rect(
            self.display, (0, 0, 255), pygame.Rect(250, 300, 100, 100))
        pygame.draw.rect(
            self.display, (0, 0, 255), pygame.Rect(400, 300, 100, 100))
        normal_text = self.get_text("Normal")
        self.display.blit(normal_text, (265, 335))
        hard_text = self.get_text("Hard")
        self.display.blit(hard_text, (425, 335))
        start_text, xy_start = self.center_text(
            "Select which difficulty mode you want to pick!", 200)
        self.display.blit(start_text, xy_start)

    def draw_start_event(self):
        start_text, xy_start = self.center_text(
            "Start the game by pressing the blue button!", 200)
        self.display.blit(start_text, xy_start)
        pygame.draw.rect(
            self.display, (0, 0, 255), pygame.Rect(325, 300, 100, 100))

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # pylint: disable=invalid-name
                if 325 <= x <= 425 and 300 <= y <= 400 and self.mode_selected:
                    screen = SpeedTyping(self.mode)
                    play = GameLoop(screen, self.display)
                    play.loop()
                if 250 <= x <= 350 and 300 <= y <= 400 and not self.mode_selected:
                    self.mode = 1
                    self.mode_selected = True
                elif 400 <= x <= 500 and 300 <= y <= 400 and not self.mode_selected:
                    self.mode = 2
                    self.mode_selected = True

    def center_text(self, text, y_position):
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render(text, True, (255, 255, 255))
        rect = txt.get_rect(center=(750/2, y_position))
        return txt, rect

    def get_text(self, text):
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render(text, True, (255, 255, 255))
        return txt
