from tui import TUI
from config import Config


class Utils:
    def __init__(self):
        self.tui = TUI()

    def replace_in_string(self, string, new, index):
        temp = list(string)
        temp[index] = new
        return "".join(temp)

    def start_download(self):
        print(Config.query, Config.categories, Config.filter)

    def assume_defaults(self, query):
        Config.query = query
        Config.categories = "101"
        Config.filter = "101"
        self.start_download()

    def render_questionaire(self):
        self.tui.render_header()
        query = self.tui.get_input("-> Query")
        general = self.tui.askyesno("-> Enable General?")
        anime = self.tui.askyesno("-> Enable Anime?", defyes=False)
        people = self.tui.askyesno("-> Enable People?")
        sfw = self.tui.askyesno("-> SFW?")
        sketchy = self.tui.askyesno("-> Sketchy?", defyes=False)
        nsfw = self.tui.askyesno("-> NSFW?")

        Config.query = query
        # -- parse the categories
        if general:
            Config.categories = self.replace_in_string(Config.categories, "1", 0)

        if anime:
            Config.categories = self.replace_in_string(Config.categories, "1", 1)

        if people:
            Config.categories = self.replace_in_string(Config.categories, "1", 2)

        if sfw:
            Config.filter = self.replace_in_string(Config.filter, "1", 0)

        if sketchy:
            Config.filter = self.replace_in_string(Config.filter, "1", 1)

        if nsfw:
            Config.filter = self.replace_in_string(Config.filter, "1", 2)

        self.start_download()
