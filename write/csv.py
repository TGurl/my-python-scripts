#!/usr/bin/env python

namelist = "data/cities.txt"
csvlist = "data/cities.dat"

with open(namelist, "r") as f:
    data = f.read().splitlines()


with open(csvlist, "w") as f:
    for d in data:
        d = d.split(",")
        n = d[1] + "," + d[2]
        print(n)
        f.write(n + "\n")
