import os
import sys
from colors import Colors
from time import sleep


class TUI:
    def __init__(self):
        self.cursor = True

    def print_error(self, msg, quit=False):
        spaces = 2 * " "
        msg = f"{spaces}%r»%R {msg}"
        self.myprint(msg)
        if quit:
            sys.exit()

    def print_warning(self, msg, quit=False):
        spaces = 2 * " "
        msg = f"{spaces}%y»%R {msg}"
        self.myprint(msg)
        if quit:
            sys.exit()

    def print_message(self, msg, quit=False):
        spaces = 2 * " "
        msg = f"{spaces}%g»%R {msg}"
        self.myprint(msg)
        if quit:
            sys.exit()

    def get_input(self, prompt):
        result = input(self.colorize(prompt) + " : ").lower()
        return result

    def askyesno(self, msg, defyes=True):
        yesno = "Y/n" if defyes else "y/N"
        prompt = self.colorize(f"{msg} ({yesno}) : ")
        while True:
            answer = input(prompt).lower()
            if answer not in ["yes", "y", "no", "n", ""]:
                self.print_error("That's not a valid answer...")
                sleep(2)
            else:
                break
        if answer == "" and defyes:
            return True
        elif answer == "" and not defyes:
            return False
        elif answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("unknown error at line 55")

    def render_header(self):
        lines = [
            "%c╭──────────────────────────╮",
            "│       %yWALLHAVEN_DL%c       │",
            "│ %RCopyright 2023 Transgirl %c│",
            "╰──────────────────────────╯%R",
        ]
        os.system("clear")
        for line in lines:
            self.myprint(line)

    def colorize(self, text):
        for color in Colors.colors:
            text = text.replace(color[0], color[1])
        return text

    def myprint(self, text, nl=False):
        newline = "\n\n" if nl else "\n"
        text = self.colorize(text)
        print(text, end=newline)

    def clearline(self):
        print("\033[1A", end="\x1b[2K")

    def toggle_cursor(self):
        if self.cursor:
            print("\033[? 25l", end="")
            self.cursor = False
        else:
            print("\033[? 25h", end="")
            self.cursor = True
