#!/usr/bin/env python3
import argparse
from utils import Utils


class WallhavenDL:
    def __init__(self):
        self.utils = Utils()

    def run(self, args):
        if args.query == "":
            self.utils.render_questionaire()
        else:
            self.utils.assume_defaults(args.query)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-q", "--query", default="", required=False, help="What to search for"
    )
    app = WallhavenDL()
    app.run(parser.parse_args())
