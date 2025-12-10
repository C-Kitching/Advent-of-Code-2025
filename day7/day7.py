

def read():
    grid = []
    with open("day7/input.txt") as f:
        for line in f:
            line = line.strip()
            grid.append([c for c in line])
    return grid


def part1():

    grid = read()

    m = len(grid)
    n = len(grid[0])

    # replace s with beam
    for j in range(n):
        if grid[0][j] == 'S':
            grid[0][j] = '|'
            break

    splits = 0

    for i in range(1, m):
        for j in range(n):

            # continued beam
            if grid[i-1][j] == '|' and grid[i][j] == '.':
                grid[i][j] = '|'
            
            # splitter
            elif grid[i-1][j] == '|' and grid[i][j] == '^':
                splits += 1
                if j > 0: grid[i][j+1] = '|'
                if j < m-1: grid[i][j-1] = '|'


    print(splits)

    return


def part2():

    grid = read()
    m, n = len(grid), len(grid[0])

    # find S
    for j in range(n):
        if grid[0][j] == "S":
            start = j
            break

    # dp grid
    dp = [[0]*n for _ in range(m)]
    dp[0][start] = 1

    for i in range(m-1):
        for j in range(n):
            ways = dp[i][j]
            if ways == 0:
                continue

            cell = grid[i+1][j]   # what lies below

            if cell == '.':
                dp[i+1][j] += ways

            elif cell == '^':
                if j > 0:
                    dp[i+1][j-1] += ways
                if j < n-1:
                    dp[i+1][j+1] += ways

    # total timelines = all ways that reach bottom row
    total = sum(dp[m-1][j] for j in range(n))
    print(total)

    return




part1()
part2()