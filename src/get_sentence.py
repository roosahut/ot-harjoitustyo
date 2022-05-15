import random


class GetSentence:
    """Luokka, joka hakee kansioista lauseen randomilla.
    """

    def get_sentence(self, mode):
        """Funktio, joka avaa kansion, ja ottaa sieltä lauseen randomilla.

        Args:
            mode: Määrää, onko pelaaja valinnut normaalin vai vaikean tason.

        Returns:
            Palauttaa haetun lauseen, joka tulee kirjoittaa.
        """
        if mode == 1:
            with open("src/sentences/sentences_normal.txt", encoding="utf-8") as file:
                file = file.read()
                sentences = file.split("\n")
                pick = random.choice(sentences)
        elif mode == 2:
            with open("src/sentences/sentences_hard.txt", encoding="utf-8") as file:
                file = file.read()
                sentences = file.split("\n")
                pick = random.choice(sentences)
        return pick
