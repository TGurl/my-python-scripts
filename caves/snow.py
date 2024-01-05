#!/usr/bin/env python
"""
This is meant as an example for the terminal based game 'Caves'

Original code: Engineer Man
Adapted by: Transgirl
Youtube: https://www.youtube.com/watch?v=_chP0a4PMTM
Snow text symbols: https://www.namecheap.com/visual/font-generator/snowflake-text-symbols/
"""

import os
import random
import time

# --- define constants
SNOW_DENSITY = 3
DELAY = 0.1
EMPTY_SPACE = " "
MESSAGE = "Merry Christmas"
RED = "\033[31;1m"
GREEN = "\033[32;1m"
RESET = "\033[0m"

# --- define variables
snowflakes = ["❅", "❇", "❉", "❃", "·", "•"]
term = os.get_terminal_size()
w = term.columns
h = term.lines
center_w = (w - len(MESSAGE)) // 2
center_h = (h - 2) // 2


# --- create the grid
grid = []

for _ in range(h):
    grid.append([EMPTY_SPACE] * w)


# --- draw grid function
def draw_grid(row_line=[EMPTY_SPACE] * w):
    grid.insert(0, row_line)
    grid.pop()
    bu_grid = grid.copy()

    mlist = [*MESSAGE]  # split the message into chars

    os.system("cls" if os.name == "nt" else "clear")
    print("\033[?25l")
    output = ""
    for idx, line in enumerate(grid):
        if idx == center_h:
            for idx1 in range(len(MESSAGE)):
                line[center_w + idx1] = mlist[idx1]

            for idx2 in range(center_h, h):
                line = bu_grid[idx2]

        output += "".join(line) + "\n"
    output = output.strip("\n")
    print(output, end="")


# --- show a snowflake?
def snowflake_generator():
    line = []
    for _ in range(w):
        if random.random() < SNOW_DENSITY / 100:
            line.append(random.choice(snowflakes))
        else:
            line.append(EMPTY_SPACE)

    return line


# --- exit strategy
def exit_app():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[?25h", end="")
    print(f"{GREEN}{MESSAGE} Everyone!{RESET}")


# --- draw the flakes to the screen
def draw_flakes():
    row = snowflake_generator()  # a list of characters
    draw_grid(row)
    time.sleep(DELAY)


# --- initialize the screen
draw_grid()

# --- the main loop
while True:
    try:
        draw_flakes()
    except KeyboardInterrupt:
        exit_app()
        break
