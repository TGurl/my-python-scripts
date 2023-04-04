#!/usr/bin/env python
import os
import random
from time import sleep


class Roller:
    def __init__(self):
        self.roll = 0

    def roll20(self):
        self.roll = random.randint(1, 21)

    def roll8(self):
        self.roll = random.randint(1, 9)

    def fake_roll(self):
        for i in range(1, 20):
            os.system('clear')
            roll = random.randint(1, 20)
            print(roll)
            sleep(0.07)
        os.system('clear')

    def run(self):
        self.fake_roll()
        self.roll20()
        print(self.roll)



if __name__ == "__main__":
    roller = Roller()
    roller.run()
