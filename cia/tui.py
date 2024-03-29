import os
import sys
import math

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

    def askyesno(self, msg):
        prompt = self.colorize(f" [%y-%R] {msg} (y/n) : ")
        self.clearline()
        while True:
            answer = input(prompt).lower()
            if answer not in ["yes", "y", "no", "n"]:
                self.print_error("That's not a valid answer...")
                sleep(2)
                self.clearline()
                self.clearline()
            else:
                break

        return True if answer in ["yes", "y"] else False

    def menu_header(self, title, maxlength=30):
        title_length = len(self.decolorize(title))
        title = self.colorize(title)

        line_length = (maxlength - title_length) // 2
        line = line_length * "─"
        header = f"%c{line}%R {title} %c{line}%R"
        # self.myprint(header)
        return header

    def render_header(self):
        lines = [
            "%c╭──────────────────────────╮",
            "│   %yCIA%R - %gConvert It All   %c│",
            "│ %RCopyright 2023 Transgirl %c│",
            "╰──────────────────────────╯%R",
        ]
        os.system("clear")
        for line in lines:
            self.myprint(line)

    def decolorize(self, text):
        for code in Colors.codes:
            text = text.replace(code, "")
        return text

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

    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_names = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        # return "%s %s" % (s, size_names[i])
        return f"{s:.2f} {size_names[i]}"
