import os
import sys
import tarfile
import pathlib
import glob
import signal
import shutil
import math
from time import sleep
from colors import Colors


class Utils:
    def __init__(self):
        signal.signal(signal.SIGINT, self.handler)
        self.cursor = True
        self.keep_saves = False
        self.delete = True
        self.archive_type = "tar.gz"
        self.folder = "I want to be raped"
        self.destination = "I love Big Black Cocks"

    # -------------------------------------------------
    # -- Signal handler to catch CTRL+C
    # -------------------------------------------------
    def handler(self, signum, frame):
        _ = frame
        _ = signum
        if not self.cursor:
            self.toggle_cursor()
        print()
        self.print_message("CTRL+C pressed, exiting...", clear=True)
        sys.exit()

    # -------------------------------------------------
    # -- Process arguments
    # -------------------------------------------------
    def parse_arguments(self, args):
        # print(args)
        # _ = input("... Press enter ...")
        self.folder = args.folder
        self.keep_saves = args.keep_saves

        self.delete = not args.no_delete

        match args.destination:
            case "keep":
                self.destination = os.path.join("~", "USB", "sexgames", "keep")
            case "usb":
                self.destination = os.path.join("~", "USB", "sexgames")
            case "archives":
                self.destination = os.path.join("~", "Games", "archives")
            case _:
                self.print_error("Unknown destination chosen...")
                sys.exit()

        self.destination = os.path.expanduser(self.destination)

        match args.type:
            case "xz":
                self.archive_type = "tar.xz"
                self.archive_extension = "w:xz"
            case "bz2":
                self.archive_type = "tar.bz2"
                self.archive_extension = "w:bz2"
            case _:
                self.archive_type = "tar.gz"
                self.archive_extension = "w:gz"

    # -------------------------------------------------
    # -- Check if the game has been archived already
    # -------------------------------------------------
    def check_if_archived(self, folder):
        # self.show_header()
        tar_file = f"{folder}.{self.archive_type}"
        message = f"Checking if %i{tar_file}%R has been archived%R"
        self.print_step_start(message, nl=True)

        found = []

        check_paths = [
            os.path.join("~/Games/archives"),
            os.path.join("~/USB/sexgames"),
            os.path.join("~/USB/sexgames/keep"),
        ]

        for path in check_paths:
            cpath = os.path.expanduser(path)
            tar_path = os.path.join(cpath, tar_file)
            if os.path.exists(tar_path):
                found.append(path)

        if len(found) > 0:
            self.myprint(f"   %b└>%R {tar_file} has already been archived")
            for path in found:
                self.clearline()
                self.myprint(f"   %b└>%R Removing {tar_file}...", clear=True)
                fullpath = os.path.join(path, tar_file)
                os.remove(os.path.expanduser(fullpath))
                self.clearline()
                message = f"%i{tar_file}%R has been removed%R"
                self.print_step_end(message)
        else:
            self.clearline()
            message = f"%i{tar_file}%R has not been found%R"
            self.print_step_end(message)

    # -------------------------------------------------
    # -- Clear folder before archiving it
    # -------------------------------------------------
    def clear_folder(self, folder):
        message = f"Clearing %i{folder}%R"
        self.print_step_start(message, nl=True)
        renpy_path = os.path.expanduser(os.path.join("~", ".renpy"))

        if os.path.exists(renpy_path):
            self.myprint(f"   %b└>%R Deleting %i{renpy_path}%R", clear=True)

            shutil.rmtree(renpy_path)
            sleep(0.3)

        if not self.keep_saves:
            path = f"{self.folder}/**/*.save"
            files = glob.glob(path, recursive=True)
            for file in files:
                self.myprint(f"   %b└>%R Deleting save file %i{file}%R", clear=True)
                os.remove(file)
                sleep(0.3)
            # self.clearline()

        for name in ["log.txt", "traceback.txt", "errors.txt"]:
            path = f"{self.folder}/**/{name}"
            files = glob.glob(path, recursive=True)
            for file in files:
                self.myprint(f"   %b└>%R Deleting {file}", clear=True)
                os.remove(file)
                sleep(0.3)

        self.clearline()
        self.print_step_end(message + " → DONE")

    # -------------------------------------------------
    # -- Archive it all
    # -------------------------------------------------
    def read_folder(self, folder):
        path = pathlib.Path(folder)
        return list(path.rglob("*"))

    def create_archive(self, folder):
        self.toggle_cursor()
        tar_file = f"{folder}.{self.archive_type}"
        message = f"Creating %i{tar_file}%R"
        list_of_files = self.read_folder(folder)
        total = len(list_of_files)
        lead = len(str(total))

        # -- check if file exists in current folder
        # -- if so remove it.
        if os.path.exists(tar_file):
            os.remove(tar_file)

        self.print_step_start(message, nl=True)

        tar = tarfile.open(tar_file, self.archive_extension)
        for count, file in enumerate(list_of_files):
            percent = count * 100 // total
            if len(str(file)) > 40:
                name = ".." + str(file)[-38:]
            else:
                name = file
            counter = f"{count:{lead}}/{total}"
            self.myprint(
                f"   %b└>%R adding {counter} [{percent:3}%] %i{name}%R", clear=True
            )
            tar.add(file, recursive=False)
        tar.close()

        self.clearline()
        total_size = os.stat(tar_file).st_size
        total_size = self.convert_size(total_size)
        self.print_step_end(message + f" ({total_size}) → DONE")
        self.toggle_cursor()
        return tar_file

    # -------------------------------------------------
    # -- Convert bytes to Mb etc
    # -------------------------------------------------
    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_names = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        # return "%s %s" % (s, size_names[i])
        return f"{s:.2f} {size_names[i]}"

    # -------------------------------------------------
    # -- Move file with percentage
    # -------------------------------------------------
    def move_file(self, archive):
        self.toggle_cursor()
        source_size = os.stat(archive).st_size
        TARGET_FN = os.path.join(self.destination, archive)
        copied = 0
        perc = 0
        message = f"Moving %i{archive}%R to %i{self.destination}%R"
        self.print_step_start(message, nl=True)

        source = open(archive, "rb")
        target = open(TARGET_FN, "wb")

        while True:
            chunk = source.read(32768)
            if not chunk:
                break
            target.write(chunk)
            copied += len(chunk)
            perc = int(copied * 100 / source_size)
            cn = self.convert_size(copied)
            sn = self.convert_size(source_size)
            self.myprint(f"   %b└>%R moved {cn}/{sn} [{perc:3}%]", clear=True)

        self.clearline()
        self.print_step_end(message + " → DONE")

        self.print_step_start("Syncing to make sure everything has been moved")
        os.system("sync")
        self.print_step_end("Syncing to make sure everything has been moved → DONE")
        os.remove(archive)
        self.toggle_cursor()

    # -------------------------------------------------
    # -- Delete source folder
    # -------------------------------------------------
    def delete_source_folder(self, folder):
        message = f"Deleting source %i{folder}%R"
        if self.delete:
            self.print_step_start(message)
            shutil.rmtree(folder)
            self.print_step_end(f"{message} → DONE")
        else:
            self.print_message(f"Source %i{folder}%R not removed as requested.")

    # -------------------------------------------------
    # -- Input and output functions
    # -------------------------------------------------
    def colorize(self, text):
        for color in Colors.colors:
            text = text.replace(color[0], color[1])
        return text

    def myprint(self, text, nl=False, clear=False):
        newline = "\n\n" if nl else "\n"
        text = self.colorize(text)
        if clear:
            self.clearline(number=1)
        print(text, end=newline)

    def myinput(self, prompt="%g> %R"):
        prompt = self.colorize(prompt)
        result = input(prompt).lower()
        return result

    def askyesno(self, text, yes=True):
        prompt = "(%yY%R/n)" if yes else "(y/%yN%R)"
        message = self.colorize(f" %g»%R {text} {prompt} : ")

        while True:
            answer = input(message).lower()
            if answer not in ["y", "n", ""]:
                self.print_error("That is not an answer to my question")
                sleep(0.8)
                self.clearline()
            else:
                break

        if answer in ["", "y"] and yes is True:
            answer = "y"
        else:
            answer = "n"

        return True if answer == "y" else False

    def print_step_start(self, text, nl=False):
        text = f" %y▷%R {text}"
        self.myprint(text, nl=nl)

    def print_step_end(self, text):
        text = f" %g▶%R {text}"
        self.myprint(text, clear=True)

    def print_message(self, text, clear=False):
        text = f" %g»%R {text}"
        self.myprint(text, clear=clear)

    def print_error(self, text):
        text = f" %r»%R {text}"
        self.myprint(text)

    def print_warning(self, text):
        text = f" %y»%R {text}"
        self.myprint(text)

    def clearline(self, number=1):
        for _ in range(number):
            print("\033[1A", end="\x1b[2K")

    def show_header(self):
        os.system("clear")
        lines = [
            "%c╭──────────────────────────╮",
            "│    %yARC%R - %gversion 0.02    %c│",
            "│ %R%iCopyright 2023 TransGirl %R%c│",
            "╰──────────────────────────╯%R",
        ]
        for _, line in enumerate(lines):
            self.myprint(line)

    def toggle_cursor(self):
        if self.cursor:
            print("\033[? 25l", end="")
            self.cursor = False
        else:
            print("\033[? 25h", end="")
            self.cursor = True
