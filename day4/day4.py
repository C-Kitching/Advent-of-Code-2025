

def read():
    grid = []
    with open("day4/input.txt") as f:
        for line in f:
            line = line.strip()
            grid.append([c for c in line])
    return grid

def part1():

    grid = read()
    n = len(grid)
    m = len(grid[0])

    dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

    movable_rolls = 0

    for r in range(n):
        for c in range(m):

            # skip non rolls
            if grid[r][c] != '@': continue

            adjacent_rolls = 0
            
            # count number of adjacent rolls
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if 0<=nr<n and 0<=nc<m and grid[nr][nc] == '@':
                    adjacent_rolls += 1

            if adjacent_rolls < 4:
                movable_rolls += 1

    print(movable_rolls)

    return


def part2():

    grid = read()
    n = len(grid)
    m = len(grid[0])

    dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

    res = 0
    can_remove = True

    while can_remove:

        roll_coords = []
        can_remove = False

        for r in range(n):
            for c in range(m):

                # skip non rolls
                if grid[r][c] != '@': continue

                adjacent_rolls = 0
                
                # count number of adjacent rolls
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if 0<=nr<n and 0<=nc<m and grid[nr][nc] == '@':
                        adjacent_rolls += 1

                # track coords of rolls to be removed
                if adjacent_rolls < 4:
                    can_remove = True
                    res += 1
                    roll_coords.append((r, c))

        # remove rolls
        for r, c in roll_coords:
            grid[r][c] = 'x'

    print(res)

    return



part1()
part2()