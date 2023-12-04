
# import required package
import re
from collections import defaultdict
from operator import mul
from typing import Dict, List, Tuple

input_file = "3_day3_input.txt"
try:
    with open(input_file, 'r') as file:
        # Read the contents of the file
        file_content = file.readlines()
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")

#Checking positions beyond the top or bottom rows 
# or beyond the left or right columns results in out-of-bounds errors.
#To circumvent these boundary-related we can add an extra layer of dots around the entire grid. 
def padded_input(file_content):
        width = len(file_content[0])
        # ensure every line is the same length; we'll mess up lines if it's not
        assert all(len(l) == width for l in file_content)

        #return ["." * (width + 2), * [f".{l}." for l in input_file], "." * (width + 2)]
        return ["." * (width + 2)] + [".{0}.".format(l) for l in file_content] + ["." * (width + 2)]

#In this scenario, we're tasked with examining a grid of numbers and symbols. 
# For each potentially multi-digit number within the grid, 
# we need to inspect four adjacent positions around that number (labeled A, B, C, D):
# A A A A A
# B 1 2 3 C
# D D D D D
#If any of these adjacent positions contain a symbol (anything that is not a dot (.) or a number), 
# we'll include the value of the number in our running total.

def find_part_numbers(input_file):


    gears: Dict[Tuple[int, int], List[int]] = defaultdict(list)
    grid = input_file

    for line_num, line in enumerate(grid):
        for number in re.finditer(r"\d+", line):
            # A
            if "*" in (
                l := grid[line_num - 1][number.start() - 1 : number.end() + 1]
            ):
                assert l.count("*") == 1
                gears[(line_num - 1, number.start() - 1 + l.index("*"))].append(
                    int(number.group())
                )

            # B
            if line[number.start() - 1] == "*":
                gears[(line_num, number.start() - 1)].append(int(number.group()))

            # C
            if line[number.end()] == "*":
                gears[(line_num, number.end())].append(int(number.group()))

            # D
            if "*" in (
                l := grid[line_num + 1][number.start() - 1 : number.end() + 1]
            ):
                assert l.count("*") == 1
                gears[(line_num + 1, number.start() - 1 + l.index("*"))].append(
                    int(number.group())
                )
    return sum([mul(*nums) for nums in gears.values() if len(nums) == 2])



                            
file_content = [l.strip("\n") for l in file_content]
padded_file_content = padded_input(file_content)

result = find_part_numbers(padded_file_content)
print("Sum of part numbers:", result)
