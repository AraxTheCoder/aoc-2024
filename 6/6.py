def findInitialPosition(grid):
    for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] not in {".", "#"}:
                    return (x, y, grid[y][x])
                
    return (0, 0, ">")

def go(x, y, d, grid):
    turnDirections = {
        "^": (0, -1, ">"),
        "v": (0, 1, "<"),
        ">": (1, 0, "v"),
        "<": (-1, 0, "^"),
    }

    posX = x
    posY = y
    direction = d

    visited = set()
    seen = set()

    while((posX >= 0 and posX < len(grid[0])) and (posY >= 0 and posY < len(grid))):
        (dx, dy, d) = turnDirections[direction]
        if grid[posY][posX] == "#":
            posX -= dx
            posY -= dy
            direction = d
        else:
            grid[posY][posX] = "X"
            if (posX, posY, direction) in visited:
                return ({}, True)
            visited.add((posX, posY, direction))
            seen.add((posX, posY))

            posX += dx
            posY += dy

    return (seen, False)

def a():
    # with open("./input-test.txt") as inputFile:
    with open("./input.txt") as inputFile:
        grid = []
        for line in inputFile:
            grid.append(list(line.strip()))

        (posX, posY, direction) = findInitialPosition(grid)    

        (visited, looped) = go(posX, posY, direction, grid)

        print(len(visited))

def b():
    # with open("./input-test.txt") as inputFile:
    with open("./input.txt") as inputFile:
        grid = []
        for line in inputFile:
            grid.append(list(line.strip()))

        # find initial position
        (iX, iY, idirection) = findInitialPosition(grid)

        (visited, looped) = go(iX, iY, idirection, grid)
        
        loops = set()
        for (x, y) in visited:
            if (x == iX and y == iY) or (x, y) in loops:
                continue

            grid[y][x] = "#"
            (_, looped) = go(iX, iY, idirection, grid)
            if looped:
                loops.add((x, y))

            grid[y][x] = "X"

        print(len(loops))
    
print("\n" * 50)
a()
b()