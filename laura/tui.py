import readchar
from colors import Colors



class TUI:
    def __init__(self):
        self.cursor = True

    def colorize(self, text):
        for color in Colors.colors:
            text = text.replace(color[0], color[1])
        return text

    def decolorize(self, text):
        for code in Colors.codes:
            text = text.replace(code, '')
        return text

    def clearline(self, num=1):
        for _ in range(num):
            print('\033[1A', end='\x1b[2K')

    def myprint(self, text, nl=False, clear=False, noreturn=False):
        newline = '\n\n' if nl else '\n'
        newline = '' if noreturn else newline
        if clear:
            self.clearline()
        text = self.colorize(text)
        print(text, end=newline)

    def keyprint(self):
        return readchar.readkey()

    def getyesno(self, text):
        while True:
            self.myprint(text, noreturn=True)
            key = self.keyprint()
            if key.lower() not in ['y', 'n']:
                print('Ooops')
                self.clearline()
            else:
                break
        return True if key == 'y' else False

    def toggle_cursor(self):
        if self.cursor:
            print('\033[? 25l', end="")
            self.cursor = False
        else:
            print('\033[? 25h', end="")
            self.cursor = True
