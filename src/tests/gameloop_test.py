from gameloop import GameLoop
from speedtyping import SpeedTyping
import unittest
import pygame


class TestGetSentence(unittest.TestCase):
    def setUp(self):
        pygame.init()
        display = pygame.display.set_mode((750, 500))
        screen = SpeedTyping(1)
        self.screen = GameLoop(screen, display, 'pate', 1)

    def test_center_text(self):
        self.screen.text_colour = (255, 255, 255)
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render('moi', True, (255, 255, 255))
        rect = txt.get_rect(center=(750/2, 25))
        test = self.screen.center_text('moi', 25)
        self.assertIn(rect, test)

    def test_change_mode_to_white(self):
        pygame.init()
        display = pygame.display.set_mode((750, 500))
        screen = SpeedTyping(1)
        test_screen = GameLoop(screen, display, 'pate', 1)
        test_screen.mode = (0)
        test_screen.change_mode()
        self.screen.change_mode()
        self.assertEqual(test_screen.mode, self.screen.mode)

    def test_change_mode_to_black(self):
        self.screen.change_mode()
        pygame.init()
        display = pygame.display.set_mode((750, 500))
        screen = SpeedTyping(1)
        test_screen = GameLoop(screen, display, 'pate', 1)
        test_screen.mode = (255, 255, 255)
        test_screen.change_mode()
        self.screen.change_mode()
        self.assertEqual(test_screen.mode, self.screen.mode)

    def test_check_xy_reset(self):
        self.screen.end = True
        self.screen.check_xy(333, 400)
        self.assertEqual(False, self.screen.mode)

    def test_check_xy_change_mode(self):
        self.screen.mode = (0)
        self.screen.check_xy(555, 15)
        self.assertEqual((255, 255, 255), self.screen.mode)
