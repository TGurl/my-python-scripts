import os
import sys
import pickle
import random
from config import Config
from colors import Colors
from time import sleep
from subprocess import Popen, PIPE, getoutput


class MyUtils:
    def __init__(self):
        pass
    
    def dictify(self):
        return dict(
                walldir=Config.walldir,
                configpath=Config.configpath,
                maincat=Config.maincat,
                subcat=Config.subcat,
                current=Config.current,
                app=Config.app,
                rootpw=Config.rootpw,
                random=Config.random,
                auto=Config.auto,
                grub=Config.grub,
                notify=Config.notify
                )

    def save_config(self):
        data = self.dictify()
        pickleout = open(Config.configpath, 'wb')
        pickle.dump(data, pickleout)
        pickleout.close()

    def load_config(self):
        picklein = open(Config.configpath, 'rb')
        data = pickle.load(picklein)
        picklein.close()

        Config.walldir = data['walldir']
        Config.configpath = data['configpath']
        Config.maincat = data['maincat']
        Config.subcat = data['subcat']
        Config.current = data['current']
        Config.app = data['app']
        Config.rootpw = data['rootpw']
        Config.random = data['random']
        Config.auto = data['auto']
        Config.grub = data['grub']
        Config.notify = data['notify']

    def check_configpath(self):
        return os.path.exists(Config.configpath)

    def complete_wallpaper_path(self):
        return os.path.join(Config.walldir, Config.maincat, Config.subcat, Config.current)

    def complete_folder(self):
        return os.path.join(Config.walldir, Config.maincat, Config.subcat)

    def maincat_folder(self):
        return os.path.join(Config.walldir, Config.maincat)

    def execute_root_command(self, command):
        args = ["sudo", "-S"]
        command = command.split()
        p = Popen(
            args + command,
            stdin=PIPE,
            stderr=PIPE, universal_newlines=True
        )
        r = p.communicate(Config.rootpw + "\n")[1]
        del r

    def collect_wallpapers(self):
        wallpapers = []
        valid = ['.jpg', '.png']
        folder = self.complete_folder()
        for image in os.listdir(folder):
            extension = os.path.splitext(image)[1].lower()
            if extension in valid:
                wallpapers.append(image)
        wallpapers.sort()
        return wallpapers

    def collect_maincat_folders(self):
        folders = []
        ignore = ['.git', 'downloads', 'keepers']
        for folder in os.listdir(Config.walldir):
            path = os.path.join(Config.walldir, folder)
            if os.path.isdir(path) and folder not in ignore:
                folders.append(folder)
        folders.sort()
        return folders

    def collect_subcat_folders(self):
        folders = []
        ignore = ['.git', 'downloads', 'keepers']
        for folder in os.listdir(self.maincat_folder()):
            path = os.path.join(Config.walldir, Config.maincat, folder)
            if os.path.isdir(path) and folder not in ignore:
                folders.append(folder)
        folders.sort()
        return folders

    def choose_random_wallpaper(self):
        Config.current = random.choice(self.collect_wallpapers())
        self.save_config()

    def goto_next_wallpaper(self):
        if Config.random:
            self.choose_random_wallpaper()
        wallpapers = self.collect_wallpapers()
        if Config.current == '' or Config.current not in wallpapers:
            idx = -1
        else:
            idx = wallpapers.index(Config.current)
        idx += 1
        if idx > len(wallpapers) - 1:
            idx = 0
        Config.current = wallpapers[idx]
        self.save_config()

    def goto_previous_wallpaper(self):
        if Config.random:
            self.choose_random_wallpaper()
        wallpapers = self.collect_wallpapers()
        if Config.current == '' or Config.current not in wallpapers:
            idx = 0
        else:
            idx = wallpapers.index(Config.current)
        idx -= 1
        if idx < 0:
            idx = len(wallpapers) - 1
        Config.current = wallpapers[idx]
        self.save_config()

    def set_grub_background(self):
        grubpath = '/boot/grub/themes/girls/background.png'
        _, extension = os.path.splitext(Config.current)
        
        wallpath = self.complete_wallpaper_path()
        if extension == '.jpg':
            cmd = f'convert {wallpath} {grubpath}'
        else:
            cmd = f'cp {wallpath} {grubpath}'
        self.execute_root_command(cmd)

    # def set_sddm_background(self):
    #    sddmpath = '/usr/share/sddm/themes/mywall/Backgrounds/mywall.png'
    #    extension = os.path.splitext(Config.current)[1].lower()

    #    wallpath = self.complete_wallpaper_path()
    #    if extension == '.jpg':
    #        cmd = f'convert {wallpath} {sddmpath}'
    #    else:
    #        cmd = f'cp {wallpath} {sddmpath}'
    #    self.execute_root_command(cmd)

    def set_wallpaper(self):
        path = self.complete_wallpaper_path()
        match Config.app:
            case 'feh': cmd = 'feh --bg-scale '
            case 'nitrogen': cmd = 'nitrogen --set-scaled --save '
            case _:
                print('ERROR: Unkown wallpaper app configured, exiting')
                sys.exit()
        path = self.complete_wallpaper_path()
        cmd += path
        os.system(cmd)
        if Config.grub:
            self.set_grub_background()

        # if Config.sddm:
        #    self.set_sddm_background()

        if Config.notify:
            cmd = f"notify-send -u normal '{Config.current}'"
            os.system(cmd)

    def colorize(self, text):
        for color in Colors.colors:
            text = text.replace(color[0], color[1])
        return text

    def decolorize(self, text):
        for code in Colors.codes:
            text = text.replace(code, '')
        return text

    def myprint(self, text, nl=False):
        newline = '\n\n' if nl else '\n'
        text = self.colorize(text)
        print(text, end=newline)

    def change_maincat(self):
        folders = self.collect_maincat_folders()
        total = len(folders)
        insubmenu = True
        spaces = 4 * ' '
        valid = ['r']

        while insubmenu:
            newline = False
            os.system('clear')
            self.myprint(f'%c{spaces}-= %yCHANGE MAIN CATEGORY %c=-%R', nl=True)
            for num, folder in enumerate(folders, start=1):
                valid.append(str(num))
                title = folder.replace('_', ' ').upper()
                # isset = '(current)' if Config.maincat == folder else ''
                if num == total:
                    newline = True
                if Config.maincat == folder:
                    self.myprint(f'%c[%y{num}%c]%R %g{title}%R', nl=newline)
                else:
                    self.myprint(f'%c[%y{num}%c]%R {title}', nl=newline)
            self.myprint(f'%c[%yr%c]%R Return to main menu', nl=True)
            prompt = self.colorize('%c>%R ')
            response = input(prompt).lower()
            if response not in valid:
                self.myprint(f'%rERROR%R: not a valid option')
                sleep(2)
            elif response == 'r':
                insubmenu = False
            else:
                idx = int(response) - 1
                Config.maincat = folders[idx]
                Config.subcat = 'none'
                self.save_config()
                insubmenu = False
        self.change_subcat()

    def change_subcat(self):
        folders = self.collect_subcat_folders()
        total = len(folders)
        insubmenu = True
        spaces = 4 * ' '
        valid = ['r']

        while insubmenu:
            newline = False
            os.system('clear')
            self.myprint(f'%c{spaces}-= %yCHANGE SUB CATEGORY %c=-%R', nl=True)
            for num, folder in enumerate(folders, start=1):
                title = folder.replace('_', ' ').title()
                valid.append(str(num))
                # isset = '(current)' if Config.subcat == folder else ''
                if num == total:
                    newline = True
                if Config.subcat == folder:
                    self.myprint(f'%c[%y{num}%c]%R %g{title}%R', nl=newline)
                else:
                    self.myprint(f'%c[%y{num}%c]%R {title}', nl=newline)
            self.myprint(f'%c[%yr%c]%R Return to main menu', nl=True)
            prompt = self.colorize('%c>%R ')
            response = input(prompt).lower()
            if response not in valid:
                self.myprint(f'%rERROR%R: not a valid option')
                sleep(2)
            elif response == 'r':
                insubmenu = False
            else:
                idx = int(response) - 1
                Config.subcat = folders[idx]
                wallpapers = self.collect_wallpapers()
                Config.current = wallpapers[0]
                self.set_wallpaper()
                self.save_config()
                insubmenu = False

    def get_output(self):
        output = getoutput('systemctl --user status wallpaper.timer')
        if 'inactive' in output.split('\n')[2]:
            line = output.split('\n')[2].split(' ')[1]
        else:
            line = output.split('\n')[3].split(';')[1].lstrip()
        return line

    def toggle_autochange(self):
        cmd = 'disable' if Config.auto else 'enable'
        cmd = f'systemctl --user --now {cmd} wallpaper.timer > /dev/null 2>&1'
        Config.auto = not Config.auto
        self.save_config()
        os.system(cmd)
        self.myprint('%gINFO%R: Waiting for timers to restart...')
        sleep(4)

    def wallpaper_menu(self):
        spaces = 7 * ' '
        inmenu = True

        while inmenu:
            os.system('clear')

            rcol = '%g' if Config.random else '%r'
            acol = '%g' if Config.auto else '%r'
            gcol = '%g' if Config.grub else '%r'
            # scol = '%g' if Config.sddm else '%r'
            ncol = '%g' if Config.notify else '%r'

            if Config.subcat == 'none':
                subcat = '%rNOT SET%R'
            else:
                subcat = Config.subcat

            self.myprint(f'%c{spaces}-= %yWALLPAPER MENU %c=-%R', nl=True)
            if Config.auto:
                self.myprint(f'Current wallpaper : %y{Config.current}%R')
                self.myprint(f'Countdown to next : %y{self.get_output()}%R', nl=True)
            else:
                self.myprint(f'Current wallpaper : %y{Config.current}%R', nl=True)

            maintitle = Config.maincat.replace('_', ' ').upper()
            subtitle = subcat.replace('_', ' ').title()

            self.myprint(f'%c[%y1%c]%R Change main category   : %y{maintitle}%R')
            self.myprint(f'%c[%y2%c]%R Change sub category    : %y{subtitle}%R')
            self.myprint(f'%c[%y3%c]%R Wallpaper application  : %y{Config.app}%R')
            self.myprint(f'%c[%y4%c]%R Auto change wallpaper  : {acol}{Config.auto}%R')
            self.myprint(f'%c[%y5%c]%R Randomize wallpaper    : {rcol}{Config.random}%R')
            self.myprint(f'%c[%y6%c]%R Change grub/SDDM wall  : {gcol}{Config.grub}%R')
            # self.myprint(f'%c[%y7%c]%R Change sddm background : {scol}{Config.sddm}%R')
            self.myprint(f'%c[%y7%c]%R Change notification    : {ncol}{Config.notify}%R', nl=True)

            self.myprint(f'%c[%yq%c]%R Quit', nl=True)
            prompt = self.colorize('%c>%R ')
            valid = ['1', '2', '3', '4', '5', '6', '7', 'q']
            response = input(prompt).lower()
            if response not in valid:
                self.myprint(f'%rERROR%R: not a valid option')
                sleep(2)
            elif response == 'q':
                self.save_config()
                inmenu = False
            elif response == '1':
                self.change_maincat()
            elif response == '2':
                self.change_subcat()
            elif response == '3':
                Config.app = 'nitrogen' if Config.app == 'feh' else 'feh'
            elif response == '4':
                self.toggle_autochange()
            elif response == '5':
                Config.random = not Config.random
            elif response == '6':
                Config.grub = not Config.grub
            #elif response == '7':
            #    Config.sddm = not Config.sddm
            elif response == '7':
                Config.notify = not Config.notify
