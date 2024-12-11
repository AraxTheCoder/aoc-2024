def hike(x, y, expectedHeight, visited, grid):
    if (x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)):
        return 0

    if grid[y][x] != expectedHeight:
        return 0

    if visited != None and (x, y) in visited:
        return 0
    
    if visited != None:
        visited.add((x, y))
    
    if grid[y][x] == 9:
        return 1

    return hike(x - 1, y, expectedHeight + 1, visited, grid) + hike(x + 1, y, expectedHeight + 1, visited, grid) + hike(x, y - 1, expectedHeight + 1, visited, grid) + hike(x, y + 1, expectedHeight + 1, visited, grid)

def a():
    # with open("input-test.txt") as file:
    with open("input.txt") as file:
        grid = []

        for line in file:
            grid.append(list(map(lambda x: int(x), list(line.strip()))))

        # print(grid)

        sumScores = 0

        width = len(grid[0])
        height = len(grid)

        for y in range(height):
            for x in range(width):
                sumScores += hike(x, y, 0, set(), grid)

        print(sumScores)

def b():
    # with open("input-test.txt") as file:
    with open("input.txt") as file:
        grid = []

        for line in file:
            grid.append(list(map(lambda x: int(x), list(line.strip()))))

        # print(grid)

        sumScores = 0

        width = len(grid[0])
        height = len(grid)

        for y in range(height):
            for x in range(width):
                sumScores += hike(x, y, 0, None, grid)

        print(sumScores)

print('\n' * 50)
a()
b()