import pygame
import time
import random

class SpeedTyping:
    def __init__(self):
        pass

    def draw_text(self):
        pass

    def get_sentence(self):
        file = open("src/sentences.txt").read()
        sentences = file.split("\n")
        pick = random.choice(sentences)
        return pick