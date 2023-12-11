#!/usr/bin/env python
import os
import sys
import shutil

class MMV:
    def __init__(self, args):
        self.source = args[1]
        self.destination = args[2]
        self.cwd = False

        if self.destination == ".":
            self.destination = os.getcwd()
            self.cwd = True

        self.freespace = shutil.disk_usage(self.destination).free

    def clear_line(self):
        print('\033[1A', end='\x1b[2K')
    
    def readable_size(self, num, suffix = 'b'):
        for unit in ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z']:
            if abs(num) < 1024.0:
                return "%3.1f %s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f%s%s" % (num, 'Yi', suffix)

    def check_freespace(self):
        size = os.stat(self.source).st_size
        # print(size, self.freespace)
        if size >= self.freespace:
            print("Not enough space on destination!")
            sys.exit()

    def check_paths(self):
        if os.path.isdir(self.source):
            print(f"I can't move a folder!")
            sys.exit()

        if not os.path.exists(self.source) and not os.path.exists(self.destination):
            print(f"Both {self.source} and {self.destination} don't exist!")
            sys.exit()

        if not os.path.exists(self.source):
            print(f"{self.source} doesn't exist!")
            sys.exit()

        if not os.path.exists(self.destination):
            print(f"{self.destination} doesn't exist!")
            sys.exit()

    def move_file(self):
        source_size = os.stat(self.source).st_size
        size = self.readable_size(source_size)
        copied = 0
        p = 0
        
        target = os.path.join(self.destination, self.source)
        if os.path.exists(target) and not self.cwd:
            print(f"> {target} already exists!")
            sys.exit()

        #print(f"-- MMV - my simple mv with progress indicator --")
        print("> Source size :", size)
        print("> Free space  :", self.readable_size(self.freespace))
        
        source = open(self.source, 'rb')
        target = open(target, 'wb')

        while True:
            p = int(copied * 100 / source_size)
            print(f">> {p:3}% moved : {self.source} to {self.destination}")
            chunk = source.read(32768)
            if not chunk:
                break
            target.write(chunk)
            copied += len(chunk)
            self.clear_line()

        target.close()
        source.close()
        
        self.clear_line()
        # self.clear_line()
        os.remove(self.source)
        print(f"> {self.source} moved")
        print("> Syncing...")
        os.system("sync")
        self.clear_line()
        print("> Syncing done")

    def run(self):
        self.check_paths()
        self.check_freespace()
        self.move_file()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("MMV - A simple move with progression")
        print("Usage:")
        print("    mmv {origins} {destination}")
        sys.exit()

    app = MMV(sys.argv)
    app.run()
