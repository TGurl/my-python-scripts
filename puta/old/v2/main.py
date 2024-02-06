#!/usr/bin/env python
"""
PUTA 0.0.1
A simple script to manage my porngame collection
"""
import os
import sys
import argparse

from time import sleep
from pyfzf.pyfzf import FzfPrompt
from colors import Colors

class Puta:
    def __init__(self, args):
        self.query = args.query
        self.add_archive = args.add
        self.store_to_usb = args.usb

        self.fzf = FzfPrompt()
        self.usbdir = os.path.join("/", "USB", "sexgames")
        self.loredir = os.path.join("/", "lore", "sexgames")
        self.playdir = os.path.join("/", "lore", "playing")

    def clear_lines(self, num=1):
        for _ in range(num):
            print('\033[1A', end='\x1b[2K')

    def colorize(self, message, remove=False):
        for color in Colors.colors:
            if remove:
                message = message.replace(color[0], '')
            else:
                message = message.replace(color[0], color[1])
        return message

    def cprint(self, message):
        tmp = self.colorize(message, remove=True)
        message = self.colorize(message, remove=False)
        width = os.get_terminal_size().columns
        spaces = ((width - len(tmp)) // 2) * " "
        print(f"{spaces}{message}")

    def fprint(self, message):
        message = self.colorize(message, remove=False)
        print(f"{message}")

    def msg(self, message):
        self.fprint(f"%c>%R {message}")

    def error(self, message, exit_app=False):
        self.fprint(f"%r[ERROR] %c>%R {message}")
        if exit_app:
            sys.exit()

    def warning(self, message):
        self.fprint(f"%y[WARNING] %c>%R {message}")
    
    def draw_line(self):
        width = os.get_terminal_size().columns
        line =  width * "─"
        self.fprint(f"%c{line}%R")

    def check_length(self, message):
        real_length = len(self.colorize(message, remove=True))
        return real_length > os.get_terminal_size().columns

    def draw_banner(self, infobar=None, clear=True):
        title = "%yPuta v0.0.1%R - %gManage your Pr0n games with ease%R"
        if self.check_length(title):
            title = "%yPuta v0.0.1%R"
        if clear:
            os.system('clear')
        self.draw_line()
        self.cprint(title)
        if infobar:
            self.cprint(infobar)
        self.draw_line()

    def collect_all_games(self):
        self.msg('Collecting games...')
        games = []
        folders = [self.usbdir, self.loredir]
        for folder in folders:
            for item in os.scandir(folder):
                needle = ".zip" if not self.query else f"{self.query.lower()}"
                if needle in item.path.lower() and item.is_file():
                    games.append(item.path)

        games.sort()
        self.clear_lines()
        return games

    def show_fuzzy_menu(self, game_list):
        data = self.fzf.prompt(game_list, '--reverse --multi --exact')
        if not data:
            self.draw_banner()
            self.error("You didn't select any games...", exit_app=True)
        return data

    def unzip(self, archive):
        a_name = archive.split('/')[-1]
        self.msg(f"Unzipping {a_name}")
        sleep(1.5)

    def process(self, gamelist):
        total = len(gamelist)
        padding = len(str(total))

        for gidx, game in enumerate(gamelist):
            percent = gidx * 100 // len(gamelist)
            ibar = f"Processing {gidx:{padding}}/{total} [{percent:3}%]"
            if self.check_length(ibar):
                ibar = f"{gidx:{padding}}/{total} [{percent:3}]"
            self.draw_banner(infobar=ibar)
            self.unzip(game)
        
        self.draw_banner(infobar=f"Processing done")
        self.msg("Have fun!")
        sys.exit()

    def check_if_archived(self):
        found = []
        zipfile_name = self.add_archive + ".zip"
        for destination in [self.usbdir, self.loredir]:
            ibar = f"Checking {destination} for {zipfile_name}"
            if self.check_length(ibar):
                ibar = "Checking..."
            self.draw_banner(infobar=ibar)
            archive_path = os.path.join(destination, zipfile_name)
            if os.path.exists(archive_path):
                found.append(archive_path)

        if found:
            sheher = "them" if len(found) > 1 else "her"
            ibar = f"{zipfile_name} found!"
            if self.check_length(ibar):
                ibar = "Found!"
            self.draw_banner(infobar=ibar)
            for path in found:
                self.msg(f"Already archived in {path}")
            self.msg(f"Please use -d to remove {sheher}")
            sys.exit()

    def create_archive(self):
        zipfile_name = self.add_archive + ".zip"
        destination = self.usbdir if self.store_to_usb else self.loredir
        archive_path = os.path.join(destination, zipfile_name)
        ibar = f"Creating {archive_path}"
        if self.check_length(ibar):
            ibar = "Zipping..."
        self.draw_banner(infobar=ibar)
        sleep(2.8)

    def check_archive(self):
        zipfile_name = self.add_archive + ".zip"
        destination = self.usbdir if self.store_to_usb else self.loredir
        archive_path = os.path.join(destination, zipfile_name)
        ibar = f"Checking {archive_path}"
        if self.check_length(ibar):
            ibar = f"Checking..."
        self.draw_banner(infobar=ibar)

        self.msg("Please wait...")
        sleep(2.8)

    def add_game_to_archives(self):
        self.check_if_archived()
        self.create_archive()
        self.check_archive()
        self.draw_banner()
        message = f"{self.add_archive}.zip has been added to the archives"
        if self.check_length(message):
            message = f'Added {self.add_archive}'
        self.msg(message)

    def run(self):
        all_games = self.collect_all_games()
        if not self.add_archive:
            games = self.show_fuzzy_menu(all_games)
            self.process(games)
        else:
            self.add_game_to_archives()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--query', required=False, help='Query to search for')
    parser.add_argument('-a', '--add', required=False, help='Add a game to the archives')
    parser.add_argument('-u', '--usb', required=False, action='store_true', help='Store archive to USB')
    puta = Puta(parser.parse_args())
    puta.run()
