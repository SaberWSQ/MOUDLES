"""
Program: database_test.py
Author: Shiqi Wang
Last date modified: 12/12/2020

The purpose of this program is to test methods from class Database
"""
import unittest
from main.Database import Database


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.database = Database("test_log.db")

    def tearDown(self):
        del self.database

    def test_create_table(self):
        self.database.create_table()
        cur = self.database.conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        self.assertEqual(cur.fetchall(), [('history', )])

    def test_create_record(self):
        self.database.create_table()
        cur = self.database.conn.cursor()
        cur.execute("DELETE FROM history")

        record = ("2020-12-01 06:10:02", "course", str(["source"]))
        self.database.create_record(record)

        cur.execute("SELECT * FROM history")
        self.assertEqual(len(cur.fetchall()), 1)

    def test_select_record_by_word(self):
        self.database.create_table()
        cur = self.database.conn.cursor()
        cur.execute("DELETE FROM history")
        record = ("2020-12-01 06:10:02", "course", str(["source"]))
        self.database.create_record(record)
        res = self.database.select_record_by_word("course")
        self.assertEqual(res, [(1, '2020-12-01 06:10:02', 'course', "['source']")])


if __name__ == '__main__':
    unittest.main()
