import curses


def main(stdscr):
    status = [curses.A_BLINK, curses.A_BOLD, curses.A_DIM, curses.A_REVERSE, curses.A_STANDOUT, curses.A_UNDERLINE]

    stdscr.clear()

    for i, s in enumerate(status):
        i1 = i + 1
        stdscr.addstr(i1, 0, "Current Mode: Typing Mode", s)

    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
