#!/usr/bin/env python3
"""ARC a simple script to archive folders recursively"""

# ---------------------------------------------------------
# imports
# ---------------------------------------------------------
import os
import sys
import glob
import tarfile
import argparse
from shutil import rmtree
from utils import Utils


class Archiver(Utils):
    def __init__(self):
        super().__init__()
        self.locations = [os.path.join('~', 'USB', 'sexgames'),
                          os.path.join('~', 'USB', 'sexgames', 'keep'),
                          os.path.join('~', 'Games', 'archives')]

    def read_folder(self, folder):
        items = glob.glob(f"{folder}/**", recursive=True, include_hidden=True)
        return items

    def check_if_already_in_archives(self, folder, ftype='gz'):
        ftype = 'gz' if ftype == '' else ftype
        arcname = f"{folder}.tar.{ftype}"
        zipname = f"{folder}.zip"

        # self.show_step_start(f'Checking if {arcname} or {zipname} has been archived...')
        self.show_step_start(f'Checking...')

        found_items = []
        for location in self.locations:
            for item in os.listdir(os.path.expanduser(location)):
                if f".{ftype}" or ".zip" in item:
                    if item == arcname or item == zipname:
                        found_items.append(os.path.join(location, item))
        if found_items:
            for item in found_items:
                os.remove(os.path.expanduser(item))
            self.show_step_end('Old archives cleared')
        else:
            self.show_step_end('No old archives found')

    def create_archive(self, folder, ftype='gz'):
        ftype = 'gz' if ftype == '' else ftype
        filename = f"{folder}.tar.{ftype}"

        if os.path.exists(filename):
            # If an archive by that name already exists in current directory, remove it
            os.remove(filename)

        self.show_step_start(f'Creating archive %i{filename}%R', nl=True)
        contents = self.read_folder(folder)
        total = len(contents)
        lead = len(str(total))
        tar = tarfile.open(f"{filename}", f"w:{ftype}")
        for num, item in enumerate(contents, start=1):
            percent = int(num * 100 / total)
            it = "..." + item[-27:] if len(item) > 30 else item
            self.show_step_start(f"adding {num:{lead}}/{total} [{percent:3}%]: {it}", style=2)
            tar.add(item, recursive=False)
        tar.close()
        size = self.format_bytes(os.stat(f"{folder}.tar.{ftype}").st_size)
        self.clear_line()
        self.show_step_end(f"Archive %i{filename}%R created ({size})")

    def move_archive(self, folder, destination, ftype='gz'):
        ftype = 'gz' if ftype == '' else ftype
        archive_name = f"{folder}.tar.{ftype}"
        short_dest = destination
        destination = os.path.expanduser(
                os.path.join(destination, archive_name))
        source_size = os.stat(archive_name).st_size
        copied = 0
        perc = 0
        source = open(archive_name, 'rb')
        target = open(destination, 'wb')

        self.show_step_start(f"Moving {archive_name} -> {short_dest} [{perc:3}%]")

        while True:
            chunk = source.read(32768)
            if not chunk:
                break
            target.write(chunk)
            copied += len(chunk)
            perc = int(copied * 100 / source_size)
            self.show_step_start(f"Moving {archive_name} -> {short_dest} [{perc:3}%]")

        source.close()
        target.close()

        if 'USB' in destination:
            self.show_step_start("Syncing to complete the move...")
            os.system('sync')

        self.show_step_start("Removing temporary archive...")
        os.remove(archive_name)

        self.show_step_end(f"{archive_name} moved to {short_dest}")

    def clear_save_files(self, folder, keepsaves=False):
        if keepsaves:
            self.show_step_end("Keeping the save files")
        else:
            self.show_step_start(f"Clearing save and log files...")
            savefiles = glob.glob(f"{folder}/**/**.save", recursive=True)
            logfiles = glob.glob(f"{folder}/log.txt", recursive=True)
            renpyfolder = os.path.join('~', '.renpy')

            if len(savefiles) > 0 or len(logfiles) > 0:
                if os.path.exists(renpyfolder):
                    rmtree(os.path.expanduser(renpyfolder))

                for item in savefiles:
                    os.remove(item)

                for item in logfiles:
                    os.remove(item)

                self.show_step_end("Save and log files cleared")
            else:
                self.show_step_end("No save and log files found, nothing cleared")

    def escape_this_shit(self):
        self.render_title()
        self.clear_line()
        self.myprint(" %r>%R Unkown file-extension passed.")
        self.myprint(" %r>%R Valid extensions are: gz, bz2 or xz")
        sys.exit()

    def remove_source_folder(self, folder):
        self.show_step_start("Removing source folder...")
        rmtree(folder)
        self.show_step_end("Source folder removed.")

    def run(self, args):
        if args.type not in ['gz', 'bz2', 'xz']:
            self.escape_this_shit()

        match args.destination:
            case 'usb' : destination = self.locations[0]
            case 'keep' : destination = self.locations[1]
            case 'archives' : destination = self.locations[2]
            case _:
                self.myprint(f" %r>>%R Unknown destination chosen")
                sys.exit(1)

        self.render_title()
        self.check_if_already_in_archives(args.folder, ftype=args.type)
        self.clear_save_files(args.folder, keepsaves=args.keepsaves)
        self.create_archive(args.folder, ftype=args.type)
        self.move_archive(args.folder, destination, ftype=args.type)

        if not args.keep:
            self.remove_source_folder(args.folder)

        self.render_done()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('folder', help='Folder to archive')

    parser.add_argument('-d', '--destination',
                        default='usb',
                        required=False,
                        help='Final destination')

    parser.add_argument('-ks', '--keepsaves',
                        action='store_true',
                        default=False,
                        required=False,
                        help='Keep the save files')

    parser.add_argument('-t', '--type',
                        default='gz',
                        required=False,
                        help='Choose either gz, bz2 or xz')

    parser.add_argument('-k', '--keep',
                        action='store_true',
                        default=False,
                        required=False,
                        help='Keep the source folder')

    app = Archiver()
    app.run(parser.parse_args())
