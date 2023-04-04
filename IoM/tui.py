#!/usr/bin/env python
import os

class TUI:
    def __init__(self):
        pass

    def clear_screen(self):
        os.system('clear')

    def draw_line(self):
        line = 79 * "-"
        print(line)

    def show_title(self, title=""):
        self.clear_screen()
        self.draw_line()
        print(title)
        self.draw_line()

    def top_bar(self, items):
        for item in items:
            letter = item[0]
            rest = item[1:]
            print(f"[{letter}]{rest} ", end="")
        print()
        print()

    def end_game(self):
        self.clear_screen()
        print("Thanks for playing...")
        exit()

    def bot_bar(self):
        pass


