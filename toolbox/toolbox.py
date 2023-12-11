import os

from colors import Colors


class Toolbox:
    def __init__(self):
        pass
    
    # ------------------------------------------------------
    # -- Render a header
    # ------------------------------------------------------
    def render_header(self, text, colborder='%c', coltitle='%y', clear=True, style=2):
        if clear:
            os.system('clear')
        
        horline = (len(text) + 2) * "─"

        if style == 1:
            lines = [
                f"{colborder}┌{horline}┐",
                f"│ {coltitle}{text} {colborder}│",
                f"└{horline}┘%R",
            ]
        else:
            lines = [
                f"{colborder}╭{horline}╮",
                f"│ {coltitle}{text} {colborder}│",
                f"╰{horline}╯%R",
            ]

        for line in lines:
            self.myprint(line)

    # ------------------------------------------------------
    # -- UI functions
    # ------------------------------------------------------
    def colorize(self, text):
        for color in Colors.colors:
            text = text.replace(color[0], color[1])
        return text

    def decolorize(self, text):
        for code in Colors.codes:
            text = text.replace(code, "")
        return text

    def myprint(self, text, nl=False):
        newline = '\n\n' if nl else '\n'
        text = self.colorize(text)
        print(text, end=newline)

    def move_up_and_clear(self):
        print('\033[1A', end='\x1b[2K')
