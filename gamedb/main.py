#!/usr/bin/env python
import os
import pickle
import json

class GameInfo:
    title: str
    archive: str


class GameDB:
    def __init__(self):
        self.dbname = os.path.expanduser(os.path.join("~", ".local", "share", "gamedb", "database.pickle"))
        self.gamelist = []

    def run(self):
        GameInfo.title = input("game title: ")
        GameInfo.archive = input("archive name: ")
        self.gamelist.append(GameInfo)
        print(self.gamelist)


if __name__ == "__main__":
    app = GameDB()
    app.run()
