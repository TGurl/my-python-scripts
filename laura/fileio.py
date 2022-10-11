#!/usr/bin/env python

import os
import toml


class FileIO:
    def __init__(self):
        cwd = os.getcwd()
        self.tomldir = os.path.join(cwd, 'data', 'toml')
        self.textdir = os.path.join(cwd, 'data', 'text')

    # ----------------------------------------------------------------
    # ------------------------------------------------- Save TOML File
    # ----------------------------------------------------------------
    def savegame(self, Laura):
        def truefalse(item):
            return "true" if item else "false"

        tips = truefalse(Laura.tips)
        tipcup = truefalse(Laura.tipcup)
        illegal = truefalse(Laura.illegal)
        std = truefalse(Laura.std)
        pregnant = truefalse(Laura.pregnant)
        arrested = truefalse(Laura.arrested)
        path = os.path.join(self.tomldir, 'savegame.toml')

        data = f"age = {Laura.age}\n"
        data += f"cup = {Laura.cup}\n"
        data += f"sexy = {Laura.sexy}\n"
        data += f"health = {Laura.health}\n"
        data += f"bank = {Laura.bank}\n"
        data += f"maxtip = {Laura.wage}\n"
        data += f"job = '{Laura.job}'\n"
        data += f"location = '{Laura.location}'\n"
        data += f"room = '{Laura.room}'\n"
        data += f"tips = {tips}\n"
        data += f"tipcup = {tipcup}\n"
        data += f"illegal = {illegal}\n"
        data += f"std = {std}\n"
        data += f"pregnant = {pregnant}\n"
        data += f"arrested = {arrested}\n"
        data += f"wearing = {Laura.wearing}\n"
        data += f"inventory = {Laura.inventory}\n"
        data += f"partners = {Laura.partners}\n"
        with open(path, 'w') as f:
            f.write(data)

    # ----------------------------------------------------------------
    # ------------------------------------------------- Read TOML File
    # ----------------------------------------------------------------
    def read_toml(self, filename):
        if ".toml" not in filename:
            filename += ".toml"
        path = os.path.join(self.tomldir, filename)
        with open(path, 'r') as f:
            data = toml.load(f)
        return data

    # ----------------------------------------------------------------
    # ------------------------------------------------- Read TEXT File
    # ----------------------------------------------------------------
    def read_text(self, filename):
        if ".txt" not in filename:
            filename += ".txt"
        path = os.path.join(self.textdir, filename)
        with open(path, 'r') as f:
            data = f.read().splitlines()
        return data
