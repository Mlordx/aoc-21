#!/usr/bin/python3
import sys
from math import prod

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

ops = {
    '000': sum,
    '001': prod,
    '010': min,
    '011': max,
    '101': lambda a, b: 1 if a > b else 0,
    '110': lambda a, b: 1 if a < b else 0,
    '111': lambda a, b: 1 if a == b else 0,
}

packet = ''
with open(input_file, 'r') as file:
    for line in file:
        stripped = line.strip()

        for c in stripped:
            packet += hex_to_bin[c]


def parse_literal(packet):
    number = ''
    i = 0
    while True:
        lead = packet[i]
        number += packet[i+1:i+5]

        i += 5
        if lead == '0':
            break

    return int(number, 2), i


operations = []


def solve(packet, count=1, limit=float('inf')):
    if len(packet) < 11:
        return 0, packet

    if count > limit:
        return 0, packet

    version = int(packet[0:3], 2)

    type = packet[3:6]
    version_sum = version

    if type == '100':
        number, i = parse_literal(packet[6:])
        operations.append(number)
        left = packet[6+i:]
    else:
        operations.append(type)
        if packet[6] == '0':
            subpackets_length = int(packet[7:22], 2)
            version_count, _ = solve(packet[22:22+subpackets_length], count + 1)
            version_sum += version_count
            left = packet[22+subpackets_length:]
        else:
            number_of_subpackets = int(packet[7:18], 2)
            version_count, left = solve(packet[18:], limit=number_of_subpackets)
            version_sum += version_count
        operations.append(')')

    version_count, left2 = solve(left, count+1, limit)
    version_sum += version_count

    return version_sum, left2


def process():
    answer = []

    while len(operations) > 0:
        current = operations.pop()

        if current in ops.keys():
            if int(current, 2) in range(5, 8):
                a, b = answer.pop(), answer.pop()
                answer.pop()
                answer.append(ops[current](a, b))
            else:
                numbers = []
                x = answer.pop()
                while x != ')':
                    numbers.append(x)
                    x = answer.pop()

                answer.append(ops[current](numbers))
        else:
            answer.append(current)

    return answer[0]


def answer1():
    return solve(packet)[0]


def answer2():
    return process()


print(answer1())
print(answer2())
