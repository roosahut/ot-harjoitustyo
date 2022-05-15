import sys
import pygame
from services.results_service import results_service


class SeeResults:
    """Luokka, joka näyttää pelin 12 edellistä tulosta.

    Attributes:
        display: pygame näkymä
        results: Tietokannasta haetut entiset tulokset.
    """

    def __init__(self, display):
        """Luokan konstruktori.

        Args:
            display: Pygame näkymä.
        """
        self.display = display
        self.results = results_service.get_results()

    def see_results(self):
        """Pygame looppi, joka hakee käyttäjän tapahtumat ja piirtää näkymän.
        """
        while True:
            self.draw_screen()
            self.get_events()

    def draw_screen(self):
        """Piirtää näkymän, näyttää tietokannan 12 edellistä lisäystä.
        """
        self.display.fill(0)

        info_text, xy_info = self.center_text(
            "Results of the last 12 games played", 15)
        self.display.blit(info_text, xy_info)

        y_pos = 50
        for i in self.results:
            result_text, xy_result = self.center_text(
                f"{i[1]}, {i[2]} - Sentences: {i[3]} Time: {i[4]} s Accuracy: {i[5]} % WPM: {i[6]}", y_pos)
            self.display.blit(result_text, xy_result)
            y_pos += 25

        pygame.draw.rect(
            self.display, (0, 0, 255), pygame.Rect(300, 390, 150, 100))
        start_text, xy_start = self.center_text(
            "New game", 435)
        self.display.blit(start_text, xy_start)

        pygame.display.flip()

    def get_events(self):
        """Ottaa ylös pelaajan syötteet.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # pylint: disable=invalid-name
                if 300 <= x <= 450 and 390 <= y <= 490:
                    from surfaces.start import Start
                    new_game = Start(self.display)
                    new_game.start()

    def center_text(self, text, y_position):
        """Keskittää halutun tekstin pygamelle sopivaksi.

        Args:
            text: Haluttu teksti.
            y_position: Halutun tekstin y-positio.

        Returns:
            Halutun tekstin pygamen muodossa ja sen koordinaatin.
        """
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render(text, True, (255, 255, 255))
        rect = txt.get_rect(center=(750/2, y_position))
        return txt, rect
