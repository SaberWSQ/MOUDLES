"""
Program: Database.py
Author: Shiqi Wang
Last date modified: 12/12/2020

The purpose of this program is to write a Database class to save and search data
"""
import sqlite3
from sqlite3 import Error
from datetime import datetime

class Database:
    def __init__(self, database_file_name):
        self.conn = None
        self.create_connection(database_file_name)

    def create_connection(self, db):
        """ Connect to a SQLite database
        :param db: filename of database
        :return None
        """
        try:
            self.conn = sqlite3.connect(db)
        except Error as err:
            print(err)

    def create_table(self):
        """Create a table name history if it doesn't exist in the database
        :return: None
        """
        sql_create_history_table = """CREATE TABLE IF NOT EXISTS history (
                                        id integer PRIMARY KEY,
                                        created_at timestamp,
                                        search_word text NOT NULL,
                                        result test NOT NULL);
                                    """
        if self.conn is not None:
            try:
                c = self.conn.cursor()
                c.execute(sql_create_history_table)
            except Error as e:
                print(e)

        self.conn.commit()

    def create_record(self, record):
        """Insert a new record of searching into the history table
        :param tuple record: (created_at, search_word, result)
        :return: record id, integer
        """
        sql = ''' INSERT INTO history(created_at, search_word, result)
                      VALUES(?, ?, ?) '''
        cur = self.conn.cursor()
        cur.execute(sql, record)
        self.conn.commit()
        return cur.lastrowid

    def select_record_by_word(self, word):
        cur = self.conn.cursor()
        sql = """SELECT * FROM history WHERE search_word = ?"""
        cur.execute(sql, (word, ))

        # get all results
        rows = cur.fetchall()
        return rows
