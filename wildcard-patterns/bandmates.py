#!/usr/bin/env python3

INFILE = "musicians.txt"
HUMANLY_POSSIBLE = 3  # the most instruments anyone could possibly play

with open(INFILE, "r") as f_in:
    for line in f_in:
        match line.rstrip().split(":"):
            case [name, instruments, bands]:
                pass
            case _:
                print(line.rstrip())

