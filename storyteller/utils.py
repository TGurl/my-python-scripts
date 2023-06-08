import os
import pickle
from colors import Colors


class Utils:
    def __init__(self):
        pass

    # ----------------------------------------------------
    # ---- Print functions
    # ----------------------------------------------------
    def colorize(self, line):
        for color in Colors.colors:
            line = line.replace(color[0], color[1])
        return line

    def decolorize(self, line):
        for code in Colors.codes:
            line = line.replace(code, '')
        return line

    def myprint(self, line, width=0, clear=False, center=False, nl=False):
        newline = '\n\n' if nl else '\n'
        spaces = ''
        if width == 0:
            width = os.get_terminal_size().columns
        if center:
            temp = self.decolorize(line)
            numspaces = (width - len(temp)) // 2
            spaces = numspaces * ' '
        if clear:
            os.system('clear')
        print(f"{spaces}{line}", end=newline)

    def create_top_bot_lines(self, width):
        boxchar = ('╭', '╮', '╰', '╯ ', '│', '─')
        horline = (width - 2) * boxchar[5]
        topline = boxchar[0] + horline + boxchar[1]
        botline = boxchar[2] + horline + boxchar[3]
        return topline, botline

    def box(self, line, width=0, center=False, nl=False):
        char = '│'
        newline = '\n\n' if nl else '\n'
        if width == 0:
            width = os.get_terminal_size().columns
        if center:
            numspaces = (width - len(line)) // 2
            spaces = numspaces * ' '
        topline, botline = self.create_top_bot_lines(width)
        line = char + ' ' + line + + ' ' + char

    def multibox(self, lines, width=0, center=False, nl=False):
        char = '│'
        newline = '\n\n' if nl else '\n'
        if width == 0:
            width = os.get_terminal_size().columns

    # ----------------------------------------------------
    # ---- File IO functions
    # ----------------------------------------------------
    def read_contents_textfile(self, path):
        """
        Reads the contents of a textfile

        path: full path to file
        returns: List
        """
        with open(path, 'r') as txtfile:
            data = txtfile.read().splitlines()
        return data

    def pickle_it(self, data, path):
        """
        Save data to a pickle file

        data: dictionary containing the data
        path: full path to the pickle file
        """
        pickle_out = open(path, 'wb')
        pickle.dump(data, pickle_out)
        pickle_out.close()

    def open_pickle(self, path):
        """
        Load the data from a pickle file

        path: full path to the pickle file
        Returns: dictionary of data.
        """
        pickle_in = open(path, 'rb')
        data = pickle.load(path)
        pickle_in.close()
        return data

