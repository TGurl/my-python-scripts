import os
import pickle
from subprocess import Popen, PIPE, getoutput
from config import Config
from colors import Colors


class Utils:
    def __init__(self):
        pass

    def dictstr(self):
        return dict(title=Config.title,
                    current=Config.current,
                    maincat=Config.maincat,
                    subcat=Config.subcat,
                    wpsetter=Config.wpsetter,
                    rootpw=Config.rootpw,
                    auto=Config.auto,
                    sddm=Config.sddm,
                    grub=Config.grub,
                    random=Config.random,
                    walldir=Config.walldir,
                    grubpath=Config.grubpath,
                    sddmpath=Config.sddmpath)

    def send_notification(self, title, message):
        cmd = f"notify-send -u normal '{title}' '{message}'"
        os.system(cmd)

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

    def get_change_duration(self):
        output = getoutput('systemctl --user status wallpaper.timer')
        line = output.split('\n')[3].split(';')[1]
        return line.lstrip()

    def save_config(self, filename='wp.cfg'):
        path = os.path.expanduser(
                os.path.join('~', '.bin', filename)
                )
        dictstr = self.dictstr()
        pickle_out = open(path, "wb")
        pickle.dump(dictstr, pickle_out)
        pickle_out.close()

    def load_config(self, filename='wp.cfg'):
        path = os.path.expanduser(
                os.path.join('~', '.bin', filename)
                )
        if os.path.exists(path):
            pickle_in = open(path, 'rb')
            data = pickle.load(pickle_in)
            pickle_in.close()

            Config.title = data['title']
            Config.current = data['current']
            Config.maincat = data['maincat']
            Config.subcat = data['subcat']
            Config.wpsetter = data['wpsetter']
            Config.rootpw = data['rootpw']
            Config.sddm = data['sddm']
            Config.grub = data['grub']
            Config.walldir = data['walldir']
            Config.grubpath = data['grubpath']
            Config.sddmpath = data['sddmpath']
            Config.auto = data['auto']
            Config.random = data['random']

    def colorize(self, text):
        for code in Colors.colors:
            text = text.replace(code[0], code[1])
        return text

    def decolorize(self, text):
        for code in Colors.codes:
            text = text.replace(code, '')
        return text

    def myprint(self, text, nl=False):
        newline = '\n\n' if nl else '\n'
        text = self.colorize(text)
        print(text, end=newline)

    def boxit(self, text, width=40):
        boxchar = ('╭', '╮', '╰', '╯ ', '│', '─')
        horline = width * boxchar[5]
        topline = boxchar[0] + horline + boxchar[1]
        botline = boxchar[2] + horline + boxchar[3]
        spaces = ((width - len(text)) // 2) * " "
        text = f"{spaces}%y{text}%c{spaces}"
        verline = boxchar[4] + text + boxchar[4]

        self.myprint(f"%c{topline}%R")
        self.myprint(f"%c{verline}%R")
        self.myprint(f"%c{botline}%R")

    def print_info(self, text):
        prompt = f"%g>%R {text}"
        self.myprint(prompt)

    def print_error(self, text):
        prompt = f"%r>%R {text}"
        self.myprint(prompt)

    def show_info(self):
        self.load_config()
        auto = "%gTrue%R" if Config.auto else "%rFalse%R"
        grub = "%gTrue%R" if Config.grub else "%rFalse%R"
        sddm = "%gTrue%R" if Config.sddm else "%rFalse%R"
        rand = "%gTrue%R" if Config.random else "%rFalse%R"
        if Config.auto:
            remaining = self.get_change_duration()
        else:
            remaining = "%rDisabled%R"

        os.system('clear')
        self.boxit(Config.title)

        self.myprint(f"  Current walpaper: %G{Config.current}%R")
        self.myprint(f"     Main category: %G{Config.maincat}%R")
        self.myprint(f"      Sub category: %G{Config.subcat}%R")
        self.myprint(f"    Time remaining: %G{remaining}%R")
        self.myprint(f"       Auto change: {auto}")
        self.myprint(f"    Change grub wp: {grub}")
        self.myprint(f"    Change sddm wp: {sddm}")
        self.myprint(f"         Randmized: {rand}")