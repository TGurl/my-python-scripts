#!/usr/bin/env python
import json
import os
import pickle


class GameInfo:
    idx: int = 0
    title: str
    archive: str


class GameDB:
    def __init__(self):
        self.dbname = os.path.expanduser(
            os.path.join("~", ".local", "share", "gamedb", "database.pickle")
        )
        self.gamelist = []

    def run(self):
        while True:
            GameInfo.idx += 1
            GameInfo.title = input("game title: ")
            GameInfo.archive = input("archive name: ")
            self.gamelist.append(
                {
                    "index": GameInfo.idx,
                    "title": GameInfo.title,
                    "archive": GameInfo.archive,
                }
            )
            print(self.gamelist)


if __name__ == "__main__":
    app = GameDB()
    app.run()
