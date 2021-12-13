file = open('input.txt', 'r')

days = []
for line in file:
    starting_lanternfish = [int(x) for x in line.split(',')]

def answer(rounds):
    number_of_fish = [0 for i in range(9)]

    for fish in starting_lanternfish:
        number_of_fish[fish] += 1

    for i in range(rounds):
        current_number_of_fish = number_of_fish
        new_number_of_fish = [0 for j in range(9)]

        for i in range(1, 9):
            new_number_of_fish[i-1] += current_number_of_fish[i]

        new_number_of_fish[6] += current_number_of_fish[0]
        new_number_of_fish[8] += current_number_of_fish[0]

        number_of_fish = new_number_of_fish

    total_fish = 0
    for number in number_of_fish:
        total_fish += number

    return total_fish

print(answer(80))
print(answer(256))
