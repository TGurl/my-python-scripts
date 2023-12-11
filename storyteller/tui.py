import os

from colors import Colors
from time import sleep
from random import choice


class TUI:
    def __init__(self):
        self.cursor = True

    def get_new_story_info(self):
        title = self.get_input("%wPlease give the title for the new story.%R")
        return title

    def not_implemented(self):
        self.toggle_cursor()
        self.move_up_and_clear()
        self.print_error("Not yet implemented.", wait=2)
        self.toggle_cursor()

    def print_message(self, text, nl=False):
        prompt = self.colorize(f"  %g»%R {text}")
        self.myprint(prompt, nl=nl)

    def print_warning(self, text, nl=False):
        prompt = self.colorize(f"  %y»%R {text}")
        self.myprint(prompt, nl=nl)

    def print_error(self, text, wait=0, nl=False):
        sp = 2 * " "
        prompt = self.colorize(f"{sp}%r»%R {text}")
        self.myprint(prompt, nl=nl)
        if wait > 0:
            sleep(wait)

    def get_input(self, text=""):
        sp = 2 * " "
        if text != "":
            self.print_message(f"{self.colorize(text)}")
            self.print_warning("%iLeave empty to return to main menu")
            print()

        prompt = self.colorize(f"{sp}%g»%R ")
        result = input(prompt).lower().strip()
        return result

    # -- render the menu
    def render_menu(self, stories, options):
        valid_options = []
        rendered_stories = True if len(stories) else False

        for num, title in enumerate(stories, start=1):
            title = title.split("/")[-1].replace("_", " ").replace(".md", "").title()
            self.myprint(f" %c[%y{num}%c]%R {title}")
            valid_options.append(str(num))

        if rendered_stories:
            print()

        for option in options:
            if option[1] == 'SKIPIT':
                continue
            self.myprint(f" %c[%y{option[0]}%c]%R {option[1]}")
            if "Edit note" in option[1]:
                print()
            valid_options.append(option[0])

        print()
        self.myprint(" %c[%rq%c]%R Quit")
        valid_options.append("q")

        print()
        return valid_options

    def render_delete_story_menu(self, stories):
        valid_options = [""]
        for num, title in enumerate(stories, start=1):
            title = title.split("/")[-1].replace("_", " ").replace(".md", "").title()
            self.myprint(f" %c[%y{num}%c]%R {title}")
            valid_options.append(str(num))
        print()

        return valid_options

    def render_header(self, clear=True):
        if clear:
            os.system("clear")
        colors = ["%c", "%y", "%y", "%b", "%g"]
        col = choice(colors)
        self.myprint(f"{col}╭──────────────────────────╮")
        self.myprint("│     Storyteller v0.6     │")
        self.myprint(f"│ %RCopyright 2023 Transgirl {col}│")
        self.myprint("╰──────────────────────────╯%R", nl=True)

    # -- some general fucntions
    def colorize(self, text):
        for color in Colors.colors:
            text = text.replace(color[0], color[1])
        return text

    def myprint(self, text, nl=False):
        newline = "\n\n" if nl else "\n"
        text = self.colorize(text)
        print(text, end=newline)

    def move_up_and_clear(self, num=1):
        for _ in range(num):
            print("\033[1A", end="\x1b[2K")

    def toggle_cursor(self):
        if self.cursor:
            print("\033[? 25l", end="")
            self.cursor = False
        else:
            print("\033[? 25h", end="")
            self.cursor = True
