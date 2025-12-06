def part1():

    with open("day1/input.txt") as f:
        lines = [line.strip() for line in f]

    pos = 50
    count = 0

    for line in lines:
        dir = line[0]
        val = int(line[1:])

        if dir == "R": pos += val
        else: pos -= val

        pos %= 100

        if pos == 0: count += 1

    print(count)

def part2():

    with open("day1/input.txt") as f:
        lines = [line.strip() for line in f]

    pos = 50
    count = 0

    for line in lines:
        dir = line[0]
        val = int(line[1:])

        step = -1 if dir == 'L' else +1

        for _ in range(val):
            pos = (pos + step) % 100
            if pos == 0:
                count += 1

    print(count)


part1()
part2()
