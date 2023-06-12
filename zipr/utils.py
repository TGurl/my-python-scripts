import os, sys
import glob
import zipfile
import shutil
import math
from settings import *
from colors import *
from time import sleep
from random import choice


class Utils:
    def __init__(self):
        self.cursor = True
        self.debug = True
    
    def show_title(self):
        os.system('clear')
        title = f"{TITLE}  {VERSION}"
        cr = "Copyright (C) 2023 TransGirl"
        length = len(cr)
        spaces = ((length - len(title)) // 2) * " "
        dashes = (length + 2) * '@'
        lines = []
        lines.append(f"${dashes}%")
        lines.append(f"# %y{spaces}{title}{spaces}%R #")
        lines.append(f"# %w{cr}%R #")
        lines.append(f"&{dashes}*")
        chars  = [('$', '%c╭'),
                ('%', '%c╮'),
                ('&', '%c╰'),
                ('*', '%c╯%R'),
                ('#', '%c│'),
                ('@', '%c─')]
        for line in lines:
            for char in chars:
                line = self.colorize(line.replace(char[0], char[1]))
            print(line)

    def colorize(self, text):
        for color in Colors.colors:
            text = text.replace(color[0], color[1])
        return text

    def show_quote(self):
        quotes = [
                'Now go suck a dick...',
                'Life needs things to live',
                'TransGirl craves a Big Black Cock!',
                'Oh daddy, fill me up. I want your baby...',
                'I love fucking daddy, mommy. He feels so good..',
                'TransGirl wants to be gangraped!'
                ]
        print()
        quote = self.colorize(f"%y{choice(quotes)}%R")
        print(f"> {quote} <")

    def toggle_cursor(self):
        if self.cursor:
            print('\033[? 25l', end="")
            self.cursor = False
        else:
            print('\033[? 25h', end="")
            self.cursor = True

    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        # s = round(size_bytes / p, 2)
        s = round(size_bytes / p)
        return '%s %s' % (s, size_name[i])

    def print_message(self, message, style='info', nl=False, stop=False):
        newline = '\n\n' if nl else '\n'
        match style:
            case 'error' : prompt = self.colorize('%rERROR%R :')
            case 'saves' : prompt = self.colorize('%wSAVES%R :')
            case 'move' : prompt = self.colorize('%bMOVE%R  :')
            case 'zip' : prompt = self.colorize('%gZIP%R   :')
            case _ : prompt = self.colorize('%yINFO%R  :')
        
        print(f"{prompt}", message, end=newline)
        if stop:
            sys.exit()
    
    def print_info(self, title, message, nl=False):
        newline = '\n\n' if nl else '\n'
        title = self.colorize(title)
        message = self.colorize(message)
        print(title, message, end=newline)

    def ask_yes_no(self, message):
        prompt = self.colorize(f"%yINPUT%R: {message} (%gY%R/n) : ")
        inloop = True
        answer = 'y'
        while inloop:
            answer = input(prompt).lower()
            if answer not in ['y', 'n', '']:
                self.print_message('Not a valid answer', style='error')
                sleep(2)
                print('\033[1A', end='\x1b[2K')
            else:
                inloop = False
        
        print('\033[1A', end='\x1b[2K')
        return True if answer == 'y' or answer == '' else False

    def parse_destination(self, destination):
        match destination:
            case 'keep':
                return os.path.expanduser(DEST_KEEP)
            case 'archives':
                return os.path.expanduser(DEST_ARC)
            case 'usb':
                return os.path.expanduser(DEST_USB)
            case _:
                self.print_message('Unknown destination chosen.', style='error')
                self.print_message('Choose either usb, keep or archives', style='info', stop=True)
                sys.exit()

    def collect_contents_folder(self, folder):
        pattern = os.path.join(folder, '**')
        content = glob.glob(pattern, recursive=True, include_hidden=True)
        return content

    def zip_it(self, folder, nocheck):
        if not self.debug:
            self.toggle_cursor()

        files_to_zip = self.collect_contents_folder(folder)
        
        if '.zip' not in folder:
            folder += '.zip'

        if os.path.exists(folder):
            self.print_message(f"'{folder}' already exists in the current directory.", style='error')
            answer = self.ask_yes_no('Do you want to delete it?')
            if answer:
                print('\033[1A', end='\x1b[2K')
                self.print_message(f"Preemptively removed '{folder}'", style='info')
                os.remove(folder)
            else:
                self.print_message('Exiting...', style='info', stop=True)

        total = len(files_to_zip)
        lead = len(str(total))
        
        zip_filename = zipfile.ZipFile(folder, 'w', zipfile.ZIP_DEFLATED)

        for num, file in enumerate(files_to_zip, start=1):
            filestr = file
            if len(file) > 50:
                filestr = file[:23] + '...' + file[-27:]
            percentage = (num * 100) // total
            self.print_message(f'{percentage}% {num:0{lead}}/{total:0{lead}} {filestr}', style='zip')
            zip_filename.write(file)
            print('\033[1A', end='\x1b[2K')

        if not nocheck:
            self.print_message('Checking archive...', style='zip')
            
            try:
                ret = zip_filename.testzip()
                if ret is not None:
                    self.print_message('Bad file in zip: %s' % ret, style='error', stop=True)
            except Exception as ex:
                self.print_message(f"Exception: {ex}", style='error', stop=True)

            print('\033[1A', end='\x1b[2K')
        
        zip_filename.close()
        size = self.convert_size(os.stat(folder).st_size)

        self.print_message(f'Done. Size: {size}', style='zip')

        if not self.debug:
            self.toggle_cursor()
    
    def move_archive(self, src, dst):
        tagline = f"Moving '{src}' to '{dst}'"
        dst = os.path.join(self.parse_destination(dst), src)
        if os.path.exists(dst):
            answer = self.ask_yes_no(f"{src} already exists in destination. Delete it?")
            if answer:
                os.remove(dst)
            else:
                self.print_message("Can't continue. {dst} already exists...", style='error')
                sys.exit()

        if not self.debug:
            self.toggle_cursor()
        source_size = os.stat(src).st_size
        copied = 0
        source = open(src, 'rb')
        target = open(dst, 'wb')

        while True:
            chunk = source.read(32768)
            if not chunk:
                break
            target.write(chunk)
            copied += len(chunk)
            percentage = copied * 100 // source_size
            self.print_message(f"{percentage}% {tagline}", style='move')
            print('\033[1A', end='\x1b[2K')

        os.remove(src)
        self.print_message('Done', style='move')
        if not self.debug:
            self.toggle_cursor()

    def clear_saves(self, folder):
        self.print_message('Clearing saves...', style='saves')
        sleep(0.5)
        # Collect all 'save' folders in 'folder'
        pattern1 = os.path.join(folder, '**', 'saves')
        pattern2 = os.path.expanduser(os.path.join('~', '.renpy'))

        save_folders1 = glob.glob(pattern1, recursive=True, include_hidden=True)
        save_folders2 = glob.glob(pattern2, recursive=True, include_hidden=True)
        
        if len(save_folders1) > 0:
            for folder in save_folders1:
                shutil.rmtree(folder)

        if len(save_folders2) > 0:
            for folder in save_folders2:
                shutil.rmtree(folder)
        
        print('\033[1A', end='\x1b[2K')
        if len(save_folders1) > 0 or len(save_folders2):
            self.print_message('Done', style='saves')
        else:
            self.print_message('No saves found', style='saves')

    def remove_source(self, folder):
        self.print_message(f"Deleting '{folder}'...", style='saves')
        shutil.rmtree(folder)
        print('\033[1A', end='\x1b[2K')

    def zipfolder(self, folder, dest, nocheck, keep, clearsaves):
        zip_filename = folder + '.zip'
        final_destination = self.parse_destination(dest.lower())

        fstr = '%rFalse%R'
        tstr = '%gTrue%R'
        
        self.print_info(self.colorize('%c- Zipfile       :%R'), f'%w{zip_filename}%R')
        self.print_info(self.colorize('%c- Destination   :%R'), f'%w{final_destination}%R')

        prompt = self.colorize('%c- Clear saves   :%R')
        if clearsaves:
            self.print_info(prompt, tstr)
        else:
            self.print_info(prompt, fstr)

        prompt = self.colorize('%c- Check archive :%R')
        if nocheck:
            self.print_info(prompt, fstr)
        else:
            self.print_info(prompt, tstr)

        prompt = self.colorize('%c- Keep source   :%R')
        if keep:
            self.print_info(prompt, tstr)
        else:
            self.print_info(prompt, fstr, nl=True)

        del prompt
        if clearsaves:
            self.clear_saves(folder)
        
        self.zip_it(folder, nocheck)
        self.move_archive(zip_filename, dest)
    
        if not keep:
            self.remove_source(folder)
