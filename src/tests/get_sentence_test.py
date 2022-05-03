from get_sentence import GetSentence
import unittest


class TestGetSentence(unittest.TestCase):
    def setUp(self):
        self.screen = GetSentence()

    def test_get_sentence_normal(self):
        file = open("src/sentences_normal.txt").read()
        sentences = file.split("\n")
        sentence = self.screen.get_sentence(1)
        self.assertIn(sentence, sentences)

    def test_get_sentence_hard(self):
        file = open("src/sentences_hard.txt").read()
        sentences = file.split("\n")
        sentence = self.screen.get_sentence(2)
        self.assertIn(sentence, sentences)