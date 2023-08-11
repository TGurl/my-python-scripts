import os
from colors import Colors

class Utils:
    def __init__(self):
        pass

    def render_title(self):
        os.system('clear')
        self.myprint(f"%c╭────────────────────────────╮")
        self.myprint(f"│ %yARC v0.01%R - %bTransgirl 2023 %c│")
        self.myprint(f"╰────────────────────────────╯%R", nl=True)

    def render_done(self):
        self.clear_line()
        self.myprint(" %g>%R All done!")

    def show_step_start(self, text, nl=False, style=1):
        prompt = f" %y>%R" if style == 1 else f"   %b└>%R"
        self.myprint(f"{prompt} {text}", clear=True, nl=nl)

    def show_step_end(self, text):
        prompt = f" %g>%R"
        self.myprint(f"{prompt} {text}", clear=True, nl=True)

    def format_bytes(self, size):
        power = 2**10
        n = 0
        power_labels = {0: 'b', 1: 'Kb', 2: 'Mb', 3: 'Gb', 4: 'Tb'}
        while size > power:
            size /= power
            n += 1
        size = str(round(size, 2))
        return f"{size} {power_labels[n]}"

    def colorize(self, text):
        for color in Colors.colors:
            text = text.replace(color[0], color[1])
        return text

    def clear_line(self):
        LINE_UP = '\033[1A'
        LINE_CLEAR = '\x1b[2K'
        print(LINE_UP, end=LINE_CLEAR)

    def myprint(self, text, nl=False, clear=False):
        newline = '\n\n' if nl else '\n'
        text = self.colorize(text)
        if clear: self.clear_line()
        print(text, end=newline)
