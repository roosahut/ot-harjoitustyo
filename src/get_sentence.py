import random


class GetSentence:
    def __init__(self):
        pass

    def get_sentence(self, mode):
        if mode == 1:
            with open("src/sentences_normal.txt", encoding="utf-8") as file:
                file = file.read()
                sentences = file.split("\n")
                pick = random.choice(sentences)
        elif mode == 2:
            with open("src/sentences_hard.txt", encoding="utf-8") as file:
                file = file.read()
                sentences = file.split("\n")
                pick = random.choice(sentences)
        return pick
