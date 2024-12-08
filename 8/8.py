from collections import defaultdict

def a():
    # with open("./input-test.txt") as inputFile:
    with open("./input.txt") as inputFile:
        grid = []
        for line in inputFile:
            grid.append(list(line.strip()))

        print("\n".join(map(lambda x: " ".join(x), grid)))
        width = len(grid[0])
        height = len(grid)

        frequencyLocations = defaultdict(list)
        for y in range(height):
            for x in range(width):
                if grid[y][x] != ".":
                    frequencyLocations[grid[y][x]].append((x, y))
        print(frequencyLocations)

        antinodeLocations = set()
        for frequency in frequencyLocations:
            for a in frequencyLocations[frequency]:
                (x1, y1) = a
                for b in frequencyLocations[frequency]:
                    if a == b:
                        continue

                    (x2, y2) = b
                    vecX = x2 - x1
                    vecY = y2 - y1

                    antinodeX = x1 - vecX
                    antiNodeY = y1 - vecY
                    if antinodeX >= 0 and antinodeX < width and antiNodeY >= 0 and antiNodeY < height:
                        grid[antiNodeY][antinodeX] = "#"
                        antinodeLocations.add((antinodeX, antiNodeY))

        print(antinodeLocations)
        print(len(antinodeLocations))
        print("\n".join(map(lambda x: " ".join(x), grid)))

def diffGrid(grid):
    target = list(map(lambda x: list(x.strip()),  """##....#....#
                                                .#.#....0...
                                                ..#.#0....#.
                                                ..##...0....
                                                ....0....#..
                                                .#...#A....#
                                                ...#..#.....
                                                #....#.#....
                                                ..#.....A...
                                                ....#....A..
                                                .#........#.
                                                ...#......##""".splitlines()))
    for y in range(len(grid)):
        out = ""
        for x in range(len(grid[0])):
            if target[y][x] != grid[y][x]:
                out += '\x1b[6;30;42m' + grid[y][x] + '\x1b[0m'
            else:
                out += grid[y][x]

            out += " "
        print(out)

def b():
    # with open("./input-test.txt") as inputFile:
    with open("./input.txt") as inputFile:
        # inputFile = """T.........
        #                 ...T......
        #                 .T........
        #                 ..........
        #                 ..........
        #                 ..........
        #                 ..........
        #                 ..........
        #                 ..........
        #                 ..........""".splitlines()
        grid = []
        for line in inputFile:
            grid.append(list(line.strip()))

        print("\n".join(map(lambda x: " ".join(x), grid)))
        width = len(grid[0])
        height = len(grid)

        frequencyLocations = defaultdict(list)
        for y in range(height):
            for x in range(width):
                if grid[y][x] != ".":
                    frequencyLocations[grid[y][x]].append((x, y))
        print(frequencyLocations)

        antinodeLocations = set()
        for frequency in frequencyLocations:
            for a in frequencyLocations[frequency]:
                (x1, y1) = a
                for b in frequencyLocations[frequency]:
                    if a == b:
                        continue

                    (x2, y2) = b
                    vecX = x2 - x1
                    vecY = y2 - y1

                    antinodeX = x2
                    antiNodeY = y2
                    while antinodeX >= 0 and antinodeX < width and antiNodeY >= 0 and antiNodeY < height:
                        grid[antiNodeY][antinodeX] = "#"
                        # print(antinodeX, antiNodeY)
                        antinodeLocations.add((antinodeX, antiNodeY))
                        antinodeX = antinodeX + vecX
                        antiNodeY = antiNodeY + vecY
                    # print(antinodeX, antiNodeY)

        # print(antinodeLocations)
        print(len(antinodeLocations))
        # print("\n".join(map(lambda x: " ".join(x), grid)))
        # diffGrid(grid)

# a()
b()