#!/usr/bin/env python

import os
from fileio import FileIO

class testit:
    def __init__(self):
        cwd = os.getcwd()
        self.fileio = FileIO()
        self.tomldir = os.path.join(cwd, 'data', 'toml')
        self.data = self.fileio.readtoml('pornstars')
    
    def run(self):
        self.data['pornstars'].append('test_folder')
        babeinfo = []
        babeinfo.append(f"[test_folder]")
        babeinfo.append(f"id = 'test_folder'")
        babeinfo.append(f"name = 'Test Folder'")
        babeinfo.append(f"alias = 'test'")
        babeinfo.append(f"active = false")
        babeinfo.append(f"since = 2003")
        babeinfo.append(f"retired = 2005")
        babeinfo.append(f"nationality = 'Dutch'")
        babeinfo.append(f"ethnicity = 'Caucasian'")
        babeinfo.append(f"birthdate = '1996/03'")
        babeinfo.append(f"cup = 'DDDD'")
        babeinfo.append(f"boobs = 'Natural'")
        babeinfo.append(f"bust = 37")
        babeinfo.append(f"waist = 24")
        babeinfo.append(f"hips = 39")
        babeinfo.append(f"height = 156")
        babeinfo.append(f"weight = 58")
        babeinfo.append(f"eyecolor = 'Hazel'")
        babeinfo.append(f"haircolor = 'Black'")
        babeinfo.append(f"tattoos = 'none'")
        babeinfo.append(f"piercings = 'unkown'")
        babeinfo.append(f"shoesize = 36")
        babeinfo.append(f"rating = 9")

        self.fileio.appendtotoml(babeinfo, self.data['pornstars'])


if __name__ == "__main__":
    t = testit()
    t.run()