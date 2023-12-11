#!/usr/bin/env python

import os
import glob
import zipfile

folder = '4YearsInTehran'
files = []

path = os.path.join(folder, '**')

files = glob.glob(path, recursive=True)

with zipfile.ZipFile("output.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    for i, file in enumerate(files, start=1):
        print(f"-> {i}/{len(files)}")
        print('\033[1A', end='\x1b[2K')
        zf.write(file)
