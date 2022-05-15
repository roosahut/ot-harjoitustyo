class Results:
    """Yksittäistä tulosta kuvaava luokka.

    Attributes:
        nickname: Tuloksen tekijän lempinimi.
        mode: Tuloksen pelin vaikeustaso.
        amount: Pelituloksessa kirjoitettujen lauseiden määrä.
        time: Pelituloksen lauseiden keskiarvo aika
        accuracy: Pelituloksen lauseiden keskiarvo oikeellisuus.
        wpm: Pelituloksen kaikkien lauseiden keskiarvo wpm-nopeus.
    """

    def __init__(self, nickname, mode, amount, time, accuracy, wpm):
        self.nickname = nickname
        self.mode = mode
        self.amount = amount
        self.time = time
        self.accuracy = accuracy
        self.wpm = wpm
