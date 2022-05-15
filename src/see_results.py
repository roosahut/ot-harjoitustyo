import sys
import pygame
from services.results_service import results_service


class SeeResults:
    def __init__(self, display):
        self.display = display
        self.results = results_service.get_results()

    def see_results(self):
        while True:
            self.draw_screen()
            self.get_events()

    def draw_screen(self):
        self.display.fill(0)

        y_pos = 10
        for i in self.results:
            result_text, xy_result = self.center_text(
            f"{i[1]}, {i[2]} Sentences: {i[3]} Time: {i[4]} s Accuracy: {i[5]} % WPM: {i[6]}", y_pos)
            self.display.blit(result_text, xy_result)
            y_pos += 10
        pygame.display.flip()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def center_text(self, text, y_position):
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render(text, True, (255, 255, 255))
        rect = txt.get_rect(center=(750/2, y_position))
        return txt, rect

    def get_text(self, text):
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render(text, True, (255, 255, 255))
        return txt
