import os
import sys

from settings import COMMANDS, STORYDIR


class CLI:
    def __init__(self):
        self.title = 'Fable'
        self.version = '0.01'

    def header(self):
        title_line = f"{self.title} shell, version {self.version}"
        print(title_line)
        print("Type 'help' for more information", end='\n\n')

    def shell(self, prompt=None, clear = False):
        os.system('clear')
        self.header()

        running = True
        prompt = f"> " if prompt is None else prompt + " > "

        while running:
            if clear:
                os.system('clear')
                self.header()

            command = input(prompt).lower()
            self.process(command)

    def process(self, command):
        match command.split(" ")[0]:
            case 'list': self.list_stories()
            case 'create': pass
            case 'open': self.open_story(command.split(" ")[1])
            case 'delete': pass
            case 'clear': self.shell(clear=True)
            case 'help': self.help()
            case 'exit': sys.exit()
            case _:
                print("Unkown command given. Type 'help' for more information.", end='\n\n')

    def help(self):
        print(f"{self.title} shell help")
        print("You can issue one of the following commands", end="\n\n")
        for _, item in enumerate(COMMANDS):
            print(f" {item[0]}\t\t{item[1]}")
        print()
        return True
    
    def index_stories(self):
        stories = []
        contents = os.scandir(STORYDIR)
        for item in contents:
            if ".md" in item.name and not "notes.md" in item.name:
                stories.append((item.name, item.path))
        return stories
    
    def list_stories(self):
        contents = self.index_stories()
        for idx, item in enumerate(contents, start=1):
            story_title = item[0].replace("_", " ").replace(".md", "")
            print(f"({idx}) {story_title}")
        print()

    def open_story(self, idx):
        idx = int(idx) - 1
        contents = self.index_stories()
        story_file = contents[idx][1]
        notes_file = story_file.replace(".md", "_notes.md")
        global_notes = os.path.join(STORYDIR, "global_notes.md")
        
        cli_command = f"vim -p {story_file} {notes_file} {global_notes}"
        os.system(cli_command)
        self.shell(clear=True)


