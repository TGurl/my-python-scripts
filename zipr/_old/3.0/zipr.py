#!/usr/bin/env python
from classes import FileIO, Zipit
import argparse

def main(args):
    fileio = FileIO()
    check = False if args.nocheck else True

    zipit = Zipit(args.folder, check)

    zipit.start()
    fileio.move_file(f"{args.folder}.zip", args.destination.lower(), args.keep)

    print("> All done")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('folder', type=str,
                        help='Folder to zip')

    parser.add_argument('-d', '--destination',
                        default='archives',
                        type=str,
                        required=False,
                        help='Final destination')

    parser.add_argument('-nc', '--nocheck',
                        action='store_true',
                        default=False,
                        required=False,
                        help="Don't check the archive")

    parser.add_argument('-k', '--keep',
                        action='store_true',
                        default=False,
                        required=False,
                        help='Keep the source after')

    args = parser.parse_args()
    main(args)
