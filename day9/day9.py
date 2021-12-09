import sys
from collections import defaultdict
from functools import reduce
import heapq

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

depths = defaultdict(int)
with open(input_file, 'r') as file:
    for i, line in enumerate(file):
        line_values = [int(x) for x in line.split()[0]]
        for j, value in enumerate(line_values):
            depths[(i,j)] = value

def is_low_point(x, y):
    adjacents = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    for adjacent in adjacents:
        if adjacent in depths and depths[adjacent] <= depths[(x, y)]:
            return False

    return True

def basin_size(x, y):
    size = 0
    keys = [(x,y)]

    sequence = []
    seen = defaultdict(bool)

    while len(keys) > 0:
        key = keys.pop()

        if key not in depths or seen[key]:
            continue

        seen[key] = True
        size += 1

        sequence.append(depths[key])

        adjacent_keys = [
            (key[0]+1, key[1]),
            (key[0]-1, key[1]),
            (key[0], key[1]+1),
            (key[0], key[1]-1)
        ]

        for adjacent in adjacent_keys:
            if depths[adjacent] != 9 and depths[adjacent] > depths[key]:
                keys.append(adjacent)

    return size

def answer1():
    answers = []
    for key in depths.keys():
        if is_low_point(*key):
            answers.append(depths[key]+1)

    return sum(answers)

print(answer1())

def answer2():
    answers = []
    heapq.heapify(answers)

    for key in depths.keys():
        if is_low_point(*key):
            heapq.heappush(answers, basin_size(*key))

    return reduce(lambda x, y: x*y, list(heapq.nlargest(3, answers)))

print(answer2())