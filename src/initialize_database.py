from database_connection import get_database_connection


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


def create_tables(connection):
    cursor = connection.cursor()

    sql_create_results = '''CREATE TABLE results (
        id INTEGER PRIMARY KEY,
        nickname TEXT,
        mode TEXT,
        amount TEXT,
        time TEXT,
        accuracy TEXT,
        wpm TEXT
        )'''
    cursor.execute(sql_create_results)
    connection.commit()


def drop_tables(connection):
    sql_drop_results = '''DROP TABLE IF EXISTS results'''

    connection.execute(sql_drop_results)
    connection.commit()


if __name__ == "__main__":
    initialize_database()
