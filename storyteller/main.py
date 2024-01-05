#!/usr/bin/env python
import argparse

from settings import LASTOPENED
from utils import Utils


class StoryTeller(Utils):
    def __init__(self, args):
        self.new_story = args.new_story
        self.continue_story = args.continue_story

    def run(self):
        if self.new_story:
            self.start_newstory()

        if self.continue_story:
            self.open_story(LASTOPENED)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-c",
        "--continue_story",
        action="store_true",
        default=False,
        help="Continue last story",
    )

    parser.add_argument(
        "-n",
        "--new_story",
        action="store_true",
        default=False,
        help="Start a new story",
    )
    app = StoryTeller(parser.parse_args())
    app.run()
