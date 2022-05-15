import sqlite3
from config import DATABASE_FILE_PATH

connect = sqlite3.connect(DATABASE_FILE_PATH)
connect.row_factory = sqlite3.Row


def get_database_connection():
    return connect
