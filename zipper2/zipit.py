#!/usr/bin/env python
import os
import zipfile
from utils import Utils


class Zipit(Utils):
    def __init__(self):
        super().__init__()

    def count_number_of_files(self, folder) -> int:
        total = 0
        for _, _, files in os.walk(folder):
            total += len(files)
        return total

    def compress(self, srcpath, check=False, clevel=7):
        zipfilename = srcpath + '.zip'
        total_files = self.count_number_of_files(srcpath)
        num_digits = len(str(total_files))
        count = 0

        print()  # To preserve the title
        with zipfile.ZipFile(zipfilename, 'w',
                             zipfile.ZIP_DEFLATED,
                             compresslevel=clevel
                             ) as archive_file:
            for dirpath, _, filenames in os.walk(srcpath):
                for filename in filenames:
                    perc = round(count * 100 / total_files)
                    path = os.path.join(dirpath, filename)
                    shortfp = path
                    if len(shortfp) > 40:
                        shortfp = ".." + path[-38:]
                    info = f"Zipping: [{perc:3}%] {count:{num_digits}}/"
                    info += f"{total_files}: {shortfp}"
                    self.print_info(info, clearline=True)

                    archive_path = os.path.relpath(path)
                    archive_file.write(path, archive_path)
                    count += 1

        info = "Zipping: %gDONE%R"
        self.print_info(info, clearline=True, nl=False)

        path = os.path.join(os.getcwd(), zipfilename)
        if check:
            msg = "Checking archive: "
            self.print_info(msg)
            with zipfile.ZipFile(zipfilename, 'r') as archive:
                badfile = zipfile.ZipFile.testzip(archive)

                if badfile:
                    print('\033[?25h', end='')
                    raise zipfile.BadZipFile(
                            'CRC check failed for {} with file {}'.format(
                                zipfilename, badfile))

            msg += "%gOK%R"
            self.print_info(msg, clearline=True)

        stats = os.stat(path)
        filesize = self.convert_size(stats.st_size)
        info = f"Filesize: %g{filesize}%R"
        self.print_info(info)
