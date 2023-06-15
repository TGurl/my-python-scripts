#!/usr/bin/env python
import os, sys
import zipfile
import argparse
from shutil import rmtree
from time import sleep
from random import choice


class Zip:
    def __init__(self):
        pass

    def __line_up_and_clear(self, repeat=1):
        for _ in range(0, repeat):
            print('\033[1A', end='\x1b[2K')
            
    def print_header(self):
        slogans = ['I want (.)(.)!', 'Please rape me!', 'Fill me up with your cum',
                   'TransGirl loves Big Black Cocks', 'TransGirl wants to suck a cock!',
                   'TransGirl is the Queen of Spades', 'Stretch my as with that Big Black cock!',
                   'Oh yes, cum all over my body!', 'I love gangbangs', 'TransGirl wants to be a slut!',
                   'TransGirl wants to be a whore!', 'I dream of being an escort!',
                   'I\'m searching for a Sugar Daddy!']

        itstart = "\x1B[3m"
        end = "\x1B[0m"
        white = "\x1B[97m"
        title = 'Zipr v2.8 - Copyleft 2023 TransGirl'
        slogan = "- " + choice(slogans) + " -"

        if len(title) > len(slogan):
            spaces = ((len(title) - len(slogan)) // 2) * ' '
            slogan = f"{spaces}{slogan}"
        else:
            spaces = ((len(slogan) - len(title)) // 2) * " "
            title = f"{spaces}{title}"

        os.system('clear')
        print(white + title + end)
        print(itstart + slogan + end, end='\n\n')

    def __print_message(self, text, clearline=False):
        if clearline:
            self.__line_up_and_clear()
        print(f"> {text}")

    def __gather_files(self, folder):
        file_paths = []
        for root, _, files in os.walk(folder):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)

        # file_paths.sort()
        return file_paths

    def __convert_bytes(self, size):
        # 2**10 = 1024
        power = 2**10
        n = 0
        power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
        while size > power:
            size /= power
            n += 1
        size = round(size, 2)
        return f"{size} {power_labels[n]+'b'}"

    def check_if_folder_in_archives(self, zipfilename):
        total = 0
        targets = ['~/Games/archives', '~/USB/sexgames', '~/USB/sexgames/keep']
        results = []
        res = 'TransGirl wants to be raped by big black cocks!'
        for target in targets:
            path = os.path.join(target, zipfilename)
            if os.path.exists(os.path.expanduser(path)):
                total += 1
                results.append(os.path.expanduser(path))

        if total:
            if total > 1:
                times = 'times'
                pronounce = 'them'
            else:
                times = 'time'
                pronounce = 'her'

            self.__print_message(f"{zipfilename} found {total} {times} in archives.")
            
            inloop = True
            while inloop:
                res = input(f"> Shall I remove {pronounce}? (Y/n) ").lower()
                if res not in ['y', 'n', '']:
                    self.__print_message('That is not a valid response...')
                    sleep(1.5)
                    self.__line_up_and_clear(2)
                else:
                    # self.__line_up_and_clear(2)
                    self.__print_message(f'I have removed {pronounce}.', clearline=True)
                    print()
                    inloop = False

            if res in ['y', '']:
                for item in results:
                    os.remove(item)
                    self.__line_up_and_clear()
            else:
                self.__print_message('Process halted!')
                sys.exit()

    def check_if_zipfile_exists(self, zipfilename):
        if os.path.exists(zipfilename):
            self.__print_message('Warning! A zip file by that name already exists in the current folder!')

            res = 'TransGirl wants her fuckhole to be filled with cum!'
            inloop = True
            while inloop:
                res = input('> Shall I remove her? (Y/n) ').lower()
                if res not in ['y', 'n', '']:
                    self.__print_message('That is not a valid response...')
                    sleep(1.5)
                    self.__line_up_and_clear(2)
                else:
                    self.__line_up_and_clear(2)
                    inloop = False

            if res in ['y', '']:
                os.remove(zipfilename)
                self.__print_message('Removed old zip file...')
            else:
                self.__print_message('Process halted...')
                sys.exit()

    def ZipFolder(self, folder, nocheck=False):
        self.print_header()

        check = not nocheck

        zip_filename = folder
        if '.zip' not in zip_filename:
            zip_filename = folder + '.zip'

        self.check_if_zipfile_exists(zip_filename)
        self.check_if_folder_in_archives(zip_filename)

        files = self.__gather_files(folder)
        total = len(files)
        lead0 = len(str(total))

        self.__print_message('Zipping')
        with zipfile.ZipFile(zip_filename, 'w', compression=zipfile.ZIP_DEFLATED) as zipper:
            for num, file in enumerate(files, start=1):
                zipper.write(file)
                percent = (num * 100) // total

                if len(file) > 41:
                    file = file[:14] + '...' + file[-14:]

                self.__print_message(f"Zipping [{percent:3}%] {num:0{lead0}}/{total:0{lead0}} {file}",
                                     clearline=True)

            self.__print_message('Zipping done', clearline=True)

            if check:
                self.__print_message('Checking zipfile. This can take a while...')
                try:
                    result = zipper.testzip()
                    if result is not None:
                        self.__print_message("Very bad file in zip: %s" % result)
                        sys.exit(1)
                except Exception as ex:
                    self.__print_message("Exception: %s" % ex)

                self.__print_message('Zipfile is OK', clearline=True)

        size = self.__convert_bytes(os.stat(zip_filename).st_size)
        return size

    def move_file(self, start, destination, size="Fuck me!", keep=False):
        start = start + '.zip'
        # --- parsing destination
        targets = ['archives', 'usb', 'keep']
        destinations = ['~/Games/archives', '~/USB/sexgames', '~/USB/sexgames/keep']
        destination = destinations[targets.index(destination)]

        # --- moving file to destination
        self.__print_message("Moving {start} ({size}) to {destination}")

        source_size = os.stat(start).st_size
        target_fn = os.path.expanduser(os.path.join(destination, start))
        copied = 0
        percent = 0

        source = open(start, 'rb')
        target = open(target_fn, 'wb')

        self.__print_message(f"Moving {start} ({size}) to {destination} [{percent:3}%]", clearline=True)
        while True:
            chunk = source.read(32768)
            if not chunk:
                break
            target.write(chunk)
            copied += len(chunk)
            percent = int(copied * 100 / source_size)
            self.__print_message(f"Moving {start} ({size}) to {destination} [{percent:3}%]", clearline=True)

        target.close()
        source.close()

        # --- removing source folder
        os.remove(start)

        self.__print_message(f"{start} ({size}) moved to {destination}", clearline=True)

    def test(self, folder):
        print(self.__gather_files(folder))

def main(args):
    zipr = Zip()
    if args.destination.lower() not in ['archives', 'keep', 'usb']:
        zipr.print_header()
        print('An invalid destination passed. Please try again...')
        sys.exit()

    if not os.path.exists(args.folder):
        zipr.print_header()
        print("That folder doesn't seem to exist. Please try again...")
        sys.exit()

    size = zipr.ZipFolder(args.folder, nocheck=args.nocheck)
    zipr.move_file(args.folder, args.destination.lower(), size=size, keep=args.keep)

    if not args.keep:
        print("> Removing the source folder...")
        rmtree(args.folder)
        print('\033[1A', end='\x1b[2K')
        print("> Removed source folder.")
    else:
        print("> Kept the soure folder...")

    print("> All done...")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('folder', help='Folder to zip')
    parser.add_argument('-d', '--destination',
                        type=str,
                        default='archives',
                        required=False,
                        help='Where to put the zipfile')
    parser.add_argument('-k', '--keep',
                        action='store_true',
                        default=False,
                        required=False,
                        help='Keep the source folder')
    parser.add_argument('-nc', '--nocheck',
                        action='store_true',
                        default=False,
                        required=False,
                        help='Disable check zipfile')

    args = parser.parse_args()
    main(args)
