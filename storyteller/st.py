#!/usr/bin/env python
import os
from utils import Utils


class StoryTeller:
    def __init__(self):
        self.utils = Utils()

    def run(self):
        config_path = os.path.expanduser(os.path.join('~', '.bin', 'st.pickle'))
        if os.path.exists(config_path):
            self.utils.load_config()
        self.utils.menu()


if __name__ == "__main__":
    app = StoryTeller()
    app.run()
