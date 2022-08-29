#!/usr/bin/env python

import os
import sys
from random import randint, choice
from time import sleep
from shutil import get_terminal_size
from pathlib import Path


class Colors:
    res = "\033[0m"
    red = "\033[31;1m"
    gre = "\033[32;1m"
    yel = "\033[33;1m"
    blu = "\033[34;1m"
    pin = "\033[35;1m"
    cya = "\033[36;1m"
    whi = "\033[37;1m"


class Write:
    def __init__(self):
        self.cursor = True
        self.appdir = os.path.dirname(os.path.realpath(__file__))
        self.datadir = os.path.join(self.appdir, "data")
        self.photodir = os.path.join(self.datadir, "photos")
        self.width = get_terminal_size().columns
        self.colors = Colors()

    def read_text(self, filename):
        if ".txt" not in filename:
            filename += ".txt"
        path = os.path.join(self.datadir, filename)
        with open(path, "r") as f:
            data = f.readlines()
        return data

    def read_csv(self, filename):
        if ".csv" not in filename:
            filename += ".csv"
        path = os.path.join(self.datadir, filename)
        with open(path, "r") as f:
            data = f.read().replace("\n", "").split(",")
        return data

    def cursor_off(self):
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    def cursor_on(self):
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

    def toggle_cursor(self):
        if self.cursor:
            self.cursor = False
            self.cursor_off()
        else:
            self.cursor = True
            self.cursor_on()

    def wait_for_enter(self):
        answer = input(f"")
        del answer

    def are_you_sure(self):
        yn_loop = True
        text = "Sure? (y/n) "

        while yn_loop:
            os.system("clear")
            answer = input(text).lower()
            if answer in ["y", "yes"]:
                yn_loop = False
                return yn_loop
            elif answer in ["n", "no"]:
                return yn_loop
            else:
                self.error("only y or n")

    def show_name(self, name):
        os.system("clear")
        res = self.colors.res
        col = self.colors.yel
        print(f" {col}{name}{res}")

    def choose_girl_name(self):
        data = self.read_csv("girlnames")
        self.toggle_cursor()
        self.show_name(choice(data))
        self.wait_for_enter()
        self.toggle_cursor()

    def choose_boy_name(self):
        data = self.read_csv("boynames")
        self.toggle_cursor()
        self.show_name(choice(data))
        self.wait_for_enter()
        self.toggle_cursor()

    def ask_yn(self, query="", enable_enter=False):
        # if query == "":
        #    query = "Are you sure?"
        # query += " (y/n) : "
        subloop = True
        answer = "y"
        valid = ["y", "n", "yes", "no", "q", "quit"]
        yesanswers = ["yes", "y", "true", "ja", "j"]
        if enable_enter:
            valid.append("")
            yesanswers.append("")

        while subloop:
            answer = input(query).lower()
            if answer in valid:
                subloop = False
            else:
                print("Please answer either yes or no")

        if answer in yesanswers:
            return True
        else:
            return False

    def show_photo(self):
        subloop = True
        valid = [".jpg", ".jpeg", ".png"]
        photos = []
        self.toggle_cursor()

        for f in os.listdir(self.photodir):
            if Path(f).suffix.lower() in valid:
                photos.append(os.path.join(self.photodir, f))

        photos.sort()
        numphotos = len(photos) - 1
        # idx = randint(0, numphotos)
        idx = 0

        while subloop:
            # photo = choice(photos)
            photo = photos[idx]
            os.system("clear")
            # print(f"Photo number {idx:4}/{numphotos}")
            # os.system(f"viu -h 10 -w 20 {photo}")
            os.system(f"viu {photo}")
            nextphoto = self.ask_yn("", enable_enter=True)

            if not nextphoto:
                subloop = False
            idx += 1
            if idx > numphotos - 1:
                idx = 0

        self.toggle_cursor()

    def show_info(self):
        os.system("clear")
        data = self.read_text("laura")
        cols = ["{res}", "{yel}", "{gre}"]
        codes = [self.colors.res, self.colors.yel, self.colors.gre]

        for line in data:
            if line.startswith("#"):
                continue
            else:
                line = line.replace("\n", "")
                for remove in cols:
                    idx = cols.index(remove)
                    line = line.replace(remove, codes[idx])
                if line == "---":
                    line = " "
                print(f"{line}")

        self.toggle_cursor()
        self.wait_for_enter()
        self.toggle_cursor()

    def choose_town_name(self):
        res = self.colors.res
        blu = self.colors.blu
        gre = self.colors.gre

        with open(os.path.join(self.datadir, "citynames.txt"), "r") as f:
            data = f.readlines()
        name = choice(data)
        name = name.replace("\n", "").split(",")
        town = name[0]
        state = name[1]

        self.toggle_cursor()
        os.system("clear")
        print(f"{gre}{town}{res}\n{blu}{state}{res}")
        self.wait_for_enter()
        self.toggle_cursor()

    #
    # Conversions
    #

    def calculate_wages(self):
        os.system("clear")

        colors = self.colors
        res = colors.res
        yel = colors.yel
        gre = colors.gre

        hourly = input(f"{yel}Wage:{res} ").lower()
        hours = input(f"{yel}Hours:{res} ").lower()
        print()
        wages = float(hourly) * float(hours)
        print(f"Earned: {gre}{wages}{res}")
        self.toggle_cursor()
        self.wait_for_enter()
        self.toggle_cursor()

    def cmtoinch(self):
        rate = 2.54
        res = self.colors.res
        red = self.colors.red
        gre = self.colors.gre
        yel = self.colors.yel

        unit1 = "Cm"
        unit2 = "Inch"
        os.system("clear")
        reply = input(f"{yel}{unit1}:{res} ").lower()
        convert = True
        if reply == "":
            os.system("clear")
            reply = input(f"{yel}{unit2}:{res} ").lower()
            convert = False
        if convert:
            os.system("clear")
            answer = round(float(reply) / rate)
            print(f"{gre}{reply} {unit1}{res} = {red}{answer} {unit2}{res}")
        else:
            os.system("clear")
            answer = round(float(reply) * rate)
            print(f"{gre}{reply} {unit2}{res} = {red}{answer} {unit1}{res}")
        self.toggle_cursor()
        self.wait_for_enter()
        self.toggle_cursor()

    def kgtolbs(self):
        rate = 2.20462
        res = self.colors.res
        red = self.colors.red
        gre = self.colors.gre
        yel = self.colors.yel

        unit1 = "Kg"
        unit2 = "Lbs"
        os.system("clear")
        reply = input(f"{yel}{unit1}:{res} ").lower()
        convert = True
        if reply == "":
            os.system("clear")
            reply = input(f"{yel}{unit2}:{res} ").lower()
            convert = False
        if convert:
            os.system("clear")
            answer = round(float(reply) * rate)
            print(f"{gre}{reply} {unit1}{res} = {red}{answer} {unit2}{res}")
        else:
            os.system("clear")
            answer = round(float(reply) / rate)
            print(f"{gre}{reply} {unit2}{res} = {red}{answer} {unit1}{res}")
        self.toggle_cursor()
        self.wait_for_enter()
        self.toggle_cursor()

    def metertofeet(self):
        rate = 3.28084
        res = self.colors.res
        red = self.colors.red
        gre = self.colors.gre
        yel = self.colors.yel

        unit1 = "M"
        unit2 = "Ft"
        os.system("clear")
        reply = input(f"{yel}{unit1}:{res} ").lower()
        convert = True
        if reply == "":
            os.system("clear")
            reply = input(f"{yel}{unit2}:{res} ").lower()
            convert = False
        if convert:
            os.system("clear")
            answer = round(float(reply) * rate)
            print(f"{gre}{reply} {unit1}{res} = {red}{answer} {unit2}{res}")
        else:
            os.system("clear")
            answer = round(float(reply) / rate)
            print(f"{gre}{reply} {unit2}{res} = {red}{answer} {unit1}{res}")
        self.toggle_cursor()
        self.wait_for_enter()
        self.toggle_cursor()

    def kmtom(self):
        rate = 0.621371
        res = self.colors.res
        red = self.colors.red
        gre = self.colors.gre
        yel = self.colors.yel

        unit1 = "Km"
        unit2 = "Mi"
        os.system("clear")
        reply = input(f"{yel}{unit1}:{res} ").lower()
        convert = True
        if reply == "":
            os.system("clear")
            reply = input(f"{yel}{unit2}:{res} ").lower()
            convert = False
        if convert:
            os.system("clear")
            answer = round(float(reply) / rate)
            print(f"{gre}{reply} {unit1}{res} = {red}{answer} {unit2}{res}")
        else:
            os.system("clear")
            answer = round(float(reply) * rate)
            print(f"{gre}{reply} {unit2}{res} = {red}{answer} {unit1}{res}")
        self.toggle_cursor()
        self.wait_for_enter()
        self.toggle_cursor()

    def ctof(self):
        res = self.colors.res
        red = self.colors.red
        gre = self.colors.gre
        yel = self.colors.yel

        unit1 = "°C"
        unit2 = "°F"

        os.system("clear")
        reply = input(f"{yel}{unit1}: ").lower()
        convert = True
        if reply == "":
            os.system("clear")
            reply = input(f"{yel}{unit2}: ").lower()
            convert = False
        if convert:
            rate = 9 / 5
            answer = round((float(reply) * rate) + 32)
            os.system("clear")
            print(f"{gre}{reply}{unit1}{res} = {red}{answer}{unit2}{res}")
        else:
            rate = 5 / 9
            answer = round((float(reply) - 32) * rate)
            os.system("clear")
            print(f"{gre}{reply}{unit2}{res} = {red}{answer}{unit1}{res}")
        self.toggle_cursor()
        self.wait_for_enter()
        self.toggle_cursor()

    #
    # Messages
    #
    def error(self, text):
        res = self.colors.res
        red = self.colors.red
        print(f"{red}{text}{res}")
        sleep(0.8)

    def show_menu(self):
        menu_loop = True
        res = self.colors.res
        yel = self.colors.yel
        pin = self.colors.pin
        cya = self.colors.cya
        blu = self.colors.blu
        gre = self.colors.gre
        red = self.colors.red

        while menu_loop:
            os.system("clear")
            print(f" 1. {yel}Laura{res}")
            print(f" 2. {cya}Photo{res}")
            print(f" 3. {pin}Girl name{res}")
            print(f" 4. {blu}Boy name{res}")
            print(f" 5. {gre}Town name{res}")
            print(f" 6. {yel}Convert{res}")
            print()
            print(f" 7. {cya}Edit Info{res}")
            print()
            print(f" 0. {red}Quit{res}")
            print()

            reply = input("> ").lower()
            if reply == "0" or reply == "q" or reply == "":
                menu_loop = self.are_you_sure()
                return menu_loop
            elif reply == "1":
                self.show_info()
            elif reply == "2":
                self.show_photo()
            elif reply == "3":
                self.choose_girl_name()
            elif reply == "4":
                self.choose_boy_name()
            elif reply == "5":
                self.choose_town_name()
            elif reply == "6":
                menu_loop = False
                self.show_convert_menu()
            elif reply == "7":
                filename = os.path.join(self.datadir, "laura.txt")
                os.system(f"vim {filename}")
            else:
                self.error("Unknown option")

    def show_convert_menu(self):
        os.system("clear")
        convert_loop = True
        res = self.colors.res
        yel = self.colors.yel
        red = self.colors.red
        pin = self.colors.pin
        cya = self.colors.cya
        blu = self.colors.blu
        gre = self.colors.gre

        while convert_loop:
            os.system("clear")
            print(f" 1. {yel}Km to M{res}")
            print(f" 2. {cya}M to Ft{res}")
            print(f" 3. {pin}Cm to Inch{res}")
            print(f" 4. {blu}Kg to Lbs{res}")
            print(f" 5. {gre}C to F{res}")
            print(f" 6. {yel}Wages{res}")
            print()
            print(f" 0. {red}Return{res}")
            print()

            reply = input("> ").lower()
            if reply == "0" or reply == "":
                convert_loop = False
                self.show_menu()
            elif reply == "1":
                self.kmtom()
            elif reply == "2":
                self.metertofeet()
            elif reply == "3":
                self.cmtoinch()
            elif reply == "4":
                self.kgtolbs()
            elif reply == "5":
                self.ctof()
            elif reply == "6":
                self.calculate_wages()
            else:
                self.error("Unkown option")

    def run(self):
        loop = True
        while loop:
            loop = self.show_menu()
        os.system("clear")
        print("Bye...")


if __name__ == "__main__":
    write = Write()
    write.run()
