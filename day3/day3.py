import numpy as np


def read():
    banks = []
    with open("day3/input.txt") as f:
        for bank in f:
            bank = bank.strip()
            banks.append([int(battery) for battery in bank])
    return banks



def part1():

    banks = read()

    res = 0

    for bank in banks:
        first_digit = max(bank[:-1])
        first_digit_idx = bank[:-1].index(first_digit)

        second_digit = max(bank[first_digit_idx+1:])

        res += first_digit*10 + second_digit

    print(res)

    return

def max_joltage_from_bank(bank, length = 12):

    n = len(bank)
    result = []

    start = 0
    for i in range(length):

        # leave enough digits for remaining selections
        remaining_digits = length - i

        # furthest digit away we can pick
        end = n - remaining_digits + 1

        max_digit = max(bank[start:end])
        result.append(max_digit)

        # move start to one after first occurance of this max digit
        start = bank.index(max_digit, start) + 1

    return int("".join(map(str, result)))


def part2():

    banks = read()

    res = 0

    for bank in banks:
        res += max_joltage_from_bank(bank)

    print(res)

    return





part1()
part2()