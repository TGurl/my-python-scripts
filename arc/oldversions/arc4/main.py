#!/usr/bin/env python
import argparse
import glob
import os
import shutil
import sys
from time import sleep
from zipfile import ZipFile


class Archiver:
    def __init__(self, args):
        self.folder = args.folder.strip("/")
        self.archive_name = self.folder + ".zip"
        self.keep = args.keep
        self.usb = args.usb
        self.delete = args.delete
        self.clear = args.clear
        self.keep_savefiles = args.saves
        self.archive_dir = os.path.join("/", "lore", "sexgames")
        self.usb_dir = os.path.join("/", "USB", "sexgames")
        self.files = []

    def header(self):
        """Pring a simple header"""
        os.system("clear")
        print("--------------------------------")
        print(" ARC 4 - A simple game archiver")
        print("--------------------------------")

    def clear_line(self):
        """clear a line"""
        print("\033[1A", end="\x1b[2K")

    def readable_size(self, num, suffix="b"):
        """Turn size into readable text"""
        for unit in ["", "k", "M", "G", "T", "P", "E", "Z"]:
            if abs(num) < 1024.0:
                # return "%3.1f %s%s" % (num, unit, suffix)
                return f"{num:3.1f} {unit}{suffix}"
            num /= 1024.0
        # return "%.1f%s%s" % (num, "Yi", suffix)
        return f"{num:.1f} Yi{suffix}"

    def get_free_space(self, location):
        """Get free space"""
        total, _, free = shutil.disk_usage(location)
        percent = (free * 100) // total
        return percent

    def check_if_folder_exists(self):
        """Check if the given folder exists"""
        if not os.path.exists(self.folder):
            print(f"{self.folder} does not seem to exist...")
            sys.exit()

    def check_if_already_archived(self):
        """Check if the game has been archived already"""
        folders = [self.archive_dir, self.usb_dir]

        for f in folders:
            fullpath = os.path.join(f, self.archive_name)
            if os.path.exists(fullpath):
                # print(f"> {self.archive_name} already exists.")
                if self.delete:
                    os.remove(fullpath)
                    # self.clear_line()
                    print("> Archived version deleted.")
                    break
                if self.clear:
                    shutil.rmtree(self.folder)
                    print("> Source folder cleared")
                    sys.exit()
                print(f"> {self.archive_name} found in {f}.")
                print("> Use either one of the following options:")
                print("  -d -> Delete the archived version")
                print("  -c -> Clear the source folder")
                sys.exit()
            else:
                # print(f"> {self.archive_name} does not exist yet")
                pass

    def read_contents(self):
        """Read contenst of folders"""
        print(f">> Reading contents of {self.folder}")
        pattern = os.path.join(self.folder, "**")
        self.files = glob.glob(pattern, recursive=True)
        # self.files.sort()
        self.clear_line()

    def clean_source_folder(self):
        """Clean the source folder"""
        print(f">> Cleaning {self.folder}")
        self.read_contents()

        # --- remove unwanted files
        remove = [
            "traceback.txt",
            "log.txt",
            "desktop.ini",
            "errors.txt",
            ".bak",
            ".log",
        ]
        if not self.keep_savefiles:
            remove.append(".save")

        for file in self.files:
            for needle in remove:
                if needle in file:
                    print(f"> Removing {file}", end="\n")
                    os.remove(file)
                    sleep(0.2)
                    self.clear_line()

        # --- clear out the save files
        # if not self.keep_savefiles:
        #    pattern = os.path.join(self.folder, "**", "saves")
        #    saves = glob.glob(pattern, recursive=True)
        #    for item in saves:
        #        print(f"> Removing {item}")
        #        shutil.rmtree(item)
        #        self.clear_line()

        self.clear_line()

    def create_archive(self):
        """Create the zip file"""
        print(f"> Archiving {self.folder} to {self.archive_name}")
        total = len(self.files)
        lead = len(str(total))

        with ZipFile(self.archive_name, "w", compresslevel=9) as zf:
            for i, file in enumerate(self.files, start=1):
                filename = file if len(file) <= 40 else ".." + file[-38:]
                p = i * 100 // total

                if os.path.isdir(file):
                    print(f"  └> creating: {i:{lead}}/{total} [{p:3}%]: {filename}")
                else:
                    print(f"  └> adding: {i:{lead}}/{total} [{p:3}%]: {filename}")
                zf.write(file)
                self.clear_line()

        self.clear_line()
        print(f"> Archive {self.archive_name} created")

    def move_archive(self):
        """Move the archive to it's destination"""
        source_size = os.stat(self.archive_name).st_size
        size = self.readable_size(source_size)
        copied = 0
        p = 0
        dest_dir = self.usb_dir if self.usb else self.archive_dir

        print(f"> Moving {self.archive_name} ({size})")

        source = open(self.archive_name, "rb")
        target = open(os.path.join(dest_dir, self.archive_name), "wb")

        while True:
            p = int(copied * 100 / source_size)
            print(f"  └> {p:3}% moved to {dest_dir}")
            chunk = source.read(32768)
            if not chunk:
                break
            target.write(chunk)
            copied += len(chunk)
            self.clear_line()

        self.clear_line()
        target.close()
        source.close()
        print("  └> syncing...")
        os.system("sync")
        os.remove(self.archive_name)

        self.clear_line()
        self.clear_line()
        print(f"> {self.archive_name} ({size}) moved to {dest_dir}")

    def new_move_archive(self):
        """Move the archive to it's destination"""
        source_size = os.stat(self.archive_name).st_size
        size = self.readable_size(source_size)
        print(f"> Moving {self.archive_name} ({size})")
        shutil.move(self.archive_name, self.archive_dir)
        os.system("sync")
        self.clear_line()
        print(f"> {self.archive_name} ({size}) moved")

    def remove_source(self):
        """Remove the source folder"""
        if not self.keep:
            print(f"> Removing source folder {self.folder}")
            shutil.rmtree(self.folder)
            self.clear_line()
            print("> Source folder removed")
        else:
            print("> Source folder not removed")

    def finished(self):
        """All done"""
        if os.path.exists(self.archive_name):
            os.remove(self.archive_name)
        print("> All done...")

    def run(self):
        """The main loop"""
        if os.path.exists(self.archive_name):
            os.remove(self.archive_name)

        self.header()
        self.check_if_folder_exists()
        self.check_if_already_archived()
        self.clean_source_folder()
        self.read_contents()
        self.create_archive()
        if self.usb:
            percent = self.get_free_space(self.usb_dir)
            print(f"> Free space left: {percent}%")
            self.move_archive()
        else:
            percent = self.get_free_space(self.archive_dir)
            print(f"> Free space left: {percent}%")
            self.new_move_archive()

        self.remove_source()
        self.finished()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("folder")
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep the source folder"
    )
    parser.add_argument(
        "-d", "--delete", action="store_true", help="Delete the archived version"
    )
    parser.add_argument(
        "-c", "--clear", action="store_true", help="Clear the source folder"
    )
    parser.add_argument(
        "-s", "--saves", action="store_true", help="Keep the save files"
    )
    parser.add_argument(
        "-u", "--usb", action="store_true", help="Move archive to USB device"
    )

    app = Archiver(parser.parse_args())
    try:
        app.run()
    except KeyboardInterrupt:
        print("Process stopped!")
        sys.exit()
