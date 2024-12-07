def add(a, b):
    return a + b

def mult(a, b):
    return a * b

def concat(a, b):
    return int(str(a) + str(b))

def canBeCombinedUsing(target, values, operation, calculations, operations):
    if len(values) == 0:
        return target == calculations

    value = values[0]
    calculations = operation(calculations, value)
    if calculations > target:
        return False
    
    values = values[1:]

    for operation in operations:
        if canBeCombinedUsing(target, values, operation, calculations, operations):
            return True

    return False

def a():
    # with open("./input-test.txt") as inputFile:
    with open("./input.txt") as inputFile:
        totalCalibrationResult = 0
        for line in inputFile:
            parts = line.strip().split(" ")
            target = int(parts[0][:-1])
            values = list(map(lambda x: int(x), parts[1:]))

            if canBeCombinedUsing(target, values, add, 0, [add, mult]):
                totalCalibrationResult += target

        print(totalCalibrationResult)

def b():
    # with open("./input-test.txt") as inputFile:
    with open("./input.txt") as inputFile:
        totalCalibrationResult = 0
        for line in inputFile:
            parts = line.strip().split(" ")
            target = int(parts[0][:-1])
            values = list(map(lambda x: int(x), parts[1:]))

            if canBeCombinedUsing(target, values, add, 0, [add, mult, concat]):
                totalCalibrationResult += target

        print(totalCalibrationResult)
        
a()
b()