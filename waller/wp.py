#!/usr/bin/env python3

from rich import box, print
from rich.console import Console
from rich.panel import Panel


from settings import CONFIG

print(Panel.fit("[yellow]WALLr[/yellow] - [cyan]Version 4.0[/cyan] - [cyan]Copyleft 2023 [magenta]Transgirl[/magenta]",
                box=box.HORIZONTALS, width=60))
