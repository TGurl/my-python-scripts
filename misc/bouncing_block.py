#!/usr/bin/env python

from shutil import get_terminal_size

class BouncingBlock:
    def __init__(self):
        self.columns = get_terminal_size().columns
        self.rows = get_terminal_size().lines

    def run(self):
        print(self.columns)
        print(self.rows)


if __name__ == "__main__":
    app = BouncingBlock()
    app.run()