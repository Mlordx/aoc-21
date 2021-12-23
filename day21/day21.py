#!/usr/bin/python3

from collections import defaultdict


def answer1():
    pos1 = 3
    pos2 = 7
    i = 1
    score1 = 0
    score2 = 0

    while True:
        for _ in range(3):
            val = (i - 1) % 100 + 1
            assert 1 <= val <= 100
            pos1 = (pos1 + val - 1) % 10 + 1
            assert 1 <= pos1 <= 10
            i += 1

        score1 += pos1
        if score1 >= 1000:
            break

        for _ in range(3):
            val = (i - 1) % 100 + 1
            pos2 = (pos2 + val - 1) % 10 + 1
            assert 1 <= pos2 <= 10
            i += 1

        score2 += pos2
        if score2 >= 1000:
            break

    return (i - 1) * min(score1, score2)


print(answer1())

num_of_wins = defaultdict(int)


def solve(p1, score1, p2, score2):
    if (p1, score1, p2, score2) in num_of_wins:
        return num_of_wins[(p1, score1, p2, score2)]

    if score2 >= 21:
        return (0, 1)

    w1, w2 = 0, 0
    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            for k in [1, 2, 3]:
                val = i + j + k
                new_p1 = (p1 + val - 1) % 10 + 1
                count2, count1 = solve(p2, score2, new_p1, score1 + new_p1)
                w1 += count1
                w2 += count2

    num_of_wins[(p1, score1, p2, score2)] = (w1, w2)
    return w1, w2


def answer2():
    return max(solve(3, 0, 7, 0))


print(answer2())
