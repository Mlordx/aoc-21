import math

with open('input.txt', 'r') as file:
    for line in file:
        crabs = [int(x) for x in line.split(',')]

def sum_up_to(number):
    return (number*number + number)//2

def answer1():
    total_fuel = 0

    sorted_crabs = sorted(crabs)
    median = sorted_crabs[len(crabs)//2] if len(crabs) % 2 != 0 else \
        (sorted_crabs[len(crabs)//2] + sorted_crabs[len(crabs)//2-1])/2

    for crab in crabs:
        total_fuel += abs(crab-median)

    return total_fuel

print(answer1())

def answer2():
    min_sum = 1 << 31
    for i in range(min(crabs), max(crabs)+1):
        current_sum = 0
        for crab in crabs:
            current_sum += sum_up_to(abs(crab - i))

        if current_sum < min_sum:
            min_sum = current_sum

    return min_sum

print(answer2())