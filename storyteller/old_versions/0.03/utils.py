import os
import pickle

from settings import DISCLAIMER


class Utils:
    def __init__(self):
        self.config_file = os.path.expanduser(
            os.path.join("~", ".local", "share", "storyteller", "st.cfg")
        )
        self.story_dir = os.path.expanduser(os.path.join("~", "stories"))
        self.stories = []
        self.last_story = ""
        self.load_settings()

    def load_settings(self):
        if not os.path.exists(self.config_file):
            self.last_story = ""
        else:
            pickle_in = open(self.config_file, "rb")
            data = pickle.load(pickle_in)
            pickle_in.close()
            self.last_story = data["last_story"]

    def save_settings(self):
        data = {"last_story": self.last_story}
        pickle_out = open(self.config_file, "wb")
        pickle.dump(data, pickle_out)
        pickle_out.close()

    def collect_stories(self) -> list:
        collection = []
        for file in os.listdir(self.story_dir):
            path = os.path.join(self.story_dir, file)
            _, ext = os.path.splitext(path)
            if "notes" not in path and not os.path.isdir(path) and ext == ".md":
                collection.append(path)
        collection.sort()
        return collection

    def refresh_story_list(self):
        self.stories = []
        self.stories = self.collect_stories()

    def clean_text(self, title):
        title = title.replace(" ", "_")
        title = title.replace(",", "")
        title = title.replace("\\", "")
        title = title.replace("'", "")
        return title

    def create_new_story(self, new_title):
        if new_title == "":
            return
        story = os.path.join(self.story_dir, f"{new_title}.md")
        story = self.clean_text(story)
        notes = story.replace(".md", "_notes.md")
        overall = os.path.join(self.story_dir, "global_notes.md")

        with open(story, "w") as storyfile:
            storyfile.write(f"# {new_title.upper()}\n")
            storyfile.write("_an erotic tale by Transgirl_\n\n")
            for line in DISCLAIMER:
                storyfile.write(line)
            storyfile.write("## Chapter One\n\n")

        with open(notes, "w") as notefile:
            notefile.write(f"# NOTES FOR {new_title.upper()}\n\n")
            notefile.write("Room for some notes")

        self.last_story = story
        self.save_settings()
        os.system(f"vim -p {story} {notes} {overall}")

    def open_story(self, id):
        if id == "":
            return
        id = int(id) - 1
        self.refresh_story_list()
        story = self.stories[id]
        notes = story.replace(".md", "_notes.md")
        overall = os.path.join(self.story_dir, "global_notes.md")

        self.last_story = story
        self.save_settings()
        os.system(f"vim -p {story} {notes} {overall}")

    def continue_story(self):
        story = self.last_story
        notes = story.replace(".md", "_notes.md")
        overall = os.path.join(self.story_dir, "global_notes.md")
        os.system(f"vim -p {story} {notes} {overall}")

    def edit_story_notes(self):
        notes = self.last_story.replace(".md", "_notes.md")
        os.system(f"vim -p {notes}")

    def delete_story(self, id):
        if id == "":
            return
        id = int(id) - 1
        self.refresh_story_list()
        story = self.stories[id]
        notes = story.replace(".md", "_notes.md")

        if self.last_story == story:
            self.last_story = ""
            self.save_settings()

        os.remove(story)
        os.remove(notes)
        self.collect_stories()

    def edit_overall_notes(self):
        overall = os.path.join(self.story_dir, "global_notes.md")
        os.system(f"vim -p {overall}")

    def get_title(self, storyname):
        storyname = storyname.split("/")[-1]
        storyname = storyname.replace("_", " ")
        storyname = storyname.replace(".md", "")
        storyname = storyname.title()
        return storyname
