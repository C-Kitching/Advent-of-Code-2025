import math
import numpy as np 

def read():
    ranges = []
    with open("day2/input.txt") as f:
        for line in f:
            line = line.strip().rstrip(",")      
            parts = line.split(",")             
            for p in parts:
                if not p:
                    continue
                a, b = p.split("-")          
                ranges.append((int(a), int(b)))
    return ranges

def is_repeated_exactly_twice(n):
    s = str(n)
    L = len(s)
    if L % 2 != 0:
        return False
    half = L // 2
    block = s[:half]
    return block == s[half:] and block[0] != '0'

def is_repeated_at_least_twice(n):
    s = str(n)
    return s in (s + s)[1:-1]

def part1():

    # read in ranges
    ranges = read()

    invalid_IDs = []

    for start, end in ranges:
        for num in range(start, end + 1):
            if is_repeated_exactly_twice(num):
                invalid_IDs.append(num)

    print(np.sum(invalid_IDs))

    return

def part2():

    # read in ranges
    ranges = read()

    invalid_IDs = []

    for start, end in ranges:
        for num in range(start, end + 1):
            if is_repeated_at_least_twice(num):
                invalid_IDs.append(num)

    print(np.sum(invalid_IDs))

    return




part1()
part2()