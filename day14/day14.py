#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict
input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'


starting_polymer = defaultdict(int)
translation = defaultdict(str)
letter_count = defaultdict(int)
with open(input_file, 'r') as file:
    for line in file:
        if line == '\n':
            break

        stripped_line = line.strip()
        for i in range(len(stripped_line)-1):
            starting_polymer[stripped_line[i:i+2]] += 1

        for c in stripped_line:
            letter_count[c] += 1

    for line in file:
        x, y = line.strip().split(' -> ')
        translation[x] = y


def combine(rounds):
    current_polymer = starting_polymer

    for _ in range(rounds):
        new_polymer = defaultdict(int)

        for key in current_polymer:
            new_pair1 = key[0] + translation[key]
            new_pair2 = translation[key] + key[1]

            new_polymer[new_pair1] += current_polymer[key]
            new_polymer[new_pair2] += current_polymer[key]
            letter_count[translation[key]] += current_polymer[key]

        current_polymer = new_polymer


def answer(rounds):
    combine(rounds)

    M = -1
    m = 1 << 200

    for key in letter_count:
        M = max(M, letter_count[key])
        m = min(m, letter_count[key])

    return M - m


print(answer(10))
print(answer(40))
