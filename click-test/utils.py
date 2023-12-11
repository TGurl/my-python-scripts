import os
import glob

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from settings import *


class Utils:
    def __init__(self):
        self.console = Console()

    def collect_games(self):
        files = []
        for folder in FOLDERS:
            pattern = os.path.join(folder, '*.zip')
            content = glob.glob(pattern)
            files.extend(content)
        files.sort()
        return files

    def render_content(self, content):
        os.system('clear')
        content = f"\n[white]{content}[/white]"
        self.console.print(Panel(content, title='Porngames', title_align='left', height=20, highlight=True))
