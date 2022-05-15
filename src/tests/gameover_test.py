from gameover import GameOver
import unittest
import pygame


class TestGetSentence(unittest.TestCase):
    def setUp(self):
        pygame.init()
        display = pygame.display.set_mode((750, 500))
        self.screen = GameOver(display, [(0, 0, 0)], 'pate', 1)

    def test_center_text(self):
        self.screen.text_colour = (255, 255, 255)
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render('moi', True, (255, 255, 255))
        rect = txt.get_rect(center=(750/2, 25))
        test = self.screen.center_text('moi', 25)
        self.assertIn(rect, test)

    def test_get_difficulty_mode_in_str(self):
        self.screen.difficulty = 2
        difficulty_str = self.screen.get_difficulty_in_str()
        self.assertEqual(difficulty_str, 'Hard')