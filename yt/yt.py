#!/usr/bin/env python
import os

def main():
    with open('list.txt', 'r') as tf:
        lines = tf.readlines()

    for line in lines:
        cmd = f"mpv {line}"
        os.system(cmd)


if __name__ == "__main__":
    main()
