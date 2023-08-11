#!/usr/bin/env python

import os

GIRLNAMES = 'girlnames.txt'
BOYNAMES = 'boynames.txt'

VARIABLES = 'variables.py'

with open(GIRLNAMES, 'r') as infile:
    girlnames = infile.read().split()

with open(BOYNAMES, 'r') as infile:
    boynames = infile.read().split()

with open(VARIABLES, 'w') as outfile:
    outfile.write('"""LISTS OF NAMES FOR GIRLS AND BOYS"""\n')
    outfile.write('GIRLNAMES = [')
    for name in girlnames:
        outfile.write(f"'{name}', ")
    outfile.write(']\n\n')

with open(VARIABLES, 'a') as outfile:
    outfile.write('BOYNAMES = [')
    for name in boynames:
        outfile.write(f"'{name}',  ")
    outfile.write(']')
