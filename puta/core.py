import os

from colors import Colors


class PutaCore:
    def __init__(self):
        pass

    def colorizer(self, message, remove_colors=False):
        for color in Colors.colors:
            if remove_colors:
                replacement = ''
            else:
                replacement = color[1]
            message = message.replace(color[0], replacement)
        return message

    def fprint(self, message, new_line=False):
        carriage_return = '\n\n' if new_line else '\n'
        message = self.colorizer(message)
        print(f"{message}", end=carriage_return)
