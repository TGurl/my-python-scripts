from settings import Config
from colors import Colors
from random import choice
from time import sleep
import pickle
import os
import glob


class Utils:
    def __init__(self):
        pass

    def colorize(self, text):
        for code in Colors.colors:
            text = text.replace(code[0], code[1])
        return text

    def decolorize(self, text):
        for code in Colors.colors:
            text = text.replace(code[0], '')
        return text

    def save_config(self):
        data = {
                'title': Config.title,
                'version': Config.version,
                'storydir': Config.storydir,
                'laststory': Config.laststory,
                'lastquote': Config.lastquote
                }
        config_path = os.path.expanduser(os.path.join('~', '.bin', 'st.pickle'))
        pickle_out = open(config_path, 'wb')
        pickle.dump(data, pickle_out)
        pickle_out.close()

    def load_config(self):
        config_path = os.path.expanduser(os.path.join('~', '.bin', 'st.pickle'))
        pickle_in = open(config_path, 'rb')
        data = pickle.load(pickle_in)
        pickle_in.close()
        
        Config.storydir = data['storydir']
        Config.laststory = data['laststory']
        Config.lastquote = data['lastquote']

    def myprint(self, text, italic=False, nl=False):
        newline = '\n\n' if nl else '\n'
        text = self.colorize(text)
        if italic:
            text = "\x1B[3m" + text + "\x1B[0m"
        print(text, end=newline)

    def print_error(self, message):
        print('\033[1A', end='\x1b[2K')
        self.myprint(f"%r‼%R {message}")
        sleep(1.2)

    def select_quote(self):
        quote = choice(Config.quotes)
        idx = Config.quotes.index(quote)
        while idx == Config.lastquote:
            quote = choice(Config.quotes)
            idx = Config.quotes.index(quote)
        Config.lastquote = idx
        self.save_config()
        return quote
    
    def print_header(self):
        os.system('clear')
        quote = self.select_quote()
        title = '%g»%R %y' + Config.title + ' ' + Config.version + ' %g«%R'
        t_spaces = ''
        q_spaces = ''
        len_title = len(self.decolorize(title))
        len_quote = len(self.decolorize(quote))
        if len_title > len_quote:
            line = '%c' + ((len_title + 4) * '─') + '%R'
            q_spaces = ((len_title - len_quote) // 2) * ' '
        else:
            line = '%c' + ((len_quote + 4) * '─') + '%R'
            t_spaces = ((len_quote - len_title) // 2) * ' '

        self.myprint(line)
        self.myprint(f'  {t_spaces}{title}')
        self.myprint(f'  {q_spaces}{quote}', italic=True)
        self.myprint(line, nl=True)

    def collect_stories(self):
        stories = []
        pattern = os.path.join(Config.storydir, '*.md')
        stories1 = glob.glob(pattern)
        for story in stories1:
            # Remove the notes from the list of stories
            if "_notes" not in story:
                stories.append(story)
        stories.sort()
        return stories

    def open_files(self, story, notes):
        os.system(f"vim -p + {story} + {notes}")

    def open_story(self, story_id):
        stories = self.collect_stories()
        story = stories[story_id - 1]
        notes = story.replace('.md', '_notes.md')
        Config.laststory = story
        self.save_config()
        self.open_files(story, notes)
    
    def continue_last_story(self):
        notes = Config.laststory.replace('.md', '_notes.md')
        self.open_files(Config.laststory, notes)

    def delete_a_story(self):
        exit_menu = False
        while True:
            self.print_header()
            stories = self.collect_stories()
            valid = []
            self.myprint('%cWhich story do you want to delete?%R', nl=True)
            for num, story in enumerate(stories, start=1):
                valid.append(str(num))
                story_name = story.split('/')[-1].replace('_', ' ').replace('.md', '').title()
                if num < len(stories):
                    self.myprint(f"%c[%y{num}%c]%R {story_name}")
                else:
                    self.myprint(f"%c[%y{num}%c]%R {story_name}", nl=True)
            self.myprint('Leave empty to return to main menu', italic=True, nl=True)
            prompt = self.colorize('%c»%R ')
            response = input(prompt).lower()
            if response == '':
                exit_menu = True
                break
            elif response not in valid:
                self.print_error('That is not a valid option...')
            else:
                break

        if not exit_menu:
            filepath = stories[int(response) - 1]
            if filepath == Config.laststory:
                Config.laststory = ''
            notepath = filepath.replace('.md', '_notes.md')
            os.remove(filepath)
            os.remove(notepath)
            stories = self.collect_stories()

    def create_a_new_story(self):
        exit_menu = False
        filepath = ''
        notepath = ''
        while True:
            self.print_header()
            self.myprint('%cWhat title do you want to give this story?%R')
            self.myprint('Leave empty to return to main menu', italic=True, nl=True)
            prompt = self.colorize('%c»%R ')
            title = input(prompt).lower()
            if title == '':
                exit_menu = True
                break
            else:
                filepath = os.path.join(Config.storydir, title.replace(' ', '_') + '.md')
                notepath = filepath.replace('.md', '_notes.md')

                if os.path.exists(filepath):
                    self.print_error('There already is a story with that title...')
                else:
                    break

        if not exit_menu and filepath != '':
            with open(filepath, 'w') as story:
                story.write(f"# {title.title()}\n")
                story.write("_an erotic tale by TransGirl_\n\n")
                story.write("## Disclaimer\n\n")
                story.write("This story is a work of fiction. Any resemblance to any person living or dead is\n")
                story.write("purely coincidental. All characters are presumed to be of legal age.\n\n")
                story.write('## Chapter One\n\n')

            with open(notepath, 'w') as note:
                note.write(f"# {title.title()} notes\n\n")

            Config.laststory = filepath
            self.save_config()
            self.open_files(filepath, notepath)

    def process_choice(self, choice):
        match choice:
            case 'n': self.create_a_new_story()
            case 'c': self.continue_last_story()
            case 'd': self.delete_a_story()
            case _: self.open_story(int(choice))


    def menu(self):
        last_story_name = ''
        while True:
            self.print_header()
            if Config.laststory != '':
                last_story_name = Config.laststory.split('/')[-1].replace('_', ' ').replace('.md', '').title()
                # self.myprint(f"%wLast story%R: {story_name}", nl=True)
            valid = []
            stories = self.collect_stories()

            if len(stories) == 0:
                self.myprint('%gYou didn\'t write any stories yet...%R', italic=True, nl=True)
            for count, story in enumerate(stories, start=1):
                valid.append(str(count))
                story_name = story.split('/')[-1].replace('_', ' ').replace('.md', '').title()
                if count < len(stories):
                    self.myprint(f"%c[%y{count}%c]%R {story_name}")
                else:
                    self.myprint(f"%c[%y{count}%c]%R {story_name}", nl=True)

            valid.extend(['n', 'd', 'q'])
            if Config.laststory != '':
                valid.append('c')

            self.myprint('%c[%yn%c]%R Start a new story')
            if Config.laststory != '':
                self.myprint(f"%c[%yc%c]%R Continue %c%i{last_story_name}%R")
            if len(stories) > 0:
                self.myprint("%c[%yd%c]%R Delete a story", nl=True)
            self.myprint('%c[%rq%c]%R Quit', nl=True)
            prompt = self.colorize(f'%c»%R ')
            response = input(prompt).lower()
            if response not in valid:
                self.print_error('That is not a valid option...')
            elif response == 'q':
                break
            else:
                self.process_choice(response)
