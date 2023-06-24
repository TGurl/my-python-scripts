#!/usr/bin/env python
from colors import Colors
from tui import TUI

class GameLoop(TUI):
    def __init__(self):
        super().__init__()


    def run(self):
        self.draw_header()

if __name__ == "__main__":
    app = GameLoop()
    app.run()
