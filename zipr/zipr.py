#!/usr/bin/env python3
"""Zipr - A simple script to archive porngames"""

import os, sys
from utils import Utils
import argparse


class Main(Utils):
    def __init__(self):
        super().__init__()

    def run(self, args):
        zipfile = args.folder
        if '.zip' not in zipfile:
            zipfile = args.folder + '.zip'

        self.show_title()

        # 1. Parse the destination given
        match args.dest.lower():
            case 'usb': destination = os.path.join('~', 'USB', 'sexgames')
            case 'keep': destination = os.path.join('~', 'USB', 'sexgames', 'keep')
            case 'archives': destination = os.path.join('~', 'Games', 'archives')
            case _:
                self.print_error('An unknown destination given, exiting...')
                sys.exit(1)

        # 2. Check if an archive with that name already exists in temp directory
        self.check_temp_directory(zipfile)

        # 3. Check if an archive with that name has already been archived
        self.check_archives_for_zipfile(zipfile, args.yes)

        # 4. Clear the save files from the game
        self.clear_saves(zipfile)

        # 5. Create the archive
        self.create_zip(zipfile)

        # 6. Check the archive for errors
        self.check_zip_archive(zipfile)

        # 7. Move the archive to destination
        self.move_archive(zipfile, destination, args.keep, args.nosync)

        # 8. All done.
        self.print_message('All done.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('folder',
                        help='folder to zip')

    parser.add_argument('-d', '--dest',
                        type=str,
                        required=True,
                        default='archives',
                        help='where to store the archive'
                        )

    parser.add_argument('-k', '--keep',
                        action='store_true',
                        required=False,
                        default=False,
                        help='keep the source folder')

    parser.add_argument('-y', '--yes',
                        action='store_true',
                        required=False,
                        default=False,
                        help='Assume yes for any questions')

    parser.add_argument('-ns', '--nosync',
                        action='store_true',
                        required=False,
                        default=False,
                        help='Do not sync after moving to usb')

    app = Main()
    app.run(parser.parse_args())
