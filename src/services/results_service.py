from entities.results import Results

from repositories.results_repository import results_repository

class ResultsService:
    def __init__(self):
        self._results_repository = results_repository

    def add_result(self, nickname, mode, amount, time, accuracy, wpm):
        result = self._results_repository.add_result(Results(nickname, mode, amount, time, accuracy, wpm))
        return result
    
    def get_results(self):
        results = self._results_repository.get_results()
        return results

results_service = ResultsService()