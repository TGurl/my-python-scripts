#!/usr/bin/env python
from tui import TUI

class Test(TUI):
    def __init__(self):
        super().__init__()

    def run(self):
        self.getyesno('Does this work? (y/n) :')


if __name__ == "__main__":
    app = Test()
    app.run()
