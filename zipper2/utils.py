#!/usr/bin/env python
import os
import sys
import math
from colors import Colors


class Utils:
    def __init__(self):
        self.cursor = True

    def toggle_cursor(self) -> None:
        if self.cursor:
            print('\033[?25l', end='')
            self.cursor = False
        else:
            print('\033[?25h', end='')
            self.cursor = True

    def colorize(self, text):
        for code in Colors.colors:
            text = text.replace(code[0], code[1])
        return text

    def decolorize(self, text):
        for code in Colors.codes:
            text = text.replace(code, '')
        return text

    def movelineup_clear(self):
        sys.stdout.write('\x1b[1A')  # move one line up
        sys.stdout.write('\x1b[2K')  # clear that line

    def render_progressbar(self, progress, total, barlength=10, style=1):
        match style:
            case 2:
                chars = ('>' '.')
            case 3:
                chars = ('█', '░')
            case 4:
                chars = ('🯉', '🯅')
            case 5:
                chars = ('○', '·')
            case _:
                chars = ('#', '-')

        percentage = int(progress * 100 / total)
        num = percentage // 10
        full = num * chars[0]
        empty = (barlength - num) * chars[1]
        bar = full + empty
        return f"[{percentage:3}%] [{bar}]"

    def box(self, text, style=1):
        match style:
            case 2:
                boxchar = ('╔', '╗', '╚', '╝', '║', '═')
            case 3:
                boxchar = ('╒', '╕', '╘', '╛', '│', '═')
            case 4:
                boxchar = ('╓', '╖', '╙', '╜', '║', '─')
            case 5:
                boxchar = ('╭', '╮', '╰', '╯ ', '│', '─')
            case _:
                boxchar = ('┌', '┐', '└', '┘', '│', '─')

        length = len(text) + 2
        horline = length * boxchar[5]
        verline = '%c' + boxchar[4] + f" %y{text}%R %c" + boxchar[4] + '%R'
        topline = '%c' + boxchar[0] + horline + boxchar[1] + '%R'
        botline = '%c' + boxchar[2] + horline + boxchar[3] + '%R'
        return topline, botline, verline

    def myprint(self, text, clearline=False, center=False, nl=False):
        newline = '\n\n' if nl else '\n'
        tw = os.get_terminal_size().columns
        spaces = ''
        temp = self.decolorize(text)
        text = self.colorize(text)

        if center:
            spaces = ((tw - len(temp)) // 2) * " "

        if clearline:
            self.movelineup_clear()

        print(f"{spaces}{text}", end=newline)

    def title(self, title, clear=False, center=False, style=1):
        if clear:
            os.system('clear')

        topline, botline, verline = self.box(title, style=style)
        self.myprint(topline, center)
        self.myprint(verline, center)
        self.myprint(botline, center, nl=True)

    def print_msg(self, text, clearline=False, nl=False):
        msg = f"%y›%R {text}"
        self.myprint(msg, clearline=clearline, nl=nl)

    def print_err(self, text, clearline=False, nl=False):
        msg = f"%r»%R {text}"
        self.myprint(msg, clearline=clearline, nl=nl)

    def print_info(self, text, clearline=False, nl=False):
        msg = f"%g›%R {text}"
        self.myprint(msg, clearline=clearline, nl=nl)

    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = (
                "B", "KiB", "MiB", "GiB", "TiB",
                "PiB", "EiB", "ZiB", "YiB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])
