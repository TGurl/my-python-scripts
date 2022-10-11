#!/usr/bin/env python


class BigLetters:
    def __init__(self):
        self.alphabet = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', '.', '!', '?', ' '
        ]

        self.letters = [
            '█▀█n█▄█', '▄█n █', '▀█n█▄', '▀▀█n▄██', '█ █n▀▀█',
            '█▀n▄█', '█▄▄n█▄█', '▀▀█n  █', '███n█▄█', '█▀█n▀▀█',
            '▄▀█n█▀█', '█▄▄n█▄█', '█▀▀n█▄▄', '█▀▄n█▄▀', '█▀▀n██▄',
            '█▀▀n█▀ ', '█▀▀n█▄█', '█ █n█▀█', '█n█', '  █n█▄█',
            '█▄▀n█ █', '█  n█▄▄', '█▀▄▀█n█ ▀ █', '█▄ █n█ ▀█',
            '█▀█n█▄█', '█▀█n█▀▀', '█▀█n▀▀█', '█▀█n█▀▄', '█▀n▄█',
            '▀█▀n █ ', '█ █n█▄█', '█ █n▀▄▀', '█ █ █n▀▄▀▄▀',
            '▀▄▀n█ █', '█▄█n █ ', '▀█n█▄', ' n▄', '█n▄', '▀█n ▄',
            'n'
        ]

    def test(self):
        print(len(self.alphabet))
        print(len(self.letters))

    def convert(self, text):
        letters = []
        bigletters = []
        letters.extend(text.replace("_", " ").lower())
        for letter in letters:
            idx = self.alphabet.index(letter)
            sign = self.letters[idx]
            bigletters.append(sign)
        return bigletters

    def titler(self, text):
        topline = ""
        botline = ""
        letters = self.convert(text)
        for letter in letters:
            parts = letter.split('n')
            topline += parts[0] + ' '
            botline += parts[1] + ' '
        result = f"{topline}\n{botline}"
        return result


if __name__ == "__main__":
    bl = BigLetters()
    test = bl.titler('Geertje loves big black cocks!')
    print(test)
