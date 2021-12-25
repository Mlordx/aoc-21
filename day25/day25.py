#!/usr/bin/python3
import sys
input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

east = set()
south = set()

with open(input_file, 'r') as file:
    for i, line in enumerate(file):
        stripped = line.strip()
        for j, c in enumerate(stripped):
            if c == '.':
                continue

            if c == '>':
                east.add((i, j))
            else:
                south.add((i, j))

WIDTH = i + 1
HEIGHT = j + 1


def answer1():
    current_east = east
    current_south = south
    i = 1
    while True:
        moved = 0
        new_east = set()
        new_south = set()

        for x, y in current_east:
            if (x, (y + 1) % HEIGHT) in current_east or (x, (y + 1) % HEIGHT) in current_south:
                new_east.add((x, y))
            else:
                moved += 1
                new_east.add((x, (y + 1) % HEIGHT))

        for x, y in current_south:
            if ((x + 1) % WIDTH, y) in new_east or ((x + 1) % WIDTH, y) in current_south:
                new_south.add((x, y))
            else:
                moved += 1
                new_south.add(((x + 1) % WIDTH, y))

        current_east = new_east
        current_south = new_south
        if moved == 0:
            break

        i += 1

    return i


print(answer1())
