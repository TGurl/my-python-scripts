#!/usr/bin/env python3
import argparse
from utils import Utils


class Archiver(Utils):
    def __init__(self):
        super().__init__()

    def run(self, args):
        self.parse_arguments(args)

        self.show_header()
        self.check_if_archived(self.folder)
        self.clear_folder(self.folder)
        archive = self.create_archive(self.folder)
        self.move_file(archive)
        self.delete_source_folder(self.folder)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("folder")

    parser.add_argument(
        "-d",
        "--destination",
        default="archives",
        required=False,
        help="Set destination",
    )

    parser.add_argument("-t", "--type", default="gz", required=False)
    parser.add_argument(
        "-ks",
        "--keep_saves",
        action="store_true",
        default=False,
        required=False,
        help="Keep the save files",
    )
    parser.add_argument(
        "-nd",
        "--no_delete",
        action="store_true",
        default=False,
        required=False,
        help="Don't delete source folder",
    )

    app = Archiver()
    app.run(parser.parse_args())
