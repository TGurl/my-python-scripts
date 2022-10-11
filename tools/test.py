#!/usr/bin/env python

import os
import random
from tools import Tools, Colors

class Test:
    def __init__(self):
        self.home = os.path.expanduser("~")
        self.wd = os.path.join(self.home, 'Dev', 'python', 'heroes')
        self.imgdir = os.path.join(self.wd, 'data', 'img')
        self.colors = Colors()
        self.tools = Tools()

    def run(self):
        self.tools.clear()
        col = self.colors.yellow
        res = self.colors.reset
        text = self.tools.bigletters(f"testing tools")
        print(f"{col}{text}{res}")

        data = self.tools.get_contens_of_folder_recursive(self.imgdir)
        folders = []
        for file in data:
            name = file.split("/")[-2]
            if name not in folders:
                folders.append(name)
        folders.sort()
    
        chosen = random.choice(folders)
        folder = os.path.join(self.imgdir, chosen)
        images = self.tools.get_contents_of_folder(folder)
        print(images)

if __name__ == "__main__":
    test = Test()
    test.run()