import os
from colors import Colors
from settings import *


class TUI:
    def __init__(self):
        pass

    def colorize(self, text):
        for color in Colors.colors:
            text = text.replace(color[0], color[1])
        return text

    def decolorize(self, text):
        for code in Colors.codes:
            text = text.replace(code, '')
        return text

    def myprint(self, text, center=False, nl=False):
        newline = '\n\n' if nl else '\n'
        width = os.get_terminal_size().columns
        temp = self.decolorize(text)
        text = self.colorize(text)
        if center:
            spaces = ((width - len(temp)) // 2) * ' '
        else:
            spaces = ''
        print(f"{spaces}{text}", end=newline)

    def drawline(self, nl=False):
        line = (os.get_terminal_size().columns - 1) * '─'
        self.myprint(f"%c{line}%R", nl=nl)

    def generate_info_bars(self):
        topbar = ''
        for key in TOPBAR:
            value = CONFIG[key]
            topbar += f"{key.capitalize()}: {value}  "
        
        botbar = ''
        for key in BOTBAR:
            value = CONFIG[key]
            botbar += f"{key.capitalize()}: {value}  "

        return topbar, botbar

    def draw_header(self):
        topbar, botbar = self.generate_info_bars()
        os.system('clear')
        self.myprint('%yLAURA%R', center=True)
        self.drawline()
        self.myprint(topbar, center=True)
        self.myprint(botbar, center=True)
        self.drawline()
        self.myprint(f"%c[%yH%c]%Rome  %c[%yT%c]%Rown  %c[%yW%c]%Rork  %c[%rQ%c]%Ruit",
                     center=True, nl=True)
