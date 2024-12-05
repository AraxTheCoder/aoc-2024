from collections import defaultdict
from functools import cmp_to_key

def a():
    # with open("./input-test.txt") as inputFile:
    with open("./input.txt") as inputFile:
        dependsOn = defaultdict(set)
        parseUpdates = False
        updates = []

        for line in inputFile.readlines():
            if line.strip() == "":
                parseUpdates = True
                continue

            if parseUpdates:
                updates.append(line.strip().split(","))
                continue

            [X, Y] = line.strip().split("|")
            dependsOn[Y].add(X)
        
        # print(dependsOn)
        # print(updates)

        res = 0

        for update in updates:
            rightOrder = True
            updateSet = set(update)
            for a in reversed(range(0, len(update))):
                allDependencies = True
                for dependency in dependsOn[update[a]]:
                    found = (dependency not in updateSet)
                    for b in range(0, a):
                        if update[b] == dependency:
                            found = True
                            break
                    
                    if not found:
                        allDependencies = False
                        break   

                if not allDependencies:
                    rightOrder = False
            
            if rightOrder:
                # print(update)
                res += int(update[int(len(update) / 2)])
        
        print(res)

def b():
    # with open("./input-test.txt") as inputFile:
    with open("./input.txt") as inputFile:
        dependsOn = defaultdict(set)
        parseUpdates = False
        updates = []

        for line in inputFile.readlines():
            if line.strip() == "":
                parseUpdates = True
                continue

            if parseUpdates:
                updates.append(line.strip().split(","))
                continue

            [X, Y] = line.strip().split("|")
            dependsOn[Y].add(X)
        
        # print(dependsOn)
        # print(updates)

        res = 0

        for update in updates:
            rightOrder = True
            updateSet = set(update)
            for a in reversed(range(0, len(update))):
                allDependencies = True
                for dependency in dependsOn[update[a]]:
                    found = (dependency not in updateSet)
                    for b in range(0, a):
                        if update[b] == dependency:
                            found = True
                            break
                    
                    if not found:
                        allDependencies = False
                        break   

                if not allDependencies:
                    rightOrder = False
            
            if not rightOrder:
                update = sorted(update, key=cmp_to_key(lambda item1, item2: -1 if item1 in dependsOn[item2] else 1))
                # print(update)

                res += int(update[int(len(update) / 2)])
        
        print(res)
a()#4462
b()#6767