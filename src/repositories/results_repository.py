from database_connection import get_database_connection


class ResultsRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_result(self, result):
        cursor = self._connection.cursor()
        sql_insert_result = '''INSERT INTO results (nickname, mode, amount, time, accuracy, wpm)
        VALUES (?, ?, ?, ?, ?, ?)'''
        cursor.execute(sql_insert_result, (result.nickname, result.mode,
                       result.amount, result.time, result.accuracy, result.wpm))
        self._connection.commit()

    def get_results(self):
        cursor = self._connection.cursor()

        sql_find_results = 'SELECT * FROM results ORDER BY id DESC LIMIT 12'
        user_results = cursor.execute(
            sql_find_results).fetchall()
        return user_results


results_repository = ResultsRepository(get_database_connection())
