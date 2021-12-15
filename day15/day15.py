import sys
from collections import defaultdict
from queue import PriorityQueue

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

risk = defaultdict(int)
risk_bigger = defaultdict(int)
SIZE = 0
with open(input_file, 'r') as file:
    for i, line in enumerate(file):
        line_values = [int(x) for x in line.split()[0]]
        for j, value in enumerate(line_values):
            risk[(i, j)] = value

    SIZE = i+1


def dijkstra(weight, cost):
    pq = PriorityQueue()
    pq.put((0, (0, 0)))
    visited = set()

    while not pq.empty():
        (dist, current) = pq.get()
        x, y = current
        visited.add(current)

        adjacents = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

        for adjacent in adjacents:
            if adjacent in weight and adjacent not in visited:
                old = cost[adjacent]
                new = dist + weight[adjacent]

                if new < old:
                    pq.put((new, adjacent))
                    cost[adjacent] = new

    return cost


def answer1():
    cost = defaultdict(int)

    for a in range(SIZE):
        for b in range(SIZE):
            cost[(a, b)] = 0 if (a == 0 and b == 0) else float('inf')

    return dijkstra(risk, cost)[(SIZE-1, SIZE-1)]


print(answer1())


def answer2():
    cost = defaultdict(int)
    NEW_SIZE = 5*SIZE

    for a in range(NEW_SIZE):
        for b in range(NEW_SIZE):
            cost[(a, b)] = 0 if (a == 0 and b == 0) else float('inf')

    for key in risk:
        for i in range(5):
            for j in range(5):
                x, y = key
                value = risk[key] + i + j
                if value > 9:
                    value = value - 9
                risk_bigger[(x + i*SIZE, y + j*SIZE)] = value

    return dijkstra(risk_bigger, cost)[(NEW_SIZE-1, NEW_SIZE-1)]


print(answer2())
