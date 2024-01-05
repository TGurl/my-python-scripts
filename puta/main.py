#!/usr/bin/env python
"""
PUTA 0.0.1
A simple script to manage my porngame collection
"""
import os

import mysql.connector
from pyfzf.pyfzf import FzfPrompt


class DataBase:
    def __init__(self):
        self.debug = True
        self.host = "localhost"
        self.user = "geertje"
        self.password = "cyber008"
        self.database = "gamedb"
        if self.debug:
            self.table = "games_dev"
        else:
            self.table = "games"

    def connect(self):
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        return connection

    def fetch_all(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table}")
        result = cursor.fetchall()
        return result

    def fetch_one(self, haystack, needle) -> tuple:
        result = []
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * from {self.table} WHERE {haystack} = '{needle}'")
        result = cursor.fetchone()
        return result

    def fuzzy_search_db(self, haystack, needle):
        conn = self.connect()
        cursor = conn.cursor()
        query = f"SELECT * FROM {self.table} WHERE {haystack} LIKE '%{needle}%'"
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    def exact_search_db(self, haystack, needle):
        conn = self.connect()
        cursor = conn.cursor()
        query = f"SELECT * FROM {self.table} WHERE {haystack} = '{needle}'"
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    def insert_item(self, values):
        columns = "(title, archive, location, type, fp)"
        values_str = "(%s, %s, %s, %s, %s)"
        sql = f"INSERT INTO {self.table} {columns} VALUES {values_str}"

        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()

        return cursor.lastrowid


class Puta:
    def __init__(self):
        self.database = DataBase()
        self.fzf = FzfPrompt()
        self.usbdir = os.path.join("/", "USB", "sexgames")
        self.loredir = os.path.join("/", "lore", "sexgames")

    def get_gameinfo_by_id(self, idx):
        result = self.database.fetch_one("gid", idx)
        return result

    def show_all_entries(self):
        results = self.database.fetch_all()
        game_list = [game[1] for game in results]
        game = self.fzf.prompt(game_list, "--reverse")
        index = game_list.index(game[0]) + 1
        return index

    def show_location(self, location):
        results = self.database.exact_search_db("location", location)
        for item in results:
            print(item)

    def show_all_female(self):
        results = self.database.exact_search_db("fp", 1)
        for item in results:
            print(item)

    def draw_line(self):
        print(30 * "-")

    def insert_game(self, game_info):
        values = (game_info[0], game_info[1], game_info[2], game_info[3], game_info[4])
        row_id = self.database.insert_item(values)
        print(f"Game added at {row_id}")

    def work(self):
        game_id = self.show_all_entries()
        game_info = self.get_gameinfo_by_id(game_id)
        if game_info[3] == "usb":
            archive = os.path.join(self.usbdir, game_info[2])
        elif game_info[3] == "lore":
            archive = os.path.join(self.loredir, game_info[2])
        print(archive)


if __name__ == "__main__":
    puta = Puta()
    puta.work()
