#!/usr/bin/env python

import os
import toml
import shutil

from random import randint
from time import sleep


class FileIO:
    def __init__(self):
        cwd = os.path.dirname(__file__)
        self.tomldir = os.path.join(cwd, 'data', 'toml')
        self.textdir = os.path.join(cwd, 'data', 'text')
        self.imgdir = os.path.join(cwd, 'data', 'img')

    # ---------------------------------------------------------
    # ------ Copied here to prevent circular imports
    # ---------------------------------------------------------
    def message(self, msg):
        col = self.colors.green
        res = self.colors.reset
        prompt = ">"
        print(f"{col}{prompt}{res} {msg}")

    def error(self, msg):
        col = self.colors.red
        res = self.colors.reset
        prompt = ">>"
        print(f"{col}{prompt}{res} {msg}")

    def warning(self, msg):
        col = self.colors.yellow
        res = self.colors.reset
        prompt = ">>"
        print(f"{col}{prompt}{res} {msg}")

    # ---------------------------------------------------------
    # ------ CREATE A DIRECTORY
    # ---------------------------------------------------------
    def makedir(self, dirname):
        """A simple function to create a folder in the image folder"""
        path = os.path.join(self.imgdir, dirname)
        if not os.path.exists(path):
            os.mkdir(path)
            self.message("Image folder created.")
        else:
            self.message("Image folder already exists, creation skipped.")

    # ---------------------------------------------------------
    # ------ HELPER FUNCTIONS
    # ---------------------------------------------------------
    def checkfilename(self, filename, filetype="toml"):
        """Check if a filename has the correct extensions"""
        if filetype == "toml":
            filename += ".toml" if ".toml" not in filename else ""
        elif filetype == "text":
            filename += ".txt" if ".txt" not in filename else ""
        else:
            print("[CheckFilename] Unknown filetpe, exiting...")
            exit()
        return filename

    # ---------------------------------------------------------
    # ------ TOML
    # ---------------------------------------------------------
    def readtoml(self, filename):
        """Read a toml file and return the data"""
        filename = self.checkfilename(filename, filetype='toml')
        path = os.path.join(self.tomldir, filename)
        with open(path, "r") as f:
            data = toml.load(f)
        return data

    def appendtotoml(self, babeinfo, pornstars, filename='pornstars'):
        """Appends data to a toml file as text"""
        filename = self.checkfilename(filename, filetype='toml')
        backup = filename + ".backup"
        
        path = os.path.join(self.tomldir, filename)
        backuppath = os.path.join(self.tomldir, backup)
        shutil.copy2(path, backuppath)

        current = self.readtext(path, checkext=False)
        # ---- remove pornstar list from the text
        idx = current.index("[template]")
        del current[0:idx]

        # ---- create pornstar list
        spaces = 4 * " "
        content = f"pornstars = [\n"
        total = len(pornstars) - 1
        for c, star in enumerate(pornstars):
            content += f"{spaces}'{star}'"
            if c < total:
                content += ","
            content += "\n"
        content += "]\n\n"

        for line in current:
            content += f"{line}\n"
        content += f"\n"
        for line in babeinfo:
            content += f"{line}\n"
        
        with open(path, 'w') as f:
            f.write(content)

    # ---------------------------------------------------------
    # ------ TEXT
    # ---------------------------------------------------------
    def readtext(self, filename, checkext=True):
        """Read a text file and return the data"""
        if checkext:
            filename = self.checkfilename(filename, filetype='text')
        path = os.path.join(self.textdir, filename)
        with open(path, 'r') as f:
            data = f.read().splitlines()
        return data

    # ---------------------------------------------------------
    # ------ IMAGES
    # ---------------------------------------------------------
    def getimages(self, name):
        """Read all image files in a folder and return the data"""
        valid = ["jpg", "png", "jpeg"]
        images = []
        path = os.path.join(self.imgdir, name)
        for item in os.scandir(path):
            extension = item.name.split(".")[1].lower()
            if extension in valid:
                images.append(item.name)
        return images

    def openimgdir(self, name):
        """Open folder and use 'feh' to start a slideshow"""
        # --- check if there are images in the folder
        images = self.getimages(name)
        if len(images) == 0:
            self.error("There aren't any images in that folder, please add some.")
            sleep(2)
        else:
            waitfor = randint(2, 6)
            waitfor = 2
            path = os.path.join(self.imgdir, name)
            cmd = f"feh -F -Z -z --scale-down --slideshow-delay {waitfor} {path}"
            os.system(cmd)
