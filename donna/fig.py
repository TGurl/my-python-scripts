#!/usr/bin/env python3

import os

from random import choice, randint
from faker import Faker
from datetime import date
from time import sleep


class Colors:
    res = "\033[0m"
    red = "\033[31;1m"
    gre = "\033[32;1m"
    yel = "\033[33;1m"
    blu = "\033[34;1m"
    pin = "\033[35;1m"
    cya = "\033[36;1m"
    whi = "\033[37;1m"


class TUI:
    def __init__(self):
        pass

    def clear_terminal(self):
        os.system('clear')


class FileIO:
    def __init__(self):
        self.cwd = os.getcwd()
        self.wip_path = os.path.join(
            '/',
            'data',
            'dev',
            'stories',
            'wip'
        )

    def save_file(self, filename,
                  firstname,
                  lastname,
                  birthdate,
                  age,
                  measurements,
                  ssn,
                  address,
                  job):
        filename = filename.lower()
        path = os.path.join(self.wip_path, filename)
        with open(path, "w") as f:
            f.write(f"Name         : {firstname} {lastname}\n")
            f.write(f"DoB          : {birthdate}\n")
            f.write(f"Age          : {age}\n")
            f.write(f"Measurements : {measurements}\n")
            f.write(f"SSN          : {ssn}\n")
            f.write(f"Address      : {address}\n")
            f.write(f"Job          : {job}\n")


class Fig:
    def __init__(self):
        self.tui = TUI()
        self.faker = Faker()
        self.colors = Colors()
        self.fileio = FileIO()
        self.currentyear = date.today().year
        self.firstname = ""
        self.lastname = ""
        self.birthdate = ""
        self.age = 0
        self.measurements = ""
        self.address = ""
        self.ssn = ""
        self.job = ""
        self.minyear = 1985
        self.maxyear = 2002
        self.cupsizes = ["C", "D", "DD", "DDD", "E", "F", "G", "H"]


    def choose_measurements(self):
        bust = randint(32, 36)
        cup = choice(self.cupsizes)
        waist = bust - randint(6, 9)
        hips = bust + randint(1, 6)
        self.measurements = f"{bust}{cup}-{waist}-{hips}"

    def choose_last_name(self):
        self.lastname = self.faker.last_name()

    def choose_female_first_name(self):
        self.firstname = self.faker.first_name_female()

    def choose_address(self):
        address = self.faker.address()
        self.address = address.replace("\n", ", ")

    def choose_profile(self):
        profile = self.faker.profile()
        return profile

    def choose_birthdate(self):
        t = self.faker.profile(['birthdate'])
        bdate = t['birthdate']
        year = str(bdate.year).split("-")[0]
        while int(year) < self.minyear or int(year) > self.maxyear:
            t = self.faker.profile(['birthdate'])
            bdate = t['birthdate']
            year = str(bdate.year).split('-')[0]
        self.birthdate = bdate
        self.age = self.currentyear - int(year)

    def choose_job(self):
        self.job = self.faker.profile(['job'])['job']

    def choose_ssn(self):
        self.ssn = self.faker.profile(['ssn'])['ssn']

    def initial_generation(self):
        self.choose_female_first_name()
        self.choose_last_name()
        self.choose_measurements()
        self.choose_address()
        self.choose_birthdate()
        self.choose_job()
        self.choose_ssn()

    def show_info(self):
        yel = self.colors.yel
        gre = self.colors.gre
        res = self.colors.res
        print(f"{gre}Personel Information{res}")
        print(f"1. Name         : {yel}{self.firstname} {self.lastname}{res}")
        print(f"2. DoB          : {yel}{self.birthdate}{res}")
        print(f"3. Age          : {yel}{self.age}{res}")
        print(f"4. Measurements : {yel}{self.measurements}{res}")
        print(f"5. SSN          : {yel}{self.ssn}{res}")
        print(f"6. Address      : {yel}{self.address}{res}")
        print(f"7. Job          : {yel}{self.job}{res}")
        print()
        print(f"{gre}Menu{res}")
        print("a. roll again,")
        print("s. save info,")
        print("q. quit,")
        print("or any of the numbers above to change it.")
        print()

    def save_info(self):
        cya = self.colors.cya
        yel = self.colors.yel
        res = self.colors.res
        line = 7 * "─"
        title = "FIG - Female Information Generator"
        filename = f"{self.firstname}-{self.lastname}.md"
        self.fileio.save_file(
            filename,
            self.firstname,
            self.lastname,
            self.birthdate,
            self.age,
            self.measurements,
            self.ssn,
            self.address,
            self.job
        )
        os.system('clear')
        print(f"{cya}{line} {yel}{title} {cya}{line}{res}")
        print()
        print(f">> Info saved as {filename}")
        sleep(2)

    def run(self):
        self.initial_generation()
        cya = self.colors.cya
        yel = self.colors.yel
        res = self.colors.res
        line = 7 * "─"
        title = "FIG - Female Information Generator"
        loop = True
        while loop:
            os.system('clear')
            print(f"{cya}{line} {yel}{title} {cya}{line}{res}")
            print()
            self.show_info()
            print()
            answer = input("> ").lower()
            if answer in ["0", "q"]:
                loop = False
            elif answer == "a":
                self.initial_generation()
            elif answer == "s":
                self.save_info()
            elif answer == "1":
                self.choose_female_first_name()
                self.choose_last_name()
            elif answer in ["2", "3"]:
                self.choose_birthdate()
            elif answer == "4":
                self.choose_measurements()
            elif answer == "5":
                self.choose_ssn()
            elif answer == "6":
                self.choose_address()
            elif answer == "7":
                self.choose_job()
            else:
                print(">> I didn't get that part...")


if __name__ == "__main__":
    fig = Fig()
    fig.run()
