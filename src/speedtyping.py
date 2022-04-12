import random
import pygame

class SpeedTyping:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.sentence = self.get_sentence()
        self.input = ''
        self.words = 1

    def get_sentence(self):
        # the file won't open without src/ for me, don't know if 
        # that's the case for everyone
        file = open("src/sentences.txt").read()
        sentences = file.split("\n")
        pick = random.choice(sentences)
        return pick

    def results(self):
        timer = self.end_time - self.start_time
        input_counter = 0
        counter = 0
        for i in self.sentence:
            if len(self.input) > input_counter:
                if self.input[input_counter] == i:
                    counter += 1
            input_counter += 1
        n = len(self.sentence)
        accuracy = (counter/n) * 100
        wpm = len(self.input)*60/(self.words*timer)
        return f"Time: {round(timer, 1)} s  Accuracy: {round(accuracy)} %  WPM: {round(wpm)}"

    def center_text(self, text, y):
        font = pygame.font.SysFont("Times New Roman", 24)
        txt = font.render(text, True, (255,255,255))
        rect = txt.get_rect(center=(750/2, y))
        return txt, rect

    def reset(self):
        self.start_time = 0
        self.end_time = 0
        self.sentence = self.get_sentence()
        self.input = ''
        self.words = 1

