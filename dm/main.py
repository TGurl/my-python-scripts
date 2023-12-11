#!/usr/bin/env python
import os

from zipfile import ZipFile
from pyfzf.pyfzf import FzfPrompt


class Config:
    title = 'Dungeon Master'
    version = '0.01'
    cright = 'Copyright 2023 TransGirl'
    archive_dir = os.path.join("/", "lore", "sexgames")
    play_dir = os.path.join("/", "lore", "playing")


class TUI:
    def __init__(self):
        pass

    def clear_line(self):
        print('\033[1A', end='\x1b[2K')

    def myprint(self, text, nl=False):
        newline = '\n\n' if nl else '\n'
        print(text, end=newline)

    def header(self, clear=False):
        if clear:
            os.system('clear')
        self.myprint(f">> {Config.title} {Config.version} <<")
        self.myprint(Config.cright, nl=True)

    def step_msg(self, msg):
        self.myprint(f"=> {msg}")

    def info_msg(self, msg):
        self.myprint(f"  -> {msg}")


class Utils:
    def __init__(self):
        self.tui = TUI()
        self.fzf = FzfPrompt()

    def convert_size(self, size: float, decimals=2):
        unit = 'B'
        for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']:
            if size < 1024.0 or unit == 'PiB':
                break
            size /= 1024.0
        return f"{size:.{decimals}f} {unit}"

    def collect_games(self):
        games = []
        for item in os.scandir(Config.archive_dir):
            if ".zip" in item.name:
                games.append(item.name)
        games.sort()
        return games

    def choose_game(self):
        games = self.collect_games()

        item = self.fzf.prompt(games, '--reverse')
        if not item:
            return 'TransgirlLovesBigCocks'
        else:
            return item[0]

    def unzip(self, archive, keep=True):
        arcpath = os.path.join(Config.archive_dir, archive)
        with ZipFile(arcpath, 'r') as zf:
            filelist = zf.infolist()
            total = len(filelist)

            for i, item in enumerate(filelist, start=1):
                p = i * 100 // total
                if len(item.filename) < 30:
                    fn = item.filename
                else:
                    fn = ".." + item.filename[-28:]
                self.tui.info_msg(f"[{p:3}%] extracting {fn}")
                ep = zf.extract(item, Config.play_dir)
                if item.create_system == 3:
                    ua = item.external_attr >> 16
                    if ua:
                        os.chmod(ep, ua)
                self.tui.clear_line()

        if not keep:
            self.tui.step_msg('Removing archive...')
            os.remove(arcpath)
            self.tui.clear_line()


class DungeonMaster:
    def __init__(self):
        self.tui = TUI()
        self.utils = Utils()

    def run(self):
        self.tui.header(clear=True)
        item = self.utils.choose_game()
        if item == 'TransgirlLovesBigCocks':
            self.tui.step_msg('No game chosen')
        else:
            self.tui.step_msg(f"Installing {item}")
            self.utils.unzip(item)


if __name__ == "__main__":
    app = DungeonMaster()
    app.run()
