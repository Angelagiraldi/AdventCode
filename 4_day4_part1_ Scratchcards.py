import math 

input_file = "4_day4_input.txt"
try:
    with open(input_file, 'r') as file:
        # Read the contents of the file
        file_content = file.readlines()
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")

sum = 0
for games in file_content:
    subsets = games.strip("\n").split(': ')[1].split('| ')
    winning_numbers = subsets[0].split(' ')
    played_numbers = subsets[1].split(' ')
    points = [p for p in played_numbers if p in winning_numbers and p!='']
    if len(points)>0:
        sum += pow(2, len(points)-1)

print(sum)