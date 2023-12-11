#!/usr/bin/env python
# ════════════════════════════════════════════
#  ╔╦╗┬─┐┌─┐┌┐┌┌─┐┌─┐┬┬─┐┬    ╔╦╗┌─┐┌─┐┬  ┌─┐
#   ║ ├┬┘├─┤│││└─┐│ ┬│├┬┘│     ║ │ ││ ││  └─┐
#   ╩ ┴└─┴ ┴┘└┘└─┘└─┘┴┴└─┴─┘   ╩ └─┘└─┘┴─┘└─┘
# ════════════════════════════════════════════
#  Bookmarks : collect urls to favorite sites
# ════════════════════════════════════════════
import os
import sys
from myfunctions import MyFunctions


class Bookmarks(MyFunctions):
    def __init__(self):
        super().__init__()
        self.browser = self.check_browser()
        self.terminal = self.check_terminal()
        
    def run(self):
        pass


if __name__ == "__main__":
    app = Bookmarks()
    app.run()
