import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

lines = []
with open(input_file, 'r') as file:
    for line in file:
        lines.append(line.split()[0])

complement = {
    '(': ')',
    ')': '(',
    '[': ']',
    ']': '[',
    '}': '{',
    '{': '}',
    '<': '>',
    '>': '<'
}

def first_corrupted_character(i):
    chunk = []
    opening = set('[{<(')
    for c in lines[i]:
        if c in opening:
            chunk.append(c)
        else:
            if chunk[-1] == complement[c]:
                chunk.pop()
            else:
                return c

    return None

def line_completion_score(i):
    chunk = []
    opening = set('[{<(')
    completion_value = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    score = 0
    for c in lines[i]:
        if c in opening:
            chunk.append(c)
        else:
            if chunk[-1] == complement[c]:
                chunk.pop()

    for c in chunk[::-1]:
        score = score*5 + completion_value[complement[c]]

    return score

def answer1():
    answers = []
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    for i in range(len(lines)):
        corrupted_char = first_corrupted_character(i)
        if corrupted_char:
            answers.append(points[corrupted_char])

    return sum(answers)

print(answer1())

def answer2():
    answers = []
    for i in range(len(lines)):
        corrupted_char = first_corrupted_character(i)
        if corrupted_char:
            continue

        answers.append(line_completion_score(i))

    return sorted(answers)[len(answers)//2]

print(answer2())
