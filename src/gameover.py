import sys
import pygame
from services.results_service import results_service
from see_results import SeeResults


class GameOver:
    """Luokka, joka näyttää näkymän, kun peli on ohi.

    Attributes:
        display: Pygame näkymä.
        results: Menneen pelin kaikki tulokset.
        nickname: Menneen pelin pelaajan lempinimi.
        difficulty: Menneen pelin vaikeustaso. (1 tai 2)
        difficulty_str: Menneen pelin vaikeustaso kirjotettuna. (Normal tai Hard)
        amount_of_sentences: Menneen pelin kirjotettujen lauseiden määrä.
        average_result: Menneen pelin kaikkien lauseiden keskiarvo tulokset.
    """

    def __init__(self, display, results, nickname, difficulty):
        """Luokan konstruktori.

        Args:
            display: Pygame näkymä
            results: Menneen pelin kaikki tulokset listana.
            nickname: Menneen pelin pelaajan lempinimi.
            difficulty: Menneen pelin vaikeustaso (1 tai 2)
        """
        self.display = display
        self.results = results
        self.nickname = nickname
        self.difficulty = difficulty
        self.difficulty_str = self.get_difficulty_in_str()
        self.amount_of_sentences = len(results)
        self.average_result = self.get_average_results()

    def gameover(self):
        """Pelin loppumisen jälkeisen näkymän pygame looppi, joka
            piirtää näytön ja kerää käyttäjän syötteet.
        """
        self.add_result_to_database()
        while True:
            self.draw_screen()
            self.get_events()

    def draw_screen(self):
        """Piirtää pygame näytön.
        """
        self.display.fill(0)

        info_text, xy_info = self.center_text(
            f'Nickname: {self.nickname} Mode: {self.difficulty_str}', 75)
        self.display.blit(info_text, xy_info)

        avg_text, xy_avg = self.center_text(
            f'Your average results for all {self.amount_of_sentences} sentences:', 125)
        self.display.blit(avg_text, xy_avg)

        avg = self.get_average_results()
        result_text, xy_result = self.center_text(
            f"Time: {avg[0]} s Accuracy: {avg[1]} % WPM: {avg[2]}", 150)
        self.display.blit(result_text, xy_result)

        info_text, xy_info = self.center_text(
            'Challenge a friend or play again by pressing new game', 200)
        self.display.blit(info_text, xy_info)

        pygame.draw.rect(
            self.display, (0, 0, 255), pygame.Rect(300, 390, 150, 100))
        start_text, xy_start = self.center_text(
            "New game", 435)
        self.display.blit(start_text, xy_start)

        pygame.draw.rect(
            self.display, (0, 0, 255), pygame.Rect(300, 300, 150, 80))
        start_text, xy_start = self.center_text(
            "See all results", 335)
        self.display.blit(start_text, xy_start)

        pygame.display.flip()

    def get_events(self):
        """Ottaa ylös käyttäjän antamat syötteet.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # pylint: disable=invalid-name
                if 300 <= x <= 450 and 390 <= y <= 490:
                    from start import Start
                    new_game = Start(self.display)
                    new_game.start()
                if 300 <= x <= 450 and 300 <= y <= 380:
                    see_results = SeeResults(self.display)
                    see_results.see_results()

    def get_difficulty_in_str(self):
        """Muuttaa pelin vaikeutason str- muotoon.

        Returns:
            Palauttaa Hard tai Normal.
        """
        if self.difficulty == 1:
            return 'Normal'
        return 'Hard'

    def get_average_results(self):
        """Laskee menneen pelin keskiarvo tulokset kaikkien lauseiden tuloksista.

        Returns:
            Palauttaa keskiarvo ajan, oikeellisuuden ja wpm.
        """
        if len(self.results) == 0:
            return [0, 0, 0]
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
        return [round(time, 1), round(accuracy), round(wpm)]

    def center_text(self, text, y_position):
        """keskittää halutun tekstin ja muuttaa sen pygame muotoon.

        Args:
            text: Haluttu teksti.
            y_position: halutun tekstin y-positio.

        Returns:
            palauttaa halutun tekstin pygame muodossa ja sen koordinaatit.
        """
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render(text, True, (255, 255, 255))
        rect = txt.get_rect(center=(750/2, y_position))
        return txt, rect

    def add_result_to_database(self):
        """Lisää pelin käyttäjän lempinimen, pelin vaikeustason ja pelin tulokset tietokantaan.
        """
        results = self.get_average_results()
        time = str(results[0])
        accuracy = str(results[1])
        wpm = str(results[2])
        results_service.add_result(self.nickname, self.difficulty_str, str(
            self.amount_of_sentences), time, accuracy, wpm)
