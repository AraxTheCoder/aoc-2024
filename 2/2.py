def sign(num):
    return 1 if num >= 0 else -1

def a():
    # with open("./input-test.txt") as inputFile:
    with open("./input.txt") as inputFile:
        safeReports = 0

        for line in inputFile.readlines():
            report = line.strip().split(" ")
            dir = sign(int(report[0]) - int(report[1]))

            for index in range(len(report) - 1):
                diff = int(report[index]) - int(report[index + 1])
                if sign(diff) != dir or (abs(diff) > 3 or abs(diff) < 1):
                    safeReports -= 1
                    # print(diff, sign(diff), dir, report)
                    break
            
            safeReports += 1


        print(safeReports)

def b():
    # with open("./input-test.txt") as inputFile:
    with open("./input.txt") as inputFile:
        safeReports = 0

        for line in inputFile.readlines():
            report = list(map(lambda x: int(x), line.strip().split(" ")))
            if isSafe(report, 1):
                safeReports += 1

        print(safeReports)

def isSafe(items, mistakes_allowed):
    direction = 1 if items[1] > items[0] else -1

    for x in range(1, len(items)):
        dif = (items[x] - items[x-1]) * direction
        if dif < 1 or dif > 3:
            if mistakes_allowed:
                arr1 = items[:x] + items[x+1:]
                arr2 = items[:x-1] + items[x:]
                arr3 = items[:x-2] + items[x-1:]
                return isSafe(arr1, False) or isSafe(arr2, False) or isSafe(arr3, False)
            else:
                return False

    return True

print("\n" * 20)
a()
b()