#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
SIZE = 1311
paper = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
instructions = []

with open(input_file, 'r') as file:
    for line in file:
        if line == '\n':
            break

        y, x = line.strip().split(',')

        paper[int(x)][int(y)] = 1

    for line in file:
        instruction = line.split('fold along ')[1].split('=')
        instructions.append((instruction[0], int(instruction[1])))


ANSWER_1 = 0


def count_points():
    global ANSWER_1
    for i in range(SIZE):
        for j in range(SIZE):
            if paper[i][j] != 0:
                ANSWER_1 += 1


def fold(instructions):
    for count, instruction in enumerate(instructions):
        direction, pos = instruction

        if direction == 'y':
            for i in range(pos+1, SIZE):
                for j in range(SIZE):
                    paper[i-2*(i-pos)][j] += paper[i][j]
                    paper[i][j] = 0
        else:
            for i in range(SIZE):
                for j in range(pos+1, SIZE):
                    paper[i][j-2*(j-pos)] += paper[i][j]
                    paper[i][j] = 0

        if count == 0:
            count_points()


def answer1():
    fold(instructions)
    print(ANSWER_1)


def answer2():
    for i in range(SIZE):
        for j in range(SIZE):
            if paper[i][j] != 0:
                paper[i][j] = '██'
            else:
                paper[i][j] = '  '

    for i in range(7):
        line = ''
        for count, c in enumerate(paper[i]):
            if count < 50:
                line += c

        print(line)


answer1()
answer2()
