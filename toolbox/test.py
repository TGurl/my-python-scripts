#!/usr/bin/env python
from toolbox import Toolbox


class TestToolbox:
    def __init__(self):
        self.tui = Toolbox()

    def run(self):
        self.tui.render_header('TOOLBOX')
        self.tui.render_header('TOOLBOX', style=1, clear=False)


if __name__ == "__main__":
    app = TestToolbox()
    app.run()
