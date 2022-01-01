import sys
from collections import defaultdict

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

beacons = []

with open(input_file, 'r') as file:
    current_set = set()
    for line in file:
        if line[0:3] == '---':
            continue

        if line == '\n':
            beacons.append(current_set)
            current_set = set()
            continue

        stripped_line = line.strip()
        x, y, z = stripped_line.split(',')
        x, y, z = int(x), int(y), int(z)

        current_set.add((x, y, z))
beacons.append(current_set)


def apply_rotation(n, x, y, z):
    rots = [
        (+x, +y, +z),
        (+x, +z, -y),
        (+x, -y, -z),
        (+x, -z, +y),
        (-x, +y, -z),
        (-x, -z, -y),
        (-x, -y, +z),
        (-x, +z, +y),
        (+y, +z, +x),
        (+y, +x, -z),
        (+y, -z, -x),
        (+y, -x, +z),
        (-y, +x, +z),
        (-y, +z, -x),
        (-y, -x, -z),
        (-y, -z, +x),
        (+z, +y, -x),
        (+z, -x, -y),
        (+z, -y, +x),
        (+z, +x, +y),
        (-z, -x, +y),
        (-z, +y, +x),
        (-z, +x, -y),
        (-z, -y, -x)
    ]

    return rots[n]


def manhattan_dist(x1, y1, z1, x2, y2, z2):
    return abs(x1-x2) + abs(y1 - y2) + abs(z1-z2)


def solve():
    scanner_pos = [(0, 0, 0)]
    distinct_scanners = set(beacons.pop(0))

    while beacons:
        b2 = beacons.pop(0)
        overlaps = False
        for i in range(24):
            diffs = defaultdict(int)
            new_points = set()
            for p1 in distinct_scanners:
                for p2 in b2:
                    new_point = apply_rotation(i, *p2)
                    new_points.add(new_point)
                    x1, y1, z1 = p1
                    x2, y2, z2 = new_point
                    diff = (x2 - x1, y2 - y1, z2 - z1)
                    diffs[diff] += 1

            for key in diffs:
                if diffs[key] >= 12:
                    x1, y1, z1 = key
                    overlaps = True
                    scanner_pos.append((-x1, -y1, -z1))
                    for p in new_points:
                        x2, y2, z2 = p
                        distinct_scanners.add((x2 - x1, y2 - y1, z2 - z1))

        if not overlaps:
            beacons.append(b2)

    return distinct_scanners, scanner_pos


distinct_scanners, scanner_pos = solve()


def answer1():
    return len(distinct_scanners)


def answer2():
    max_dist = -1
    for i in range(len(scanner_pos)):
        for j in range(i+1, len(scanner_pos)):
            max_dist = max(max_dist, manhattan_dist(*scanner_pos[i], *scanner_pos[j]))
    return max_dist


print(answer1())
print(answer2())
