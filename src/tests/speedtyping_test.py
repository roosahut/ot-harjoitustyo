from services.speedtyping import SpeedTyping
import unittest


class TestSpeedTyping(unittest.TestCase):
    def setUp(self):
        self.screen = SpeedTyping(1)

    def test_results(self):
        self.screen.end_time = 2
        self.screen.start_time = 0.5
        self.screen.sentence = 'this is a test'
        self.screen.input = 'this is a test'
        self.screen.words = 4
        wpm = round(len(self.screen.input)*60/(self.screen.words*1.5))
        results = self.screen.results()
        self.assertEqual(results, [1.5, 100, 140])

    def test_reset(self):
        self.screen.start_time = 2
        self.screen.end_time = 30
        self.screen.input = 'jee'
        self.screen.words = 34
        self.screen.reset()
        self.assertEqual(self.screen.start_time, 0)
        self.assertEqual(self.screen.end_time, 0)
        self.assertEqual(self.screen.input, '')
        self.assertEqual(self.screen.words, 1)

    def test_count_words_if_zero(self):
        self.screen.input = ''
        self.screen.count_words()
        self.assertEqual(1, self.screen.words)

    def test_count_words_if_not_zero(self):
        self.screen.input = 'moi kiakki heh'
        self.screen.count_words()
        self.assertEqual(3, self.screen.words)

