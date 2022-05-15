from get_sentence import GetSentence


class SpeedTyping:
    """Luokka, joka pitää huolta yksittäisen pelin tekstistä ja tuloksista.

    Attributes:
        sentence_mode: Pelin vaikeustaso.
        start_time: Alkaa, kun lausetta aletaan kirjoittamaan.
        end_time: Aika, kun lauseen kirjoitus päättyy ja painetaan enter.
        sentence: Yhteen peliin randomilla valittu lause.
        input: Pelaajan kirjoittama teksti
        words: Kuinka monta sanaa pelaajan kirjoittamassa tekstissä on.
    """

    def __init__(self, sentence_mode):
        """Konstruktori.

        Args:
            sentence_mode: Pelin vaikeustaso.
        """
        self.start_time = 0
        self.end_time = 0
        self.sentence_mode = sentence_mode
        self.sentence = GetSentence().get_sentence(self.sentence_mode)
        self.input = ''
        self.words = 1

    def results(self):
        """Laskee pelaajan kirjoittaman lauseen nopeuden, oikeuden sekä
        kuinka monta sanaa hän kirjoitti minuutissa.

        Returns:
            Palauttaa yhden lauseen tulokset listamuodossa.
        """
        timer = self.end_time - self.start_time
        input_counter = 0
        counter = 0
        for i in self.sentence:
            if len(self.input) > input_counter:
                if self.input[input_counter] == i:
                    counter += 1
            input_counter += 1
        accuracy = (counter/len(self.sentence)) * 100
        wpm = len(self.input)*60/(self.words*timer)
        return [round(timer, 1), round(accuracy), round(wpm)]

    def results_sentence(self):
        """Ilmoittaa tuloksen lausemuodossa.

        Returns:
            Tulokset muotoiltuna lauseena.
        """
        result = self.results()
        return f"Time: {result[0]} s  Accuracy: {result[1]} %  WPM: {result[2]}"

    def count_words(self):
        """Laskee kuinka monta sanaa pelaajan kirjoittamassa lauseessa on.
        """
        if len(self.input) == 0:
            self.words = 1
        else:
            for i in self.input:
                if i == ' ':
                    self.words += 1

    def reset(self):
        """Asettaa pelin tiedot alusta, kun pelaaja painaa Reset-nappia.
        """
        self.start_time = 0
        self.end_time = 0
        self.sentence = GetSentence().get_sentence(self.sentence_mode)
        self.input = ''
        self.words = 1
