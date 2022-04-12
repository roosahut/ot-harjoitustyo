from speedtyping import SpeedTyping
import unittest


class TestSpeedTyping(unittest.TestCase):
    def setUp(self):
        self.screen = SpeedTyping()

    def test_get_sentence(self):
        # the file won't open without src/ for me, don't know if
        # that's the case for everyone
        file = open("src/sentences.txt").read()
        sentences = file.split("\n")
        sentence = self.screen.get_sentence()
        self.assertIn(sentence, sentences)

    def test_results(self):
        self.screen.end_time = 2
        self.screen.start_time = 0.5
        self.screen.sentence = 'this is a test'
        self.screen.input = 'this is a test'
        self.screen.words = 4
        wpm = round(len(self.screen.input)*60/(self.screen.words*1.5))
        results = self.screen.results()
        self.assertEqual(results, f"Time: 1.5 s  Accuracy: 100 %  WPM: {wpm}")
