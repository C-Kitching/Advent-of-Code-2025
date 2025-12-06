
import numpy as np


def read():

    with open("day6/test.txt") as f:
        lines = [line.strip() for line in f if line.strip()]

    # last line is ops
    ops = lines[-1].split()
    # rest are numbers
    num_lines = lines[:-1]

    # split each line into numbers
    num_matrix = [list(map(int, line.split())) for line in num_lines]

    # tranpose
    columns = [list(col) for col in zip(*num_matrix)]

    return columns, ops



def part1():

    nums, ops = read()

    res = 0

    for i in range(len(nums)):
        if ops[i] == '+':
            res += np.sum(nums[i])
        else:
            res += np.prod(nums[i])

    print(res)

    return

def read2():

    with open("day6/input.txt") as f:
        lines = [line[:-1] for line in f]

    ops = lines[-1].split()
    num_lines = lines[:-1]

    # cast to matrix
    num_matrix = []
    for num_line in num_lines:
        num_matrix.append([c for c in num_line])

    # transpose
    num_matrix = np.array(num_matrix).T

    # convert to int
    nums = [int(''.join(x for x in row if x != ' ')) if not all(x == ' ' for x in row) else 0 for row in num_matrix]

    # group in threes
    group_nums = []
    for i in range(0, len(nums), 4):
        group_nums.append(nums[i:i+3])

    return group_nums, ops

def part2():

    nums, ops = read2()

    res = 0

    for i in range(len(nums)):
        if ops[i] == '+':
            res += np.sum(nums[i])
        else:
            res += np.prod(nums[i])

    print(res)

    
part1()
part2()