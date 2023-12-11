#!/usr/bin/env python
import os
import typer

from settings import *
from utils import Utils
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def install(file_name: Annotated[str, typer.Argument()]):
    pass

@app.command()
def remove():
    pass

@app.command()
def search(pattern: Annotated[str, typer.Argument(help='Search for a game [required]')]):
    utils = Utils()
    games = utils.collect_games()
    content = f">> Searching for [cyan][i]{pattern}[/i][/cyan]\n\n"
    for game in games:
        if pattern.lower() in game.lower():
            content += f"- {game}\n"
    utils.render_content(content)

@app.command()
def list():
    utils = Utils()
    games = utils.collect_games()
    total = len(games)
    content = f">> Total games: [cyan][i]{total}[/i][/cyan]\n\n"
    for game in games:
        content += f"- {game}\n"
    utils.render_content(content)


if __name__ == "__main__":
    app()
