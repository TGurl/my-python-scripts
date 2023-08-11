#!/usr/bin/env python
"""A simple script to change the wallpaper"""

import os
import sys
import argparse
from utils import Utils


def main(args):
    utils = Utils()

    if args.next:
        utils.next_wallpaper()
    elif args.previous:
        utils.previous_wallpaper()
    elif args.setup:
        utils.setup()
    else:
        utils.info()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='wp',
                                     description='Easily set wallpapers',
                                     epilog='Trans rights are human rights')

    group = parser.add_mutually_exclusive_group()

    group.add_argument('-n', '--next',
                        action='store_true',
                        default=False,
                        required=False,
                        help='go to next wallpaper')
    
    group.add_argument('-p', '--previous',
                        action='store_true',
                        default=False,
                        required=False,
                        help='go to previous wallpaper')

    group.add_argument('-s', '--setup',
                        action='store_true',
                        default=False,
                        required=False,
                        help='enter setup')

    main(parser.parse_args())
