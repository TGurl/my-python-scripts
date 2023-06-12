#!/usr/bin/env python
##########################################
## Zipr - a simple tool to zip a folder ##
##########################################
from utils import Utils
from settings import *
import argparse

class Zipr():
    def __init__(self, args):
        self.utils = Utils()
        self.folder = args.folder
        self.dest = args.dest
        self.keep = args.keep
        self.nocheck = args.nocheck
        self.clearsaves = args.clearsaves

    def run(self):
        self.utils.show_title()
        self.utils.zipfolder(self.folder, self.dest, self.nocheck, self.keep, self.clearsaves)
        self.utils.print_message('All done', style='info')
        self.utils.show_quote()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--folder',
                        required=True,
                        help='Folder to zip')
    parser.add_argument('-d', '--dest',
                        required=False,
                        default='archives',
                        help='Destination for the zipfile')
    parser.add_argument('-k', '--keep',
                        action='store_true',
                        default=False,
                        required=False,
                        help='Keep the source folder')
    parser.add_argument('-cs', '--clearsaves',
                        default=True,
                        required=False,
                        help='Clear save files')
    parser.add_argument('-nc', '--nocheck',
                        action='store_true',
                        default=False,
                        required=False,
                        help='Check the archive')
    args = parser.parse_args()

    app = Zipr(args)
    app.run()
