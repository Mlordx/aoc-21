file = open("input.txt", "r")

numbers = []
for num in file:
  numbers.append(int(num))

def answer1():
    answer = 0
    for i in range(len(numbers)-1):
        if numbers[i] < numbers[i+1]:
            answer += 1

    return answer

print(answer1())

def answer2():
    answer = 0
    previousSum = numbers[0] + numbers[1] + numbers[2]
    for i in range(1, len(numbers)-2):
        currentSum = numbers[i] + numbers[i+1] + numbers[i+2]
        if currentSum > previousSum:
            answer += 1
        previousSum = currentSum

    return answer

print(answer2())
