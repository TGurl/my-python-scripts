import os
import sys
import zipfile
import glob
from shutil import rmtree
from time import sleep
from random import choice


class Settings:
    title = 'Zipr'
    version = 'v3.0'
    cright = 'Copyright (c) 2023 TransGirl'
    tagline = ['Back to basics',
               'I want to suck a cock!',
               'I love Big Black Cocks',
               'I want to be raped',
               'I am a Queen of Spades',
               'I love a BBC up my ass',
               'Fill me up with your cum'
               ]


class TUI:
    def __init__(self):
        pass

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def ask_yesno(self, prompt):
        prompt = f"{prompt} (Y/n) : "
        res = '-1'

        insub = True
        while insub:
            res = input(prompt).lower()
            insub = False if res in ['y', 'n', ''] else True

        return True if res in ['y', ''] else False

    def print_header(self):
        self.clear_screen()
        tagline = choice(Settings.tagline)
        lines = [f"{Settings.title}  {Settings.version}",
                 f"{tagline}"]
        maxlen = 0
        for line in lines:
            if len(line) > maxlen:
                maxlen = len(line)

        horline = '+' + ((maxlen + 2) * '-') + '+'
        print(horline)
        for line in lines:
            if len(line) < maxlen:
                spaces = ((maxlen - len(line)) // 2) * ' '
            else:
                spaces = ''
            print(f"| {spaces}{line}{spaces} |")
        print(horline, end='\n\n')

    def print_message(self, text, clear_line=False):
        if clear_line:
            print('\033[1A', end='\x1b[2K')
        print(f"> {text}")
    
    def print_error(self, text, clear_line=False):
        if clear_line:
            print('\033[1A', end='\x1b[2K')
        print(f"! {text}")


class Zipit(TUI):
    def __init__(self, folder_name, check):
        self.folder = folder_name
        self.check = check
        self.tui = TUI()
        self.fileio = FileIO()

    def start(self):
        zipfile_name = self.folder + '.zip'
        
        self.print_header()
        self.fileio.check_all_destinations(zipfile_name)
        self.fileio.clear_save_files(self.folder)

        self.print_message(f"Creating {zipfile_name}...", clear_line=True)
        # ---------------------------- Zip the folder
        if self.fileio.check_if_path_exists(zipfile_name):
            prompt = f"- {zipfile_name} found in working directory. Do you want to remove it?"
            if self.ask_yesno(prompt):
                os.remove(zipfile_name)
                print('\033[1A', end='\x1b[2K')

        prompt = f"Creating zip"
        self.print_message(prompt, clear_line=True)
       
        all_files = self.fileio.collect_files_in_folder(self.folder)
        total = len(all_files)

        # ---------------------------- Actually do the zipping
        zip_file = zipfile.ZipFile(zipfile_name, 'w', zipfile.ZIP_DEFLATED)
        for num, item in enumerate(all_files, start=1):
            item_str = item
            if len(item_str) > 20:
                item_str = item_str[:10] + '...' + item_str[-10:]
            percentage = (num * 100) // total
            prompt = f"Creating {zipfile_name} {percentage:3}% - Adding: {item_str}"
            self.print_message(prompt, clear_line=True)
            zip_file.write(item)

        # ---------------------------- Checking the archive
        if self.check:
            self.print_message(f"Checking {zipfile_name}. This can take a while...", clear_line=False)
            
            try:
                ret = zip_file.testzip()
                if ret is not None:
                    self.print_error('Bad file in zip: %s' % ret, clear_line=True)
                    sys.exit()
            except Exception as ex:
                self.print_error(f"Exception: %s" % ex, clear_line=True)
                sys.exit()

            self.print_message(f"{zipfile_name} is OK", clear_line=True)
            sleep(1.5)

        zip_file.close()
        # -------------------------------------------
        print('\033[1A', end='\x1b[2K')
        prompt = f"Creating zip done"
        self.print_message(prompt, clear_line=True)

class FileIO(TUI):
    def __init__(self):
        pass

    def check_if_path_exists(self, path):
        return True if os.path.exists(path) else False

    def collect_files_in_folder(self, foldername):
        pattern = os.path.join(foldername, '**')
        return glob.glob(pattern, recursive=True, include_hidden=True)

    def clear_save_files(self, folder):
        if os.path.exists(os.path.expanduser('~/.renpy')):
            rmtree(os.path.expanduser('~/.renpy'))

        files = glob.glob(os.path.join(folder, '**', 'saves'))
        for file in files:
            rmtree(file)

    def parse_destination(self, destination):
        match destination:
            case 'keep': final_destination = os.path.expanduser('~/USB/sexgames/keep')
            case 'usb': final_destination = os.path.expanduser('~/USB/sexgames')
            case 'archives': final_destination = os.path.expanduser('~/Games/archives')
            case _ :
                self.print_error("Unknown destination! Please try again...")
                sys.exit()
        return final_destination

    def check_all_destinations(self, filename):
        self.print_message('Checking destinations...')
        found = []
        dests = ['~/Games/archives', '~/USB/sexgames/', '~/USB/sexgames/keep']
        for dest in dests:
            check = os.path.expanduser(os.path.join(dest, filename))
            if os.path.exists(check):
                found.append(check)

        if len(found):
            num = len(found)
            times = 'times' if num > 1 else 'time'
            prompt = f"! {filename} found {num} {times}. Do you want to remove "
            if len(found) == 1:
                prompt += 'it?'
            else:
                prompt += 'them?'
            
            print('\033[1A', end='\x1b[2K')
            if self.ask_yesno(prompt):
                self.print_message("Removing old versions...", clear_line=True)
                for item in found:
                    os.remove(item)

    def move_file(self, source_fn, destination, keep=False):
        # self.check_all_destinations(source_fn)
        destination = self.parse_destination(destination)
        source_size = os.stat(source_fn).st_size
        target_fn = os.path.join(destination, source_fn)

        #if self.check_if_path_exists(target_fn):
        #    self.print_error(f"{target_fn} already exists...", clear_line=True)
        #    if self.ask_yesno('Do you want to remove it?'):
        #        os.remove(target_fn)
        #        self.print_message(f"{target_fn} removed", clear_line=True)
        #    else:
        #        self.print_message(f"Process halted. {target_fn} already exists...")
        #        sys.exit()

        copied = 0
        source = open(source_fn, 'rb')
        target = open(target_fn, 'wb')
        
        self.print_message(f"Moving {source_fn} to {destination} [  0%]")
        perc = 0
        while True:
            chunk = source.read(32768)
            if not chunk:
                break
            target.write(chunk)
            copied += len(chunk)
            perc = int(copied * 100 / source_size)
            self.print_message(f"Moving {source_fn} to {destination} [{perc:3}%]", clear_line=True)

        source.close()
        target.close()
        os.remove(source_fn)
        if not keep:
            source_fn = source_fn.replace('.zip', '')
            rmtree(source_fn)
        
        prompt = f"Moving done"
        self.print_message(prompt, clear_line=True)
