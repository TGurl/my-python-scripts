#!/usr/bin/env python3
from typing import NoReturn
from settings import Config
from colors import Colors
import pickle
import os, sys


class Utils:
    def __init__(self):
        self.config = Config()

    def save_config(self):
        data = vars(self.config)
        pickle_out = open(self.config.savefile, 'wb')
        pickle.dump(data, pickle_out)
        pickle_out.close()

    def load_config(self):
        pickle_in = open(self.config.savefile, 'rb')
        data = pickle.load(pickle_in)
        pickle_in.close()

        self.config.maincat = data['maincat']
        self.config.subcat = data['subcat']
        self.config.savefile = data['savefile']
        self.config.wallpath = data['wallpath']
        self.config.current = data['current']
        self.config.oldlist = data['oldlist']
    
    def colorize(self, text):
        for color in Colors.colors:
            text = text.replace(color[0], color[1])
        return text

    def myprint(self, text, clearline=False, nl=False):
        newline = '\n\n' if nl else '\n'
        if clearline:
            print('\033[1A', end='\x1b[2K')
        text = self.colorize(text)
        print(text, end=newline)

    def collect_all_wallpapers(self):
        if self.config.maincat is None or self.config.subcat is None:
            self.info(errno=404)

        path = os.path.join(self.config.wallpath, self.config.maincat, self.config.subcat)


    def next_wallpaper(self):
        wallpapers = self.collect_all_wallpapers()
        print('Next')

    def previous_wallpaper(self):
        print('Previous')

    def setup(self):
        os.system('clear')
        self.myprint('%c>> %Wallpaper Setup %c<<%R', nl=True)



    def error_message(self, errno):
        msg = ''
        match errno:
            case 404: msg = 'The main and/or the sub category aren\'t set.'

        return msg

    def info(self, errno=0) -> NoReturn:
        if errno > 0:
            errormsg = self.error_message(errno)
        else:
            errormsg = ''

        os.system('clear')
        self.myprint('%c>> %yWallpaper Settings %c<<%R', nl=True)

        if errno > 0:
            self.myprint(f'%r{errormsg}%R', nl=True)

        self.myprint(f'%cMain category     : %y{self.config.maincat}%R')
        self.myprint(f'%cSub category      : %y{self.config.subcat}%R')
        self.myprint(f'%cCurrent Wallpaper : %y{self.config.current}%R')

        sys.exit()
