from entities.results import Results

from repositories.results_repository import results_repository


class ResultsService:
    """Pelien tuloksista vastaava luokka.
    """
    def __init__(self):
        """Luokan konstruktori.
        """
        self._results_repository = results_repository

    def add_result(self, nickname, mode, amount, time, acc, wpm):
        """Luo uuden pelituloksen tietokantaan Results-olion avulla.

        Args:
            nickname: Pelituloksen pelaajan lempinimi.
            mode: Pelituloksen vaikeustaso.
            amount: Pelituloksen aikana kirjoitettujen lauseiden määrä.
            time: Pelituloksen lauseiden keskiarvo aika.
            acc: Pelituloksen lauseiden keskiarvo oikeellisuus.
            wpm: Pelituloksen lauseiden keskiarvo wpm-nopeus.
        """
        self._results_repository.add_result(
            Results(nickname, mode, amount, time, acc, wpm))

    def get_results(self):
        """Hakee edelliset pelitulokset.

        Returns:
            Palauttaa edelliset tulokset.
        """
        results = self._results_repository.get_results()
        return results


results_service = ResultsService()
