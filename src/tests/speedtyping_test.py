from speedtyping import SpeedTyping
import unittest

class TestSpeedTyping(unittest.TestCase):
    def setUp(self):
        self.screen = SpeedTyping()

    def test_get_sentence(self):
        file = open("src/sentences.txt").read()
        sentences = file.split("\n")
        sentence = self.screen.get_sentence()
        self.assertIn(sentence, sentences)