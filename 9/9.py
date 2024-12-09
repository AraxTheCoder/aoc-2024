from collections import defaultdict

def extractFileSystem(diskMap):
    fileSystem = []
    spaces = []
    fileBlocks = []
    id = 0
    isSpace = False

    for symbol in diskMap:
        if isSpace:
            spaces.append((len(fileSystem), int(symbol)))
        else:
            fileBlocks.append((len(fileSystem), int(symbol)))

        for position in range(int(symbol)):
            if isSpace:
                fileSystem.append(".")
            else:
                fileSystem.append(id)
        if not isSpace:
            id += 1
        isSpace = not isSpace

    return fileSystem, spaces, fileBlocks

def a():
    # with open("./input-test.txt") as inputFile:
    with open("./input.txt") as inputFile:
        fileSystem, _, _ = extractFileSystem(inputFile.readlines()[0].strip())
        # print(fileSystem)

        left = 0
        right = len(fileSystem) - 1

        while(left <= right):
            if fileSystem[left] == "." and fileSystem[right] != ".":
                fileSystem[left] = fileSystem[right]
                fileSystem[right] = "."
                right -= 1
                left += 1
            elif fileSystem[left] != ".":
                left += 1
            elif fileSystem[right] == ".":
                right -= 1

        # print(fileSystem)

        checksum = 0
        for blockIndex in range(len(fileSystem)):
            if fileSystem[blockIndex] == ".":
                break
            checksum += blockIndex * fileSystem[blockIndex]

        print(checksum)

def b():
    # with open("./input-test.txt") as inputFile:
    with open("./input.txt") as inputFile:
        fileSystem, _, fileBlocks = extractFileSystem(inputFile.readlines()[0].strip())
        # print(fileSystem, fileBlocks)

        for fileIndex, fileLength in reversed(fileBlocks):
            moveToIndex = None

            for index in range(fileIndex):
                fits = True
                for length in range(fileLength):
                    if fileSystem[index + length] != ".":
                        fits = False
                        break
                if fits:
                    moveToIndex = index
                    break
            
            # print(fileSystem[fileIndex], moveToIndex)
            if moveToIndex == None:
                continue

            index = fileIndex
            while index < fileIndex + fileLength:
                fileSystem[moveToIndex] = fileSystem[index]
                fileSystem[index] = "."
                index += 1
                moveToIndex += 1
            
        # print(fileSystem)

        checksum = 0
        for blockIndex in range(len(fileSystem)):
            if fileSystem[blockIndex] == ".":
                continue
            checksum += blockIndex * fileSystem[blockIndex]

        print(checksum)
        
a()
b()