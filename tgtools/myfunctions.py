#!/usr/bin/env python
"""General tools/functions for my scripts"""
# ════════════════════════════════════════════
#  ╔╦╗┬─┐┌─┐┌┐┌┌─┐┌─┐┬┬─┐┬    ╔╦╗┌─┐┌─┐┬  ┌─┐
#   ║ ├┬┘├─┤│││└─┐│ ┬│├┬┘│     ║ │ ││ ││  └─┐
#   ╩ ┴└─┴ ┴┘└┘└─┘└─┘┴┴└─┴─┘   ╩ └─┘└─┘┴─┘└─┘
# ════════════════════════════════════════════
#  Functions: common used functions
# ════════════════════════════════════════════
import os
import sys

from colors import Colors
from config import Config


class MyFunctions:
    """A simple list of my porngames"""

    def __init__(self):
        self.terminal_width = 60

    # ----------------------------------------------
    #  Terminal UI functions
    # ----------------------------------------------
    def clear_lines(self, number=1):
        """clear an x number of lines"""
        for _ in range(number):
            print("\033[1A", end="\x1b[2K")

    def colorize(self, text, remove=False):
        """colirize or decolorize a string of text"""
        for color in Colors.colors:
            if remove:
                text = text.replace(color[0], "")
            else:
                text = text.replace(color[0], color[1])
        return text

    def myprint(self, text, clear=False, nl=False):
        """My print function"""
        if clear:
            os.system("clear")
        newline = "\n\n" if nl else "\n"
        text = self.colorize(text)
        print(text, end=newline)

    def draw_line(self, char="╌", color="%c", clear=False, nl=False):
        """draw a line"""
        line = self.terminal_width * char
        self.myprint(f"{color}{line}%R", clear, nl)

    def center_text(self, text, clear=False, nl=False):
        """center a text"""
        left_spaces = ((self.terminal_width - len(text)) // 2) * " "
        self.myprint(f"{left_spaces}{text}", clear, nl)

    def _message(self, prompt, text, clear=False, nl=False):
        """hidden function message"""
        width = self.terminal_width
        # cprompt = self.colorize(prompt, remove=True)
        # s = (7 - len(cprompt)) * " "
        # prompt = f"[{prompt}{s}]"
        prompt = f"[{prompt}]"

        if len(text) > width - 10:
            width -= 12
            width *= -1
            text = ".." + text[width:]
        self.myprint(f"{prompt} {text}", clear, nl)

    def note_message(self, text, clear=False, nl=False):
        """note msg"""
        self._message("%b➔%R", text, clear, nl)

    def ok_message(self, text, clear=False, nl=False):
        """ok msg"""
        self._message("%g✓%R", text, clear, nl)

    def error_message(self, text, clear=False, nl=False):
        """error msg"""
        self._message("%r✗%R", text, clear, nl)

    def warning_message(self, text, clear=False, nl=False):
        """warning msg"""
        self._message("%y!%R", text, clear, nl)

    # ----------------------------------------------
    #  All kinds of checks
    # ----------------------------------------------
    def check_terminal(self, terminal=None):
        """check if terminal exists"""
        for t in Config.TERMINALS:
            if os.path.exists(t):
                break
        if terminal is None:
            print("No terminal detected, exiting...")
            sys.exit(1)
        return terminal

    def check_browser(self, browser=None):
        """check if browser exists"""
        for b in Config.BROWSERS:
            if os.path.exists(b):
                break
        if browser is None:
            print("No browser detected, exiting...")
            sys.exit(1)
        return browser
