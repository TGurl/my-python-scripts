#!/usr/bin/env python
# ════════════════════════════════════════════
#  ╔╦╗┬─┐┌─┐┌┐┌┌─┐┌─┐┬┬─┐┬    ╔╦╗┌─┐┌─┐┬  ┌─┐
#   ║ ├┬┘├─┤│││└─┐│ ┬│├┬┘│     ║ │ ││ ││  └─┐
#   ╩ ┴└─┴ ┴┘└┘└─┘└─┘┴┴└─┴─┘   ╩ └─┘└─┘┴─┘└─┘
# ════════════════════════════════════════════
#  Porngames : collection of porn games
# ════════════════════════════════════════════
from time import sleep

from myfunctions import MyFunctions


class PornGames(MyFunctions):
    """A simple list for my porngames"""

    def __init__(self):
        super().__init__()
        self.browser = self.check_browser()
        self.terminal = self.check_terminal()

    def main(self) -> None:
        """The main loop"""
        self.draw_line(clear=True)
        self.center_text("Porngames v5 - Transgirl 2023")
        self.draw_line()
        self.note_message("Reading files in folder")
        sleep(1.5)
        self.clear_lines()
        self.ok_message("Collected files in folder")
        sleep(1.5)
        self.note_message("Creating zip file")
        sleep(2.5)
        self.clear_lines()
        self.ok_message("Zipfile created")
        self.warning_message("Zipfile exceeds 40Gib Size!")


if __name__ == "__main__":
    app = PornGames()
    app.main()
