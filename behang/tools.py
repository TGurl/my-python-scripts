#!/usr/bin/env python

import os
import sys
import glob
import toml

from pathlib import Path
from shutil import get_terminal_size
from time import sleep

class Colors:
    reset = "\033[0m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    pink = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"

class Tools:
    def __init__(self):
        self.colors = Colors()
        self.cols = get_terminal_size().columns

    # ----------------------------------------------------
    # ----- HELPER FUNCTIONS
    # ----------------------------------------------------
    def replace_color_codes(self, line):
        """Replace codes in a line with the corresponding color"""
        codes = [
            '{res}', '{black}', '{red}', '{green}',
            '{yellow}', '{blue}', '{pink}', '{cyan}',
            '{white}'
        ]
        colors = [
            self.colors.reset, self.colors.black, self.colors.red,
            self.colors.green, self.colors.yellow, self.colors.blue,
            self.colors.pink, self.colors.cyan, self.colors.white
        ]
        for c, code in enumerate(codes):
            line = line.replace(code, colors[c])
        return line

    def remove_color_codes(self, line):
        """Remove the codes from a line"""
        codes = [
            '{res}', '{black}', '{red}', '{green}',
            '{yellow}', '{blue}', '{ping}', '{cyan}',
            '{white}'
        ]
        for code in codes:
            line = line.replace(code, '')
        return line

    def remove_colors(self, line):
        """Remove the colors from a line"""
        colors = [
            self.colors.reset, self.colors.black, self.colors.red,
            self.colors.green, self.colors.yellow, self.colors.blue,
            self.colors.pink, self.colors.cyan, self.colors.white
        ]
        for color in colors:
            line = line.replace(color, '')
        return line

    # ----------------------------------------------------
    # ----- TERMINAL USER INTERFACE
    # ----------------------------------------------------
    def clear(self):
        """Clear the terminal"""
        os.system('clear')

    def hide_cursor(self):
        """Hide the cursor"""
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    def show_cursor(self):
        """Show the cursor"""
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

    def cprint(self, message):
        """Print a text in the middle of the screen"""
        # --- just to be sure we are going to remove both
        # --- the colors and the codes, otherwise centering
        # --- the message will not succeed.
        temp = self.remove_color_codes(message)
        temp = self.remove_colors(message)
        spaces = int((self.cols - len(temp)) / 2) * " "
        print(f"{spaces}{message}")

    def message(self, message="", prompt="»"):
        """Print a message to the screen"""
        col = self.colors.green
        res = self.colors.reset
        if message != "":
            message = f" {message}"
        print(f"{col}{prompt}{res}{message}")

    def error(self, message="", prompt="ε"):
        """Print an error to the screen"""
        col = self.colors.red
        res = self.colors.reset
        if message != "":
            message = f" {message}"
        print(f"{col}{prompt}{res}{message}")

    def warning(self, message="", prompt=">>"):
        """"Print a warning to the screen"""
        col = self.colors.yellow
        res = self.colors.reset
        if message != "":
            message = f" {message}"
        print(f"{col}{prompt}{res}{message}")

    def info(self, message="", prompt="►"):
        """Print some information to the screen"""
        col = self.colors.blue
        res = self.colors.reset
        if message != "":
            message = f" {message}"
        print(f"{col}{prompt}{res}{message}")

    def generate_menu(self, items):
        """Generate a simple menu"""
        menu = ""
        col = self.colors.yellow
        cya = self.colors.cyan
        res = self.colors.reset
        for item in items:
            letter = item[0]
            the_rest = item[1:]
            if letter in ['q', 'Q']:
                col = self.colors.red
                menu += "\n"
            menu += f"{cya}[{col}{letter}{cya}]{res} {the_rest}\n"
        return menu

    def bigletters(self, text):
        alphabet = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', '.', '!', '?', ' '
        ]
        letters = [
            '█▀█n█▄█', '▄█n █', '▀█n█▄', '▀▀█n▄██', '█ █n▀▀█',
            '█▀n▄█', '█▄▄n█▄█', '▀▀█n  █', '███n█▄█', '█▀█n▀▀█',
            '▄▀█n█▀█', '█▄▄n█▄█', '█▀▀n█▄▄', '█▀▄n█▄▀', '█▀▀n██▄',
            '█▀▀n█▀ ', '█▀▀n█▄█', '█ █n█▀█', '█n█', '  █n█▄█',
            '█▄▀n█ █', '█  n█▄▄', '█▀▄▀█n█ ▀ █', '█▄ █n█ ▀█',
            '█▀█n█▄█', '█▀█n█▀▀', '█▀█n▀▀█', '█▀█n█▀▄', '█▀n▄█',
            '▀█▀n █ ', '█ █n█▄█', '█ █n▀▄▀', '█ █ █n▀▄▀▄▀',
            '▀▄▀n█ █', '█▄█n █ ', '▀█n█▄', ' n▄', '█n▄', '▀█n ▄',
            'n'
        ]
        def convert(text):
            small = []
            big = []
            small.extend(text.replace("_", " ").lower())
            for letter in small:
                idx = alphabet.index(letter)
                sign = letters[idx]
                big.append(sign)
            return big

        # ----- create the bigletters now
        topline = ""
        botline = ""
        letters = convert(text)
        for letter in letters:
            parts = letter.split('n')
            topline += parts[0] + ' '
            botline += parts[1] + ' '
        return f"{topline}\n{botline}\n"

    # ----------------------------------------------------
    # ----- USER INPUT
    # ----------------------------------------------------
    def userinput(self, message="", prompt=">", lower=False):
        """Get the user input with a custom message and prompt"""
        col = self.colors.green
        res = self.colors.reset
        message = f"{col}{prompt}{res} {message} : "
        answer = input(message).lower() if lower else input(message)
        return answer

    def getyesno(self, message="", prompt=">", yesdefault=True):
        """
        Get a yes or no answer, defaults to yes
            message     the question to ask (with the ?)
            prompt      the prompt to show, default >
            yesdefault  boolean, wheter default answer is yes

            returns the answer in lowercase 
        """
        col = self.colors.green
        res = self.colors.reset

        if yesdefault:
            yesno = f"({col}Y{res}/n)"
            default = "y"
        else:
            yesno = f"(y/{col}N{res})"
            default = "n"

        answer = ""
        subloop = True
        while subloop:
            answer = input(f"{col}>{res} {message} {yesno} : ").lower()
            if answer not in ['y', 'n', 'yes', 'no', '']:
                self.error("That doesn't seem quit right...")
                sleep(2)
            else:
                answer = default if answer=="" else answer
                subloop = False
        return answer

    # ----------------------------------------------------
    # ----- TOML FILE OPERATIONS
    # ----------------------------------------------------
    def readtoml(self, path):
        """
        Reads the contents of a toml file and returns the content as a list
            path    full path to toml file
            returns list
        """
        with open(path, 'r') as f:
            data = toml.load(f)
        return data
    
    def savetoml(self, path, data):
        """
        Save the data to a toml file
            path    full path to toml file
            returns nothing
        """
        with open(path, 'w') as f:
            result = toml.dump(data, f)
        return result

    # ----------------------------------------------------
    # ----- TEXT FILE OPERATIONS
    # ----------------------------------------------------
    def readtext(self, path):
        """
        Reads the content of a text file and returns it as list
            path    Full path to text file
            returns list
        """
        with open(path, 'r') as f:
            data = f.read().splitlines()
        return data

    def savetext(self, path, data):
        """
        Save data to a text file !overwrites original file!
            data    list of lines to save
            returns nothing
        """
        with open(path, 'w') as f:
            for line in data:
                f.write(f"{line}\n")

    def appendtext(self, path, data):
        """
        Save data to a text file !appends to origal file!
            data    list of lines to save
            returns nothing
        """
        with open(path, 'a+') as f:
            for line in data:
                f.write(f"{line}\n")

    # ----------------------------------------------------
    # ----- GENERAL FILE OPERATIONS
    # ----------------------------------------------------
    def check_if_it_exists(self, path):
        return os.path.exists(path)

    def mkdir(self, path):
        return os.mkdir(path)

    def remove_file(self, path):
        return os.remove(path)

    def get_folders_in_folder(self, path, ignore=[]):
        folders = []
        for item in os.scandir(path):
            if item.is_dir() and item.name not in ignore:
                folders.append(item.name)
        return folders

    def get_contents_of_folder(self, path, extension=""):
        data = []
        if extension != "":
            extension = f".{extension}"
        for item in os.scandir(path):
            if extension in item.name :
                data.append(item.name)
        return data

    def get_contens_of_folder_recursive(self, path, extension="*"):
        return glob.iglob(f"{path}/**/*.{extension}", recursive=True)

    # ----------------------------------------------------
    # ----- 
    # ----------------------------------------------------
