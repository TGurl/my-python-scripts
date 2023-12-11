import os
import sys
import glob
import tarfile
import pathlib
import shutil

from tui import TUI
from zipfile import ZipFile, ZIP_DEFLATED
from time import sleep


class Utils:
    def __init__(self):
        self.folder = ""
        self.archive = ""
        self.destination = ""
        self.locations = [
            os.path.join("/", "backups", "sexgames"),
            os.path.join("/", "backups", "sexgames", "keep"),
            os.path.join("/", "backups", "sexgames", "checked"),
            os.path.join("/", "data", "downloads", "SexGames"),
        ]
        self.tui = TUI()

    # ----------------------------------------------------
    # -- The main loop
    # ----------------------------------------------------
    def main_loop(self, args):
        self.parse_arguments(args)
        self.check_if_folder_exists()
        self.check_archives()
        self.clean_source_folder()
        self.create_archive()
        self.move_archive()
        self.remove_source_folder()
        self.tui.complete_step("All done!")

    # ----------------------------------------------------
    # -- 1: Parse the arguments
    # ----------------------------------------------------
    def parse_arguments(self, args):
        self.folder = args.folder
        self.clean = not args.clean
        self.keep = args.keep
        self.assumeyes = args.yes

        match args.destination:
            case "usb":
                self.destination = self.locations[0]
            case "keep":
                self.destination = self.locations[1]
            case "checked":
                self.destination = self.locations[2]
            case _:
                self.destination = self.locations[3]

        extension = ".zip" if args.type == 'zip' else ".tar.gz"
        self.folder = self.folder.replace("/", "")
        self.archive = self.folder + extension

    # ----------------------------------------------------
    # -- 2: Check if folder exists in cwd
    # ----------------------------------------------------
    def check_if_folder_exists(self):
        self.tui.render_header()
        self.tui.start_step(f"Checking if source folder %i%c{self.folder}%R exists")
        if self.folder != "":
            if not os.path.exists(self.folder):
                self.tui.clearline()
                self.tui.errored_step(f"%i%c{self.folder}%R does not exist...")
                sys.exit()
        self.tui.complete_step(f"Source folder %i%c{self.folder}%R exists")

    # ----------------------------------------------------
    # -- 3: Check if game has already been archived
    # ----------------------------------------------------
    def remove_old_versions(self, found):
        adj = "them" if len(found) > 1 else "it"
        if not self.assumeyes:
            result = self.tui.askyesno(f"Older version found. Do you want me to remove {adj}?")
        else:
            result = True

        if result:
            for path in found:
                os.remove(path)
        else:
            self.tui.clearline()
            self.tui.errored_step("Process halted by request")
            sys.exit()

    def check_archives(self):
        self.tui.start_step(f"Checking if %i%c{self.archive}%R already exists")

        found = []
        for location in self.locations:
            path = os.path.expanduser(os.path.join(location, self.archive))
            if os.path.exists(path):
                found.append(path)

        if len(found) == 0:
            self.tui.complete_step(f"%i%c{self.folder}%R hasn't been archived before")
        else:
            self.remove_old_versions(found)
            self.tui.complete_step(f"Previous versions of %i%c{self.archive}%R removed")

    # ----------------------------------------------------
    # -- 4: Clear the source folder
    # ----------------------------------------------------
    def remove_save_files(self):
        path = os.path.expanduser(os.path.join(self.folder, "**", "game", "saves", "*.save"))
        files = glob.glob(path, recursive=True)
        cleaned_saves = False
        if len(files) > 0:
            cleaned_saves = True
            for file in files:
                self.tui.show_progress(f"Removing {file}")
                os.remove(file)
                sleep(0.6)
        return cleaned_saves

    def remove_unwanted_files(self):
        patterns = ["log.txt", "traceback.txt", "debug.txt", "errors.txt", "desktop.ini", ".DC_Store"]
        clean_unwanted = False
        files = []
        for pattern in patterns:
            path = os.path.join(self.folder, '**', pattern)
            files.extend(glob.glob(os.path.expanduser(path), recursive=True))

        for file in files:
            if os.path.exists(file):
                clean_unwanted = True
                self.tui.show_progress(f"Removing {file}")
                os.remove(file)
                sleep(0.6)

        return clean_unwanted

    def clean_source_folder(self):
        self.tui.start_step(f"Cleaning %i%c{self.folder}%R")
        if self.clean:
            cleaned_saves = self.remove_save_files()
            clean_unwanted = self.remove_unwanted_files()
            if clean_unwanted or cleaned_saves:
                self.tui.complete_step(f"Cleaned up %i%c{self.folder}%R")
            else:
                self.tui.complete_step(f"%i%c{self.folder.title()}%R didn't need cleaning")
        else:
            self.tui.complete_step(f"%i%c{self.folder}%R not cleaned as requested")

    # ----------------------------------------------------
    # -- 5: Create a local archive
    # ----------------------------------------------------
    def collect_files(self):
        path = pathlib.Path(self.folder)
        return list(path.rglob("*"))

    def create_archive(self):

        if os.path.exists(self.archive):
            os.remove(self.archive)

        self.tui.start_step(f"Creating %i%c{self.archive}%R")

        if ".zip" in self.archive:
            source_size = self.create_zip()
        else:
            source_size = self.create_tar_gz()

        self.tui.complete_step(f"%i%c{self.archive}%R created ({source_size})")

    def create_zip(self):
        content = self.collect_files()
        content.sort()
        total = len(content)
        digits = len(str(total))

        with ZipFile(self.archive, "w", ZIP_DEFLATED, compresslevel=9) as zf:
            for count, item in enumerate(content, start=1):
                name = str(item)
                if len(name) > 35:
                    name = "%c<<%R" + name[-33:]
                percent = count * 100 // total
                self.tui.show_progress(
                    f"adding {count:{digits}}/{total} [{percent:3}%]: {name}"
                )
                zf.write(item)
        
        source_size = self.tui.convert_size(os.stat(self.archive).st_size)
        return source_size

    def create_tar_gz(self):
        content = self.collect_files()
        content.sort()
        total = len(content)
        digits = len(str(total))

        tar = tarfile.open(self.archive, "w:gz")
        for count, item in enumerate(content, start=1):
            name = str(item)
            if len(name) > 35:
                name = ".." + name[-33:]
            percent = count * 100 // total
            self.tui.show_progress(
                f"adding {count:{digits}}/{total} [{percent:3}%]: {name}"
            )
            tar.add(item, recursive=False)
        tar.close()

        source_size = self.tui.convert_size(os.stat(self.archive).st_size)
        return source_size


    # ----------------------------------------------------
    # -- 6: Move archive to final destination
    # ----------------------------------------------------
    def move_archive(self):
        self.tui.start_step(f"Moving %i%c{self.archive}%R to %i%c{self.destination}%R")

        destination = os.path.expanduser(self.destination)
        source_size = os.stat(self.archive).st_size
        TARGET_FN = os.path.join(destination, self.archive)

        copied = 0
        perc = 0

        source = open(self.archive, "rb")
        target = open(TARGET_FN, "wb")

        while True:
            chunk = source.read(32768)
            if not chunk:
                break
            target.write(chunk)
            copied += len(chunk)
            perc = int(copied * 100 / source_size)
            cn = self.tui.convert_size(copied)
            sn = self.tui.convert_size(source_size)
            self.tui.show_progress(f"moved {cn}/{sn} [{perc:3}%]")

        target.close()
        source.close()

        # self.tui.clearline()
        self.tui.complete_step(f"Moving %i%c{self.archive}%R to %i%c{self.destination}%R")

        self.tui.start_step("Syncing to make sure everything has been moved")
        os.system("sync")
        self.tui.complete_step("Syncing to make sure everything has been moved")

        os.remove(self.archive)

        # self.tui.complete_step(
        #     f"%i%c{self.archive}%R moved to %i%c{self.destination}%R"
        # )

    # ----------------------------------------------------
    # -- 7: Move archive to final destination
    # ----------------------------------------------------
    def remove_source_folder(self):
        if self.keep:
            self.tui.complete_step(f"Source %i%c{self.folder}%R kept as requested")
        else:
            self.tui.start_step(f"Removing source folder %i%c{self.folder}%R")
            shutil.rmtree(self.folder)
            self.tui.complete_step(f"Source %i%c{self.folder}%R removed")
