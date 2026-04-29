# db_proxy.py

import sqlite3
from code.settings import DB_NAME


class DbProxy:
    def __init__(self):
        self.db_name: str = DB_NAME

        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `results` (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            deleted_at DATETIME,
            player_name TEXT NOT NULL,
            score INTEGER NOT NULL,
            last_level TEXT NOT NULL,
            is_winner BOOLEAN NOT NULL DEFAULT FALSE,
            date TEXT NOT NULL)
            ''')

    def save_results(self, result_dict: dict):
        self.cursor.execute("""INSERT INTO `results` (
            player_name, score, last_level, is_winner, date) VALUES (
            :player_name, :score, :last_level, :is_winner, :date)
            """, result_dict)
        self.connection.commit()

    def retrieve_top10(self):
        return self.cursor.execute("""SELECT player_name, score, last_level, is_winner, date FROM `results` 
            WHERE deleted_at IS NULL ORDER BY score DESC LIMIT 10
            """).fetchall()

    def retrieve_winners_top10(self):
        return self.cursor.execute("""SELECT player_name, score, last_level, is_winner, date FROM `results` 
            WHERE deleted_at IS NULL AND is_winner ORDER BY score DESC LIMIT 10
            """).fetchall()

    def close_connection(self):
        self.connection.close()
