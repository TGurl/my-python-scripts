#!/usr/bin/env python

import os
import sys
import toml

from time import sleep
from colors import Colors
from shutil import get_terminal_size
from dataclasses import dataclass

@dataclass
class Laura:
    age = int
    rent = int
    innocence = int
    energy = int
    hunger = int
    did_chores = bool
    did_work = bool
    did_nightjob = bool
    new_arrival = bool

class Game:
    def __init__(self):
        self.colors = Colors()
        self.cols = get_terminal_size().columns
        path = os.path.dirname(__file__)
        self.textdir = os.path.join(path, 'data', 'text')
        self.tomldir = os.path.join(path, 'data', 'toml')
        self.storydir = os.path.join(path, 'data', 'story')
        self.cursor_on = True


    #----------------------------------------------------------------
    #--- Game Loop
    #----------------------------------------------------------------
    def show_introduction(self):
        os.system('clear')
        self.toggle_cursor()
        self.render_text('introduction')
        sleep(1)
        self.toggle_cursor()
        os.system('clear')

    def run(self):
        self.show_introduction()
        lines = self.read_story_file("01_start.txt")
        self.typewriter(lines)

    #----------------------------------------------------------------
    #--- Rendering texts
    #----------------------------------------------------------------
    def typewriter(self, lines):
        for line in lines:
            if line == "<BREAK>":
                sleep(5)
                os.system('clear')
            else:
                for char in line:
                    sleep(0.06)
                    sys.stdout.write(char)
                    sys.stdout.flush()
                print()

    def cprint(self, line):
        line = line.replace("*", " ")
        t = self.remove_color_codes(line)
        t = self.remove_colors(t)
        width = round((self.cols - len(t)) / 2) * " "
        print(f"{width}{line}")

    def remove_color_codes(self, line):
        codes = ['$g', '$y', '$r']
        for code in codes:
            line = line.replace(code, '')
        return line 
    
    def remove_colors(self, line):
        colors = [self.colors.green, self.colors.yellow, self.colors.reset]
        for color in colors:
            line = line.replace(color, '')
        return line

    def replace_color_codes(self, line):
        colors = [self.colors.green, self.colors.yellow, self.colors.reset]
        codes = ['$g', '$y', '$r']
        for c, code in enumerate(codes):
            line = line.replace(code, colors[c])
        return line

    def render_text(self, filename, center=True):
        lines = self.read_text_file(filename)
        for line in lines:
            line = self.replace_color_codes(line)
            if center:
                self.cprint(line)
            else:
                print(line)

        
    #----------------------------------------------------------------
    #--- File Operations
    #----------------------------------------------------------------
    def read_text_file(self, filename):
        if ".txt" not in filename:
            filename += ".txt"
        path = os.path.join(self.textdir, filename)
        with open(path, 'r') as f:
            data = f.read().splitlines()
        return data

    def read_story_file(self, filename):
        if ".txt" not in filename:
            filename += ".txt"
        path = os.path.join(self.storydir, filename)
        with open(path, 'r') as f:
            data = f.read().splitlines()
        return data
    
    #----------------------------------------------------------------
    #--- System stuff
    #----------------------------------------------------------------
    def hide_cursor(self):
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    def show_cursor(self):
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

    def toggle_cursor(self):
        self.cursor_on = not self.cursor_on
        self.show_cursor() if self.cursor_on else self.hide_cursor()
