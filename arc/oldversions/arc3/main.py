#!/usr/bin/env python
import argparse
from utils import Utils


class Arc:
    def __init__(self):
        self.utils = Utils()

    def run(self, args):
        try:
            self.utils.zip(args.folder, keep=args.keep, assumeyes=args.yes)
        except KeyboardInterrupt:
            print("Process interrupted!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("folder", help="Folder to archive")
    parser.add_argument("-k", "--keep",
                        action="store_true",
                        help="Keep the source folder when done")
    parser.add_argument("-y", "--yes",
                        action="store_true",
                        help="Assume yes on all questions")

    app = Arc()
    app.run(parser.parse_args())
