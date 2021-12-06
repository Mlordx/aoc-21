file = open("input.txt", "r")

def answer1():
    horizontal = 0
    vertical = 0

    for line in file:
        command = line.rstrip().split()
        if command[0] == 'forward':
            horizontal += int(command[1])
        elif command[0] == 'down':
            vertical += int(command[1])
        else:
            vertical -= int(command[1])

    return vertical * horizontal

# print(answer1())

def answer2():
    horizontal = 0
    vertical = 0
    aim = 0

    for line in file:
        command = line.rstrip().split()
        if command[0] == 'forward':
            horizontal += int(command[1])
            vertical += aim * int(command[1])
        elif command[0] == 'down':
            aim += int(command[1])
        else:
            aim -= int(command[1])

    return horizontal*vertical

print(answer2())