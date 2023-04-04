#!/usr/bin/env python
from tui import *

class GAME:
    def __init__(self):
        self.tui = TUI()

    def use_computer(self):
        options = [
            "Search internet",
            "Find a job",
            "Bank",
            "Return"
        ]
        use_computer = True
        while use_computer:
            self.tui.show_title(title="MY LAPTOP")
            self.tui.top_bar(options)
            action = input("> ").lower()
            if action in ['r', 'return']:
                use_computer = False
            else:
                pass
