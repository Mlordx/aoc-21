def answer1():
    count = 0
    with open('input.txt', 'r') as file:
        for line in file:
            for signal in line.split('|')[1].split():
                if len(signal) in [2, 3, 4, 7]:
                    count += 1

    return count

print(answer1())

def is_in(word1, word2):
    count = 0
    for c in word1:
        if c in word2:
            count += 1

    return count == len(word1)

def answer2():
    outputs = []
    with open('input.txt', 'r') as file:
        for line in file:
            signal_to_number = {}
            current_display = [ 'x' for i in range(8)]
            inputs = line.split('|')[0].split()
            output = line.split('|')[1].split()

            one = ''
            four = ''
            seven = ''
            for signal in inputs:
                if len(signal) == 2:
                    one = signal
                elif len(signal) == 3:
                    seven = signal
                elif len(signal) == 4:
                    four = signal

            current_output = ''
            for signal in output:
                if len(signal) == 2:
                    current_output += '1'
                elif len(signal) == 3:
                    current_output += '7'
                elif len(signal) == 4:
                    current_output += '4'
                elif len(signal) == 5:
                    if is_in(seven, signal):
                        current_output += '3'
                    else:
                        diff_4_1 = ''
                        for c in four:
                            if c not in one:
                                diff_4_1 += c

                        if is_in(diff_4_1, signal):
                            current_output += '5'
                        else:
                            current_output += '2'
                elif len(signal) == 6:
                    if is_in(four, signal):
                        current_output += '9'
                    else:
                        if is_in(one, signal):
                            current_output += '0'
                        else:
                            current_output += '6'
                else:
                    current_output += '8'

            outputs.append(int(current_output))
    return sum(outputs)

print(answer2())
