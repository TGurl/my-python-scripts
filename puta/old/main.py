#!/usr/bin/env python
import os
import sys
import glob
import argparse

from time import sleep
from zipfile import ZipFile
from pyfzf.pyfzf import FzfPrompt


class Colors:
    reset = "\033[0m"
    black = "\033[30;1m"
    red = "\033[31;1m"
    green = "\033[32;1m"
    darkgreen = "\033[32m"
    yellow = "\033[33;1m"
    blue = "\033[34;1m"
    pink = "\033[35;1m"
    cyan = "\033[36;1m"
    white = "\033[37;1m"
    gray = "\033[37m"
    italic = "\x1B[3m"

    colors = [
            ('%R', reset),
            ('%B', black),
            ('%G', gray),
            ('%r', red),
            ('%g', green),
            ('%dg', darkgreen),
            ('%y', yellow),
            ('%b', blue),
            ('%p', pink),
            ('%c', cyan),
            ('%w', white),
            ('%i', italic)
    ]


class Config:
    usbdir = os.path.join("/", "USB", "sexgames")
    loredir = os.path.join("/", "lore", "sexgames")
    donedir = os.path.join("/", "lore", "sexgames", "done")
    playdir = os.path.join("/", "lore", "playing")
    

class Archiver:
    def __init__(self, args):
        self.fzf = FzfPrompt()
        self.install = args.install
        self.delete = args.delete
        self.yes = args.yes
        self.query = args.query

    def clearline(self, num=1):
        for _ in range(num):
            print('\033[1A', end='\x1b[2K')

    def colorize(self, text):
        for color in Colors.colors:
            text = text.replace(color[0], color[1])
        return text
    
    def decolorize(self, text):
        for color in Colors.colors:
            text = text.replace(color[0], '')
        return text
    
    def printf(self, text, new_line=False):
        carriage_return = '\n\n' if new_line else '\n'
        text = self.colorize(text)
        print(text, end=carriage_return)

    def logo(self):
        os.system('clear')
        lines = [
            "%c__________________________________",
            "%y  ______ _______ _______ _______ ",
            " |   __ \\   |   |_     _|   _   |",
            " |    __/   |   | |   | |       |",
            " |___|  |_______| |___| |___|___|%R",
            "          %bversion 0.0.1          ",
            "     made with %r\u2764 %bTransgirl",
            "%c──────────────────────────────────%R",
        ]
        for line in lines:
            self.printf(line)

    def okmsg(self, message):
        message = self.colorize(message)
        self.printf(f"%g\u2713%R {message}")

    def errmsg(self, message):
        message = self.colorize(message)
        self.printf(f"%r\u2718%R {message}")

    def infomsg(self, message):
        message = self.colorize(message)
        self.printf(f"%y\u2B9E%R {message}")

    def yesno(self, message):
        if self.yes:
            return True
        
        prompt = self.colorize(message)
        while True:
            answer = input(f"{prompt} (y,n) : ").lower()
            if answer in "yn":
                break
            self.clearline()
        
        if answer == "y":
            return True
        
        return False
        
    def panic(self, message):
        self.errmsg(message)
        sys.exit()

    def progress(self, message):
        spaces = 2 * " "
        self.printf(f"{spaces}%b\u2BA1%R {message}")

    def read_files_in_folder(self, folder):
        pattern = os.path.join(folder, "**.zip")
        contents = glob.glob(pattern, recursive=True)
        contents.sort()
        return contents
    
    def unzip(self, path):
        with ZipFile(path, "r") as zf:
            filelist = zf.infolist()
            total = len(filelist)

            for i, item in enumerate(filelist, start=0):
                percent = i * 100 // total
                fn = (
                    item.filename
                    if len(item.filename) < 30
                    else ".." + item.filename[-28:]
                )
                #self.printf(f"  %b└>%R [{percent:3}%] inflating {fn}")
                self.progress(f"[{percent:3}%] inflating {fn}")
                extracted_path = zf.extract(item, Config.playdir)
                if item.create_system == 3:
                    unix_attr = item.external_attr >> 16
                    if unix_attr:
                        os.chmod(extracted_path, unix_attr)
                self.clearline()

    def install_a_game(self):
        folders = [Config.loredir, Config.usbdir, Config.donedir]
        file_list = []
        for folder in folders:
            content = self.read_files_in_folder(folder)
            if self.query is None:
                file_list.extend(content)
            else:
                for item in content:
                    if self.query.lower() in item.lower():
                        file_list.append(item)

        data = self.fzf.prompt(file_list, "--reverse --multi --exact")
        total = len(data)
        count = 0
        # self.infomsg(f"Installing {total} games...")
        for idx, item in enumerate(data, start=1):
            game = item.split('/')[-1]
            temp_f = game.replace(".zip", "")
            if os.path.exists(os.path.join(Config.playdir, temp_f)):
                self.errmsg(f"{game} is already installed...")
                if total > 1 and idx < total:
                    sleep(1.5)
                self.clearline()
            else:
                self.infomsg(f"Unzipping: {game}")
                self.unzip(item)
                count += 1
                self.clearline()
        
        if count:
            ext = "s" if count != 1 else ""
            self.okmsg(f"{count} game{ext} installed.")
        else:
            self.okmsg("No games were installed")
            

    def run(self):
        self.logo()
        if self.install:
            self.install_a_game()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--install",
                        action="store_true",
                        default=False,
                        help="Install a game")

    parser.add_argument("-d", "--delete",
                        action="store_true",
                        default=False,
                        help="Delete archive after install")
    
    parser.add_argument("-y", "--yes",
                        action="store_true",
                        default=False,
                        help="Asume yes to all questions")
    
    parser.add_argument("-q", "--query",
                        default=None,
                        help="Query to search for")
    
    app = Archiver(parser.parse_args())
    app.run()