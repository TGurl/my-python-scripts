#!/usr/bin/env python3
"""ARC 2 - A simple way to archive my games"""
import argparse
from utils import Utils
from tui import TUI


class Archiver:
    def __init__(self):
        self.utils = Utils()
        self.tui = TUI()

    def run(self, args):
        try:
            self.utils.main_loop(args)
        except KeyboardInterrupt:
            # self.tui.print_error("CTRL+C detected. Exiting...")
            print()
            self.tui.clearline()
            self.tui.errored_step("CTRL+C detected. Exiting...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("folder", help="Folder to archive")

    parser.add_argument(
        "-d",
        "--destination",
        required=False,
        default="archives",
        choices=["archives", "checked", "usb", "keep"],
        help="Set destination (default archives)",
    )

    parser.add_argument(
        "-y",
        "--yes",
        action="store_true",
        required=False,
        default=False,
        help="Assume yes (default false)",
    )

    parser.add_argument(
        "-c",
        "--clean",
        action="store_true",
        default=False,
        required=False,
        help="Keep the save files (default false)",
    )

    parser.add_argument(
        "-k",
        "--keep",
        action="store_true",
        default=False,
        required=False,
        help="Do not delete source folder (default false)",
    )

    parser.add_argument(
        "-t",
        "--type",
        default='zip',
        choices=['zip', 'tar.gz'],
        required=False,
        help="Type of archive (default zip)",
    )

    arc = Archiver()
    arc.run(parser.parse_args())
