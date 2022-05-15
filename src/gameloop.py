import time
import sys
import pygame
from gameover import GameOver


class GameLoop:
    """Luokka, joka pitää yllä aina yhtä SpeedTyping-peliä.

    Attributes:
        clock: Pygamen ajastin.
        screen: SpeedTyping-luokassa pohja kirjoitukselle ja tuloksille
        display: Pygame näkymä.
        mode: Pygamen näkymän taustaväri.
        text_colour: Pygamen näkymän tekstin väri.
        end: Onko yhden lauseen kirjoitus lopetettu vai ei.
        game_timer: Aika sekunneissa, joka pelaajalla on kirjoittaa lauseita. Vähenee kokoajan.
    """

    def __init__(self, screen, display, nickname, difficulty):
        """Luokan konstruktori, joka määrää pelin näkymän.

        Args:
            screen: SpeedTyping-luokassa pohja kirjoitukselle ja tuloksille.
            display: Pygame näkymä
        """
        self.pygame_clock = pygame.time.Clock()
        self.screen = screen
        self.display = display
        self.nickname = nickname
        self.difficulty_mode = difficulty
        self.mode = (0)
        self.text_colour = (255, 255, 255)
        self.end = False
        self.game_timer = 30
        self.results = []

    def loop(self):
        """Pelin päälooppi, jossa kello käy, sekä tapahtumat kerätään ylös.
        """
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    self.game_timer -= 1
                    if self.game_timer == 0:
                        gameover = GameOver(
                            self.display, self.results, self.nickname, self.difficulty_mode)
                        gameover.gameover()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()  # pylint: disable=invalid-name
                    self.check_xy(x, y)
                elif event.type == pygame.KEYDOWN:
                    if not self.end:
                        if event.key == pygame.K_RETURN:
                            self.screen.end_time = time.time()
                            self.screen.count_words()
                            self.results.append(self.screen.results())
                            self.end = True
                        elif event.key == pygame.K_BACKSPACE:
                            self.screen.input = self.screen.input[:-1]
                        else:
                            self.start_time()
                            self.screen.input += event.unicode
                    elif self.end:
                        self.screen.reset()
                        self.end = False
                self.draw_screen()
                pygame.display.flip()
                self.pygame_clock.tick(60)

    def draw_screen(self):
        """Pelin päänäkymä, funktio piirtää lauseet ja napit tarpeen mukaan.
        """

        self.display.fill(self.mode)

        gametimer_text = self.get_text(f'Time left: {self.game_timer} seconds')
        self.display.blit(gametimer_text, (15, 15))

        self.draw_colour_mode_button()

        sentence_input, xy_sentence = self.center_text(
            self.screen.sentence, 175)
        self.display.blit(sentence_input, xy_sentence)

        text_input, xy_text = self.center_text(self.screen.input, 250)
        self.display.blit(text_input, xy_text)

        if self.end is False:
            start_text, xy_start = self.center_text(
                "Start typing the given sentence, press enter to finish", 100)
            self.display.blit(start_text, xy_start)
        if self.end is True:
            self.draw_reset()

    def draw_colour_mode_button(self):
        """Funktio, joka piirtää peliin napin, josta pystyy vaihtamaan väriteemaa.
        """
        pygame.draw.rect(
            self.display, (0, 0, 255), pygame.Rect(540, 10, 205, 45))
        changemode_text = self.get_text("Change colour mode")
        self.display.blit(changemode_text, (543, 15))

    def draw_reset(self):
        """Funktio, joka piirtää näkymän siitä, kun pelaaja on valmis lauseen kirjoituksessa.
        """
        pygame.draw.rect(
            self.display, (0, 0, 255), pygame.Rect(325, 385, 100, 100))
        reset, xy_reset = self.center_text("Reset", 435)
        self.display.blit(reset, xy_reset)

        playagain_text, xy_playagain = self.center_text(
            "Click reset or any key to get the next sentence", 100)
        self.display.blit(playagain_text, xy_playagain)

        result = self.screen.results_sentence()
        text_result, xy_result = self.center_text(result, 325)
        self.display.blit(text_result, xy_result)

    def check_xy(self, x, y):  # pylint: disable=invalid-name
        """Funktio, joka katsoo onko hiiren painallukset oikeissa paikoissa,
        ja tekee toimenpiteet jos on.

        Args:
            x: Hiiren kohta x-suunnassa
            y: Hiiren kohta y-suunnassa
        """
        if 540 <= x <= 745 and 10 <= y <= 55:
            self.change_mode()
        if 325 <= x <= 425 and 385 <= y <= 485 and self.end is True:
            self.screen.reset()
            self.end = False

    def start_time(self):
        """Aloittaa ajastimen, joka laskee ajan, joka kuluu yhden lauseen kirjoitukseen.
        """
        if self.screen.input == '':
            self.screen.start_time = time.time()

    def center_text(self, text, y_position):
        """Luo tekstin sopivaksi Pygameen ja keskittää sen näyttöön.

        Args:
            text: Haluttu teksti
            y_position: Halutun tekstin haluttu y-positio.

        Returns:
            Valmiin tekstin, sekä xy-koordinaatin sille.
        """
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render(text, True, self.text_colour)
        rect = txt.get_rect(center=(750/2, y_position))
        return txt, rect

    def get_text(self, text):
        """Luo tekstin sopivaksi Pygameen.

        Args:
            text: Haluttu teksti

        Returns:
            Halutun tekstin pygame -muodossa.
        """
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render(text, True, self.text_colour)
        return txt

    def change_mode(self):
        """Muuttaa Pygame näkymän väriteemaa, eli taustaväriä sekä tekstinväriä.
        """
        if self.mode == (255, 255, 255):
            self.mode = (0)
            self.text_colour = (255, 255, 255)
        elif self.mode == (0):
            self.mode = (255, 255, 255)
            self.text_colour = (0, 0, 0)
