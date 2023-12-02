input_file = "2_day2_input.txt"
try:
    with open(input_file, 'r') as file:
        # Read the contents of the file
        file_content = file.readlines()
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")

def calculate_power(red_count, green_count, blue_count):
    return red_count * green_count * blue_count

def sum_of_powers(games):
    total_power = 0

    subsets = games.split(': ')[1].split('; ')  # Split subsets of cubes
    cube_counts = {'red': 0, 'green': 0, 'blue': 0}  # Initialize with zero

    for subset in subsets:
        subset_info = subset.split(', ')
        for info in subset_info:
            count, color = info.split()
            count = int(count)
            cube_counts[color] = max(cube_counts[color], count)

    game_power = calculate_power(cube_counts['red'], cube_counts['green'], cube_counts['blue'])
    total_power += game_power

    return total_power

result = 0
for games in file_content:
    result += sum_of_powers(games)

print(result)