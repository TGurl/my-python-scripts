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
                        shortfp = path[-40:]
                    info = f"%c[%g{perc:3}%%c] %y{count:{num_digits}}%R/"
                    info += f"%g{total_files}%R: {shortfp}"
                    self.print_info(info, clearline=True)

                    archive_path = os.path.relpath(path)
                    archive_file.write(path, archive_path)
                    count += 1

            info = f"%c[%g100%%c] %y{total_files}%R/%g{total_files}%R: DONE]"
            self.print_info(info, clearline=True, nl=True)

            path = os.path.join(os.getcwd(), zipfilename)
            stats = os.stat(path)
            filesize = self.convert_size(stats.st_size)
            info = f"%cFilesize%R: %y{filesize}%R"
            self.myprint(info)

            if check:
                msg = "Checking %y{zipfilename}%R: "
                self.print_msg(msg)
                with zipfile.ZipFile(zipfilename, 'r') as archive:
                    badfile = zipfile.ZipFile.testzip(archive)

                    if badfile:
                        raise zipfile.BadZipFile(
                                'CRC check failed for {} with file {}'.format(
                                    zipfilename, badfile))

                msg += "%gOK%R"
                self.print_msg(msg, clearline=True)
