#!/usr/bin/env python
from utils.utils import Utils
from time import sleep


class StoryTeller(Utils):
    def __init__(self):
        super().__init__()

    def run(self):
        running = True
        while running:
            response = self.main_menu()
            if response is False:
                running = False
            else:
                print(response)
                sleep(2)


if __name__ == "__main__":
    app = StoryTeller()
    app.run()
