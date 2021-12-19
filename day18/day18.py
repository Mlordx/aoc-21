#!/usr/bin/python3
import sys
from functools import reduce

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
snailfish_numbers = []
DIGITS = '0123456789'
with open(input_file, 'r') as file:
    for line in file:
        snailfish_numbers.append(line.strip())


def needs_fixing(line):
    bracket_count = 0
    for i in range(len(line)):
        c = line[i]
        if c == '[':
            bracket_count += 1
        elif c == ']':
            bracket_count -= 1

        if bracket_count == 5:
            return True

        if c in DIGITS and line[i+1] in DIGITS:
            return True

    return False


def add_left(line, val):
    for i in range(len(line))[::-1]:
        c = line[i]

        if c in DIGITS:
            if line[i-1] in DIGITS:
                number = int(line[i-1]+line[i]) + val
                return line[:i-1] + str(number) + line[i+1:]
            else:
                number = int(c) + val
                return line[:i] + str(number) + line[i+1:]

    return line


def add_right(line, val):
    for i in range(len(line)):
        c = line[i]

        if c in DIGITS:
            if line[i+1] in DIGITS:
                number = int(line[i]+line[i+1]) + val
                return line[:i] + str(number) + line[i+2:]
            else:
                number = int(c) + val
                return line[:i] + str(number) + line[i+1:]

    return line


def fix_line(line):
    brackets = 0
    split_pos = None
    for i in range(len(line)):
        c = line[i]
        if c == '[':
            brackets += 1
        elif c == ']':
            brackets -= 1

        if brackets == 5:
            j = i
            while line[j] != ']':
                j += 1

            l, r = line[i+1:j].split(',')

            return add_left(line[:i], int(l)) + '0' + add_right(line[j+1:], int(r))

        if c in DIGITS and line[i+1] in DIGITS and not split_pos:
            split_pos = i

    if split_pos:
        k = split_pos
        val = int(line[k:k+2])
        new = f'[{val//2},{(val+1)//2}]'

        return line[:k] + new + line[k+2:]

    return line


def add(line1, line2):
    new_line = '[' + line1 + ',' + line2 + ']'

    current_line = new_line
    while needs_fixing(current_line):
        current_line = fix_line(current_line)

    return current_line


def evaluate(line):
    return eval(line.replace("[", "(3*").replace(",", " + 2*").replace("]", ")"))


def answer1():
    final = reduce(add, snailfish_numbers)
    return evaluate(final)


def answer2():
    max_sum = -1
    for i in range(len(snailfish_numbers)):
        for j in range(len(snailfish_numbers)):
            if i != j:
                line_sum = add(snailfish_numbers[i], snailfish_numbers[j])
                max_sum = max(max_sum, evaluate(line_sum))

    return max_sum


print(answer1())
print(answer2())
