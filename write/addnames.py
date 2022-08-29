#!/usr/bin/env python

import os


class Colors:
    res = "\033[0m"
    red = "\033[31;1m"
    gre = "\033[32;1m"
    yel = "\033[33;1m"
    blu = "\033[34;1m"
    pin = "\033[35;1m"
    cya = "\033[36;1m"
    whi = "\033[37;1m"


class AddNames:
    def __init__(self):
        self.appdir = os.path.dirname(os.path.realpath(__file__))
        self.datadir = os.path.join(self.appdir, "data")
        self.girldata = os.path.join(self.datadir, "girlnames.csv")
        self.boydata = os.path.join(self.datadir, "boynames.csv")
        self.girlnames = self.read_csv(self.girldata)
        self.boynames = self.read_csv(self.boydata)

    def read_csv(self, filename):
        with open(filename, "r") as f:
            data = f.read().replace("\n", "").split(",")
        return data

    def check_girlname_and_add_it(self, name):
        if name in self.girlnames:
            print(f"{name} already is in the database...")
            print()
        else:
            self.girlnames.append(name)
            print(f"{name} added to the database...")
            print()

    def savedata(self):
        with open(self.girldata, "w") as f:
            for idx, name in enumerate(self.girlnames):
                if idx < len(self.girlnames) - 1:
                    name += ","
                f.write(name)
            f.close()
        print("Data saved...")

    def run(self):
        loop = True
        while loop:
            answer = input("Which name would you like to add? : ")
            if answer == "" or answer.lower() in ["none", "q"]:
                loop = False
            else:
                self.check_girlname_and_add_it(answer.title())
        self.savedata()


if __name__ == "__main__":
    addnames = AddNames()
    addnames.run()
