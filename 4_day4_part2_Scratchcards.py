import math 

input_file = "4_day4_input.txt"
try:
    with open(input_file, 'r') as file:
        # Read the contents of the file
        file_content = file.readlines()
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")

games = []
for line in file_content:
    subsets = line.strip().split(':')[1].split('|')
    winning_numbers = [int(x) for x in subsets[0].split()]
    played_numbers = [int(x) for x in subsets[1].split()]
    games.append([winning_numbers, played_numbers, 1])

for number, game in enumerate(games):
    total = 0
    for winner in game[0]:
        if winner in game[1]:
            total += 1
    if total >=1 :
        for n in range(int(total)):
            print((number + n + 1) < len(games))
            if (number + n + 1) < len(games):
                games[number + n + 1][2] += game[2]

sum = 0
for game in games:
    sum += game[2]

print(sum)