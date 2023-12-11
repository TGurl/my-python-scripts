#!/usr/bin/env python
"""CIA - Convert It All"""

from utils import Utils


class CIA:
    def __init__(self):
        self.utils = Utils()

    def run(self):
        self.utils.main_menu()


if __name__ == "__main__":
    app = CIA()
    app.run()
