#!/usr/bin/env python3
"""Utils for Zipr"""
import os
import sys
import shutil
import glob
from time import sleep
from colors import Colors
from zipfile import ZipFile, ZIP_DEFLATED

class Utils:
    def __init__(self):
        self.archive_folders = [os.path.join('~', 'Games', 'archives'),
                                os.path.join('~', 'USB', 'sexgames'),
                                os.path.join('~', 'USB', 'sexgames', 'keep'),
                                ]
        self.temp_folder = os.getcwd() 

    def colorize(self, text):
        for color in Colors.colors:
            text = text.replace(color[0], color[1])
        return text

    def show_title(self):
        os.system('clear')
        self.myprint(f"%c╭─────────────────────╮")
        self.myprint(f"│ %yZipr%R - %gversion 3.01 %c│")
        self.myprint(f"╰─────────────────────╯%R", nl=False)

    def up_and_clear(self, amount=1):
        for _ in range(amount):
            print('\033[1A', end='\x1b[2K')

    def myprint(self, text, clear=False, nl=False):
        newline = '\n\n' if nl else '\n'
        if clear:
            self.up_and_clear()
        text = self.colorize(text)
        print(text, end=newline)

    def ask_yesno(self, message, default_yes=True):
        prompt = self.colorize(f" %p>%R {message} ({'%yY%R/n' if default_yes else 'y/%yN%R'}) : ")
       
        answer = ''
        submenu = True
        while submenu: 
            answer = input(prompt).lower()
            if answer in ['', 'yes', 'y', 'no', 'n']:
                submenu = False
            else:
                self.print_error('That is not a valid response...', clear=True)
                sleep(1.5)

        if default_yes:
            if answer in ['', 'yes', 'y']:
                return True
            else: 
                return False  
        else:
            if answer in ['', 'no', 'n']:
                return False
            else:
                return True

    def print_message(self, message, clear=False, nl=False):
        message = f" %g>%R {message}"
        self.myprint(message, clear, nl)

    def print_error(self, message, clear=False, nl=False):
        message = f" %r>%R {message}"
        self.myprint(message, clear, nl)

    def print_step(self, message, clear=False, nl=False):
        message = f" %y>%R {message}"
        self.myprint(message, clear, nl)

    def print_substep(self, message, clear=False, nl=False):
        message = f"   %b└>%R {message}"
        self.myprint(message, clear, nl)
    
    def format_bytes(self, path):
        size = os.stat(path).st_size
        # 2**10 = 1024
        power = 2**10
        n = 0
        power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
        while size > power:
            size /= power
            n += 1
        filesize = f"{round(size, 2)} {power_labels[n]}b"
        return filesize

    def check_temp_directory(self, filename):
        self.print_message('Checking temporary directory')
        path = os.path.join(self.temp_folder, filename)
        if os.path.exists(path):
            os.remove(path)
            self.print_message('Temporary archive removed', clear=True)
        else:
            self.print_message('No temporary archive found', clear=True)

    def check_archives_for_zipfile(self, filename, yes=False):
        self.print_message(f'Checking whether {filename} has been archived')
        found = []
        for folder in self.archive_folders:
            path = os.path.expanduser(os.path.join(folder, filename))
            if os.path.exists(path):
                found.append(path)

        if len(found) > 0:
            times = 'time'
            entries = 'entry'
            them = 'it'

            if len(found) != 1:
                times = 'times'
                entries = 'entries'
                them = 'them'

            self.print_message(f"%i{filename}%R found {len(found)} {times} in archives...")
            if not yes:
                answer = self.ask_yesno(f'Do you want me to delete {them}?', default_yes=True)
            else:
                answer = True

            if answer == True:
                self.print_step('Removing old {entries}...', clear=True)
                for path in found:
                    self.print_substep(f"Removing %i{path}%R", clear=True)
                    os.remove(path)
                    sleep(0.8)
                self.up_and_clear(amount=2)
                self.print_message(f'Old {entries} removed...', clear=True)
        else:
            self.print_message(f'%i{filename}%R not found in the archives', clear=True)

    def clear_saves(self, filename):
        folder = os.path.join(filename.replace('.zip', ''), '**', '*.save')
        saves = glob.glob(folder, recursive=True)

        logs = glob.glob(os.path.join(folder, '**', 'log.txt'), recursive=True) 
        renpy_folder = os.path.expanduser(os.path.join('~', '.renpy'))
        if os.path.exists(renpy_folder):
            saves.append(renpy_folder)

        if len(saves) > 0:
            self.print_step(f'Clearing save files')
            for item in saves:
                if os.path.isdir(item):
                    shutil.rmtree(item)
                else:
                    os.remove(item)
                sleep(0.1)
            self.print_message(f'Save files cleared', clear=True)
        else:
            self.print_message('No save files found')

        if len(logs) > 0:
            self.print_step(f'Clearing log files')
            for item in logs:
                os.remove(item)
                sleep(0.1)
            self.print_message(f'Log files cleared', clear=True)
        else:
            self.print_message('No log files found')

    def create_zip(self, filename):
        folder = filename.replace('.zip', '')
        temp_path = os.path.join(self.temp_folder, filename)
        files = glob.glob(os.path.join(folder, '**'), recursive=True, include_hidden=True)
        total = len(files)
        lead = len(str(total))

        with ZipFile(temp_path, 'w') as zipfile:
            self.print_step(f'Archiving {0:{lead}}/{total} : ')
            for num, file in enumerate(files, start=1):
                percent = int(num * 100 / total)
                fn = '..' + file[-30:] if len(file) > 30 else file
                self.print_step(f'Archiving {num:{lead}}/{total} [{percent:3}%] : {fn}', clear=True)
                zipfile.write(file)

        self.up_and_clear()
        size = self.format_bytes(temp_path)

        zipfn = temp_path.split('/')[-1]
        self.print_message(f'Archive %i{zipfn}%R created ({size})')

    def check_zip_archive(self, filename):
        temp_path = os.path.join(self.temp_folder, filename)

        self.print_step(f'Testing %i{filename}%R')

        try:
            the_zip_file = ZipFile(temp_path)
            ret = the_zip_file.testzip()
            if ret is not None:
                print("First bad file in zip: %s" % ret)
                sys.exit(1)
        except Exception as ex:
            print("Exception:", ex)
            sys.exit(1)

        self.print_message(f"%i{filename}%R is good", clear=True)

    def move_archive(self, filename, destination, keep=False, nosync=False):
        temp_path = os.path.join(self.temp_folder, filename)
        dest_path = os.path.join(destination, filename)
        self.print_step(f'Moving %i{filename}%R to %i{destination}%R')

        copied = 0
        percent = 0
        total = os.stat(temp_path).st_size

        source = open(os.path.expanduser(temp_path), 'rb')
        target = open(os.path.expanduser(dest_path), 'wb')

        self.print_substep(f'Moving   0%')
        while True:
            chunk = source.read(32768)
            if not chunk:
                break
            copied += len(chunk)
            percent = int(copied * 100 / total)
            target.write(chunk)
            self.print_substep(f'Moving {percent:3}%', clear=True)

        source.close()
        target.close()
        if nosync == False:
            self.print_substep(f'Syncing to make sure everything has been moved', clear=True)
            os.system('sync')

        self.up_and_clear()
        self.print_step(f'%i{temp_path}%R moved to %i{destination}%R', clear=True)
        
        os.remove(os.path.expanduser(temp_path))

        if not keep:
            self.print_message(f'%i{filename}%R moved to %i{destination}%R and source folder removed',
                               clear=True)
            shutil.rmtree(filename.replace('.zip', ''))
        else:
            self.print_message(f'%i{filename}%R moved to %i{destination}%R and source is kept', clear=True)
