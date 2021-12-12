#!/usr/bin/python3
from collections import defaultdict
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

adj = defaultdict(list)

with open(input_file, 'r') as file:
    for line in file:
        x, y = line.strip().split('-')
        adj[x].append(y)
        adj[y].append(x)


def dfs(current, visited):
    if current == 'end':
        return 1

    total = 0

    visited.add(current)

    for neighbor in adj[current]:
        if neighbor.isupper() or neighbor not in visited:
            total += dfs(neighbor, visited.copy())

    return total


def allowed(v, visited):
    if v == 'start':
        return False

    if v == 'end':
        return True

    if v not in visited:
        return True

    for key in visited:
        if key == 'start' or key.isupper():
            continue

        if visited[key] > 1:
            return False

    return True


def dfs2(current, visited):
    if current == 'end':
        return 1

    total = 0

    visited[current] += 1

    for neighbor in adj[current]:
        if neighbor.isupper() or allowed(neighbor, visited):
            total += dfs2(neighbor, visited.copy())

    return total


def answer1():
    return dfs('start', set())


def answer2():
    seen = defaultdict(int)
    seen['start'] = 1
    return dfs2('start', seen)


print(answer1())
print(answer2())
