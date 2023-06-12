#!/usr/bin/env python
import os, sys
import shutil
import math
import glob
import zipfile


# -------------------------------------------------
# --- Class Colors
# -------------------------------------------------
class Colors:
    reset = "\033[0m"
    black = "\033[30;1m"
    red = "\033[31;1m"
    green = "\033[32;1m"
    yellow = "\033[33;1m"
    blue = "\033[34;1m"
    pink = "\033[35;1m"
    cyan = "\033[36;1m"
    white = "\033[37;1m"
    gray = "\033[37m"

    codes = ['%R', '%B', '%G', '%r', '%g', '%y', '%b', '%p', '%c', '%w']
    colors = [
            ('%R', reset),
            ('%B', black),
            ('%G', gray),
            ('%r', red),
            ('%g', green),
            ('%y', yellow),
            ('%b', blue),
            ('%p', pink),
            ('%c', cyan),
            ('%w', white)
    ]

# -------------------------------------------------
# --- Class MyUtils
# -------------------------------------------------
class MyUtils:
    def __init__(self):
        pass
    
    # ---------------------------------------------
    # --- Support functions
    # ---------------------------------------------
    def clear_screen(self):
        """Clear the screen"""
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def colorize(self, text):
        for color in Colors.colors:
            text = text.replace(color[0], color[1])
        return text

    def decolorize(self, text):
        for code in Colors.codes:
            text = text.replace(code, '')
        return text

    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return '%s %s' % (s, size_name[i])

    def determine_longest_line(self, lines):
        max_length = 0
        for line in lines:
            if len(line[0]) > max_length:
                max_length = len(line[0])
        return max_length

    # ---------------------------------------------
    # --- File I/O
    # ---------------------------------------------
    def remove_folder(self, folderName):
        """Remove a folder recursive"""
        shutil.rmtree(folderName)

    def create_folder(self, folderName):
        """Create a folder"""
        os.mkdir(folderName)

    def collect_contents_folder(self, pattern):
        """
        Collect all files in a folder according to a pattern

        eg. pattern = 'foldername/**.png' to collect all png files
        """
        content = glob.glob(pattern, recursive=True, include_hidden=True)
        return content

    def read_contents_textfile(self, fileName):
        """Read contents of file into list"""
        with open(fileName, 'r') as file:
            content = file.read().splitlines()
        return content

    # ---------------------------------------------
    # --- Print messages
    # --------------------------------------------- 
    def print_message(self, message, style='info', clear=False, nl=False, stop=False):
        """Print a message to the screen"""
        newline = '\n\n' if nl else '\n'
        message = self.colorize(message)

        match style:
            case 'error'   : prompt = '[%rERROR%R]   :'
            case 'warning' : prompt = '[%yWARNING%R] :'
            case 'move'    : prompt = '[%cMove%R]    :'
            case 'zip'     : prompt = '[%bZIP%R]     :'
            case _         : prompt = '[%wINFO%R]    :'

        prompt = self.colorize(prompt)

        if clear:
            print('\033[1A', end='\x1b[2K')

        print(f"{prompt} {message}", end=newline)
        
        if stop:
            sys.exit()

    def print_info(self, lines):
        """
        Print info given in an array
        e.g. lines = [('title', 'message')]
        """
        max_length = self.determine_longest_line(lines)

        for line in lines:
            spaces = (max_length - len(line)) * ' '
            print(f'{line[0]}{spaces}:', line[1])

    # ------------------------------------------------
    # --- Box It - draw a fancy box surrounding text
    # ------------------------------------------------
    def boxit(self, lines, width=0, clearscreen=False, color='%c', nl=False):
        """
        Draw a nice box around an array given
        e.g. lines = ['line1', 'line2']
        """
        if clearscreen:
            self.clear_screen()

        if width == 0:
            max_length = 0
            for line in lines:
                temp = self.decolorize(line)
                if len(temp) > max_length:
                    max_length = len(temp)
        else:
            max_length = width

        newline = '\n\n' if nl else '\n'
        chars  = ['╭', '╮', '╰', '╯', '│', '─']
        horline = (max_length + 2) * chars[5]
        topline = f'{color}' + chars[0] + horline + chars[1] + '%R'
        botline = f'{color}' + chars[2] + horline + chars[3] + '%R'
        info = []
        for line in lines:
            temp = self.decolorize(line)
            spacesl, spacesr = '', ''
            num_spaces = 0
            if len(temp) < max_length:
                num_spaces = ((max_length - len(temp)) // 2)
          
                spacesl = num_spaces * ' '
                if num_spaces % 2 != 0:
                    spacesr = (num_spaces + 1) * ' '
                else:
                    spacesr = spacesl
            
            info.append(f'{color}' + chars[4] + f" {spacesl}{line}{spacesr} {color}" + chars[4] + '%R')

        print(self.colorize(topline))
        for line in info:
            print(self.colorize(line))
        print(self.colorize(botline), end=newline)
