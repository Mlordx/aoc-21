with open('input2.txt', 'r') as file:
    for line in file:
        crabs = [int(x) for x in line.split(',')]

def answer1():
    total_fuel = 0
    for crab in crabs:
        total_fuel += abs(crab-2)

    return total_fuel

print(answer1())