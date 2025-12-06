

def read():
    ranges = []
    ids = []

    with open("day5/input.txt") as f:
        section = 0
        for line in f:
            line = line.strip()
            if not line:
                section = 1
                continue

            if section == 0:
                a, b = map(int, line.split('-'))
                ranges.append([a, b])
            else:
                ids.append(int(line))

    return ranges, ids


def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]: # overlap
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged

def part1():

    ranges, ids = read()
    ranges = merge_intervals(ranges)

    valid_ids = []
    for id_ in ids:
        for start, end in ranges:
            if start <= id_ <= end:
                valid_ids.append(id_)
                break

    print(len(valid_ids))

    return


def part2():

    ranges, _ = read()
    ranges = merge_intervals(ranges)

    res = 0

    for start, end in ranges:
        res += end - start + 1

    print(res)

    return


part1()
part2()