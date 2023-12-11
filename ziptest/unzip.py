#!/usr/bin/env python
import os
import sys
import time
from zipfile import ZipFile


class MyZip:
    def __init__(self):
        pass

    def progress_bar(self, c, count, prefix="Unpacking", size=20, filename=""):
        if len(filename) > 30:
            filename = ".." + filename[-28:]

        x = int(size * c / count)
        pbar = f"{prefix} [{u'#'*x}{('-'*(size-x))}] {c}/{count} : {filename}"
        return pbar

    def extract(self, archive, target_dir = None):
        if target_dir is None:
            target_dir = os.getcwd()

        with ZipFile(archive, 'r') as zf:
            filelist = zf.infolist()
            total = len(filelist)
            digits = len(str(total))
            for i, file in enumerate(filelist, start=1):
                # print(f"-> {i:{digits}}/{total}: {file.filename}")
                pbar = self.progress_bar(i, total, filename=file.filename, size=10)
                print(pbar)
                extracted_path = zf.extract(file, target_dir)
                if file.create_system == 3:
                    unix_attributes = file.external_attr >> 16
                    if unix_attributes:
                        os.chmod(extracted_path, unix_attributes)
                if i < total:
                    print('\033[1A', end='\x1b[2K')

myzip = MyZip()
myzip.extract('output.zip')
