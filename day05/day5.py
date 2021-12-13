import numpy
file = open("input.txt", "r")

def mark_line(diagram, line):
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]

    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for j in range(y1, y2+1):
            diagram[x1][j] += 1
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for i in range(x1, x2+1):
            diagram[i][y1] += 1
    else:
        dx = abs(x1-x2)

        if x1 > x2: ix = -1
        else: ix = 1

        if y1 > y2: iy = -1
        else: iy = 1

        for i in range(dx+1):
            diagram[x1 + i*ix][y1 + i*iy] += 1


segments1 = []
segments2 = []
for line in file:
    segment = line.split('->')
    start = [int(x) for x in segment[0].split(',')]
    end = [int(x) for x in segment[1].split(',')]

    if start[0] == end[0] or start[1] == end[1]:
        segments1.append([start, end])
    segments2.append([start, end])

def answer1():
    diagram = numpy.zeros(shape=(1000,1000))

    for segment in segments1:
        mark_line(diagram, segment)

    count = 0
    for i in range(1000):
        for j in range(1000):
            if diagram[i][j] > 1:
                count += 1


    return count


print(answer1())

def answer2():
    diagram = numpy.zeros(shape=(1000,1000))

    for segment in segments2:
        mark_line(diagram, segment)

    count = 0
    for i in range(1000):
        for j in range(1000):
            if diagram[i][j] > 1:
                count += 1

    return count


print(answer2())
