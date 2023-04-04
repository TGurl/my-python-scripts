#!/usr/bin/env python
import os
from dataclasses import dataclass


@dataclass
class Girl:
    age: int
    money: int
    sexy: int
    innocense: int


@dataclass
class MC(Girl):
    name: str


@dataclass
class Config:
    init = True


class Game:
    def __init__(self):
        self.game_version = "v0.0.1"

    def show_intro(self):
        os.system('clear')
        print(f"Laura {self.game_version}")
        print()
        print("Welcome to my simple game. In this game you play Laura, a simple girl from a small town.")
        print("You've always dreamed of living in the big city and now you have the chance of doing just that.")
        print("Can you keep your innocense?")
        exit()


class Laura:
    def __init__(self):
        self.game = Game()

    def initialize(self):
        MC.age = 18
        MC.money = 10
        MC.sexy = 0
        MC.innocense = 0
        MC.name = "Laura"

    def run(self):
        if Config.init:
            self.initialize()
            Config.init = False

        self.game.show_intro()


if __name__ == "__main__":
    app = Laura()
    app.run()
