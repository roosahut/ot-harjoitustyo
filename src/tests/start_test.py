from start import Start
import unittest
import pygame


class TestGetSentence(unittest.TestCase):
    def setUp(self):
        pygame.init()
        display = pygame.display.set_mode((750, 500))
        self.screen = Start(display)

    def test_center_text(self):
        self.screen.text_colour = (255, 255, 255)
        font = pygame.font.SysFont("Times New Roman", 24) 
        txt = font.render('moi', True, (255, 255, 255)) 
        rect = txt.get_rect(center=(750/2, 25)) 
        test = self.screen.center_text('moi', 25)
        self.assertIn(rect, test)