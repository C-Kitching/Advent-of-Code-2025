
import numpy as np


def read():

    with open("day6/input.txt") as f:
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


def part2():
    return




part1()
part2()