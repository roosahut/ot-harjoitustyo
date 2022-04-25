from get_sentence import GetSentence
import unittest


class TestGetSentence(unittest.TestCase):
    def setUp(self):
        self.screen = GetSentence()

    def test_get_sentence(self):
        # the file won't open without src/ for me, don't know if
        # that's the case for everyone
        file = open("src/sentences.txt").read()
        sentences = file.split("\n")
        sentence = self.screen.get_sentence()
        self.assertIn(sentence, sentences)