#!/usr/bin/python3
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

instructions = []

with open(input_file, 'r') as file:
    for line in file:
        command, xyz = line.strip().split(' ')
        value = 1 if command == 'on' else -1

        x1, x2 = xyz.split(',')[0][2:].split('..')
        x1, x2 = int(x1), int(x2)

        y1, y2 = xyz.split(',')[1][2:].split('..')
        y1, y2 = int(y1), int(y2)

        z1, z2 = xyz.split(',')[2][2:].split('..')
        z1, z2 = int(z1), int(z2)

        instructions.append((x1, x2, y1, y2, z1, z2, value))


def intersects(A, B):
    x1, x2, y1, y2, z1, z2, _ = A
    a1, a2, b1, b2, c1, c2, _ = B

    if x2 < a1 or a2 < x1:
        return False

    if y2 < b1 or b2 < y1:
        return False

    if z2 < c1 or c2 < z1:
        return False

    return True


def get_intersection(A, B):
    x1, x2, y1, y2, z1, z2, _ = A
    a1, a2, b1, b2, c1, c2, signB = B

    x3 = max(x1, a1)
    y3 = max(y1, b1)
    z3 = max(z1, c1)

    x4 = min(x2, a2)
    y4 = min(y2, b2)
    z4 = min(z2, c2)

    return (x3, x4, y3, y4, z3, z4, -signB)


def get_volume(cube):
    x1, x2, y1, y2, z1, z2, sign = cube

    return sign * (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)


def answer1():
    turned_on = set()
    for instruction in instructions:
        x1, x2, y1, y2, z1, z2, command = instruction
        for i in range(x1, x2+1):
            if abs(i) > 50:
                break
            for j in range(y1, y2+1):
                if abs(j) > 50:
                    break
                for k in range(z1, z2+1):
                    if abs(k) > 50:
                        break

                    if command == 1:
                        turned_on.add((i, j, k))
                    else:
                        if (i, j, k) in turned_on:
                            turned_on.remove((i, j, k))

    return len(turned_on)


def compute(part1=False):
    cuboids = []
    for x1, x2, y1, y2, z1, z2, command in instructions:
        new_cube = (x1, x2, y1, y2, z1, z2, command)

        if part1 and not intersects(new_cube, (-50, 50, -50, 50, -50, 50, 1)):
            continue
        intersections = []

        for cuboid in cuboids:
            if intersects(new_cube, cuboid):
                intersection = get_intersection(new_cube, cuboid)
                intersections.append(intersection)

        total = 0
        for c in intersections:
            cuboids.append(c)
            total += get_volume(c)

        if command == 1:
            cuboids.append(new_cube)
            total += get_volume(new_cube)

    answer = 0
    for cuboid in cuboids:
        answer += get_volume(cuboid)

    return answer


def answer2():
    return compute()


print(answer1())
print(compute(True))
print(answer2())
