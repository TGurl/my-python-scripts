import os
import sys
from pathlib import Path
from config import Config
from utils import Utils
from random import choice


class Wallpaper():
    def __init__(self):
        self.utils = Utils()
        self.utils.load_config()
        self.collection = self.collect_images()

    def wallpaper_maincat(self):
        return os.path.join(
                Config.walldir,
                Config.maincat
                )

    def wallpaper_path(self):
        return os.path.join(
                Config.walldir,
                Config.maincat,
                Config.subcat
                )

    def full_wallpaper_path(self):
        return os.path.join(
                self.wallpaper_path(),
                Config.current
                )

    def collect_images(self):
        images = []
        valid = ['png', 'jpg', 'jpeg', 'webp']
        activedir = self.wallpaper_path()
        for file in os.listdir(activedir):
            for item in valid:
                if item in file:
                    images.append(file)
        images.sort()
        return images

    def determine_first_wallpaper(self):
        self.collection = self.collect_images()
        return self.collection[0]

    def determine_first_subcat(self):
        path = self.wallpaper_maincat()
        folders = [f.path for f in os.scandir(path) if f.is_dir()]
        folders.sort()
        return folders[0].split('/')[-1]

    def toggle_maincat(self):
        Config.maincat = 'sfw' if Config.maincat == 'nsfw' else 'nsfw'

        Config.subcat = self.determine_first_subcat()
        Config.current = self.determine_first_wallpaper()
        Config.showwarning = False

    def change_subcat(self):
        path = self.wallpaper_maincat()
        folders = [f.path for f in os.scandir(path) if f.is_dir()]
        folders.sort()
        insubmenu = True
        while insubmenu:
            valid = ['q']
            os.system('clear')
            self.utils.boxit(Config.title)

            for num, folder in enumerate(folders, start=1):
                fname = folder.split('/')[-1]
                self.utils.myprint(f"  %c[%y{num:2}%c]%R {fname}")
                valid.append(str(num))

            print()
            self.utils.myprint("  %c[%rq%c]%R Quit", nl=True)
            response = input("  > ").lower()
            if response not in valid:
                pass
            elif response == "q":
                insubmenu = False
                exit()
            else:
                idx = int(response) - 1
                Config.subcat = folders[idx].split('/')[-1]
                Config.current = self.determine_first_wallpaper()
                Config.showwarning = False
                insubmenu = False

    def set_sddm_grub_wallpapers(self):
        jpg = [".jpg", ".jpeg"]
        curwall = self.full_wallpaper_path()
        cmd = "convert" if Path(curwall).suffix.lower() in jpg else "cp"

        if Config.sddm:
            sddm_command = f"{cmd} {curwall} {Config.sddmpath}"
            self.utils.execute_root_command(sddm_command)

        if Config.grub:
            grub_command = f"{cmd} {curwall} {Config.grubpath}"
            self.utils.execute_root_command(grub_command)

    def set_wallpaper(self):
        match Config.wpsetter:
            case 'feh':
                command = "feh --bg-scale "
            case 'nitrogen':
                command = "nitrogen --set-scaled "
            case _:
                print("Unkown app chosen...")
                sys.exit()

        fullpath = self.full_wallpaper_path()
        command += f"'{fullpath}'"
        os.system(command)
        if Config.grub or Config.sddm:
            self.set_sddm_grub_wallpapers()

    def next_wallpaper(self):
        self.colection = self.collect_images()
        if Config.random:
            self.random_wallpaper(True)
        elif Config.current == 'none':
            Config.current = self.collection[0]
        else:
            top = len(self.collection) - 1
            index = self.collection.index(Config.current) + 1
            index = 0 if index > top else index
            Config.current = self.collection[index]
        self.set_wallpaper()
        self.utils.save_config()

    def previous_wallpaper(self):
        self.colection = self.collect_images()
        if Config.random:
            self.random_wallpaper(True)
        elif Config.current == 'none':
            Config.current = self.collection[-1]
        else:
            index = self.collection.index(Config.current) - 1
            index = -1 if index < -1 else index
            Config.current = self.collection[index]
        self.set_wallpaper()
        self.utils.save_config()

    def random_wallpaper(self, internal=False):
        Config.current = choice(self.collection)
        if not internal:
            self.set_wallpaper()
            self.utils.save_config()
