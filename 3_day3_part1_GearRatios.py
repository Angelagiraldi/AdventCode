
# import required package
import re

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
        total = 0

        #Create a pattern that matches any character that is not a word character (a-z, A-Z, 0-9, or underscore) or a period (.).
        symbols = re.compile(r"[^\w.]")

        for line_num, line in enumerate(input_file):
            #Find and iterate through all sequences of digits (numbers) present in the string line
            for number in re.finditer(r"\d+", line):
                print(number.group())
                checks = [
                    # previous line
                    symbols.search(
                        input_file[line_num - 1][number.start() - 1 : number.end() + 1],
                    ),
                    # left side of the number
                    symbols.search(line[number.start() - 1]),
                    # right side of the number
                    symbols.search(line[number.end()]),
                    # following line
                    symbols.search(
                        input_file[line_num + 1][number.start() - 1 : number.end() + 1],
                    ),
                ]

                if any(checks):
                    total += int(number.group())

        return total


file_content = [l.strip("\n") for l in file_content]
padded_file_content = padded_input(file_content)

result = find_part_numbers(padded_file_content)
print("Sum of part numbers:", result)
