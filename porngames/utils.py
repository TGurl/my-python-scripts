import os
import sys
import glob
import tarfile

from colors import Colors
from unzip import UnZip
from pyfzf.pyfzf import FzfPrompt

class Utils:
    def __init__(self):
        pass

    def __colorize(self, text='') -> str|None:
        if text == '':
            return None

        for color in Colors.colors:
            text = text.replace(color[0], color[1])
        return text

    def myprint(self, text, clear=False, nl=False):
        newline = '\n\n' if nl else '\n'
        text = self.__colorize(text)
        if clear:
            print('\033[1A', end='\x1b[2K')

        print(text, end=newline)

    def __collect_games(self):
        folders = [os.path.join('~', 'Games', 'archives'),
                   os.path.join('~', 'USB', 'sexgames'),
                   os.path.join('~', 'USB', 'sexgames', 'keep')]
        games = []

        for folder in folders:
            folder = os.path.expanduser(folder)
            content = glob.glob(os.path.join(folder, '*.zip'))
            games.extend(content)

        games.sort()
        return games

    def __collect_games_new(self):
        folders = [os.path.join('~', 'Games', 'archives'),
                   os.path.join('~', 'USB', 'sexgames'),
                   os.path.join('~', 'USB', 'sexgames', 'keep')]
        extensions = ['*.zip', '*.tar.gz', '*.tar.bz2', '*.tar.xz']

        games = []
        for folder in folders:
            for extension in extensions:
                folder = os.path.expanduser(folder)
                content = glob.glob(os.path.join(folder, extension))
                games.extend(content)

        games.sort()
        return games
    
    def select_game(self) -> str|None:
        games = self.__collect_games_new()
        fzf = FzfPrompt()
        game = fzf.prompt(games, '--reverse')
        if len(game) > 0:
            return game[0]
        else:
            return None

    def render_header(self, target, prompt):
        os.system('clear')
        self.myprint('%yPorngames Collection%R - %cCopyleft 2023 %pTransGirl%R', nl=True)
        self.myprint(f'Extracting to %i%c{target}%R')
        self.myprint(prompt, clear=False)

    def unzip(self, game, target):
        with UnZip(game) as archive:
            INFO = archive.namelist()
            TOTAL = len(INFO)
            LEAD = len(str(TOTAL))
            count = 1
            perc = 0
            name = ""
            
            prompt = f" └> {count:{LEAD}}/{TOTAL} [{perc:3}%] : {name}"
            self.render_header(target, prompt)
            
            for file in INFO:
                perc = (count * 100 // TOTAL)
                name = file if len(file) < 35 else '..' + file[-35:]
                prompt = f" └> {count:{LEAD}}/{TOTAL} [{perc:3}%] : {name}"
                self.myprint(prompt, clear=True)
                archive.extract(file, target)
                count += 1

    def untar(self, game, target, atype):
        self.render_header(target, ' └> Reading archive...')
        archive = tarfile.open(game, atype)
        files = archive.getnames()
        TOTAL = len(files)
        LEAD = len(str(TOTAL))
        perc = 0
        count = 1

        for file in files:
            perc = int(count * 100 / TOTAL)
            name = file if len(file) < 35 else '..' + file[-35:]
            prompt = f" └> {count:{LEAD}}/{TOTAL} [{perc:3}%] : {name}"
            self.myprint(prompt, clear=True)
            archive.extract(file, target, set_attrs=True)
            count += 1

        archive.close()

    def install_game(self, game, target, keep=False):
        target = os.path.expanduser(target)

        if '.zip' in game:
            self.unzip(game, target)
        elif '.tar.gz' in game:
            self.untar(game, target, 'r:gz')
        elif '.tar.bz2' in game:
            self.untar(game, target, 'r:bz2')
        elif '.tar.xz' in game:
            self.untar(game, target, 'r:xz')
        else:
            os.system('clear')
            self.myprint('%yPorngames Collection%R - %cCopyleft 2023 %pTransGirl%R', nl=True)
            self.myprint('%rUnkown archive type detected!%R')
            self.myprint('Exiting...')
            sys.exit()

        if not keep:
            os.remove(game)

        os.system('clear')
        self.myprint('%yPorngames Collection%R - %cCopyleft 2023 %pTransGirl%R', nl=True)
        self.myprint('Done. Have fun playing...')
