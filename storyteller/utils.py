#!/usr/bin/env python
import os

from settings import *


class Utils:
    def __init__(self):
        pass

    def printf(self, text, new_line=False):
        cariage_return = "\n\n" if new_line else "\n"
        print(text, end=cariage_return)

    def banner(self, clear=True):
        if clear:
            os.system("cls" if os.name == "nt" else "clear")
        title_line = f"{TITLE} {VERSION} - copyright 2023 Transgirl"
        line = (len(title_line) + 2) * "-"
        print(line)
        print(f" {title_line}")
        print(line)

    def collect_all_stories(self):
        stories = []
        for item in os.scandir(STORYDIR):
            if not os.path.isdir(item) and os.path.splitext(item)[1] == ".md":
                stories.append(item.name)
        return stories

    def open_story(self, file_name=""):
        story_name, ext = os.path.splitext(file_name)

        file_name = os.path.join(STORYDIR, file_name)
        story_notes = os.path.join(STORYDIR, story_name + "_notes" + ext)
        global_notes = os.path.join(STORYDIR, "global_notes.md")
        os.system(f"vim -p {file_name} {story_notes} {global_notes}")

    def start_newstory(self):
        self.banner()
        story_name = input("What is the title of your new story? : ").lower()
        story_notes = story_name + "_notes.md"
        title = story_name.upper()
        story_name = story_name + ".md"

        with open(os.path.join(STORYDIR, story_name), "w", encoding="utf8") as story:
            story.write(f"# {title}\n")
            story.write("_an erotic tale by Transgirl_\n\n")
            story.write("## Disclaimer\n\n")
            for line in DISCLAIMER:
                story.write(line)
            story.write("## Chapter One\n\n")

        with open(os.path.join(STORYDIR, story_notes), "w", encoding="utf8") as notes:
            notes.write(f"# {title} NOTES\n\n")

        LASTOPENED = story_name
        config = {"lastopened": LASTOPENED}
        self.open_story(story_name)
