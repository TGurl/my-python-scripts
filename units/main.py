#!/usr/bin/env python
"""A simple program to convert units"""
import argparse
import os

import requests


class Convert:
    def __init__(self):
        self.api_key = "c0dad9c40a882f026976ff69"
        self.conversion_rate = 1.1043

    def cls(self):
        os.system("cls" if os.name == "nt" else "clear")

    def fetch_exchange_rates(self):
        url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/pair/EUR/USD"
        response = requests.get(url, timeout=10)
        data = response.json()

        if data["result"] != "success" or data == {}:
            self.printf("Unable to fetch the latest exchange rates...")
            self.printf(f"Using {self.conversion_rate} as the default.", new_line=True)
        else:
            self.conversion_rate = data["conversion_rate"]

    def printf(self, text, new_line=False):
        carriage_return = "\n\n" if new_line else "\n"
        print(text, end=carriage_return)

    def banner(self):
        self.cls()
        self.printf("Units v0.0.1 - made with \u2764 by Transgirl", new_line=True)

    def miles_to_kilometers(self, value):
        calc = value * 1.609
        self.printf(f"{value} miles = {calc:.2f} kilometers")

    def kilometers_to_miles(self, value):
        calc = value / 1.609
        self.printf(f"{value} kilometers = {calc:.2f} miles")

    def meters_to_feet(self, value):
        calc = value * 3.281
        self.printf(f"{value} meters = {calc:.2f} feet")

    def feet_to_meters(self, value):
        calc = value / 3.281
        self.printf(f"{value} feet = {calc:.2f} meters")

    def euro_to_dollars(self, value):
        self.fetch_exchange_rates()
        calc = value * self.conversion_rate
        self.printf(f"{value} euro = {calc:.2f} dollars")

    def dollars_to_euro(self, value):
        self.fetch_exchange_rates()
        calc = value / self.conversion_rate
        self.printf(f"{value} dollars = {calc:.2f} euro")

    def run(self, parsed_args):
        self.banner()

        if parsed_args.mi:
            self.miles_to_kilometers(parsed_args.mi)

        if parsed_args.km:
            self.kilometers_to_miles(parsed_args.km)

        if parsed_args.e:
            self.euro_to_dollars(parsed_args.e)

        if parsed_args.d:
            self.dollars_to_euro(parsed_args.d)

        if parsed_args.m:
            self.meters_to_feet(parsed_args.m)

        if parsed_args.f:
            self.feet_to_meters(parsed_args.f)


if __name__ == "__main__":
    LINE = 26 * "-"
    parser = argparse.ArgumentParser(
        prog="units",
        description="Units - A simple program to convert units",
        epilog="made with \u2764 by Transgirl",
        usage="%(prog)s [options]",
        add_help=True,
    )

    options = parser.add_mutually_exclusive_group(required=True)

    options.add_argument(
        "-mi",
        type=float,
        metavar="<value>",
        help="Convert miles to kilometers",
    )

    options.add_argument(
        "-km",
        metavar="<value>",
        type=float,
        help="Convert kilometers to miles",
    )

    options.add_argument(
        "-e", type=float, metavar="<value>", help="Convert euro to dollars"
    )

    options.add_argument(
        "-d", type=float, metavar="<value>", help="Convert dollars to euro"
    )

    options.add_argument(
        "-f", type=float, metavar="<value>", help="Convert feet to meters"
    )

    options.add_argument(
        "-m", type=float, metavar="<value>", help="Convert meters to feet"
    )

    app = Convert()
    app.run(parser.parse_args())
