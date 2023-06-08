import os
import sys
import glob
import pickle
import string
from time import sleep
from config import Config
from colors import Colors


class Utils:
    def __init__(self):
        self.stories = self.collect_stories()

    # ---- Generic functions

    def save_config(self, filename=Config.configfile):
        path = os.path.expanduser(
                os.path.join('~', '.local', 'bin', filename)
                )
        dictstr = self.dictstr()
        pickle_out = open(path, "wb")
        pickle.dump(dictstr, pickle_out)
        pickle_out.close()

    def load_config(self, filename=Config.configfile):
        path = os.path.expanduser(
                os.path.join('~', '.local', 'bin', filename)
                )
        if os.path.exists(path):
            pickle_in = open(path, 'rb')
            data = pickle.load(pickle_in)
            pickle_in.close()

            Config.title = data['title']
            Config.storydir = data['storydir']
            Config.configfile = data['configfile']
            Config.lastedited = data['lastedited']

    def colorize(self, text):
        for code in Colors.colors:
            text = text.replace(code[0], code[1])
        return text

    def decolorize(self, text):
        for code in Colors.codes:
            text = text.replace(code, '')
        return text

    def myprint(self, text, nl=False):
        newline = '\n\n' if nl else '\n'
        text = self.colorize(text)
        print(text, end=newline)

    def boxit(self, text, width=40):
        boxchar = ('╭', '╮', '╰', '╯ ', '│', '─')
        horline = width * boxchar[5]
        topline = boxchar[0] + horline + boxchar[1]
        botline = boxchar[2] + horline + boxchar[3]
        spaces = ((width - len(text)) // 2) * " "
        text = f"{spaces}%y{text}%c{spaces}"
        verline = boxchar[4] + text + boxchar[4]

        self.myprint(f"%c{topline}%R")
        self.myprint(f"%c{verline}%R")
        self.myprint(f"%c{botline}%R")

    def print_info(self, text, wait=False):
        prompt = f"%g>%R {text}"
        self.myprint(prompt)
        if wait:
            sleep(1.5)

    def print_error(self, text, clearline=True, wait=False):
        LINE_UP = '\033[1A'
        LINE_CLEAR = '\x1b[2K'

        prompt = f" %r>%R {text}"
        if clearline:
            print(LINE_UP, end=LINE_CLEAR)
        self.myprint(prompt)
        if wait:
            sleep(1.5)

    def render_title(self, title=Config.title):
        os.system('clear')
        sys.stdout.write(f"\x1b]2;{title}\x07")
        self.boxit(title)

    def user_input(self, msg=''):
        print()
        if msg != '':
            msg += ' '
        prompt = self.colorize(f" %c>%R {msg}")
        result = input(prompt)
        return result

    # ---- App specific functions

    def check_if_story_exists(self, path):
        if os.path.exists(path):
            return True
        else:
            return False

    def check_if_storydir_exists(self, filename=Config.configfile):
        configpath = os.path.expanduser(
                os.path.join('~', '.local', 'bin', filename)
                )
        if not os.path.exists(Config.storydir):
            os.mkdir(Config.storydir)
            if os.path.exists(configpath):
                os.remove(configpath)
            Config.lastedited = ''
            self.print_info('Story folder created...', wait=True)

    def dictstr(self):
        return dict(title=Config.title,
                    storydir=Config.storydir,
                    configfile=Config.configfile,
                    lastedited=Config.lastedited)

    def collect_stories(self):
        stories = []
        pattern = os.path.join(Config.storydir, '*.md')
        for name in glob.glob(pattern):
            stories.append(name)
        stories.sort()
        return stories

    def extract_title(self, filename):
        title = filename.split('/')[-1].replace('_', ' ').replace('.md', '')
        title = string.capwords(title)
        return title

    def do_change_title(self, idx):
        idx -= 1
        story = self.stories[idx]
        oldfilename = story.split('/')[-1]
        oldfilename = oldfilename.strip()
        title = self.extract_title(story)
        notempty = False
        newtitle = ''
        while not notempty:
            self.render_title(title='Change Title')
            self.myprint(f"Changing title for %y{title}%R", nl=True)
            prompt = "What will the new title be? : "
            newtitle = input(prompt).lower()
            if newtitle == '':
                self.print_error('A title cannot be empty...', wait=True)
            else:
                notempty = True

        newfilename = newtitle.lower().replace(' ', '_').replace("'", '') + '.md'
        newfilename = newfilename.strip()

        src = os.path.join(Config.storydir, oldfilename)
        dst = os.path.join(Config.storydir, newfilename)
        if not self.check_if_story_exists(dst):
            if Config.lastedited == src:
                Config.lastedited = dst
            os.rename(src, dst)
            self.stories = self.collect_stories()
            self.save_config()
        else:
            print()
            self.print_error('A story by that title already exists...', wait=True)

    def render_change_title_menu(self) -> list[str]:
        """The menu to change the title of a story"""
        valid = ['r']
        has_stories = True if len(self.stories) else False

        if not has_stories:
            Config.lastedited = ''
            self.save_config()

        for num, story in enumerate(self.stories, start=1):
            title = self.extract_title(story)
            self.myprint(" %c[%y{}%c]%R {}".format(num, title))
            valid.append(str(num))
        print()
        self.myprint(" %c[%rR%c]%R Return to main menu")
        return valid

    def render_menu(self):
        """The main menu of this application"""
        valid = ['q', 'n', 'd', 't']
        has_stories = True if len(self.stories) else False

        if not has_stories:
            Config.lastedited = ''
            self.save_config()

        for num, story in enumerate(self.stories, start=1):
            title = self.extract_title(story)
            self.myprint(" %c[%y{}%c]%R {}".format(num, title))
            valid.append(str(num))
        print()
        if Config.lastedited:
            title = self.extract_title(Config.lastedited)
            self.myprint(f" %c[%gC%c]%R Continue %p{title}%R")
            valid.append('c')
        self.myprint(" %c[%gN%c]%R Tell a new story")
        if has_stories:
            self.myprint(" %c[%gT%c]%R Change title of a story")
            self.myprint(" %c[%rD%c]%R Delete a story")
        print()
        self.myprint(" %c[%rQ%c]%R Quit")
        return valid

    def set_terminal_title(self, title):
        sys.stdout.write(f"\x1b]2;{title}\x07")

    def open_story(self, sid):
        story = self.stories[sid - 1]
        notes = story.replace('.md', '_notes.txt')
        self.set_terminal_title(f"Editing {story}")
        Config.lastedited = story
        self.save_config()
        os.system(f'vim + -p {story} {notes}')

    def continue_story(self):
        idx = self.stories.index(Config.lastedited)
        self.open_story(idx + 1)

    def tell_a_new_story(self):
        notempty = False
        title = ''
        while not notempty:
            self.render_title(title='Tell a new story')
            title = self.user_input(msg='What is the title of your story? :')
            if title == '':
                self.print_error('A title cannot be empty...', wait=True)
            else:
                notempty = True

        self.render_title(title='Creating new story... ')
        title = string.capwords(title)
        filename = title.lower().replace(' ', '_').replace("'", '') + '.md'
        filename = filename.strip()
        textfile = filename.replace('.md', '_notes.txt')
        path = os.path.join(Config.storydir, filename)
        textpath = os.path.join(Config.storydir, textfile)
        file = open(path, 'w')
        file.write(f"# {title}\n")
        file.write("_an erotic tale by TransGirl_\n\n")
        file.write("## Disclaimer\n\n")
        file.write("This is a work of fiction. Any resemblance to any person living or dead is\n")
        file.write("purely coincidental.\n\n")
        file.write("## Chapter One\n")
        file.write("\n")
        file.close()

        file = open(textpath, 'w')
        file.write(f"# {title} Notes\n\n")
        file.close()

        sleep(1)
        self.set_terminal_title(f"Editing {path}")
        os.system(f'vim + -p {path} {textpath}')
        self.stories = self.collect_stories()
        Config.lastedited = path
        self.save_config()

    def delete_story(self):
        valid = ['r']
        insubmenu = True
        while insubmenu:
            self.render_title(title='Delete a story... ')
            self.stories = self.collect_stories()
            if len(self.stories) == 0:
                self.print_error('No stories to delete',
                                 clearline=False,
                                 wait=True)
                insubmenu = False
            else:
                for num, story in enumerate(self.stories, start=1):
                    title = self.extract_title(story)
                    self.myprint(" %c[%y{}%c]%R {}".format(num, title))
                    valid.append(str(num))
                print()
                self.myprint(" %c[%gR%c]%R Return to main menu")
                print()
                result = self.user_input("Which one do you wish to delete? :")
                if result.lower() not in valid:
                    self.print_error("That is not an option...", wait=True)
                elif result == 'r':
                    insubmenu = False
                else:
                    idx = int(result) - 1
                    path = self.stories[idx]
                    os.remove(path)
                    if Config.lastedited == path:
                        Config.lastedited = ''
                        self.save_config()
                    title = self.extract_title(path)
                    self.print_error(f"{title} removed...", wait=True)
