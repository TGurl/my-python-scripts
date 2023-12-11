import os

from tui import TUI
from converttable import ConvertTable
from time import sleep


class Utils:
    def __init__(self):
        self.tui = TUI()
        self.ct = ConvertTable()

    def cm_to_inch(self):
        os.system("clear")
        self.tui.render_header()
        print()

        prompt = "Centimeters: "
        cm = input(prompt).lower()
        inch = self.ct.cm_to_inch(cm)
        self.tui.myprint(f">> {cm} centimeters = {inch:.2f} inches")

        print()
        _ = input("Press [ENTER] to continue")

    def metric_to_imerial(self):
        while True:
            os.system("clear")
            self.tui.render_header()
            print()

            self.tui.myprint(" [1] Centimeters to inches")
            self.tui.myprint(" [2] Centimeters to feet")
            self.tui.myprint(" [3] Kilometers to miles")
            self.tui.myprint(" [4] Kilograms to pounds")
            self.tui.myprint(" [5] Boobs US to EU")
            self.tui.myprint(" [6] Shoes US to EU")
            print()
            self.tui.myprint(" [q] Return")
            print()

            prompt = self.tui.colorize("  %g>>%R ")
            result = input(prompt).lower()
            if result in ["quit", "q"]:
                break
            elif result == "1":
                self.cm_to_inch()
            else:
                self.tui.print_error("That is not an option...")
                sleep(2)

    def imperial_to_metric(self):
        while True:
            os.system("clear")
            self.tui.render_header()
            print()

            self.tui.myprint(" [1] Inches to centimeters")
            self.tui.myprint(" [2] Feet to centimeters")
            self.tui.myprint(" [3] Miles to kilometers")
            self.tui.myprint(" [4] Pounds to kilograms")
            self.tui.myprint(" [5] Boobs EU to US")
            self.tui.myprint(" [6] Shoes EU to US")
            print()
            self.tui.myprint(" [q] Return")
            print()

            prompt = self.tui.colorize("  %g>>%R ")
            result = input(prompt).lower()
            if result in ["quit", "q"]:
                break
            else:
                self.tui.print_error("That is not an option...")
                sleep(2)

    def main_menu(self):
        while True:
            os.system("clear")
            self.tui.render_header()
            print()

            self.tui.myprint(" [1] Metric to Imperial")
            self.tui.myprint(" [2] Imperial to Metric")
            print()
            self.tui.myprint(" [q] Quit")

            print()
            prompt = self.tui.colorize("  %g>>%R ")
            result = input(prompt).lower()
            if result in ["quit", "q"]:
                break
            elif result == "1":
                self.metric_to_imerial()
            elif result == "2":
                self.imperial_to_metric()
            else:
                self.tui.print_error("That is not an option...")
                sleep(2)
