
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

def part2():

    with open("day6/input.txt", "r") as f:
        lines = f.read().splitlines()

    max_width = max(len(line) for line in lines)
    grid = [line.ljust(max_width) for line in lines]
    
    height = len(grid)
    width = max_width
    
    grand_total = 0
    current_problem_cols = []

    # Helper function to solve a specific group of columns
    def solve_problem(cols):
        operator = None
        numbers = []
        
        # 1. Extract Numbers and Find Operator
        # cols are ordered Right-to-Left (as discovered during scan)
        for col_idx in cols:
            # Check the bottom row (last line) for the operator
            bottom_char = grid[height - 1][col_idx]
            if bottom_char in "+*":
                operator = bottom_char
            
            # Build the number string from top to second-to-last row
            num_str = ""
            for row_idx in range(height - 1):
                num_str += grid[row_idx][col_idx]
            
            # If the column actually contains a number (not just whitespace above an operator)
            if num_str.strip():
                numbers.append(int(num_str.strip()))
        
        if not numbers or not operator:
            return 0

        # 2. Calculate result
        # The prompt implies the operator applies to the sequence
        # e.g., 4 + 431 + 623
        result = numbers[0]
        for i in range(1, len(numbers)):
            num = numbers[i]
            if operator == '+':
                result += num
            else:
                result *= num
                
        return result

    # Iterate columns from Right to Left
    for col in range(width - 1, -1, -1):
        # Check if the current column is a separator (all spaces)
        is_separator = True
        for row in range(height):
            if grid[row][col] != ' ':
                is_separator = False
                break
        
        if is_separator:
            # If we hit a separator and have accumulated columns, solve the problem
            if current_problem_cols:
                grand_total += solve_problem(current_problem_cols)
                current_problem_cols = []
        else:
            # Add column to current problem
            current_problem_cols.append(col)

    # Process the final problem if the line didn't end with a space-column
    if current_problem_cols:
        grand_total += solve_problem(current_problem_cols)

    print(grand_total)

    return




part1()
part2()