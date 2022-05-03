from get_sentence import GetSentence


class SpeedTyping:
    def __init__(self, sentence_mode):
        self.start_time = 0
        self.end_time = 0
        self.sentence_mode = sentence_mode
        self.sentence = GetSentence().get_sentence(self.sentence_mode)
        self.input = ''
        self.words = 1

    def results(self):
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
        return f"Time: {round(timer, 1)} s  Accuracy: {round(accuracy)} %  WPM: {round(wpm)}"

    def count_words(self):
        if len(self.input) == 0:
            self.words = 1
        else:
            for i in self.input:
                if i == ' ':
                    self.words += 1

    def reset(self):
        self.start_time = 0
        self.end_time = 0
        self.sentence = GetSentence().get_sentence(self.sentence_mode)
        self.input = ''
        self.words = 1
