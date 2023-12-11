import os
import sys
import glob

from shutil import move, rmtree
from zipfile import ZipFile
from settings import *


class Utils:
    def __init__(self):
        self.title = "Arc4 - Copyright 2023 Transgirl"

    def header(self):
        os.system('clear')
        print(self.title)

    def collect_files(self, folder):
        files = glob.glob(os.path.join(folder, '**'), recursive=True)
        files.sort()
        return files

    def askyesno(self, msg):
        stay = True
        answer = ''
        while stay:
            answer = input(f"- {msg} (y/n) : ").lower()
            if answer in ['y', 'n']:
                stay = False
        return True if answer == "y" else False

    def zip(self, folder, assumeyes=False, keep=False):
        self.header()
        zipfilename = folder + ".zip"
        destpath = os.path.join(ZIPDIR, zipfilename)
        files = self.collect_files(folder)
        total = len(files)
        percent = 0

        if os.path.exists(zipfilename):
            os.remove(zipfilename)

        if os.path.exists(destpath) and not assumeyes:
            print(f"- {zipfilename} already exists!")
            answer = self.askyesno("Do you want me to delete it?")
            if answer:
                print('\033[1A', end='\x1b[2K')
                print('\033[1A', end='\x1b[2K')
                os.remove(destpath)
            else:
                print(f"Not doing anything.")
                sys.exit()

        print(f"- Archiving '{zipfilename}'")

        with ZipFile(zipfilename, 'w') as zf:
            for i, file in enumerate(files, start=1):
                percent = i * 100 // total
                name = file if len(file) < 30 else ".." + file[-28:]
                print(f"- [{percent:3}%] adding: {name}")
                zf.write(file)
                print('\033[1A', end='\x1b[2K')

        if os.path.exists(zipfilename):
            move(zipfilename, destpath)
            print("- Archive created")
        else:
            print("- Ooops! Zipfile was not created...")
            sys.exit()

        if keep:
            print("- Keeping the source folder as requested")
        else:
            rmtree(folder)

        print("- Done!")
