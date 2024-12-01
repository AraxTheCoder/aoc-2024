from collections import defaultdict


def a():
    with open("./input.txt") as inputFile:
        first, second = [], []

        for line in inputFile.readlines():
            [firstVal, secondVal] = line.split("   ")
            first.append(int(firstVal))
            second.append(int(secondVal))

        first = sorted(first)
        second = sorted(second)

        sum = 0
        for a in range(len(first)):
            sum += abs(first[a] - second[a])

        print(sum)

def b():
    with open("./input.txt") as inputFile:
        first, second = [], []

        for line in inputFile.readlines():
            [firstVal, secondVal] = line.split("   ")
            first.append(int(firstVal))
            second.append(int(secondVal))

        times = defaultdict(int)

        for a in range(len(first)):
            times[second[a]] += 1

        res = 0
        for val in first:
            res += val * times[val]

        print(res)

a()
b()