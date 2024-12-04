def a():
    grid = []
    with open("input.txt") as file:
        for line in file.readlines():
            grid.append(list(line.strip()))

    # print(grid)

    width = len(grid[0])
    height = len(grid)
    occurences = 0

    for y in range(height):
        for x in range(width):
            if x + 3 < width:
                if grid[y][x] == "X" and grid[y][x + 1] == "M" and grid[y][x + 2] == "A" and grid[y][x + 3] == "S":
                    occurences += 1
            if x - 3 >= 0:
                if grid[y][x] == "X" and grid[y][x - 1] == "M" and grid[y][x - 2] == "A" and grid[y][x - 3] == "S":
                    occurences += 1
            if y + 3 < height:
                if grid[y][x] == "X" and grid[y + 1][x] == "M" and grid[y + 2][x] == "A" and grid[y + 3][x] == "S":
                    occurences += 1
            if y - 3 >= 0:
                if grid[y][x] == "X" and grid[y - 1][x] == "M" and grid[y - 2][x] == "A" and grid[y - 3][x] == "S":
                    occurences += 1
            if y + 3 < height and x + 3 < width:
                if grid[y][x] == "X" and grid[y + 1][x + 1] == "M" and grid[y + 2][x + 2] == "A" and grid[y + 3][x + 3] == "S":
                    occurences += 1
            if y - 3 >= 0 and x - 3 >= 0:
                if grid[y][x] == "X" and grid[y - 1][x - 1] == "M" and grid[y - 2][x - 2] == "A" and grid[y - 3][x - 3] == "S":
                    occurences += 1
            if y - 3 >= 0 and x + 3 < width:
                if grid[y][x] == "X" and grid[y - 1][x + 1] == "M" and grid[y - 2][x + 2] == "A" and grid[y - 3][x + 3] == "S":
                    occurences += 1
            if y + 3 < height and x - 3 >= 0:
                if grid[y][x] == "X" and grid[y + 1][x - 1] == "M" and grid[y + 2][x - 2] == "A" and grid[y + 3][x - 3] == "S":
                    occurences += 1
    
    print(occurences)

def b():
    grid = []
    with open("input.txt") as file:
        for line in file.readlines():
            grid.append(list(line.strip()))

    # print(grid)

    width = len(grid[0])
    height = len(grid)
    occurences = 0

    options = [
        [
            ['M', '.', 'M'],
            ['.', 'A', '.'],
            ['S', '.', 'S'],
        ],
        [
            ['M', '.', 'S'],
            ['.', 'A', '.'],
            ['M', '.', 'S'],
        ],
        [
            ['S', '.', 'S'],
            ['.', 'A', '.'],
            ['M', '.', 'M'],
        ],
        [
            ['S', '.', 'M'],
            ['.', 'A', '.'],
            ['S', '.', 'M'],
        ],
    ]

    for y in range(height - 2):
        for x in range(width - 2):
            for option in options:
                found = True
                for oy in range(len(option)):
                    for ox in range(len(option[0])):
                        if option[oy][ox] != "." and option[oy][ox] != grid[y + oy][x + ox]:
                            found = False
                            break
                    
                    if not found:
                        break
                
                if found:
                    occurences += 1
    
    print(occurences)

a()
b()