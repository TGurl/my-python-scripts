#!/usr/bin/env python
import os
from random import choice

from tui import TUI
from utils import Utils


class StoryTeller:
    def __init__(self):
        self.utils = Utils()
        self.tui = TUI()
        self.responses = [
            "Are you sure you want to do this?",
            "You can certainly try",
            "You rolled a natural one.",
            "Did you know in Nicodranas cupcakes are made with cinamon?",
            "Life needs things to live.",
            "Once I saw this bug carry a piece of bread up the stairs.",
            "I've seen some crazy shit",
            "Is it Thursday yet?",
            "The Ruby of the Sea says 'hello'.",
            "Bees! BEEEES! Bees?",
            "Can I pet you Henry?",
            "Traveller? Don't you like me anymore?",
        ]

    def run(self):
        os.chdir(os.path.expanduser(os.path.join("~", "stories")))

        while True:
            # -- 1: collect the stories
            stories = self.utils.collect_stories()

            # -- 2: define the last story opened
            if self.utils.last_story != "":
                title = self.utils.get_title(self.utils.last_story)
                continue_last = f"Continue %i{title}%R"
                edit_last = f"Edit notes for %i{title}%R"
            else:
                continue_last = "SKIPIT"
                edit_last = "SKIPIT"

            # -- 3: define a list of options
            options = [
                ("c", continue_last),
                ("e", edit_last),
                ("n", "New story"),
                ("d", "Delete story"),
                ("g", "Edit gobal notes"),
            ]

            # --- 4: render header and the menu
            self.tui.render_header()
            valid = self.tui.render_menu(stories, options)

            # -- 5: ask for imput and parse that input
            answer = self.tui.get_input()
            if answer not in valid:
                self.tui.toggle_cursor()
                self.tui.move_up_and_clear()
                self.tui.print_error(f"%i{choice(self.responses)}%R", wait=2)
                self.tui.toggle_cursor()
            else:
                match answer:
                    case "n":
                        self.tui.render_header(clear=True)
                        title = self.tui.get_new_story_info()
                        self.utils.create_new_story(title)
                    case "c":
                        self.utils.continue_story()
                    case "e":
                        self.utils.edit_story_notes()
                    case "d":
                        self.tui.render_header(clear=True)
                        valid = self.tui.render_delete_story_menu(stories)
                        answer = self.tui.get_input(
                            text="Which one do you want to remove?"
                        )
                        if answer not in valid:
                            self.tui.toggle_cursor()
                            self.tui.move_up_and_clear()
                            self.tui.print_error(
                                f"%i{choice(self.responses)}%R", wait=2
                            )
                            self.tui.toggle_cursor()
                        else:
                            self.utils.delete_story(answer)

                    case "g":
                        self.utils.edit_overall_notes()
                    case "q":
                        break
                    case _:
                        self.utils.open_story(answer)


if __name__ == "__main__":
    app = StoryTeller()
    app.run()
