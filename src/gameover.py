import sys
import pygame


class GameOver:
    def __init__(self, display, results):
        self.display = display
        self.results = results
        self.amount_of_sentences = len(results)
        self.average_result = self.get_average_results()

    def gameover(self):
        while True:
            self.draw_screen()
            self.get_events()

    def draw_screen(self):
        self.display.fill(0)

        avg_text, xy_avg = self.center_text(f'Your average results for all {self.amount_of_sentences} sentences:', 100)
        self.display.blit(avg_text, xy_avg)
        result_text, xy_result = self.center_text(
            self.average_result, 150)
        self.display.blit(result_text, xy_result)

        start_text, xy_start = self.center_text(
            "Play again by pressing the blue button!", 200)
        self.display.blit(start_text, xy_start)
        pygame.draw.rect(
            self.display, (0, 0, 255), pygame.Rect(325, 300, 100, 100))

        pygame.display.flip()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # pylint: disable=invalid-name
                if 325 <= x <= 425 and 300 <= y <= 400:
                    from start import Start
                    new_game = Start(self.display)
                    new_game.start()

    def get_average_results(self):
        time = 0
        accuracy = 0
        wpm = 0
        for i in self.results:
            time += i[0]
            accuracy += i[1]
            wpm += i[2]
        time = time/self.amount_of_sentences
        accuracy = accuracy/self.amount_of_sentences
        wpm = wpm/self.amount_of_sentences
        return f'Time: {round(time, 1)} s Accuracy: {round(accuracy)} % WPM: {round(wpm)}'

    def center_text(self, text, y_position):
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render(text, True, (255, 255, 255))
        rect = txt.get_rect(center=(750/2, y_position))
        return txt, rect

    def get_text(self, text):
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render(text, True, (255, 255, 255))
        return txt
