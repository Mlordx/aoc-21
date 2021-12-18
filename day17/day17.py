#!/usr/bin/python3
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(input_file, 'r') as file:
    for line in file:
        xs, ys = line.strip().split('target area: ')[1].split(',')

        x1, x2 = xs[2:].split('..')
        x1, x2 = int(x1), int(x2)

        if x1 < 0 and x2 < 0:
            x1, x2 = -x1, -x2

        y1, y2 = ys[3:].split('..')
        y1, y2 = int(y1), int(y2)


def in_target(x, y):
    return x1 <= x <= x2 and y1 <= y <= y2


def missed_target(x, y):
    return x > x2 or y < y1


def answer():
    maxY = -float('inf')
    valid_vel = set()
    for vel_x in range(x2+1):
        max_dist = (vel_x**2 + vel_x)/2

        if max_dist < x1:
            continue

        for vel_y in range(-100, 100):
            current = (0, 0)
            vx = vel_x
            vy = vel_y
            localMaxY = -float('inf')
            while not missed_target(*current):
                current = (current[0]+vx, current[1]+vy)
                localMaxY = max(localMaxY, current[1])

                if in_target(*current):
                    valid_vel.add((vel_x, vel_y))
                    maxY = max(maxY, localMaxY)

                vx = vx - 1 if vx > 0 else 0
                vy -= 1

    return maxY, len(valid_vel)


ans = answer()
print(ans[0])
print(ans[1])
