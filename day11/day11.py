#!/usr/bin/python3
from collections import defaultdict, deque
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

energy = defaultdict(int)


def reset_input():
    with open(input_file, 'r') as file:
        for i, line in enumerate(file):
            line_values = [int(x) for x in line.split()[0]]
            for j, value in enumerate(line_values):
                energy[(i, j)] = value


def answer1():
    reset_input()

    total_flashes = 0

    for _ in range(100):
        octopi = deque()
        flashed = set()
        flashes = 0

        for key in energy:
            energy[key] += 1
            if energy[key] > 9:
                octopi.append(key)

        while len(octopi) > 0:
            current = octopi.pop()

            if current in flashed:
                continue

            flashed.add(current)
            flashes += 1
            x, y = current

            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if (x+i, y+j) in energy:
                        energy[(x+i, y+j)] += 1
                        if energy[(x+i, y+j)] > 9:
                            octopi.appendleft((x+i, y+j))

        for key in energy:
            if energy[key] > 9:
                energy[key] = 0

        total_flashes += flashes

    return total_flashes


print(answer1())


def answer2():
    reset_input()
    step = 0

    while True:
        flashes = 0

        step += 1
        octopi = deque()
        flashed = set()

        for key in energy:
            energy[key] += 1
            if energy[key] > 9:
                octopi.append(key)

        while len(octopi) > 0:
            current = octopi.pop()

            if current in flashed:
                continue

            flashed.add(current)
            flashes += 1
            x, y = current

            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if (x+i, y+j) in energy:
                        energy[(x+i, y+j)] += 1
                        if energy[(x+i, y+j)] > 9:
                            octopi.appendleft((x+i, y+j))

        if flashes == len(energy):
            return step

        for key in flashed:
            energy[key] = 0


print(answer2())
