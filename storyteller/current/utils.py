import os
from colors import Colors


class Utils:
    def __init__(self):
        pass

    def colorize(self, line):
        for color in Colors.colors:
            line = line.replace(color[0], color[1])
        return line

    def decolorize(self, line):
        for code in Colors.codes:
            line = line.replace(code, '')
        return line

    def myprint(self, text, nl=False):
        newline = '\n\n' if nl else '\n'
        text = self.colorize(text)
        print(text, end=newline)

    def collect_stories(self):
        storydir = os.path.expanduser(os.path.join('~', 'stories'))
        doscan = True
        if not os.path.exists(storydir):
            os.mkdir(storydir)
            doscan = False

        stories = []
        if doscan:
            for file in os.listdir(storydir):
                if file.endswith(".md"):
                    stories.append(file)
        return stories

    def main_menu(self):
        menu_items = [
                'start a new story',
                'continue story',
                'delete story',
                'quit']
        stories = self.collect_stories()

        valid = []
        os.system('clear')
        for num, story in enumerate(stories, start=1):
            self.myprint(f"%c[%y{num}%c]%R {story}")
            valid.append(str(num))
        print()
        for item in menu_items:
            letter = item[0]
            valid.append(letter)
            self.myprint(f"%c[%y{letter.upper()}%c]%R {item}")

        response = input(">> ").lower()
        if response not in valid:
            print("Not a valid option...")
        elif response == 'q':
            return False
        else:
            return response
