#!/usr/bin/env python3

INFILE = "bandmates.txt"
HUMANLY_POSSIBLE = 3  # the most instruments anyone could possibly play

with open(INFILE, "r", encoding="utf-8") as f_in:
    for line in f_in:
        try:
            match line.rstrip().split(":"):
                case [name, instruments, bands]:
                    instruments = instruments.split(",")
                    bands = bands.split(",")
                    match name.split(" "):
                        case [first, middle, last]:
                            pass
                        case [first, last]:
                            pass
                        case _:
                            raise ValueError(f"{name}: Not enough names!")
                    match [first, [*instruments], [*bands]]:
                        case [first, instruments, bands] if len(instruments) > HUMANLY_POSSIBLE:
                            print(f"{name} plays more different instruments than humanly possible.")
                        case [first, instruments, bands] if len(bands) > 2:
                            print(f"Playing with {first} is habit-forming.")
                case _:
                    print(line.rstrip())
            except ValueError:
                pass
