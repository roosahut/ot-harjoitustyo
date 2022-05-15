import sys
import pygame
from gameloop import GameLoop
from speedtyping import SpeedTyping
from see_results import SeeResults


class Start:
    def __init__(self, display):
        self.display = display
        self.mode = 0
        self.mode_selected = False
        self.input_nickname = ''

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
        info_text, xy_info = self.get_headline()
        self.display.blit(info_text, xy_info)

        info_text, xy_info = self.center_text(
            "See who is the fastest typer in the friendgroup!", 100)
        self.display.blit(info_text, xy_info)

        pygame.draw.rect(
            self.display, (0, 0, 255), pygame.Rect(250, 300, 100, 100))
        pygame.draw.rect(
            self.display, (0, 0, 255), pygame.Rect(400, 300, 100, 100))
        normal_text = self.get_text("Normal")
        self.display.blit(normal_text, (265, 335))
        hard_text = self.get_text("Hard")
        self.display.blit(hard_text, (425, 335))
        start_text, xy_start = self.center_text(
            "Select which difficulty mode you want to pick:", 250)
        self.display.blit(start_text, xy_start)

        pygame.draw.rect(
            self.display, (0, 0, 255), pygame.Rect(300, 420, 150, 60))
        start_text, xy_start = self.center_text(
            "See results", 450)
        self.display.blit(start_text, xy_start)

    def draw_start_event(self):
        text, xy = self.center_text(
            "You will have 30 seconds to write as many sentences as possible", 100)
        self.display.blit(text, xy)

        start_text, xy_start = self.center_text(
            "Start the game by typing your nickname and press the blue button to start!", 150)
        self.display.blit(start_text, xy_start)

        error_text, xy_error = self.center_text(
            "You can't begin unless the nickname is 4-10 characters long!", 180)
        self.display.blit(error_text, xy_error)

        text_input, xy_text = self.center_text(self.input_nickname, 250)
        self.display.blit(text_input, xy_text)

        pygame.draw.rect(
            self.display, (0, 0, 255), pygame.Rect(325, 300, 100, 100))

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # pylint: disable=invalid-name
                if 325 <= x <= 425 and 300 <= y <= 400 and self.mode_selected:
                    if 4 <= len(self.input_nickname) <= 10:
                        screen = SpeedTyping(self.mode)
                        play = GameLoop(screen, self.display,
                                        self.input_nickname, self.mode)
                        play.loop()
                if 250 <= x <= 350 and 300 <= y <= 400 and not self.mode_selected:
                    self.mode = 1
                    self.mode_selected = True
                elif 400 <= x <= 500 and 300 <= y <= 400 and not self.mode_selected:
                    self.mode = 2
                    self.mode_selected = True
                elif 300 <= x <= 450 and 420 <= y <= 480 and not self.mode_selected:
                    prev_results = SeeResults(self.display)
                    prev_results.see_results()
            elif event.type == pygame.KEYDOWN and self.mode_selected:
                if event.key == pygame.K_BACKSPACE:
                    self.input_nickname = self.input_nickname[:-1]
                else:
                    self.input_nickname += event.unicode

    def get_headline(self):
        font = pygame.font.SysFont("Times New Roman", 32)
        txt = font.render('SPEED TYPING TEST', True, (255, 255, 255))
        rect = txt.get_rect(center=(750/2, 50))
        return txt, rect

    def center_text(self, text, y_position):
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render(text, True, (255, 255, 255))
        rect = txt.get_rect(center=(750/2, y_position))
        return txt, rect

    def get_text(self, text):
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render(text, True, (255, 255, 255))
        return txt
