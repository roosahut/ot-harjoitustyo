import random


class GetSentence:
    def __init__(self):
        pass

    def get_sentence(self):
        with open("src/sentences.txt", encoding="utf-8") as file:
            file = file.read()
            sentences = file.split("\n")
            pick = random.choice(sentences)
        return pick
