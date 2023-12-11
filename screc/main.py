#!/usr/bin/env python
"""A very basic Screen recorder"""
import argparse

# from config import Config
from functions import Functions


class ScreenRecorder(Functions):  # pylint: disable=too-few-public-methods
    """The main class"""

    def __init__(self, args):
        self.mouse = args.mouse
        self.filename = args.filename

    def run(self):
        """main loop"""
        self.header(mouse=self.mouse)
        self.record_screen(filename=self.filename, mouse=self.mouse)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("filename", help="Title for the recording")
    parser.add_argument(
        "-m",
        "--mouse",
        action="store_true",
        default=False,
        help="Record the mouse cursor (default: False)",
    )

    app = ScreenRecorder(parser.parse_args())
    app.run()
