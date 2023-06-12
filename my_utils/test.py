#!/usr/bin/env python
from myutils import MyUtils


class Test(MyUtils):
    def __init__(self):
        super().__init__()


    def run(self):
        lines = ['%y12345678%R', '%pCopyright (C) 2023, TransGirl%R']
        self.boxit(lines, width=36, clearscreen=True)


if __name__ == "__main__":
    app = Test()
    app.run()
