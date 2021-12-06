file = open("input.txt", "r")

def answer1():
    one_count = [0,0,0,0,0,0,0,0,0,0,0,0]
    num_lines = 0
    for line in file:
        num_lines += 1
        i = 0
        for c in line:
            if c == '1':
                one_count[i] += 1
            i+=1

    gamma = ''
    epsilon = ''

    for value in one_count:
        if value > num_lines//2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)

# print(answer1())

def answer2():
    one_count = [0,0,0,0,0,0,0,0,0,0,0,0]
    num_lines = 0
    oxygen_list = []
    co2_list = []

    for line in file:
        num_lines += 1
        i = 0
        for c in line:
            if c == '1':
                one_count[i] += 1
            i+=1

        oxygen_list.append(line.split()[0])
        co2_list.append(line.split()[0])

    def count_ones(pos, numbers):
        count = 0
        for num in numbers:
            if num[pos] == '1':
                count += 1

        return count


    i = 0
    while len(oxygen_list) > 1:
        one_count = count_ones(i, oxygen_list)

        value = '1' if one_count >= len(oxygen_list)/2 else '0'
        oxygen_list = [x for x in oxygen_list if x[i] == value]

        i += 1



    i = 0
    while len(co2_list) > 1:
        one_count = count_ones(i, co2_list)

        value = '0' if one_count >= len(co2_list)/2 else '1'
        co2_list = [x for x in co2_list if x[i] == value]

        i += 1

    return int(oxygen_list[0], 2) * int(co2_list[0], 2)

print(answer2())
