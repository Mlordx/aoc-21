#!/usr/bin/python3
import sys
from collections import defaultdict
input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

algorithm = ''
image = defaultdict(int)
with open(input_file, 'r') as file:
    for i, line in enumerate(file):
        if i == 0:
            algorithm = line.strip()
        if i >= 2:
            stripped = line.strip()
            for j, c in enumerate(stripped):
                if c == '#':
                    image[(i - 2, j)] = 1
                else:
                    image[(i - 2, j)] = 0

min_x = -1
max_x = i+1
min_y = -1
max_y = j+1


def solve(min_x, max_x, min_y, max_y, part1=False):
    current_image = image

    t = 0
    x1 = min_x
    x2 = max_x
    y1 = min_y
    y2 = max_y

    while True:
        if (part1 and t == 2) or t == 50:
            count = 0

            for key in current_image:
                if current_image[key] == 1:
                    count += 1
            return count

        new_image = defaultdict(int)

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                pos = ''
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if (x + i, y + j) in current_image:
                            pos += str(current_image[(x + i, y + j)])
                        else:
                            if algorithm[0] == '#':
                                pos += '0' if t % 2 == 0 else '1'
                            else:
                                pos += '0'

                new_image[(x, y)] = 1 if algorithm[int(pos, 2)] == '#' else 0

        x1 -= 1
        x2 += 1
        y1 -= 1
        y2 += 1
        t += 1
        current_image = new_image


def answer1():
    global min_x, max_x, min_y, max_y
    return solve(min_x, max_x, min_y, max_y, True)


def answer2():
    global min_x, max_x, min_y, max_y
    return solve(min_x, max_x, min_y, max_y)


print(answer1())
print(answer2())
