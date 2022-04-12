import time
import pygame

class GameLoop:
    def __init__(self, screen, display):
        self.screen = screen
        self.display = display
        self.end = False

    def start(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if self.end is True:
                    if event.type == pygame.MOUSEBUTTONUP:
                        x_pos, y_pos = pygame.mouse.get_pos()
                        if x_pos >= 325 and x_pos <= 425 and y_pos >= 385 and y_pos <= 485:
                            self.screen.reset()
                            self.end = False
                elif event.type == pygame.KEYDOWN:
                    if not self.end:
                        if event.key == pygame.K_RETURN:
                            self.screen.end_time = time.time()
                            if len(self.screen.input) == 0:
                                self.screen.words = 1
                            else:
                                for i in self.screen.input:
                                    if i == ' ':
                                        self.screen.words += 1
                            self.end = True
                        elif event.key == pygame.K_BACKSPACE:
                            self.screen.input = self.screen.input[:-1]
                        else:
                            if self.screen.input == '':
                                self.screen.start_time = time.time()
                            self.screen.input += event.unicode
                self.display.fill(0)
                sentence_input, xy_sentence = self.screen.center_text(
                    self.screen.sentence, 175)
                self.display.blit(sentence_input, xy_sentence)
                text_input, xy_text = self.screen.center_text(self.screen.input, 250)
                self.display.blit(text_input, xy_text)
                if self.end is False:
                    start_text, xy_start = self.screen.center_text(
                        "Start typing the given sentence, press enter to finish", 100)
                    self.display.blit(start_text, xy_start)
                if self.end is True:
                    blue = (0, 0, 255)
                    pygame.draw.rect(
                        self.display, blue, pygame.Rect(325, 385, 100, 100))
                    playagain_text, xy_playagain = self.screen.center_text(
                        "Click reset to play again", 100)
                    self.display.blit(playagain_text, xy_playagain)
                    reset, xy_reset = self.screen.center_text("Reset", 435)
                    self.display.blit(reset, xy_reset)
                    result = self.screen.results()
                    text_result, xy_result = self.screen.center_text(result, 325)
                    self.display.blit(text_result, xy_result)
                pygame.display.flip()
